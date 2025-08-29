import ru.ifmo.se.pokemon.*;
class Clamperl extends Pokemon {
    public Clamperl(String name, int level) {
        super(name, level);
        setStats(35, 64, 85, 74, 55, 32);
        setType(Type.WATER);
        setMove(new Swagger(), new Facade(), new Waterfall());
    }
}
