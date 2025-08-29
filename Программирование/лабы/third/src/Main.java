import atributes.Clothes;
import atributes.Haircut;
import shorties.BabyBoy;
import shorties.BabyGirl;


public class Main {
    public static void main(String[] args) {
        BabyBoy b1 = new BabyBoy("Незнайка", 5, Clothes.PANTS, 0.25);
        BabyGirl g1 = new BabyGirl("Кнопочка", 6, Haircut.BOW);
        BabyBoy b2 = new BabyBoy("Знайка", 7, Clothes.TROUSERS, 0.55);
        BabyGirl g2 = new BabyGirl("Голубоглазка", 8, Haircut.TAIL);
        BabyBoy b3 = new BabyBoy("Гунька", 9, Clothes.PANTS, 0.4);
        BabyGirl g3 = new BabyGirl("Мушка", 10, Haircut.RIBBON);
        String[] badWords = {"мудила", "клоп", "тупица", "вонючка", "имбицил"};

        MagicCity magicCity = new MagicCity();

        magicCity.addBoy(b1).addGirl(g1).addBoy(b2).addGirl(g2).addBoy(b3).addGirl(g3).start(badWords);
    }
}
