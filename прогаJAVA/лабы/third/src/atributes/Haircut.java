package atributes;

public enum Haircut implements Title {
    SHORT ("короткие волосы"),
    TAIL ("косы"),
    RIBBON ("ленточки"),
    BOW ("хвостик");

    private final String title;

    Haircut(String title){
        this.title = title;
    }
    @Override
    public String getTitle() {
        return title;
    }
}
