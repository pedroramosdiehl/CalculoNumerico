import org.omg.PortableInterceptor.INACTIVE;
import java.math.BigDecimal;

/**
 * Created by daniel on 21/05/17.
 */
public class main {
    public static void main(String args[]){
        long time = System.currentTimeMillis();
        System.out.println("----------------------------------------------------------------Inicio----------------------------------------------------------------");
        int grau = 3;

        BigDecimal[][] pontos = new BigDecimal[][]{
                {new BigDecimal(-2.), new BigDecimal(-3.)},
                {new BigDecimal(-1.), new BigDecimal(0.)},
                {new BigDecimal(1.), new BigDecimal(0.)},
                {new BigDecimal(2.), new BigDecimal(-3.)},
                {new BigDecimal(2.), new BigDecimal(-1.)},
                {new BigDecimal(4.), new BigDecimal(0.)},
                {new BigDecimal(5.), new BigDecimal(2.)}
        };

        InterpolacaoPolinomial.interpolar(pontos,grau);

        System.out.println("------------------------------------------------------------------Fim-----------------------------------------------------------------");
        System.out.println("Calculo efetuado em "+((System.currentTimeMillis()-time)/1000.0)+"s");
    }
}
