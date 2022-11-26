public static void main(string[] args) {
    // INTEIROS

    byte b; // 8 bits
    byte b1 = 127;
    byte b2 = -128;
    // O Range do byte vai de -128 a 127, 0 conta.


    char c; // 16 bits
    char c1 = 'A'
    char c2 = 15;
    // char c3 = 'AA' //N0K
    // char c4 = -100; //NOK

    short s; // 16 BITS
    short s1 = 32767;
    short s2 = -32768;

    int i = 2147483647 //32 bits
    int i2 = -2147486348;

    //int i3 = -2147483649; // to large

    long l = 9223372036854775807l; //64bits
    long l2 = -9223372036854775808L;
    //long l3 = 9223372036854775808L; // to large

    //FLUTUANTES

    float f = 65f; //32 BITS 3.402,823,5 E+38
    float f2 = 65.0f;
    float f3 = -0.5f;  //1.4 E-45 

    double d= 1024.99; //64 bits 1.797.693.134,
    double d2 = 10.2456; //4.9E-324

    // Variaveis blooleanas

    boolean bo = true;
    boolean bo2 = false;
    //boolean bo3 = "false"; /N0K
    //bolean bo4 = "true"; //N0K

    //void v; //palavra reservada

    //System.out.println("byte: " +b); //ERROR
}