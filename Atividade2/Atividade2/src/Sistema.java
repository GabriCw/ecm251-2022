import java.util.ArrayList;
import java.util.List;

public class Sistema {

    public void run(){
        //Cria um membro de cads tipo
        List<Membros> membro = new ArrayList<Membros>();
        membro.add(new MobileMembers("C3P0", "C3P0@gmail.com", "MobileMembers ", "regular"));
        membro.add(new HeavyLifters("XYP9 ", "XYP9@gmail.com", "HeavyLifters", "regular"));
        membro.add(new ScriptGuys("88UI", "88UI@gmail.com", "ScriptGuys", "regular"));
        membro.add(new BigBrothers("6IX", "6IX@gmail.com", "BigBrothers", "regular"));
        //printa mensagem de todos os membros
        System.out.println("------------------Mensagens----------------");
        for (Membros membros : membro) {
            System.out.println(membros.getNome()+":"+membros.Mensagem(membros.getTurno()));
        }
        //set turno para extra
        mudarTurno(membro, "extra");

        //printa mensagem de todos os membros
        System.out.println("-------------Mensagens Novas---------------");
        for (Membros membros : membro) {
            System.out.println(membros.getNome()+":"+membros.Mensagem(membros.getTurno()));
        }
        //set turno para regular
        mudarTurno(membro, "regular");
        //remove o membro HeavyLifters e o membro ScriptGuys
        membro.remove(1);
        membro.remove(1);
        //printa os membros cadastrados
        System.out.println("-----------Membros Cadastrados-------------");
        for (Membros membros : membro) {
            System.out.println(membros);
        }
    }
    public void mudarTurno(List<Membros> membro, String hora){
        for (Membros membros : membro) {
            if(hora.equals("extra"))
            membros.setTurno("extra");
            else membros.setTurno("regular");
        }
    }

}
