import javax.sql.rowset.spi.SyncResolver;

//Nome: Gabriel dos Santos Couto
//RA: 20.00273-4
public class Atividade1 {
    Usuarios usuario = new Usuarios("Midoria", "123456", "midoriae@gmail.com");
    Conta conta = new Conta(usuario, "1234");
    Usuarios usuario2 = new Usuarios("AllMight", "123457", "allmight@gmail.com");
    Conta conta2 = new Conta(usuario, "1235");
}
