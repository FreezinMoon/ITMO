package org.example;

public enum MeleeWeapon {
    POWER_SWORD("POWER_SWORD"), MANREAPER("MANREAPER"), LIGHTING_CLAW("LIGHTING_CLAW");
    private final String title;

    MeleeWeapon(String title) {
        this.title = title;
    }

    public String getTitle() {
        return title;
    }
}