import ru.ifmo.se.pokemon.Battle;

public class Main {
    public static void main(String[] args) {
        Battle battle = new Battle();
        battle.addAlly(new OricorioPomPom("Axel", 1));
        battle.addFoe(new Clamperl("Salchow", 1));
        battle.addAlly(new Huntail("Toeloop", 1));
        battle.addFoe(new Flygon("Loop", 1));
        battle.addAlly(new Trapinch("Flip", 1));
        battle.addFoe(new Vibrava("Lutz", 1));
        battle.go();
    }
}
