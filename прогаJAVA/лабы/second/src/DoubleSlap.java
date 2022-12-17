import ru.ifmo.se.pokemon.PhysicalMove;
import ru.ifmo.se.pokemon.Type;

class DoubleSlap extends PhysicalMove {
    protected DoubleSlap() {
        super(Type.NORMAL, 15, 85, 0, 2 + (int) Math.round(Math.random() * 3));
    }

    @Override
    protected String describe() {
        return "заставляет пользователя нанести от 2 до 5 ударов подряд";
    }
}
