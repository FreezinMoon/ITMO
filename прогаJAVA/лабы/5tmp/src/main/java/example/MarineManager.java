package example; /**
 * @author me
 */


import java.io.*;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardOpenOption;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashSet;
import java.util.Scanner;

import static example.Main.*;


public class MarineManager {


    public void setSpaceMarinesFromFile(String path) throws FileNotFoundException, IllegalArgumentException, NullPointerException {
        scanner = new Scanner(new FileInputStream(path));

        String line;
        while (scanner.hasNext()) {
            line = scanner.nextLine();

            try {
                spaceMarines.add(this.parseSpaceMarine(line));
            } catch (IllegalArgumentException | NullPointerException exception) {
                System.err.println(exception);
            }
        }

        scanner = new Scanner(System.in);
    }


    public void outputFile(String path) throws IOException {
        BufferedWriter bf = Files.newBufferedWriter(Path.of(path), StandardOpenOption.TRUNCATE_EXISTING);
        bf.close();
        BufferedOutputStream outputStream = new BufferedOutputStream(new FileOutputStream(path));

        for (int i = 0; i < spaceMarines.size(); i++) {
            outputStream.write(spaceMarines.get(i).getStringToCSV().getBytes());
            if (i < spaceMarines.size() - 1) outputStream.write('\n');
        }

        outputStream.flush();
        outputStream.close();
    }

    public void execute(Path path) throws IOException {
        scanner = new Scanner(path);
        Command command = new Command();
        boolean isExist1 = false;
        while (scanner.hasNext() && !isExist1) {
            isExist1 = command.serve(scanner.nextLine().split("\\s+"));
        }
        scanner = new Scanner(System.in);
    }

    public void addElement(SpaceMarine spaceMarine) {
        spaceMarines.add(spaceMarine);
    }

