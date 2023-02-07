package atributes;

public enum Profession implements Title {
    DOCTOR("доктор"), MECHANIC("механик"), HELPER("помощник"), SCIENTIST("ученый"),
    HUNTER("охотник"), ARTIST("художник"), MUSICIAN("музыкант");

    private final String title;

    Profession(String title) {
        this.title = title;
    }

    @Override
    public String getTitle() {
        return this.title;
    }
}
