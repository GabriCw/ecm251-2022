import java.util.ArrayList;

public class TestDriveArrayList {
    public static void main(String[] args) {
        //Cria um ArrayList para as Canetas
        ArrayList<Caneta> canetas = new ArrayList<Caneta>();
        //Adiciona uma caneta
        canetas.add(new Caneta("Azul", 0.7));
        canetas.add(new Caneta("Vermelha", 1.0));

        //Estudo do método size()
        System.out.println("Size agora: "+canetas.size());

        //Remove um objeto pelo índice
        canetas.remove(0);

        //Estudo do método size()
        System.out.println("Size agora: "+canetas.size());

        //Passar por todos os elementos do Array
        System.out.println("Método 1: for do C");
        for(int i = 0; i < canetas.size(); i++){
            System.out.println("Cor da caneta: " +canetas.get(i).cor);
            //Caso não tenha expecificado que o arraylist é de caneta faz assim
            //System.out.println("Cor da caneta: " +((Caneta)canetas.get(i)).cor);


        }
        //Método 2 (foreach)
        for (Caneta caneta : canetas) { 
            System.out.println("Cor da caneta: " +caneta.cor);
        }
    }
}
