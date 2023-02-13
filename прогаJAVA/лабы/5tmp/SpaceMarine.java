package org.example;

import java.time.ZonedDateTime;

public class SpaceMarine{
    private static int counter;
    private final java.time.ZonedDateTime creationDate; //Поле не может быть null, Значение этого поля должно генерироваться автоматически
    private final int id; //Значение поля должно быть больше 0, Значение этого поля должно быть уникальным, Значение этого поля должно генерироваться автоматически
    private float health; //Значение поля должно быть больше 0
    private String name; //Поле не может быть null, Строка не может быть пустой
    private Coordinates coordinates; //Поле не может быть null
    private AstartesCategory category; //Поле может быть null
    private Weapon weaponType; //Поле не может быть null
    private MeleeWeapon meleeWeapon; //Поле не может быть null
    private Chapter chapter; //Поле может быть null

    public SpaceMarine() {
        counter++;
        this.creationDate = ZonedDateTime.now();
        this.id = counter;
    }

    public SpaceMarine(float health, String name, Coordinates coordinates, AstartesCategory category, Weapon weaponType, MeleeWeapon meleeWeapon) throws ConstructorException {
        if (health > 0 && name.length() > 0 && coordinates != null && category != null && weaponType != null && meleeWeapon != null) {
            counter++;
            this.creationDate = ZonedDateTime.now();
            this.id = counter;
            this.health = health;
            this.name = name;
            this.coordinates = coordinates;
            this.category = category;
            this.weaponType = weaponType;
            this.meleeWeapon = meleeWeapon;
        }else
            throw new ConstructorException("Every argument must be not-null");
    }

    public SpaceMarine(float health, String name, Coordinates coordinates, AstartesCategory category, Weapon weaponType, MeleeWeapon meleeWeapon, Chapter chapter) throws ConstructorException {
        if (health > 0 && name.length() > 0 && coordinates != null && category != null && weaponType != null && meleeWeapon != null) {
            counter++;
            this.creationDate = ZonedDateTime.now();
            this.id = counter;
            this.health = health;
            this.name = name;
            this.coordinates = coordinates;
            this.category = category;
            this.weaponType = weaponType;
            this.meleeWeapon = meleeWeapon;
            this.chapter = chapter;
        }else
            throw new ConstructorException("Every argument except chapter must be not-null");
    }

    @Override
    public String toString() {
        return "SpaceMarine{" +
                "creationDate=" + creationDate +
                ", id=" + id +
                ", health=" + health +
                ", name='" + name + '\'' +
                coordinates.toString() +
                ", category=" + category +
                ", weaponType=" + weaponType +
                ", meleeWeapon=" + meleeWeapon +
                ", chapter=" + chapter +
                '}';
    }

    public Chapter getChapter() {
        return chapter;
    }

    public MeleeWeapon getMeleeWeapon() {
        return meleeWeapon;
    }

    public Weapon getWeaponType() {
        return weaponType;
    }

    public AstartesCategory getCategory() {
        return category;
    }

    public Coordinates getCoordinates() {
        return coordinates;
    }

    public String getName() {
        return name;
    }

    public float getHealth() {
        return health;
    }

    public int getId() {
        return id;
    }

    public ZonedDateTime getCreationDate() {
        return creationDate;
    }
}