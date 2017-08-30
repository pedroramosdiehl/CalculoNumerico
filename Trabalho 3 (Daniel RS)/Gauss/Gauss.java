package Gauss;

import java.math.BigDecimal;

/**
 * Created by daniel on 16/04/17.
 */
public class Gauss {
    public static void main(String args []){
        long time = System.currentTimeMillis();
        BigDecimal[][] matrizA;
        matrizA =  new BigDecimal[][]{
                {new BigDecimal(1.0),new BigDecimal(4.0),new BigDecimal(52.0)},
                {new BigDecimal(27.0),new BigDecimal(110.0),new BigDecimal(-3.0)},
                {new BigDecimal(22.0),new BigDecimal(2.0),new BigDecimal(14.0)}
        };

        BigDecimal[] matrizB;

        matrizB = new BigDecimal[]{new BigDecimal(157.0),
                new BigDecimal(134.0),
                new BigDecimal(38.0)};

        Matrizes.resolverSistema(matrizA,matrizB);
        System.out.printf("Calculo efetuado em %.5f segundos",(double)(System.currentTimeMillis()-time)/1000.0 );
    }
}
