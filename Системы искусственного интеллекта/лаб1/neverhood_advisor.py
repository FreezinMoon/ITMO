"""
This program is an interactive command-line system that assists a user in completing goals by suggesting actions based
on their current location, items they possess, and their intended goal. The system uses a Prolog knowledge base for
determining paths between locations, necessary items, and required actions to achieve the user's goal.

The program works by:

1. Asking the user for their current location, items they possess, and their goal.
2. Parsing this input and updating the Prolog knowledge base with the user's current state (location, items, goal).
3. Checking if the user has already achieved their goal.
4. If the goal is not achieved, it provides recommendations to the user, including paths to new locations and the
   locations of missing items required to achieve the goal.

Functions:
-----------
- parse_location(input_str):
    Parses a location from the user's input string and returns the matching known location if found, or None otherwise.

- parse_items(input_str):
    Parses and returns a list of known items mentioned in the user's input string.

- parse_goal(input_str):
    Parses the user's input to identify a known goal and returns the corresponding internal representation of that goal.

- find_path(prolog, start, end):
    Queries the Prolog knowledge base to find a path between two locations and returns the first found path as a list.
    Returns None if no path is found.

- recommend_actions(location, items, goal):
    The main function that interacts with the Prolog knowledge base. It asserts facts about the user's current state
    (location, items, and goal) and provides a set of recommendations to help the user achieve their goal.
    It identifies missing items or locations needed to achieve the goal and suggests paths or item locations.

- gather_missing_prerequisites(prolog, goal, user_items):
    Recursively gathers any missing items or locations needed to achieve the user's goal based on the Prolog knowledge base.
    Returns a set of missing prerequisites.

- get_item_location(prolog, item):
    Queries the Prolog knowledge base to find the location of a specific item and returns the location if found, or
    None if not.

Usage:
------
1. The user is prompted for their current location, items they possess, and their goal.
2. The program updates the Prolog knowledge base and checks if the goal is achieved.
3. If the goal is not achieved, it provides recommendations for missing prerequisites (e.g., locations to travel to or items to obtain).
4. The system prints instructions to the user based on the current state of the knowledge base.

Example:
--------
User: 'I am in the garden.'
User: 'I have a key and a sword.'
User: 'I want to return the crown.'

System Response:
    - You need to reach the klogg_castle. You can get there via: garden -> bridge -> klogg_castle.
    - You need to obtain the crown, which is located in the tower. You can get there via: garden -> lake -> tower.

"""

from pyswip import Prolog

known_locations = ['garden', 'klogg_castle', 'willie_house', 'dungeon', 'tower', 'lake', 'bridge', 'warehouse',
                   'royal_hall', 'neverhood']


def parse_location(input_str):
    for location in known_locations:
        if location in input_str.lower():
            return location
    return None


def parse_items(input_str):
    known_items = ['key', 'crown', 'crystal', 'trombone', 'chest', 'gauntlet', 'gear', 'map', 'stone', 'sword',
                   'shield', 'peace_crystal']
    items = []
    for item in known_items:
        if item in input_str.lower():
            items.append(item)
    return items


def parse_goal(input_str):
    known_goals = {
        'return crown': 'return_crown',
        'defeat klogg': 'defeat_klogg',
        'beat klogg': 'defeat_klogg',
        'restore peace': 'restore_peace',
        'help klaymen': 'help_klaymen',
        'help hoborg': 'help_hoborg',
        'obtain sword': 'sword',
        'get map': 'map',
        'find shield': 'shield',
        'get peace crystal': 'peace_crystal'
    }
    for key_phrase, goal in known_goals.items():
        if key_phrase in input_str.lower():
            return goal
    return None


def find_path(prolog, start, end):
    query = f"path_exists({start}, {end}, Path)."
    for sol in prolog.query(query):
        path = sol['Path']
        return path  # Return the first found path
    return None


