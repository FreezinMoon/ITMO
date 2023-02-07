package atributes;

public enum Places implements Title {
    ON_TABLE("на столе"), UNDER_TABLE("под столом"), ON_BED("на кровати"), UNDER_BED("под кроватью");
    private final String title;

    Places(String title) {
        this.title = title;
    }

    @Override
    public String getTitle() {
        return title;
    }
}