    public String getInfo() {
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

    public void clearCollection() {
        spaceMarines.clear();
        System.out.println("Collection is cleared");
    }

    public void sort() {
        IdComparator idComparator = new IdComparator();
        spaceMarines.sort(idComparator);
        System.out.println("Sorted");
    }

    public boolean removeById(int rID) {
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

    public HashSet<Float> getUniqueHealth() {
        HashSet<Float> cur = new HashSet<>();
        for (SpaceMarine elem : spaceMarines) {
            cur.add(elem.getHealth());
        }
        return cur;
    }

    public void printDescendingCategory() {
        String[] arr = new String[spaceMarines.size()];
        for (int i = 0; i < spaceMarines.size(); i++) {
            arr[i] = spaceMarines.get(i).getCategory().name();
        }
        Arrays.sort(arr, Comparator.reverseOrder());
        System.out.println(Arrays.toString(arr));
    }

    public void printDescendingMelee() {
        String[] arr = new String[spaceMarines.size()];
        for (int i = 0; i < spaceMarines.size(); i++) {
            arr[i] = spaceMarines.get(i).getMeleeWeapon().name();
        }
        Arrays.sort(arr, Comparator.reverseOrder());
        System.out.println(Arrays.toString(arr));
    }

    public String initSpaceMarine() {
        String name;
        boolean flag;
        do {
            System.out.print("name: ");
            name = scanner.nextLine();
        } while (name.length() < 1);

        String health;
        float fHealth;
        do {
            System.out.print("health: ");
            health = scanner.nextLine();
            try {
                fHealth = Float.parseFloat(health);
            } catch (Exception e) {
                fHealth = 0f;
                System.out.println("Health must be above zero");
            }
        } while (fHealth <= 0);

        System.out.println("coordinates (x y) ");
        String x;
        double fx;
        do {
            System.out.print("x: ");
            x = scanner.nextLine();
            try {
                fx = Double.parseDouble(x);
            } catch (Exception e) {
                fx = -892.;
                System.out.println("x must be above -892");
            }
        } while (fx <= -892);

        String y;
        do {
            System.out.print("y: ");
            y = scanner.nextLine();
            try {
                Float.parseFloat(y);
                flag = true;
            } catch (Exception e) {
                flag = false;
                System.out.println("y can't be null");
            }
        } while (!flag);


        String category;
        do {
            System.out.print("Astartes category(ASSAULT, INCEPTOR, CHAPLAIN, APOTHECARY): ");
            category = scanner.nextLine();
            try {
                AstartesCategory.valueOf(category);
                flag = true;
            } catch (Exception e) {
                flag = false;
                System.out.println("No such category");
            }
        } while (!flag);

        String weapon;
        do {
            System.out.print("Weapon type(BOLTGUN, HEAVY_BOLTGUN, COMBI_FLAMER, GRAV_GUN, MULTI_MELTA): ");
            weapon = scanner.nextLine();
            try {
                Weapon.valueOf(weapon);
                flag = true;
            } catch (Exception e) {
                flag = false;
                System.out.println("No such category");
            }
        } while (!flag);

        String melee;
        do {
            System.out.print("Melee weapon type(POWER_SWORD, MANREAPER, LIGHTING_CLAW): ");
            melee = scanner.nextLine();
            try {
                MeleeWeapon.valueOf(melee);
                flag = true;
            } catch (Exception e) {
                flag = false;
                System.out.println("No such category");
            }
        } while (!flag);


        StringBuilder marine = new StringBuilder(name + ',' + health + ',' + x + ',' + y + ',' + category + ',' + weapon + ',' + melee);
        Long fCount;
        String chName;
        String count;
        boolean flag2 = true;
        System.out.println("Chapter (name count): ");
        System.out.print("Chapter name: ");
        chName = scanner.nextLine();
        if (chName.length() == 0) {
            flag2 = false;
        }
        if (flag2) {
            marine.append(",").append(chName);
            System.out.print("Count: ");
            count = scanner.nextLine();
            if (count.length() == 0) {
                flag2 = false;
            }
            if (flag2) {
                do {
                    try {
                        fCount = Long.parseLong(count);
                        if (fCount > 0 && fCount <= 1000) {
                            marine.append(",").append(count);
                            flag = true;
                        } else {
                            System.out.println("Illegal argument");
                            flag = false;
                        }
                    } catch (Exception e) {
                        System.out.println("Illegal argument");
                        flag = false;
                    }
                } while (!flag);
            }
        }
        return marine.toString();
    }

    public void infoCollection() {
        System.out.println("Collection info:");
        System.out.println("Collection type: " + spaceMarines.getType());
        System.out.println("Initialization date: " + spaceMarines.getCreationDate());
        System.out.println("Size: " + spaceMarines.size());
    }

    public SpaceMarine parseSpaceMarine(String line) throws IllegalArgumentException, NullPointerException {
        String[] values = line.split(",");

        if (values.length < 7) {
            throw new IllegalArgumentException("IllegalArgumentException");
        }


        String name = values[0];
        float health = Integer.parseInt(values[1]); //Çíà÷åíèå ïîëÿ äîëæíî áûòü áîëüøå 0

        Coordinates coordinates = new Coordinates(values[2], values[3]); //Ïîëå íå ìîæåò áûòü null
        AstartesCategory category = AstartesCategory.valueOf(values[4]); //Ïîëå ìîæåò áûòü null

        Weapon weaponType = Weapon.valueOf(values[5]); //Ïîëå íå ìîæåò áûòü null
        MeleeWeapon meleeWeapon = MeleeWeapon.valueOf(values[6]); //Ïîëå íå ìîæåò áûòü null

        if (values.length == 7) {
            return new SpaceMarine(name, health, coordinates, category, weaponType, meleeWeapon);
        }

        Chapter chapter;
        if (values.length == 8) {
            chapter = new Chapter(values[7]);
        } else {
            chapter = new Chapter(Long.parseLong(values[8]), values[7]);
        }
        return new SpaceMarine(name, health, coordinates, category, weaponType, meleeWeapon, chapter);
    }

    public void add() {
        String spaceMarineToAdd = this.initSpaceMarine();
        SpaceMarine spaceMarine = this.parseSpaceMarine(spaceMarineToAdd);
        spaceMarines.add(spaceMarine);
    }
}