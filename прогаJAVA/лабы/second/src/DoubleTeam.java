import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Stat;
import ru.ifmo.se.pokemon.StatusMove;
import ru.ifmo.se.pokemon.Type;

class DoubleTeam extends StatusMove {
    protected DoubleTeam() {
        super(Type.NORMAL, 1, 1000);
    }

    @Override
    protected void applySelfEffects(Pokemon p) {
        p.setMod(Stat.EVASION, 1);
    }

    @Override
    protected String describe() {
        return "увеличивает показатель уклонения на 1 ступень";
    }
}
