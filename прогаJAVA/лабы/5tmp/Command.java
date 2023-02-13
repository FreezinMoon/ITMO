package org.example;

import java.io.IOException;
import java.nio.file.Paths;
import java.text.ParseException;

import static org.example.Main.*;

public class Command {

    public boolean serve(String[] line) throws CoordinatesException, CategoryException, ConstructorException, IOException {


        switch (line[0]) {
            case "help" -> System.out.println(getInfo());
            case "info" -> infoCollection();
            case "show" -> spaceMarines.forEach(System.out::println);
            case "clear" -> clearCollection();
            case "save" -> System.out.println("saved to file");
            case "exit" -> {
                return true;
            }
            case "sort" -> sort();
            case "print_unique_health" -> getUniqueHealth().forEach(System.out::println);
            case "print_field_descending_category" -> printDescendingCategory();
            case "print_field_descending_melee_weapon" -> printDescendingMelee();
            case "execute_script" -> execute(Paths.get(line[1]));
            case "add" -> {
                SpaceMarine spaceMarineToAdd = initSpaceMarine();
                addElement(spaceMarineToAdd);
            }
            case "remove_by_id" -> {
                int rID = Integer.parseInt(line[1]);
                boolean x = removeById(rID);
                if (x) System.out.println(rID + "removed");
                else System.out.println("no such element in collection");
            }
            case "remove_lower" -> {
                SpaceMarine spaceMarine = initSpaceMarine();
                IdComparator idComparator = new IdComparator();
                spaceMarines.removeIf(sm -> idComparator.compare(spaceMarine, sm) > 0);
                System.out.println("Element less than given are removed");
            }
            case "add_if_max" -> {
                sort();
                SpaceMarine spaceMarine = initSpaceMarine();
                IdComparator idComparator = new IdComparator();
                if (idComparator.compare(spaceMarine, spaceMarines.getLast()) > 0) {
                    addElement(spaceMarine);
                    System.out.println("added");
                } else System.out.println("not added");
            }
            case "add_if_min" -> {
                sort();
                SpaceMarine spaceMarine = initSpaceMarine();
                IdComparator idComparator = new IdComparator();
                if (idComparator.compare(spaceMarine, spaceMarines.getFirst()) < 0) {
                    addElement(spaceMarine);
                    System.out.println("added");
                } else System.out.println("not added");
            }
            case "update" -> {
                int rID = Integer.parseInt(line[1]);
                boolean x = removeById(rID);
                if (x) {
                    addElement(initSpaceMarine());
                    System.out.println(rID + "updated");
                } else System.out.println("no such element in collection");
            }
        }
        return false;
    }
}
