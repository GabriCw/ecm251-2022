
//Nome: Gabriel dos Santos Couto
//RA: 20.00273-4

public class Carro extends Veiculos{
    
    public Carro(String tipo, String idVeiculo) {
        super(tipo, idVeiculo);
    }



    @Override
    public String toString() {
        return "Carro:"+idVeiculo;
    }

    

}
