
//Nome: Gabriel dos Santos Couto
//RA: 20.00273-4
public class Transacoes {
   public static String gerarQRCode(String idConta,String nome, double valor){
      return(idConta +";" +nome +";" +valor);  
   }  
   public static void Pagamento(Conta pagamento, Conta destino, String QRCode){
    if(valor < saldo){
        String s = QRCode;
        String[] dados = s.split(";");
        transferirDinheiro(dados[3], conta2);
    }
    } 
   

}
