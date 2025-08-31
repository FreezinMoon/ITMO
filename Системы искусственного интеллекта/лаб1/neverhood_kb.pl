% Dynamic predicates
:- dynamic located_in/2.
:- dynamic has/2.
:- dynamic wants/2.
:- dynamic character/1.
:- dynamic obtained/2.

% Characters in the game
character(klaymen).
character(klogg).
character(hoborg).
character(willie_trombone).
character(bill_rhino).
character(robot_billie).
character(mousewalker).
character(dobby_link).
character(gart).
character(klaymen_father).

% Locations in the game
location(neverhood).
location(klogg_castle).
location(willie_house).
location(royal_hall).
location(dungeon).
location(tower).
location(garden).
location(lake).
location(bridge).
location(warehouse).

% Items
item(crown).
item(disk).
item(key).
item(trombone).
item(crystal).
item(chest).
item(gauntlet).
item(gear).
item(map).
item(stone).
item(sword).
item(shield).
item(peace_crystal).

% Relationships between characters
friend(klaymen, willie_trombone).
enemy(klaymen, klogg).
brother(hoborg, klogg).
creator(hoborg, neverhood).
betrayed(klogg, hoborg).
owns(hoborg, crown).
stole(klogg, crown).
guards(gart, klogg_castle).
mentor(willie_trombone, klaymen).
created(hoborg, robot_billie).

% Location of items and characters
located_in(willie_trombone, willie_house).
located_in(crown, klogg_castle).
located_in(key, dungeon).
located_in(trombone, willie_house).
located_in(klaymen, garden).
located_in(crystal, tower).
located_in(hoborg, royal_hall).
located_in(mousewalker, lake).
located_in(robot_billie, warehouse).
located_in(gear, bridge).
located_in(sword, dungeon).
located_in(shield, tower).
located_in(map, lake).
located_in(peace_crystal, royal_hall).

% Characters' goals
wants(klaymen, return_crown).
wants(klaymen, defeat_klogg).
wants(klogg, rule_neverhood).
wants(hoborg, restore_peace).
wants(willie_trombone, help_klaymen).
wants(willie_trombone, help_hoborg).

% Rules

% Rule: A character is a hero if they are not a villain
hero(X) :- character(X), \+ villain(X).

% Rule: A character is a villain if they are an antagonist or a traitor
villain(X) :- antagonist(X).
villain(X) :- betrayed(X, _).

% Definition of antagonist
antagonist(klogg).

% Rule: A character is in danger if their enemy is in the same location
in_danger(X) :- enemy(X, Y), located_in(X, Place), located_in(Y, Place).

% Rule: A character can obtain an item if they are in the same location
can_obtain(X, Item) :- character(X), item(Item), located_in(X, Place), located_in(Item, Place).

% Rule: A character has achieved their goal if they have achieved all required achievements
achieved_goal(X) :- wants(X, Goal), achieved(X, Goal).

% Rule: A character has an item if they obtained it
has(X, Item) :- obtained(X, Item).

% Achieving goals
achieved(X, return_crown) :- has(X, crown).
achieved(X, defeat_klogg) :- defeated(X, klogg).
achieved(hoborg, restore_peace) :- peace_restored.
achieved(willie_trombone, help_klaymen) :- helped(willie_trombone, klaymen).
achieved(X, Goal) :- item_goal(Goal), has(X, Goal).

defeated(klaymen, Y) :- enemy(klaymen, Y), located_in(klaymen, Place), located_in(Y, Place).

% Rule: A character has achieved all their goals if all their goals are achieved
achieved_all_goals(X) :-
    findall(Goal, wants(X, Goal), Goals),
    forall(member(G, Goals), achieved(X, G)).

% Facts about achievements
obtained(klaymen, crown).
obtained(klaymen, key).
obtained(klaymen, crystal).
helped(willie_trombone, klaymen).
peace_restored.

% Paths between locations
path(garden, tower).
path(tower, dungeon).
path(dungeon, klogg_castle).
path(garden, bridge).
path(bridge, klogg_castle).
path(willie_house, garden).
path(lake, garden).
path(warehouse, dungeon).

% Helper predicate to find a path between two locations
find_path(Start, End, Path) :-
    find_path_recursive(Start, End, [Start], PathRev),
    reverse(PathRev, Path).

% Recursive helper predicate
find_path_recursive(End, End, Path, Path).
find_path_recursive(Current, End, Visited, Path) :-
    path(Current, Next),
    \+ member(Next, Visited),
    find_path_recursive(Next, End, [Next|Visited], Path).

% Wrapper predicate to expose find_path/3
path_exists(Start, End, Path) :-
    find_path(Start, End, Path).

% Rule: A character can reach a location if there is a path from their current location
can_reach(X, Location) :-
    located_in(X, CurrentLocation),
    find_path(CurrentLocation, Location, Path),
    Path \= [].

% New goals: obtaining items
item_goal(sword).
item_goal(shield).
item_goal(map).
item_goal(peace_crystal).

% Necessary items for item goals
necessary_item(sword, key).
necessary_item(shield, map).
necessary_item(peace_crystal, none).

% Necessary items for existing goals
necessary_item(defeat_klogg, sword).
necessary_item(return_crown, crown).
necessary_item(restore_peace, peace_crystal).

% Necessary locations for item goals
necessary_location(sword, dungeon).
necessary_location(shield, tower).
necessary_location(peace_crystal, royal_hall).

% Necessary locations for existing goals
necessary_location(defeat_klogg, klogg_castle).
necessary_location(return_crown, klogg_castle).
necessary_location(restore_peace, royal_hall).

% Rule: Determine missing items or locations for achieving the goal
missing_item(X, Goal, Item) :-
    necessary_item(Goal, Item),
    Item \= none,
    \+ has(X, Item).

missing_location(X, Goal, Location) :-
    necessary_location(Goal, Location),
    \+ can_reach(X, Location).

% Rule to find all prerequisites for a goal
prerequisite(Goal, Item) :-
    necessary_item(Goal, Item),
    Item \= none.

prerequisite(Goal, Location) :-
    necessary_location(Goal, Location),
    Location \= none.

% Recursive rule to find prerequisites of prerequisites
all_prerequisites(Goal, Prereq) :-
    prerequisite(Goal, Prereq).

all_prerequisites(Goal, Prereq) :-
    prerequisite(Goal, Intermediate),
    all_prerequisites(Intermediate, Prereq).
