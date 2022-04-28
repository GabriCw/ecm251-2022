//Nome: Gabriel dos Santos Couto
//RA: 20.00273-4

public class App {
    public static void main(String[] args) throws Exception {
        Veiculos carro = new Carro("Honda",null);
        Veiculos patinete = new Patinete("Lul",null);
        Veiculos moto = new Moto("Suzuki",null);
        Veiculos bicicleta = new Bicicleta("Kaloi",null);

        Usuario usuario1 = new Usuario("Gabriel", carro);
        System.out.println("Usuario1: " +usuario1.getNome()+";" +usuario1.getVeiculo());
        Usuario usuario2 = new Usuario("Jose", patinete);
        System.out.println("Usuario1: " +usuario2.getNome()+";" +usuario2.getVeiculo());
    }
}
