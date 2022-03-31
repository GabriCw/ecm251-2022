//Nome: Gabriel dos Santos Couto
//RA: 20.00273-4
public class Usuarios {
    private String nome;
    private String senha;
    private String email;

    public Usuarios(String nome, String senha, String email){
        this.nome = nome;
        this.senha = senha;
        this.email = email;
    }
    public void visualizarUsuario(){
        System.out.println("Dados do Usuario:");
        System.out.println("Nome:" + nome);
        System.out.println("CPF:" + senha);
        System.out.println("E-mail:" + email);
    }

    public String getNome(){
        return nome;
    }
    public void setNome(String nome){
        this.nome = nome;
    }
    public String getSenha(){
        return senha;
    }
    public String getEmail(){
        return email;
    }
    public void setEmail(String email){
        this.email = email;
    }
}