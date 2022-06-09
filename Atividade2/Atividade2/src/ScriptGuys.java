public class ScriptGuys extends Membros{

    public ScriptGuys(String nome, String email, String funcao, String turno) {
        super(nome, email, funcao, turno);
    }

    @Override
    public String Mensagem(String turno) {
        if(turno.equals("regular")){
            return "Prazer em ajudar novos amigos de código!"; 
        }
        else{
            return "QU3Ro_S3us_r3curs0s.py"; 
        }
        
    }

    
    
}
