package atributes;

import shorties.BabyBoy;

public class Book {
    private final String author;
    private final String title;
    private Places place;

    public Book(String author, String title) {
        this.author = author;
        this.title = title;
    }

    public Places getPlace() {
        return place;
    }

    public void setPlace(Places place) {
        this.place = place;
        System.out.println("Книга лежит " + place.getTitle());

    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        title = title;
    }

    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        author = author;
    }

    public void readBooks(BabyBoy babyBoy) {
        this.setPlace(Places.ON_TABLE);
        babyBoy.setKnowledge(babyBoy.getKnowledge() + ((1 - babyBoy.getKnowledge()) / 2));
        System.out.println(babyBoy.getName() + " надел очки и читает книгу " + this.title);
        System.out.println("Теперь его знание оценивается в " + babyBoy.getKnowledge() + " у.е.");
    }
}
