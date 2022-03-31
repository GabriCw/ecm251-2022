//Nome: Gabriel dos Santos Couto
//RA: 20.00273-4
public class Conta {
   private String idConta;
   private double saldo; 
   private Usuarios usuario;
   
   public Conta(Usuarios usuario, String idConta){
       this.usuario = usuario;
       this.idConta = idConta;
       saldo = 0;
   }
   public String visualizarSaldo(){
    return String.format("R$ %.2f", saldo);
   }

    public boolean depositar(double valor){
    if(valor < 0)
         return false;

    this.saldo += valor;
    return true;
    }

    public boolean sacar(double valor){
   if(valor > saldo) return false;
   if(valor < 0) return false;
   this.saldo -= valor;
   return true;
    }

    public boolean transferirDinheiro(double valor, Conta destino){
    if(!sacar(valor)) return false;
    if(!destino.depositar(valor)) return false;
    return true;
    }

    public String toString(){
    return "Conta Numero:" +idConta +
    "\nSaldo:" +visualizarSaldo() +
    "\nUsuario:" +usuario.getNome();
    }
}
