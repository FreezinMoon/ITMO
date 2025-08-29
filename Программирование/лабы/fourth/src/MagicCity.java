import atributes.*;
import shorties.*;
import talking.Communicate;
import talking.FamousStory;
import talking.Walk;

import java.util.ArrayList;
import java.util.Objects;
import java.util.Random;

import static atributes.Places.*;

public class MagicCity {
    ArrayList<BabyBoy> arrayBoy = new ArrayList<>();

    ArrayList<BabyGirl> arrayGirl = new ArrayList<>();

    public MagicCity addBoy(BabyBoy boy) {
        arrayBoy.add(boy);
        return this;
    }

    public MagicCity addGirl(BabyGirl girl) {
        arrayGirl.add(girl);
        return this;
    }

    public void start(String[] badWords) {

        Random random = new Random();
        arrayBoy.forEach(System.out::println);

        arrayGirl.forEach(babyGirl -> {
            System.out.println("В годоре появилась " + babyGirl.getName());
            System.out.println(babyGirl.getClothes());
            System.out.println(babyGirl.getHaircut() + '\n');
        });

        ChangeHaircut changeHaircut = new ChangeHaircut();
        changeHaircut.change(Haircut.TAIL, arrayGirl.get(random.nextInt(arrayGirl.size())));
        changeHaircut.change(Haircut.RIBBON, arrayGirl.get(random.nextInt(arrayGirl.size())));
        changeHaircut.change(Haircut.BOW, arrayGirl.get(random.nextInt(arrayGirl.size())));
        changeHaircut.change(Haircut.SHORT, arrayGirl.get(random.nextInt(arrayGirl.size())));
        System.out.println();

        Communicate com = new Communicate();
        BabyBoy randBoy = arrayBoy.get(random.nextInt(arrayBoy.size()));
        BabyGirl randGirl = arrayGirl.get(random.nextInt(arrayGirl.size()));
        com.communicate(randBoy, randGirl, badWords);
    }

    public void start2() {
        Znaika znaika = new Znaika();
        System.out.println("Здесь живет " + znaika.getName());
        Book book = new Book("Пушкин", "Сказка о Попе и работнике его Балде");
        book.setPlace(UNDER_TABLE);
        book.setPlace(ON_BED);
        book.setPlace(UNDER_BED);
        book.readBooks(znaika);
        znaika.getClothes();
        znaika.getProfession();

        Pilulkin pilulkin = new Pilulkin();
        System.out.println("Здесь живет " + pilulkin.getName());
        pilulkin.getProfession();
        pilulkin.getClothes();
        Vintik vintik = new Vintik();
        new Healing().healing(pilulkin, vintik);


        Pulka pulka = new Pulka();
        System.out.println("Здесь живет " + pulka.getName());
        pulka.getProfession();
        Dog dog = new Dog();
        System.out.println("У Пульки есть маленькая собачка - " + dog.getName());
        Gun gun = new Gun(pulka);
        Hunt hunt = new Hunt(pulka, dog, gun);
        hunt.hunting();

        Shpuntik shpuntik = new Shpuntik();
        System.out.println("Здесь живут " + vintik.getName() + " и " + shpuntik.getName());
        vintik.getProfession();
        shpuntik.getProfession();
        Repair repair = new Repair();
        repair.repair(vintik, shpuntik, gun);

        Syropchik syropchik = new Syropchik();
        System.out.println("Здесь живет " + syropchik.getName());
        syropchik.setName("Сиропчик");
        Drinkable d = new Drinkable() {
            @Override
            public void drink(Syropchik syropchik) {
                System.out.println("Сиропчик пьет сладкую газированную воду");
            }
        };
        d.drink(syropchik);

        Tubik tubik = new Tubik();
        System.out.println("Здесь живет " + tubik.getName());
        tubik.getProfession();

        Guslya guslya = new Guslya();
        System.out.println("Здесь живет " + guslya.getName());
        guslya.getProfession();

        BabyBoy tor = new BabyBoy("Торопыжка", 8);
        BabyBoy vorchun = new BabyBoy("Ворчун", 8);
        BabyBoy molchun = new BabyBoy("Молчун", 8);
        BabyBoy ponchik = new BabyBoy("Пончик", 8);
        BabyBoy rast = new BabyBoy("Растеряйка", 8);
        BabyBoy avos = new BabyBoy("Авоська", 8);
        BabyBoy nebos = new BabyBoy("Небоська", 8);
        System.out.println("Также здесь живут: " + tor.getName() + ", " + vorchun.getName() + ", " + molchun.getName() + ", " + ponchik.getName() + ", " + rast.getName() + ", " + avos.getName() + ", " + nebos.getName());

        Neznaika neznaika = new Neznaika();
        System.out.println("Еще здесь живет " + neznaika.getName());
        System.out.println("Его знания оцениваются в " + neznaika.getKnowledge() + " у.е.");
        neznaika.getClothes();
        Communicate com = new Communicate();
        BabyGirl randGirl = new BabyGirl("девочка", 5, Haircut.BOW);
        com.communicate(neznaika, randGirl, new String[]{"дурилка", "вонючка"});
        Walk walk = new Walk(neznaika, new BabyBoy("Гунька", 6));
        walk.walk();
        for (int i = 0; i < 10; i++) {
            walk.argue();
            walk.reconcile();
        }
        walk.tellStory();
        FamousStory famousStory = new FamousStory(neznaika);
        famousStory.tell();
        Street.Building building = new Street.Building();
        building.addBaby(znaika).addBaby(pilulkin).addBaby(pulka).addBaby(vintik).addBaby(shpuntik).addBaby(syropchik).addBaby(tubik).addBaby(guslya).addBaby(tor).addBaby(vorchun).addBaby(molchun).addBaby(ponchik).addBaby(rast).addBaby(avos).addBaby(nebos).addBaby(neznaika);
    }


    @Override
    public String toString() {
        return "Вольшебный город{" + "малыши=" + arrayBoy + ", малышки=" + arrayGirl + '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof MagicCity magicCity)) return false;
        return arrayBoy.equals(magicCity.arrayBoy) && arrayGirl.equals(magicCity.arrayGirl);
    }

    @Override
    public int hashCode() {
        return Objects.hash(arrayBoy, arrayGirl);
    }

    static class Street {

        static class Building {
            private final ArrayList<Baby> barray = new ArrayList<>();

            public Building addBaby(Baby baby) {
                this.barray.add(baby);
                return this;
            }

            public ArrayList<Baby> getBarray() {
                return barray;
            }

            public String getName() {
                return "Kolokolchikov";
            }
        }
    }
}
