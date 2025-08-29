package talking;

import shorties.BabyBoy;
import shorties.Neznaika;

public class Walk {
    private boolean friends = true;

    public Walk(Neznaika neznaika, BabyBoy babyBoy) {
    }

    public void walk() {
        System.out.println("Незнайка с Гунькой бродят по кварталам");
    }

    public void tellStory() {
        System.out.println("Незнайка с Гунькой сочиняют небылицы");
    }

    public void argue() {
        System.out.println("Незнайка с Гунькой поссорились");
        this.friends = false;
    }

    public void reconcile() {
        System.out.println("Незнайка с Гунькой помирились");
        this.friends = true;
    }

    public boolean isFriends() {
        return friends;
    }
}
