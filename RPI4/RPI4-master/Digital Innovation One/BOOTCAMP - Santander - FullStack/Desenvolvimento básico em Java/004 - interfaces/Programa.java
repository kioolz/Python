package one.digitalinnovation.interfaces;

public class Programa {

    public static void main(String[] args) {

        final Gol gol = new Gol();
        System.out.println("Marca do Gol : "+gol.marca());

        final Trator trator = new Trator();
        System.out.println("Registro do Trator :$ {trator.registro()}");
        trator.ligar();

        final Fiesta fiesta = new Fiesta();
        
    }
}
    
}
