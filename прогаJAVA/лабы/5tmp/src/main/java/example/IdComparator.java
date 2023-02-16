package example; /**
 * @author me
 */



import java.util.Comparator;

public class IdComparator implements Comparator<SpaceMarine> {

    @Override
    public int compare(SpaceMarine sm1, SpaceMarine sm2) {
        return Integer.compare(sm1.getId(), sm2.getId());
    }
}