def recommend_actions(location, items, goal):
    prolog = Prolog()
    prolog.consult('~/PycharmProjects/CalcMath/neverhood_kb.pl')

    # Declare dynamic predicates if not already declared
    prolog.assertz(":- dynamic located_in/2")
    prolog.assertz(":- dynamic has/2")
    prolog.assertz(":- dynamic wants/2")
    prolog.assertz(":- dynamic character/1")
    prolog.assertz(":- dynamic obtained/2")

    # Remove previous facts about the user
    prolog.retractall("located_in(user, _)")
    prolog.retractall("has(user, _)")
    prolog.retractall("wants(user, _)")
    prolog.retractall("character(user)")
    prolog.retractall("obtained(user, _)")

    # Add facts about the user
    prolog.assertz("character(user)")
    if location:
        prolog.assertz(f"located_in(user, {location})")
    if items:
        for item in items:
            prolog.assertz(f"has(user, {item})")
    if goal:
        prolog.assertz(f"wants(user, {goal})")

    # Check if the user has achieved their goal
    results = list(prolog.query("achieved_goal(user)."))
    if results:
        print("System: Congratulations! You have achieved your goal.")
        return

    # Recursively gather all missing prerequisites
    missing_prereqs = gather_missing_prerequisites(prolog, goal, items)

    if missing_prereqs:
        print("System: Here are your recommendations:")
        for prereq in missing_prereqs:
            if prereq in items:
                continue  # Already has the item
            elif prereq == location:
                continue  # Already at the location
            elif prereq in known_locations:
                # Provide path to location
                path = find_path(prolog, location, prereq)
                if path:
                    print(f"- You need to reach the {prereq}. You can get there via:")
                    print(" -> ".join(path))
                else:
                    print(f"- The {prereq} is not reachable from your current location.")
            else:
                # It's an item, provide its location
                item_location = get_item_location(prolog, prereq)
                if item_location:
                    path = find_path(prolog, location, item_location)
                    if path:
                        print(f"- You need to obtain the {prereq}, which is located in the {item_location}.")
                        print("  You can get there via:")
                        print(" -> ".join(path))
                    else:
                        print(
                            f"- The {prereq} is located in the {item_location}, but it's not reachable from your current location.")
                else:
                    print(f"- The location of {prereq} is unknown.")
    else:
        print("System: Please provide more details about your situation or goal.")


def gather_missing_prerequisites(prolog, goal, user_items):
    to_process = [goal]
    missing_prereqs = set()
    processed = set()

    while to_process:
        current_goal = to_process.pop()
        if current_goal in processed:
            continue
        processed.add(current_goal)

        # Check if the user has achieved or has the current goal/item
        has_goal = list(prolog.query(f"achieved(user, {current_goal})."))
        has_item = current_goal in user_items

        if has_goal or has_item:
            continue

        # Get necessary items and locations for the current goal
        necessary_items = list(prolog.query(f"necessary_item({current_goal}, Item), Item \\= none."))
        necessary_locations = list(prolog.query(f"necessary_location({current_goal}, Location), Location \\= none."))

        # Add missing items to prerequisites
        for item in necessary_items:
            item_name = item['Item']
            if item_name not in user_items:
                missing_prereqs.add(item_name)
                to_process.append(item_name)

        # Add missing locations to prerequisites
        for loc in necessary_locations:
            location_name = loc['Location']
            if location_name != 'none':
                missing_prereqs.add(location_name)

    return missing_prereqs


def get_item_location(prolog, item):
    item_location_query = list(prolog.query(f"located_in({item}, ItemLocation)."))
    if item_location_query:
        return item_location_query[0]['ItemLocation']
    else:
        return None


if __name__ == "__main__":
    print("System: Which location are you currently in?")
    location_input = input("User: ")
    location = parse_location(location_input)
    if not location:
        print("System: Location not recognized. Please try again.")
        exit()

    print("System: What items do you have?")
    items_input = input("User: ")
    items = parse_items(items_input)

    print("System: What is your goal?")
    goal_input = input("User: ")
    goal = parse_goal(goal_input)
    if not goal:
        print("System: Goal not recognized. Please try again.")
        exit()

    recommend_actions(location, items, goal)
