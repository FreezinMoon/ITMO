package atributes;

import shorties.Shpuntik;
import shorties.Vintik;

public class Repair {

    public void repair(Vintik mechanik, Shpuntik helper, Gun object){
        System.out.println(mechanik.getName() + " и " + helper.getName() + " починили ружьё");
        object.setStamina(20);
    }
}
