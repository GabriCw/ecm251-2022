public class MobileMembers extends Membros{

    public MobileMembers(String nome, String email, String funcao, String turno) {
        super(nome, email, funcao, turno);
    }

    @Override
    public String Mensagem(String turno) {
        if(turno.equals("regular")){
            return "Happy Coding!"; 
        }
        else{
            return "Happy_C0d1ng. Maskers"; 
        }
        
    }
 
}
