public class Atividade1 {
    public static void run(){
        Usuarios usuario1 = new Usuarios("All Might", "123456", "email@gmail.com");
        Usuarios usuario2 = new Usuarios("One for All", "345gr", "jorge@gmail.com");
        Usuarios usuario3 = new Usuarios("Bakugo", "2244gt", "lol@gmail.com");

        usuario1.getConta().depositar(1000);
        usuario2.getConta().depositar(250);
        usuario3.getConta().depositar(3000);

        String qrCode1 = Transacoes.gerarQrCode(usuario1.getConta().getIdConta(), usuario1.getNome(), 250);

        System.out.println("Transacao 1:" + usuario2.getConta().trasnferir(extrairValorQrCode(qrCode1), usuario1.getConta()));
        System.out.println("Transacao 2:" + usuario3.getConta().trasnferir(extrairValorQrCode(qrCode1), usuario1.getConta()));
        System.out.println("Transacao 3:" + usuario2.getConta().trasnferir(extrairValorQrCode(qrCode1), usuario1.getConta()));

        String qrCode2 = Transacoes.gerarQrCode(usuario2.getConta().getIdConta(), usuario2.getNome(), 1000);

        System.out.println("Transacao 4:" + usuario3.getConta().trasnferir(extrairValorQrCode(qrCode2), usuario2.getConta()));
    }

    private static double extrairValorQrCode(String qrCode){
        String valorComVirgula = qrCode.split(";")[2];
        String valorSemVirgula = valorComVirgula.replace(",", ".");
        return Double.parseDouble(valorSemVirgula);
    }
}
