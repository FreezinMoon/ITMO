package atributes;

public class InvalidNameException extends RuntimeException{
    public InvalidNameException(String errorMessage) {
        super(errorMessage);
    }
}
