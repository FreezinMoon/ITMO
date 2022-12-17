import ru.ifmo.se.pokemon.Effect;
import ru.ifmo.se.pokemon.PhysicalMove;
import ru.ifmo.se.pokemon.Pokemon;
import ru.ifmo.se.pokemon.Type;

class Waterfall extends PhysicalMove {
    protected Waterfall() {
        super(Type.WATER, 80, 100);
    }

    @Override
    protected void applyOppEffects(Pokemon p) {
        if (Math.random() < 0.2) Effect.flinch(p);
    }

    @Override
    protected String describe() {
        return "имеет 20% шанс заставить врага дрогнуть";
    }
}
