import ru.ifmo.se.pokemon.Type;

class Vibrava extends Trapinch{
    public Vibrava(String name, int level) {
        super(name, level);
        setStats(50, 70, 50, 50, 50, 70);
        addType(Type.DRAGON);
        addMove(new BugBuzz());
    }
}
