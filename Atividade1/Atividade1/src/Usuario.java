//Nome: Gabriel dos Santos Couto
//RA: 20.00273-4

public class Usuario {
    private String nome;
    private Veiculos veiculo;

    public Usuario(String nome, Veiculos veiculo) {
        this.nome = nome;
        this.veiculo = veiculo;
    }

    public String getNome() {
        return nome;
    }

    public Veiculos getVeiculo() {
        return veiculo;
    }

    public static double alugarVeiculo(Usuario usuario, Veiculos veiculo){
        this.usuario = usuario.veiculo(veiculo);
    }
}
