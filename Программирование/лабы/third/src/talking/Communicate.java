package talking;

import shorties.BabyBoy;
import shorties.BabyGirl;

import java.util.Random;
public class Communicate{

    public boolean communicate(BabyBoy boy, BabyGirl girl, String[] badWords) {
        Random random = new Random();
        AbuseBoy abuseBoy = new AbuseBoy();
        AbuseGirl abuseGirl = new AbuseGirl();

        Predicate<Double> reshka = x -> x > 0.5;
        if (reshka.test(Math.random())) {
            System.out.println(girl.getName() + " перешла дорогу, чтобы не встретиться с мальчиком");
            return false;
        }else{
            abuseGirl.abuse(boy, girl, badWords[random.nextInt(badWords.length)]);
            if (reshka.test(boy.getFriendliness())) {
                System.out.println(boy.getName() + " толкнул " + girl.getName());
                System.out.println(boy.getName() + " дернул " + girl.getName() + " за " + girl.getHaircut());
            }
            abuseBoy.abuse(girl, boy, badWords[random.nextInt(badWords.length)]);
            return true;
        }
    }
    @FunctionalInterface
    public interface Predicate<T> {
        boolean test(T t);
    }
}
