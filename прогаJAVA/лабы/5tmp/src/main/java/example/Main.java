/**
 * @author me
 */


package example;


import java.io.IOException;
import java.util.*;


public class Main {



    public static MyLinkedList spaceMarines = new MyLinkedList();
    public static Scanner scanner;
    public static String[] savedArgs;


    public static void main(String[] args) throws IOException {

        savedArgs = args;

        MarineManager marineManager = new MarineManager();
        marineManager.setSpaceMarinesFromFile("/home/jasos/IdeaProjects/fifth/src/file.csv"); // savedArgs[0]

        boolean isExist = false;
        Command command = new Command();
        scanner = new Scanner(System.in);
        while (!isExist) {
            System.out.print("> ");
            String[] line = scanner.nextLine().split(" ");
            isExist = command.serve(line);
        }
        scanner.close();
    }
}