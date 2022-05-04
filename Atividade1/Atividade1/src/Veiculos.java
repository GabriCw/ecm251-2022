//Nome: Gabriel dos Santos Couto
//RA: 20.00273-4

import java.util.concurrent.ThreadLocalRandom;

public class Veiculos {
    public static String idVeiculo;
    private String tipo;
    
    public Veiculos(String tipo, String idVeiculo) {
        this.tipo = tipo;
        this.idVeiculo = geraIdVeiculo();
    }

    public static String geraIdVeiculo(){
        int id = ThreadLocalRandom.current().nextInt(0, 99999);
        return  String.format("%d", id);
    }

    public  String testar(Usuario usuario){
        return usuario.getVeiculo().tipo;
    }

    @Override
    public String toString() {
        return "Veiculos [tipo=" + tipo + "]";
    }

    public  String getIdVeiculo() {
        return idVeiculo;
    }
}
