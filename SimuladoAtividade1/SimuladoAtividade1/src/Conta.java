//Nome: Gabriel dos Santos Couto
//RA: 20.00273-4
public class Conta {
   private int idConta;
   private double saldo; 
   private static int totalContas = 0;

   public Conta() {
       this.saldo = 0;
       this.idConta = totalContas;
       totalContas++;
   }

   public boolean depositar(double valor){
        this.saldo += valor;
        return true;
   }

   public boolean sacar(double valor){
       if(valor>saldo)
           return false;
        this.saldo -= saldo;
        return true; 
   }

   public boolean trasnferir(double valor, Conta destino){
        if(!sacar(valor))
            return false;
        return destino.depositar(valor);
   }

public int getIdConta() {
    return idConta;
}

public double getSaldo() {
    return saldo;
}

@Override
public String toString() {
    return "Conta [idConta=" + idConta + ", saldo=" + saldo + "]";
}

}
