package operadores;

public class Igualdade {
    
    public static void main(String[] args) {

        final var numero = 11;

        //Verificar se o numero é igual

        if (numero == 10) {
            System.out.println("O numero é 10");
        } else {
            System.out.println("O Número não é 10");

        }
        // Verificar se o numero é diferente
        if (numero != 10) {
            System.out.println("O número não é 10");
        } else {
            System.out.println("O número é 10");


        }

        }

        final var letra ="B";

        //É verdade se A é igual a B?
        if ("A".equals(letra)) {
            System.out.println("É a letra A");

        }
        // É verdade se A não é igual a B?
        if (!letra.equals("A")) {
            System.out.println("Não é a letra A");
        }

    }
    
    
}
