package atributes;

import shorties.Baby;
import shorties.BabyBoy;

public class Healing {
    public void healing(BabyBoy dr, Baby patient) {
        patient.setFriendliness(patient.getFriendliness() + (1 - patient.getFriendliness()) / 2);
        System.out.println(dr.getName() + " вылечил больного " + patient.getName());
    }
}
