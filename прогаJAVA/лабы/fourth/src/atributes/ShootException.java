package atributes;

public class ShootException extends InvalidNameException {

    private final int bul;

    public ShootException(String message, int bullets) {

        super(message);
        bul = bullets;
    }

    public int getBullets() {
        return bul;
    }
}
