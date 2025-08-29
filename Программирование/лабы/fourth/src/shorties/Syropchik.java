package shorties;

public class Syropchik extends BabyBoy {
    public Syropchik() {
        super("Сахарин Сахариныч", 7, 1);
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public void setName(String name) {
        if (!name.equals("Сахарин Сахариныч")) {
            System.out.println("По имени отчеству, пожалуйста!");
        }
        this.name = name;
    }
}
