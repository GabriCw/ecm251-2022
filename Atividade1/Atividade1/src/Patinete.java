//Nome: Gabriel dos Santos Couto
//RA: 20.00273-4

public class Patinete extends Veiculos{

    public Patinete(String tipo, String idVeiculo) {
        super(tipo, idVeiculo);
    }

    @Override
    public String getIdVeiculo() {
        return super.getIdVeiculo();
    }

    @Override
    public String toString() {
        return "Patinete: " +idVeiculo;
    }


  
}
