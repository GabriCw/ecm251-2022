import java.util.concurrent.ThreadLocalRandom;

//Nome: Gabriel dos Santos Couto
//RA: 20.00273-4
public class Transacoes {
    public static String gerarQrCode(int idConta, String usuario, double valor){
        int numeroAleatorio = ThreadLocalRandom.current().nextInt(1000, 10000);
        return String.format("%d;%s;%.2f;%d", 
        idConta, 
        usuario, 
        valor, 
        numeroAleatorio);
    }
}
