package example;

/**
 * @author me
 */



public class Chapter {
    private final String name; //Ïîëå íå ìîæåò áûòü null, Ñòðîêà íå ìîæåò áûòü ïóñòîé
    private Long marinesCount; //Ïîëå ìîæåò áûòü null, Çíà÷åíèå ïîëÿ äîëæíî áûòü áîëüøå 0, Ìàêñèìàëüíîå çíà÷åíèå ïîëÿ: 1000

    public Chapter(Long marinesCount, String name) {
        this.name = name;
        this.marinesCount = marinesCount;
    }

    public Chapter(String name) {
        this.name = name;
    }

    public Chapter(String marinesCount, String name) {
        this(Long.parseLong(marinesCount), name);
    }

    public Long getMarinesCount() {
        return marinesCount;
    }

    public String getName() {
        return name;
    }

    @Override
    public String toString() {
        return "Chapter{" + "name='" + name + '\'' + ", marinesCount=" + marinesCount + '}';
    }
}