using System;
using System.Threading;

namespace SimpleTrueTable
{
    class SimpleTrueTable
    {
        public static int operators, result, condition1value, condition2value;
        public static string condition1, condition2, resultValue;
        public static void Main()
        {
            Console.Clear();
            Console.WriteLine("A 1° Condição é V ou F ?");
            condition1 = Console.ReadLine();
            if(condition1 == "v" | condition1 == "V"){
                condition1value = 1;
            }
            else if(condition1 == "f" | condition1 == "F"){
                condition1value = 0;
            }
            else{
                Console.Clear();
                Console.WriteLine("Por Favor, Digite Uma Opção Valida");
                Thread.Sleep(2000);
                Main();
            }

            Console.Clear();
            Console.WriteLine("Qual Operador Você Ira Usar ?");
            Console.WriteLine("1 - ^\n2 - v\n3 - v_\n4 - ->\n5 - <->\n\n");
            operators = int.Parse(Console.ReadLine());

            Console.Clear();
            Console.WriteLine("A 2° Condição é V ou F ?");
            condition2 = Console.ReadLine();
            if(condition2 == "v" | condition2 == "V"){
                condition2value = 1;
            }
            else if(condition2 == "f" | condition2 == "F"){
                condition2value = 0;
            }
            else{
                Console.Clear();
                Console.WriteLine("Por Favor, Digite Uma Opção Valida");
                Thread.Sleep(2000);
                Main();
            }


            // AND
            if(operators == 1){
                result = and(condition1value, condition2value);
                Converter(result);
            }
            // OR
            else if(operators == 2){
                result = or(condition1value, condition2value);
                Converter(result);
            }
            // XOR
            else if(operators == 3){
                result = xor(condition1value, condition2value);
                Converter(result);
            }
            // Implica
            else if(operators == 4){
                result = ifthen(condition1value, condition2value);
                Converter(result);
            }
            // DUPLA IMPLICA
            else if(operators == 5){
                result = ifonlyif(condition1value, condition2value);
                Converter(result);
            }
            else{
                Console.Clear();
                Console.WriteLine("Desculpe-nos, Mais Não Foi Possivel Encontrar Esta Opção...");
                Thread.Sleep(2000);
                Main();
            }
        }
        public static void Converter(int result){
            if(result == 1){
                resultValue = "V";
                Continue(resultValue);
            }
            else if(result == 0){
                resultValue = "F";
                Continue(resultValue);
            }
            else{
                Console.Clear();
                Console.WriteLine("WhAt tHe FUck ?");
                Main();
            }
        }
        public static void Continue(string resultValue){
            Console.Clear();
            Console.WriteLine("Seu Resultado é de: {0}\n\n", resultValue);
            Console.WriteLine("Press ENTER to continue...");
            Console.ReadKey();
            Main();
        }

        public static int not(int condition1) {
		if(condition1==0) return 1;
		return 0;
        }
        public static int or(int condition1, int condition2) {
            if(condition1==1 | condition2==1) return 1;
            return 0;
        }
        public static int xor(int condition1, int condition2) {
            if(condition1==1 & condition2==1){
                return 0;
            }
            else if(condition1==0 & condition2==0){
                return 0;
            }
            return 1;
        }
        public static int and(int condition1, int condition2) {
            if(condition1==1 & condition2==1) return 1;
            return 0;
        }
        public static int ifthen(int condition1, int condition2) {
            if(condition1==0 | condition2==1) return 1;
            return 0;
        }
        public static int ifonlyif(int condition1, int condition2) {
            if((condition1==1 & condition2==1) | (condition1==0 & condition2==0)){
                return 1;
            }
            return 0;
        }
    }
}
