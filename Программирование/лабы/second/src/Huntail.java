class Huntail extends Clamperl {
    public Huntail(String name, int level) {
        super(name, level);
        setStats(55, 104, 105, 94, 75, 52);
        addMove(new FeintAttack());
    }
}
