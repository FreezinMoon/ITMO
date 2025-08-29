package atributes;

import shorties.Dog;
import shorties.Pulka;

public class Hunt {
    private final Pulka pulka;
    private final Dog dog;
    private final Gun gun;

    public Hunt(Pulka pulka, Dog dog, Gun gun) {
        this.dog = dog;
        this.pulka = pulka;
        this.gun = gun;
    }

    public void hunting() throws ShootException {
        System.out.println(dog.getName() + " и " + pulka.getName() + " вышли на охоту...");
        Gun.Trigger trigger = this.gun.new Trigger();
        try {
            trigger.pull();
        } catch (Exception e) {
            System.out.println(e.getMessage());
        } finally {
            gun.reload();
            trigger.pull();
        }
    }
}
