import java.math.BigDecimal;

/**
 * Created by daniel on 21/05/17.
 */
public final class InterpolacaoPolinomial {
    public static void interpolar(BigDecimal[][] pontos, int grau){
        BigDecimal[][] matrizA = getMatrizA(pontos,grau);
        BigDecimal[][] matrizB = getMatrizB(pontos);
        BigDecimal[][] matrizAT = getMatrizTransposta(matrizA);//transposiçao

        matrizA = multiplicar(matrizAT,matrizA);
        matrizB = multiplicar(matrizAT,matrizB);

        imprimir(Matrizes.resolverSistema(matrizA,matrizB));

    }

    private static BigDecimal[][] getMatrizA(BigDecimal[][] pontos, int grau){
        BigDecimal[][] matrizA = new BigDecimal[pontos.length][grau+1];

        for(int i = 0 ; i < pontos.length ; i++){
            for(int j = 0 ; j < matrizA[i].length ; j++){
                matrizA[i][j] = pontos[i][0].pow((grau-j));
            }
        }

        return matrizA;
    }

    private static BigDecimal[][] getMatrizB(BigDecimal[][] pontos){
        BigDecimal[][] matrizB = new BigDecimal[pontos.length][2];

        for(int i = 0 ; i < pontos.length ; i++){
            for(int j = 0 ; j<matrizB[i].length ; j++){
                switch (j){
                    case 0 : matrizB[i][j] = pontos[i][1];break;
                    case 1 : matrizB[i][j] = new BigDecimal(0.0);
                }
            }
            //matrizB[i][] = pontos[i][1];
        }

        return matrizB;
    }

    private static BigDecimal[][] multiplicar(BigDecimal[][] matrizA,BigDecimal[][] matrizC){
        BigDecimal[][] matrizResultado = new BigDecimal[matrizA.length][matrizC[0].length];

        if(matrizA[0].length != matrizC.length){
            throw new IllegalArgumentException("Operaçao impossivel");
        }

        for(int i = 0 ; i < matrizResultado.length ; i++){
            for(int j = 0 ; j < matrizResultado[0].length ; j++){
                matrizResultado[i][j] = new BigDecimal(0);

                for(int k = 0 ; k < matrizC.length; k++){
                    matrizResultado[i][j] = matrizResultado[i][j].add((matrizA[i][k].multiply(matrizC[k][j])));
                }
            }
        }

        return matrizResultado;
    }

    private static BigDecimal[][] getMatrizTransposta(BigDecimal[][] matriz){
        BigDecimal[][] matrizT = new BigDecimal[matriz[0].length][matriz.length];

        for(int i = 0 ; i < matrizT.length ; i++ ){
            for(int j = 0 ; j < matrizT[i].length ; j++){
                matrizT[i][j] = matriz[j][i];
            }
        }

        return matrizT;
    }

    private static void imprimirMatriz(BigDecimal[][] matriz){

        for(int i =0 ; i< matriz.length ; i++){
            for(int j = 0 ; j< matriz[1].length ; j++){
                System.out.printf("\t%.2f",matriz[i][j],"");

                if(j == (matriz[1].length-1)){
                    System.out.println();
                }
            }
        }

        System.out.println();
    }

    private static void imprimir(BigDecimal[] polinimio){
        System.out.print("F(x) = ");

        for(int i = 0 ; i < polinimio.length ; i ++){
            if(polinimio.length-1-i != 0){
                if(polinimio[i].doubleValue() < 0.0){
                    System.out.printf("(%.2fX)^(%d) + ",polinimio[i],(polinimio.length-1-i));
                }else{
                    System.out.printf("%.2fX^(%d) + ",polinimio[i],(polinimio.length-1-i));
                }
            }else{
                if(polinimio[i].doubleValue() < 0.0){
                    System.out.printf("(%.2f) ",polinimio[i]);
                }else{
                    System.out.printf("%.2f ",polinimio[i]);
                }
            }
        }
        System.out.println();
    }
}
