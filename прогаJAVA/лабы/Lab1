import java.util.Arrays;

public class Lab1 {

    public static void main(String[] args){

        long[] set = {4,6,7,8,10,13,16};
        double origin = -7., range = 4.-origin;

        long[] k = new long[14];
        for (int i = 0; i < 14; i++) {
            k[i] = i+3;
        }

        double[] x = new double[10];
        for (int i = 0; i < 10; i++) {
            x[i] = origin + Math.random() * range;
        }


        double[][] g = new double[14][10];
        for (int i = 0; i < 14; i++) {
            for (int j = 0; j < 10; j++) {
                if (k[i]==15){
                    g[i][j] = 0.5*Math.pow(Math.pow(0.5/(1-x[j]),x[j]),2/Math.cos(x[j]));
                } else if (Arrays.binarySearch(set,k[i])>=0) {
                    g[i][j] = Math.log(Math.pow(3+Math.pow(Math.abs(x[j]),0.5),2));
                }else{
                    g[i][j] = Math.exp(Math.sin(Math.atan(Math.exp(-1*Math.abs(x[j])))));
                }
            }
        }

        for (double[] array : g) {
            for (double d : array) {
                System.out.printf("%05.4f ", d);
            }
            System.out.println();
        }
    }
}
