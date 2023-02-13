package org.example;

import org.jetbrains.annotations.Contract;
import org.jetbrains.annotations.NotNull;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashSet;
import java.util.Scanner;


public class Main {


    static Scanner scanner = new Scanner(System.in);
    static MyLinkedList<SpaceMarine> spaceMarines = new MyLinkedList<>();

    public static void main(String[] args) throws IOException, CoordinatesException, ConstructorException, CategoryException {
        Scanner scannerFile = new Scanner(Paths.get("/home/jasos/IdeaProjects/FifthUngradle/src/org/example/file.csv"));
        scannerFile.useDelimiter(System.getProperty("line.separator"));
        while (scannerFile.hasNext()) {
            SpaceMarine spaceMarine = parseCSVLine(scannerFile.next());
            addElement(spaceMarine);
        }
        scannerFile.close();

        boolean isExist = false;
        Command command = new Command();
        while (!isExist) {
            String[] line = scanner.nextLine().split("\\s+");
            isExist = command.serve(line);
        }
    }

    static void execute(Path path) throws IOException, CoordinatesException, CategoryException, ConstructorException {
        Scanner scanner1 = new Scanner(path);
        Command command = new Command();
        boolean isExist = false;
        while (scanner1.hasNext() || !isExist) {
            isExist = command.serve(scanner1.nextLine().split("\\s+"));
        }
    }

    private static SpaceMarine parseCSVLine(String line) throws ConstructorException, CategoryException, CoordinatesException {
        Scanner scanner = new Scanner(line);
        scanner.useDelimiter(",");
        String name = scanner.next();
        float health = scanner.nextFloat();
        double x = scanner.nextDouble();
        Float y = scanner.nextFloat();
        Coordinates coordinates = new Coordinates(x, y);
        String cat = scanner.next();
        AstartesCategory astartesCategory = setCategory(cat);
        String wt = scanner.next();
        Weapon weapon = setWeaponType(wt);
        String mw = scanner.next();
        MeleeWeapon meleeWeapon = setMeleeWeapon(mw);
        Chapter chapter;
        if (scanner.hasNext()) {
            String chName = scanner.next();
            if (scanner.hasNext()) {
                Long hz = scanner.nextLong();
                chapter = new Chapter(hz, chName);
            } else {
                chapter = new Chapter(chName);
            }
            scanner.close();
            return new SpaceMarine(health, name, coordinates, astartesCategory, weapon, meleeWeapon, chapter);
        }
        scanner.close();
        return new SpaceMarine(health, name, coordinates, astartesCategory, weapon, meleeWeapon);
    }

    public static void addElement(SpaceMarine spaceMarine) {
        spaceMarines.add(spaceMarine);
    }

    public static String getInfo() {
        return """
                help : вывести справку по доступным командам
                info : вывести в стандартный поток вывода информацию о коллекции (тип, дата инициализации, количество элементов и т.д.)
                show : вывести в стандартный поток вывода все элементы коллекции в строковом представлении
                add {element} : добавить новый элемент в коллекцию
                update id {element} : обновить значение элемента коллекции, id которого равен заданному
                remove_by_id id : удалить элемент из коллекции по его id
                clear : очистить коллекцию
                save : сохранить коллекцию в файл
                execute_script file_name : считать и исполнить скрипт из указанного файла. В скрипте содержатся команды в таком же виде, в котором их вводит пользователь в интерактивном режиме.
                exit : завершить программу (без сохранения в файл)
                add_if_max {element} : добавить новый элемент в коллекцию, если его значение превышает значение наибольшего элемента этой коллекции
                add_if_min {element} : добавить новый элемент в коллекцию, если его значение меньше, чем у наименьшего элемента этой коллекции
                remove_lower {element} : удалить из коллекции все элементы, меньшие, чем заданный
                print_unique_health : вывести уникальные значения поля health всех элементов в коллекции
                print_field_descending_category : вывести значения поля category всех элементов в порядке убывания
                print_field_descending_melee_weapon : вывести значения поля meleeWeapon всех элементов в порядке убывания""";
    }

    public static void clearCollection() {
        spaceMarines.clear();
        System.out.println("Collection is cleared");
    }

    public static void sort() {
        IdComparator idComparator = new IdComparator();
        spaceMarines.sort(idComparator);
        System.out.println("Sorted");
    }

