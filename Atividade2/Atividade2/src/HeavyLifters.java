public class HeavyLifters extends Membros{

    public HeavyLifters(String nome, String email, String funcao, String turno) {
        super(nome, email, funcao, turno);
    }

    @Override
    public String Mensagem(String turno) {
        if(turno.equals("regular")){
            return "Podem contar conosco!"; 
        }
        else{
            return "N00b_qu3_n_Se_r3pita.bat”"; 
        }
        
    }

    
}
