package example; /**
 * @author me
 */



import java.time.ZonedDateTime;
import java.util.LinkedList;

public class MyLinkedList extends LinkedList<SpaceMarine> { //todo подумать над композицией и идеей обертки
    private final java.time.ZonedDateTime creationDate;
    MyLinkedList(){
        super();
        this.creationDate = ZonedDateTime.now();
    }
    public java.time.ZonedDateTime getCreationDate(){
        return creationDate;
    }
    public String getType(){
        return "java.util.LinkedList<org.example.SpaceMarine>";
    }
}
