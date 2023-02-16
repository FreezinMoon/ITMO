package example; /**
 * @author me
 */



import java.io.IOException;
import java.nio.file.Paths;

import static example.Main.savedArgs;
import static example.Main.spaceMarines;

public class Command {


    public boolean serve(String[] line) throws IOException {

        MarineManager manager = new MarineManager();


        switch (line[0]) { // паттерн Команда
            case "help" -> System.out.println(manager.getInfo());
            case "info" -> manager.infoCollection();
            case "show" -> spaceMarines.forEach(System.out::println);
            case "clear" -> manager.clearCollection();
            case "save" -> manager.outputFile("/home/jasos/IdeaProjects/fifth/src/file.csv"); // savedArgs[0]
            case "exit" -> {
                return true;
            }
            case "sort" -> manager.sort();
            case "print_unique_health" -> manager.getUniqueHealth().forEach(System.out::println);
            case "print_field_descending_category" -> manager.printDescendingCategory();
            case "print_field_descending_melee_weapon" -> manager.printDescendingMelee();
            case "execute_script" -> manager.execute(Paths.get(line[1]));
            case "add" -> manager.add();
            case "remove_by_id" -> {
                try {
                    String id = line[1];
                    int rID = Integer.parseInt(line[1]);
                    boolean x = manager.removeById(rID);
                    if (x) System.out.println(rID + " removed");
                    else System.out.println("no such element in collection");
                } catch (Exception e) {
                    System.out.println("illegal id");
                }
            }
            case "remove_lower" -> {
                String spaceMarineToAdd = manager.initSpaceMarine();
                SpaceMarine spaceMarine = manager.parseSpaceMarine(spaceMarineToAdd);
                IdComparator idComparator = new IdComparator();
                spaceMarines.removeIf(sm -> idComparator.compare(spaceMarine, sm) > 0);
                System.out.println("Element less than given are removed");
            }
            case "add_if_max" -> {
                manager.sort();
                String spaceMarineToAdd = manager.initSpaceMarine();
                SpaceMarine spaceMarine = manager.parseSpaceMarine(spaceMarineToAdd);
                IdComparator idComparator = new IdComparator();
                if (idComparator.compare(spaceMarine, spaceMarines.getLast()) > 0) {
                    spaceMarines.add(spaceMarine);
                    System.out.println("added");
                } else System.out.println("not added");
            }
            case "add_if_min" -> {
                manager.sort();
                String spaceMarineToAdd = manager.initSpaceMarine();
                SpaceMarine spaceMarine = manager.parseSpaceMarine(spaceMarineToAdd);
                IdComparator idComparator = new IdComparator();
                if (idComparator.compare(spaceMarine, spaceMarines.getFirst()) < 0) {
                    spaceMarines.add(spaceMarine);
                    System.out.println("added");
                } else System.out.println("not added");
            }
            case "update" -> {
                int rID = Integer.parseInt(line[1]);
                boolean x = manager.removeById(rID);
                if (x) {
                    manager.add();
                    System.out.println(rID + "updated");
                } else System.out.println("no such element in collection");
            }
            default -> System.out.println("No such command");
        }
        return false;
    }

}
