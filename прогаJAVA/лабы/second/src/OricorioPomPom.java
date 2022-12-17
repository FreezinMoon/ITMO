import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;

class OricorioPomPom extends Pokemon {
    public OricorioPomPom(String name, int level) {
        super(name, level);
        setStats(75, 70, 70, 98, 70, 93);
        setType(Type.ELECTRIC, Type.FLYING);
        setMove(new TeeterDance(), new Agility(), new DoubleTeam(), new DoubleSlap());
    }
}
