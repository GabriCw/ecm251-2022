public class App {
    public static void main(String[] args) throws Exception {
       Cliente c1 = new Cliente("Gabriel",
          "12345678",
          "gabricouto2305@gmail.com",
          new Conta(123)
        );

       System.out.println("Nome do Cliente: " +c1.getNome());
       System.out.println("E-mail do Cliente: " +c1.getEmail());
       System.out.println("CPF do Cliente: " +c1.getCpf());
       c1.getConta().visualizarSaldo();
        
    }
}
