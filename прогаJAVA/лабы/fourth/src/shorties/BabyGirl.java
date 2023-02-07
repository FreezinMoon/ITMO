package shorties;

import atributes.ChangeClothes;
import atributes.Clothes;
import atributes.Haircut;
import java.util.Objects;

public class BabyGirl extends Baby implements ChangeClothes {
    final Clothes clothes = Clothes.DRESS;
    public BabyGirl(String name, int age, Haircut haircut) {
        super(name, age);
        this.setHaircut(haircut);
    }
    @Override
    public Baby changeClothes(Clothes clothes){
        switch (clothes) {
            case DRESS -> {
                System.out.println(this.getName() + " надела пестрое платьице");
                this.setClothes(clothes);
            }
            case PANTS, TROUSERS -> System.out.println(this.getName() + " носит только пестрые платьица");
        }
        return this;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof BabyGirl babyGirl)) return false;
        return Objects.equals(getName(), babyGirl.getName());
    }

    @Override
    public String toString() {
        return "Малышка '" + this.getName();
    }

    @Override
    public int hashCode() {
        return super.hashCode() + this.getName().hashCode();
    }
}
