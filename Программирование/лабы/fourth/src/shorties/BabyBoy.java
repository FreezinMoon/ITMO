package shorties;

import atributes.ChangeClothes;
import atributes.Clothes;
import atributes.Haircut;
import atributes.Profession;

import java.util.Objects;

public class BabyBoy extends Baby implements ChangeClothes {
    final Haircut haircut = Haircut.SHORT;
    private double knowledge;

    public BabyBoy(String name, int age, Clothes clothes, double friendliness) {
        super(name, age);
        this.setClothes(clothes);
        this.setFriendliness(friendliness);
    }
    public BabyBoy(String name, int age, Clothes clothes, double friendliness, Profession profession) {
        super(name, age, profession);
        this.setClothes(clothes);
        this.setFriendliness(friendliness);
    }


    public BabyBoy(String name, int age, double friendliness, Profession profession) {
        super(name, age, profession);
        this.setFriendliness(friendliness);
    }

    public BabyBoy(String name, int age, double friendliness) {
        super(name, age);
        this.setFriendliness(friendliness);
    }

    public BabyBoy(String name, int age) {
        super(name, age);
    }

    public double getKnowledge() {
        return knowledge;
    }

    public void setKnowledge(Double knowledge) {
        if (0 <= knowledge && knowledge <= 1) {
            this.knowledge = knowledge;
        } else {
            System.out.println("invalid value (0-1 required)");
        }
    }

    @Override
    public Baby changeClothes(Clothes clothes) {
        switch (clothes) {
            case DRESS -> System.out.println(this.getName() + " носит только штаны или брюки");
            case PANTS, TROUSERS -> {
                this.setClothes(clothes);
                System.out.println(this.getName() + " надел " + clothes.getTitle());
            }
        }
        return this;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof BabyBoy babyBoy)) return false;
        return Objects.equals(getName(), babyBoy.getName());
    }

    @Override
    public String toString() {
        return "В годоре появился " + this.getName() + "." + '\n' + this.getClothes() + '\n' + this.getHaircut() + '\n';
    }

    @Override
    public int hashCode() {
        return super.hashCode() + this.getName().hashCode();
    }
}
