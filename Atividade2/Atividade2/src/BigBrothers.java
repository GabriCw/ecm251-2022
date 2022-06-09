public class BigBrothers extends Membros{

    public BigBrothers(String nome, String email, String funcao, String turno) {
        super(nome, email, funcao, turno);
    }

    @Override
    public String Mensagem(String turno) {
        if(turno.equals("regular")){
            return "Sempre ajudando as pessoas membros ou não S2!"; 
        }
        else{
            return "..."; 
        }
        
    }

    
    
}
