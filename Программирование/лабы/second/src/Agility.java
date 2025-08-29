import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Stat;
import ru.ifmo.se.pokemon.StatusMove;
import ru.ifmo.se.pokemon.Type;

class Agility extends StatusMove {
    protected Agility() {
        super(Type.PSYCHIC, 1, 1000);
    }

    @Override
    protected void applySelfEffects(Pokemon p) {
        p.setMod(Stat.SPEED, 2);
    }

    @Override
    protected String describe() {
        return "увеличивает показатель скорости на 2 ступени";
    }
}