    public static AstartesCategory setCategory(@NotNull String s) throws CategoryException {
        return switch (s) {
            case "ASSAULT" -> AstartesCategory.ASSAULT;
            case "INCEPTOR" -> AstartesCategory.INCEPTOR;
            case "CHAPLAIN" -> AstartesCategory.CHAPLAIN;
            case "APOTHECARY" -> AstartesCategory.APOTHECARY;
            default -> throw new CategoryException("no such category");
        };
    }

    public static MeleeWeapon setMeleeWeapon(String s) throws CategoryException {
        return switch (s) {
            case "POWER_SWORD" -> MeleeWeapon.POWER_SWORD;
            case "MANREAPER" -> MeleeWeapon.MANREAPER;
            case "LIGHTING_CLAW" -> MeleeWeapon.LIGHTING_CLAW;
            default -> throw new CategoryException("no such melee weapon");
        };
    }

    public static Weapon setWeaponType(@NotNull String s) throws CategoryException {
        return switch (s) {
            case "BOLTGUN" -> Weapon.BOLTGUN;
            case "HEAVY_BOLTGUN" -> Weapon.HEAVY_BOLTGUN;
            case "COMBI_FLAMER" -> Weapon.COMBI_FLAMER;
            case "GRAV_GUN" -> Weapon.GRAV_GUN;
            case "MULTI_MELTA" -> Weapon.MULTI_MELTA;
            default -> throw new CategoryException("no such weapon");
        };
    }

    public static boolean removeById(int rID) {
        boolean flag = false;
        for (int i = 0; i < spaceMarines.size(); i++) {
            if (spaceMarines.get(i).getId() == rID) {
                spaceMarines.remove(i);
                flag = true;
                break;
            }
        }
        return flag;
    }

    public static @NotNull HashSet<Float> getUniqueHealth() {
        HashSet<Float> cur = new HashSet<>();
        for (SpaceMarine elem : spaceMarines) {
            cur.add(elem.getHealth());
        }
        return cur;
    }

    public static <E> void printSet(@NotNull HashSet<E> hashSet) {
        for (E elem : hashSet)
            System.out.println(elem);
    }

    public static void printDescendingCategory() {
        String[] arr = new String[spaceMarines.size()];
        for (int i = 0; i < spaceMarines.size(); i++) {
            arr[i] = spaceMarines.get(i).getCategory().getTitle();
        }
        Arrays.sort(arr, Comparator.reverseOrder());
        System.out.println(Arrays.toString(arr));
    }

    public static void printDescendingMelee() {
        String[] arr = new String[spaceMarines.size()];
        for (int i = 0; i < spaceMarines.size(); i++) {
            arr[i] = spaceMarines.get(i).getMeleeWeapon().getTitle();
        }
        Arrays.sort(arr, Comparator.reverseOrder());
        System.out.println(Arrays.toString(arr));
    }

    @Contract(" -> new")
    public static @NotNull SpaceMarine initSpaceMarine() throws CategoryException, CoordinatesException, ConstructorException {
        System.out.print("name: ");
        String name = scanner.nextLine();
        System.out.print("health: ");
        float health = scanner.nextFloat();
        System.out.println("coordinates (x y) ");
        System.out.print("x: ");
        double x = scanner.nextDouble();
        System.out.print("y: ");
        float y = scanner.nextFloat();
        Coordinates coordinates = new Coordinates(x, y);
        System.out.println();
        System.out.print("Astartes category(ASSAULT, INCEPTOR, CHAPLAIN, APOTHECARY): ");
        String astr = scanner.next();
        AstartesCategory category = setCategory(astr);
        System.out.print("Weapon type(BOLTGUN, HEAVY_BOLTGUN, COMBI_FLAMER, GRAV_GUN, MULTI_MELTA): ");
        Weapon weapon = setWeaponType(scanner.next());
        System.out.print("Melee weapon type(POWER_SWORD, MANREAPER, LIGHTING_CLAW): ");
        MeleeWeapon meleeWeapon = setMeleeWeapon(scanner.next());
        return new SpaceMarine(health, name, coordinates, category, weapon, meleeWeapon);
    }

    public static void infoCollection() {
        System.out.println("Collection info:");
        System.out.println("Collection type: " + spaceMarines.getType());
        System.out.println("Initialization date: " + spaceMarines.getCreationDate());
        System.out.println("Size: " + spaceMarines.size());
    }
}
