import ru.ifmo.se.pokemon.*;

class Swagger extends StatusMove {
    protected Swagger() {
        super(Type.NORMAL, 1, 90);
    }

    @Override
    protected void applyOppEffects(Pokemon p) {
        p.setMod(Stat.ATTACK, 2);
        Effect.confuse(p);
    }

    @Override
    protected String describe() {
        return "имеет 100% шанс запутать врага и увеличивает показатель атаки противника на 2 ступени";
    }
}
