class Flygon extends Vibrava {
    public Flygon(String name, int level) {
        super(name, level);
        setStats(80, 100, 80, 80, 80, 100);
        addMove(new DracoMeteor());
    }
}
