package atributes;

import shorties.BabyGirl;

public class ChangeHaircut implements ChangeHaircutInterface {
    @Override
    public boolean change(Haircut haircut, BabyGirl shorty){
        switch (haircut) {
            case SHORT -> {
                System.out.println(shorty.getName() + " не носит короткие прически");
                return false;
            }
            case TAIL -> {
                System.out.println(shorty.getName() + " сделала прическу 'хвостик'");
                shorty.setHaircut(haircut);
            }
            case RIBBON -> {
                System.out.println(shorty.getName() + " сделала прическу с ленточками");
                shorty.setHaircut(haircut);
            }
            case BOW -> {
                System.out.println(shorty.getName() + " сделала прическу с бантиком");
                shorty.setHaircut(haircut);
            }
        }
        return true;
    }
}
