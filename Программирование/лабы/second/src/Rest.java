import ru.ifmo.se.pokemon.*;

class Rest extends StatusMove {
    protected Rest() {
        super(Type.PSYCHIC, 1, 1000);
    }

    @Override
    protected void applySelfEffects(Pokemon p) {
        p.setCondition((new Effect()).condition(Status.SLEEP).attack(0.0).turns(2));
        p.setMod(Stat.HP, (int) Math.round(p.getHP() - p.getStat(Stat.HP)));
    }

    @Override
    protected String describe() {
        return "засыпает на два хода. Это полностью восстанавливает HP и исцеляет любые статусные состояния";
    }
}
