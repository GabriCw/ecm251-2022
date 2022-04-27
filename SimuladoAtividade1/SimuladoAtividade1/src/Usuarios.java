//Nome: Gabriel dos Santos Couto
//RA: 20.00273-4
public class Usuarios {
    private String nome;
    private String senha;
    private String email;
    private Conta conta;
    public Usuarios(String nome, String senha, String email) {
        this.nome = nome;
        this.senha = senha;
        this.email = email;
    }
    public String getNome() {
        return nome;
    }

    public Conta getConta() {
        return conta;
    }
    @Override
    public String toString() {
        return "Usuarios [conta=" + conta + ", email=" + email + ", nome=" + nome + ", senha=" + senha + "]";
    }
    
}