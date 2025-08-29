package shorties;

import atributes.Clothes;
import atributes.Haircut;
import atributes.Profession;

public abstract class Baby {
    protected String name;
    private Profession profession;
    private Haircut haircut = Haircut.SHORT;
    private Clothes clothes = Clothes.DRESS;
    private double fr = 1;

    public Baby(String name, int age) {
        this.name = name;
    }
    public Baby(String name, int age, Profession profession) {
        this.name = name;
        this.profession = profession;
    }
    public void getProfession() {
        System.out.println(this.getName() + " - " + profession.getTitle());
    }

    public void setProfession(Profession profession) {
        this.profession = profession;
    }

    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getHaircut() {
        return name + " носит на голове " + haircut.getTitle();
    }

    public void setHaircut(Haircut haircut) {
        this.haircut = haircut;
    }

    public String getClothes() {
        return name + " носит " + clothes.getTitle();
    }

    public void setClothes(Clothes clothes) {
        this.clothes = clothes;
    }

    public double getFriendliness() {
        return fr;
    }

    public void setFriendliness(double fr) {
        this.fr = Math.abs(fr) % 1;
    }

}
