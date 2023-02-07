package talking;

import shorties.Baby;
import talking.Abuse;

public class AbuseGirl implements Abuse {
    @Override
    public void abuse(Baby boy, Baby girl, String badWord) {
        System.out.println(boy.getName() + " обзывается: " + girl.getName() + ", ты " + badWord);
    }
}
