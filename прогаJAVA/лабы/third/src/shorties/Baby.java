package shorties;

import atributes.Clothes;
import atributes.Haircut;

public abstract class Baby {
    private final String name;
    public final int age;
    private Haircut haircut = Haircut.SHORT;

    private Clothes clothes = Clothes.DRESS;
    private double fr = 1;

    public Baby(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return this.name;
    }

    public void setHaircut(Haircut haircut) {
        this.haircut = haircut;
    }

    public String getHaircut() {
        return name + " носит на голове " + haircut.getTitle();
    }

    public void setClothes(Clothes clothes) {
        this.clothes = clothes;
    }

    public String getClothes() {
        return name + " носит " + clothes.getTitle();
    }

    public void setFriendliness(double fr) {
        this.fr = Math.abs(fr) % 1;
    }

    public double getFriendliness() {
        return fr;
    }

}
