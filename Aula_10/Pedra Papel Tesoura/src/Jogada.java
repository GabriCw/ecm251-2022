public class Jogada {
    private final EnumJogadas venco;  //atribui o valor de venco até o final
    private final EnumJogadas venco2; //atribui o valor de venco até o final

    public Jogada(EnumJogadas venco, EnumJogadas venco2) {
        this.venco = venco;
        this.venco2 = venco2;
    }
    
    public boolean verificarVenceu(Jogada jogada){
        if(jogada.getTipo().equals(venco) || jogada.getTipo().equals(venco2))
            return true;
        return false;
    }

    public EnumJogadas getTipo(){
        return EnumJogadas.PAPEL;
    }
}
