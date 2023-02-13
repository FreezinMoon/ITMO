package org.example;

public enum AstartesCategory {
    ASSAULT("ASSAULT"), INCEPTOR("INCEPTOR"), CHAPLAIN("CHAPLAIN"), APOTHECARY("APOTHECARY");
    private final String title;

    AstartesCategory(String title) {
        this.title = title;
    }

    public String getTitle() {
        return this.title;
    }
}