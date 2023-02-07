package atributes;

import shorties.Baby;

public class Gun {

    private int bullets = 0;
    private int stamina = 20;

    public Gun(Baby owner) {
    }

    public Gun reload() {
        class Magazine {
            final private int capacity;

            public Magazine(int capacity) {
                this.capacity = capacity;
            }

            public int getCapacity() {
                return capacity;
            }
        }
        this.bullets = new Magazine(2).getCapacity();
        System.out.println("Ствол заряжен");
        return this;
    }

    void setStamina(int stamina) {
        this.stamina = stamina;
    }

    private boolean shoot() throws ShootException {
        if (this.bullets == 0) {
            throw new ShootException("chik, Ружье разряжено...", bullets);
        }
        if (this.stamina == 0) {
            throw new ShootException("Ружьё сломалось, обратитесь к Винтику, он починит", bullets);
        }
        this.bullets--;
        System.out.println("bang!");
        this.stamina--;
        return true;
    }

    public class Trigger {
        public boolean pull() throws ShootException {
            return Gun.this.shoot();
        }
    }
}
