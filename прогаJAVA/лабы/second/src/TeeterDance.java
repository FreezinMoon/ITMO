import ru.ifmo.se.pokemon.Effect;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.StatusMove;
import ru.ifmo.se.pokemon.Type;

class TeeterDance extends StatusMove {
    protected TeeterDance() {
        super(Type.NORMAL, 1, 100);
    }

    @Override
    protected void applyOppEffects(Pokemon p) {
        Effect.confuse(p);
    }

    @Override
    protected String describe() {
        return "имеет 100% шанс запутать врага";
    }
}
