package Gauss;

import java.math.BigDecimal;
import java.math.RoundingMode;

/**
 * Created by daniel on 16/04/17.
 */
public final class Matrizes {
    private static int dimensao = 0;
    private static int precisaBG = 16;

    public static void resolverSistema(BigDecimal[][] matrizA, BigDecimal[] matrizB){
        dimensao = matrizB.length;
        BigDecimal[][] matrizExtendida = getMatrizExtendida(matrizA, matrizB);
        System.out.println("|Matriz Extendida|");
        imprimir(matrizExtendida);
        retrosubstituicao(escalonarMatrizExtendida(matrizExtendida));
    }

    private static BigDecimal[][] getMatrizExtendida(BigDecimal[][] matrizA, BigDecimal[] matrizB) {
        BigDecimal matrizExtendida[][] = new BigDecimal[dimensao][dimensao + 1];

        for (int i = 0; i < dimensao; i++) {
            for (int j = 0; j < (dimensao + 1); j++) {
                if (j < dimensao) {
                    matrizExtendida[i][j] = matrizA[i][j];
                } else {
                    matrizExtendida[i][j] = matrizB[i];
                }
            }
        }
        return matrizExtendida;
    }

    private static BigDecimal[][] escalonarMatrizExtendida(BigDecimal[][] matrizExtendida){
        for (int l=0 ; l< dimensao -1 ; l++){

            BigDecimal elementoDiagonal = matrizExtendida[l][l];

            for(int i = l ; i<dimensao;i++){
                BigDecimal fator = new BigDecimal("0.0");
                int indice =0;
                if(i<dimensao-1){
                    fator =  matrizExtendida[i+1][l].divide(elementoDiagonal, precisaBG,RoundingMode.HALF_DOWN);
                    indice = i+1;
                }else{
                    fator = matrizExtendida[i][l].divide(elementoDiagonal, precisaBG,RoundingMode.HALF_DOWN);
                    indice = i;
                }
                for(int j= 0; j< dimensao+1; j++){
                    matrizExtendida[indice][j] =
                            (matrizExtendida[indice][j].subtract(matrizExtendida[l][j].multiply(fator)));
                }
            }
        }
        System.out.println("|Matriz escalonada|");
        imprimir(matrizExtendida);
        return matrizExtendida;
    }

    private static void retrosubstituicao(BigDecimal[][] matrizEscalonada){
        BigDecimal[] x = new BigDecimal[dimensao];

        for(int i =0;i<dimensao;i++){
            x[i] = new BigDecimal(1);
        }

        BigDecimal soma =new BigDecimal(0);
        for(int i = dimensao-1 ; i>=0 ; i--){
            for(int j = 0 ; j< dimensao ; j++){
                if(j>i){
                    BigDecimal var = matrizEscalonada[i][j].multiply(x[j]);
                    soma = soma.add(var);
                }
                if(j== dimensao-1){
                    x[i] = matrizEscalonada[i][j+1].subtract(soma).divide(matrizEscalonada[i][i], precisaBG,RoundingMode.HALF_DOWN);
                }
            }
            soma = new BigDecimal(0);
        }
        System.out.println("|Soluçao do Sistema|");
        for(int i = 0 ;i< x.length ; i++){
            System.out.printf("\tx%d = %.3f\n",i,x[i]);
        }
        System.out.println();
    }

    private static void imprimir(BigDecimal[][] matriz){
        for(int i =0 ; i< dimensao ; i++){
            for(int j = 0 ; j< dimensao+1 ; j++){
                System.out.printf("\t%.2f",matriz[i][j],"");
                if(j == (dimensao)){
                    System.out.println();
                }
            }
        }
        System.out.println();
    }

}
