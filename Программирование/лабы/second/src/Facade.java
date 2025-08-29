import ru.ifmo.se.pokemon.*;

class Facade extends PhysicalMove {
    protected Facade() {
        super(Type.NORMAL, 70, 100);
    }

    @Override
    protected void applyOppDamage(Pokemon p, double damage) {
        Status Condition = p.getCondition();
        if (Condition.equals(Status.BURN) || Condition.equals(Status.POISON) || Condition.equals(Status.PARALYZE))
            p.setMod(Stat.HP, (int) Math.round(damage * 2));

    }

    @Override
    protected String describe() {
        return "удваивает силу, если враг обожжён, отравлен или парализован";
    }
}
