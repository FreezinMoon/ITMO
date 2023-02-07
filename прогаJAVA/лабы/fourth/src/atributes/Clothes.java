package atributes;

public enum Clothes implements Title {
    TROUSERS ("длинные брюки навыпуск"),
    PANTS ("коротенькие штанишки на помочах"),
    BLACK_SUIT("Черный костюм"),
    MEDICAL_SUIT("Белый халат с колпаком"),
    COLOURFUL_SUIT("голубая шляпа, желтые, канареечные, брюки и оранжевая рубашка с зеленым галстуком"),
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
