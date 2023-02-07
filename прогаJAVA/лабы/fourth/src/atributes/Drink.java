package atributes;

import shorties.Syropchik;

public class Drink implements Drinkable{

    @Override
    public void drink(Syropchik syropchik) {
        System.out.println(syropchik.getName()+" пьет газированную воду с сиропом");
    }
}
