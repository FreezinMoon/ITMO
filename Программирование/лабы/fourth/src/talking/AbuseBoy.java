package talking;

import shorties.Baby;
import talking.Abuse;

public class AbuseBoy implements Abuse {
    @Override
    public void abuse(Baby girl, Baby boy, String badWord) {
        System.out.println(girl.getName() + " обзывается: " + boy.getName() + ", ты забияка и " + badWord);
    }
}
