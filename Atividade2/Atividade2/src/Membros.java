public abstract class Membros implements PostarMensagem{
    private final String nome;
    private final String email;
    private final String funcao;
    private String turno;
    
    public Membros(String nome, String email, String funcao, String turno) {
        this.nome = nome;
        this.email = email;
        this.funcao = funcao;
        this.turno = turno;
    }

    public String getNome() {
        return nome;
    }

    public String getEmail() {
        return email;
    }

    public String getFuncao() {
        return funcao;
    }

    public String getTurno() {
        return turno;
    }
    public void setTurno(String turno) {
        this.turno = turno;
    }
    
    @Override
    public String toString() {
        return "Membros [email=" + email + ", funcao=" + funcao + ", nome=" + nome + ", turno=" + turno + "]";
    }

   
    
}
