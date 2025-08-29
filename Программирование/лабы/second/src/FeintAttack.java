import ru.ifmo.se.pokemon.PhysicalMove;
import ru.ifmo.se.pokemon.Type;

class FeintAttack extends PhysicalMove {
    protected FeintAttack() {
        super(Type.DARK, 60, 1000);
    }
}
