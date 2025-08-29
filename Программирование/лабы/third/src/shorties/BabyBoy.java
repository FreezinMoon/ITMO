package shorties;

import atributes.ChangeClothes;
import atributes.Clothes;
import atributes.Haircut;
import shorties.Baby;

import java.util.Objects;

public class BabyBoy extends Baby implements ChangeClothes {
    final Haircut haircut = Haircut.SHORT;

    public BabyBoy(String name, int age, Clothes clothes, double friendliness) {
        super(name, age);
        this.setClothes(clothes);
        this.setFriendliness(friendliness);
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
        String name = this.getName();
        return "В годоре появился " + this.getName() + ", ему " + this.age + " лет." + '\n' + this.getClothes() + '\n' + this.getHaircut() + '\n';
    }

    @Override
    public int hashCode() {
        return super.hashCode() + this.getName().hashCode();
    }
}
