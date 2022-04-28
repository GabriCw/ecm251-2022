//Nome: Gabriel dos Santos Couto
//RA: 20.00273-4

public class Bicicleta extends Veiculos{

    public Bicicleta(String tipo, String idVeiculo) {
        super(tipo, idVeiculo);
    }

    @Override
    public String getIdVeiculo() {
        return super.getIdVeiculo();
    }

    @Override
    public String toString() {
        return "Bicicleta: " +idVeiculo;
    }
   
    
}
