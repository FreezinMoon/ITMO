package example; /**
 * @author me
 */


import java.time.ZonedDateTime;

public class SpaceMarine {
    private static int counter;
    private final ZonedDateTime creationDate; //Ïîëå íå ìîæåò áûòü null, Çíà÷åíèå ýòîãî ïîëÿ äîëæíî ãåíåðèðîâàòüñÿ àâòîìàòè÷åñêè
    private final int id; //Çíà÷åíèå ïîëÿ äîëæíî áûòü áîëüøå 0, Çíà÷åíèå ýòîãî ïîëÿ äîëæíî áûòü óíèêàëüíûì, Çíà÷åíèå ýòîãî ïîëÿ äîëæíî ãåíåðèðîâàòüñÿ àâòîìàòè÷åñêè
    private float health; //Çíà÷åíèå ïîëÿ äîëæíî áûòü áîëüøå 0
    private String name; //Ïîëå íå ìîæåò áûòü null, Ñòðîêà íå ìîæåò áûòü ïóñòîé
    private Coordinates coordinates; //Ïîëå íå ìîæåò áûòü null
    private AstartesCategory category; //Ïîëå ìîæåò áûòü null
    private Weapon weaponType; //Ïîëå íå ìîæåò áûòü null
    private MeleeWeapon meleeWeapon; //Ïîëå íå ìîæåò áûòü null
    private Chapter chapter; //Ïîëå ìîæåò áûòü null

    private SpaceMarine() {
        this.creationDate = ZonedDateTime.now();
        this.id = ++counter;
    }

    public SpaceMarine(String name, float health, Coordinates coordinates, AstartesCategory category, Weapon weaponType, MeleeWeapon meleeWeapon) {
        this();
        if (health > 0 && name.length() > 0 && coordinates != null && category != null && weaponType != null && meleeWeapon != null) {
            this.health = health;
            this.name = name;
            this.coordinates = coordinates;
            this.category = category;
            this.weaponType = weaponType;
            this.meleeWeapon = meleeWeapon;
        } else throw new NullPointerException("Every argument must be not-null");
    }


    public SpaceMarine(String name, float health, Coordinates coordinates, AstartesCategory category, Weapon weaponType, MeleeWeapon meleeWeapon, Chapter chapter) {
        this(name, health, coordinates, category, weaponType, meleeWeapon);
        this.chapter = chapter;
    }



    @Override
    public String toString() {
        return "SpaceMarine{" + "creationDate=" + creationDate + ", id=" + id + ", health=" + health + ", name='" + name + "', " + coordinates.toString() + ", category=" + category + ", weaponType=" + weaponType + ", meleeWeapon=" + meleeWeapon + ", " + chapter.toString() + '}';
    }

    public String getStringToCSV() {
        return "" + name + "," + health + "," + coordinates.getX() + "," + coordinates.getY() + "," + category + "," + weaponType + "," + meleeWeapon + "," + chapter.getName() + "," + chapter.getMarinesCount();
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