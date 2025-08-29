package atributes;

public enum Clothes implements Title {
    TROUSERS ("длинные брюки навыпуск"),
    PANTS ("коротенькие штанишки на помочах"),
    DRESS ("пестрое платьице");

    private final String title;

    Clothes(String title){
        this.title = title;
    }
    @Override
    public String getTitle() {
        return title;
    }
}
