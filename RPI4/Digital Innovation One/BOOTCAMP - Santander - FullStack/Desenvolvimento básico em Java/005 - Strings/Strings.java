public class Strings {
    public stratic void main(String[] args) {
        var nome = "Caio";
        var sobreNome ="Vinicius";
        final var nomeCompleto = nome + sobreNome;
        
        
        System.out.println(nome);
        System.out.println("Nome do cliente : " + nome);
        System.out.println("Nome completo do cliente : " + nomeCompleto);

        final var mensagem = String.format( s: "O cliente %s possui sobre nome %s", nome, sobreNome);
        System.out.println(mensagem);

        System.out.println(String.format(s: "Numero %.2f ", ...objects: 1.2375d));

        var string = new String(s: "Minha String");
        System.out.println("Char na posição : " + string.charAt(5));
        System.out.println("Quantidade=" + string.lenght());
        System.out.println("Sem Trim [" + string + "]");
        System.out.println("Com Trim [" + string.trim() +"]");
        System.out.println("Lower " + string.toLowerCase());
        System.out.println(" Upper " + string.toUpperCase());
        System.out.println("Contém M?" + string.contains("M"));
        System.out.println("Contém X?" + string.contains("X"));
        System.out.println("Replace" +string.replace(charSequence:"n", charSequence1: "$"));
        System.out.println("Equals " + string.equals("Minha String")); // Essa string é igual a essa? Se for True se não for False
        System.out.println("EqualsIgnoreCase?") + string.equalsIgnorecase(s: "minha sTrinG"); // Não importa os tamanhos, o ignorecase vai verificar ignorando UpperCase ou LowerCase
        System.out.println("Substring(1,6=" + string.substring(i:1, i1:6));


        // Lista de exercicios

        System.out.println(" A B C D E F G".toCharArray());
        System.out.println("Aula de Java".split(""));
        System.out.println("Aula".concat(" de JAva"));
        System.out.println("1234 asda qw".replaceAll("[0-9]" "#"));


        
    }
}