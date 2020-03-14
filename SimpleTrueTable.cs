using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;

namespace SimpleTrueTable
{
    class SimpleTrueTable
    {   
        #region Array2
        public static int[] p2 = new[] { 1, 1, 0, 0};
        public static int[] q2 = new[] { 1, 0, 1, 0};
        public static int[] np2 = new[] { 0, 0, 1, 1};
        public static int[] nq2 = new[] { 0, 1, 0, 1};
        #endregion
        #region Array3
        public static int[] p3 = new[] { 1, 1, 1, 1, 0, 0, 0, 0};
        public static int[] q3 = new[] { 1, 1, 0, 0, 1, 1, 0, 0};
        public static int[] r3 = new[] { 1, 0, 1, 0, 1, 0, 1, 0};
        public static int[] np3 = new[] { 0, 0, 0, 0, 1, 1, 1, 1};
        public static int[] nq3 = new[] { 0, 0, 1, 1, 0, 0, 1, 1};
        public static int[] nr3 = new[] { 0, 1, 0, 1, 0, 1, 0, 1};
        #endregion

        public static int operators, result, condition1value, condition2value, option, amount;
        public static string condition1, condition2, resultValue, stringOperators;
        public static void Main()
        {
            Console.Clear();
            Console.WriteLine("Main Menu\n\n1 - Calculate\n2 - Calculate All Possibilities\n3 - Show Table\n\n4 - Create a Poposition\n\n0 - Exit");
            option = int.Parse(Console.ReadLine());
            if(option == 1){
                Calculator();
            }
            else if(option == 2){
                ExpressionCalculator();
            }
            else if(option == 3){
                Table();
            }
            else if(option == 4){
                CreateProposition();
            }
            else if(option == 0){
                Exit();
            }
            else{
                Console.Clear();
                Console.WriteLine("Invalid option..");
                Thread.Sleep(500);
                Console.WriteLine("Invalid option...");
                Thread.Sleep(500);
                Console.WriteLine("Invalid option....");
                Thread.Sleep(500);
                Main();
            }
        }
        #region Calculator
        public static void Calculator(){
            Console.Clear();
            Console.WriteLine("The 1st Condition is True or False ? (0 - Return)\n");
            Console.WriteLine("T - True\nF - False\n");
            condition1 = Console.ReadLine();
            if(condition1 == "t" | condition1 == "T"){
                condition1value = 1;
            }
            else if(condition1 == "f" | condition1 == "F"){
                condition1value = 0;
            }
            else if(condition1 == "0"){
                Main();
            }
            else{
                Console.Clear();
                Console.WriteLine("Please Enter a Valid Option.");
                Thread.Sleep(2000);
                Calculator();
            }

            Console.Clear();
            Console.WriteLine("Whatch Operator Will You Use ?");
            Console.WriteLine("1 - ^\n2 - v\n3 - v_\n4 - ->\n5 - <->\n\n");
            operators = int.Parse(Console.ReadLine());

            Console.Clear();
            Console.WriteLine("The 2nd Condition is True or False ?\n");
            Console.WriteLine("T - True\nF - False\n");
            condition2 = Console.ReadLine();
            if(condition2 == "t" | condition2 == "T"){
                condition2value = 1;
            }
            else if(condition2 == "f" | condition2 == "F"){
                condition2value = 0;
            }
            else{
                Console.Clear();
                Console.WriteLine("Please Enter a Valid Option.");
                Thread.Sleep(2000);
                Calculator();
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
                Console.WriteLine("Sorry, We Dont Find This Option ...");
                Thread.Sleep(2000);
                Calculator();
            }
        }
        public static void Converter(int result){
            if(result == 1){
                resultValue = "T";
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
            Console.WriteLine("Your Result is: {0}\n\n", resultValue);
            Console.WriteLine("Press ENTER to continue...");
            Console.ReadKey();
            Calculator();
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
        #endregion
        
        #region ExpressionCalculator
        public static void ExpressionCalculator(){
            Console.Clear();

            Console.WriteLine("How Many Propositions Will You Use ? (0 - Return)");
            amount = int.Parse(Console.ReadLine());

            #region twoPropositions
            if(amount == 2){

                ShowTable2();

                Console.WriteLine("Enter The 1st Proposition:");
                Console.WriteLine("p, q, np, nq\n");
                condition1 = Console.ReadLine();

                int[] possibility1 = new int[4];
                if(condition1 == "p"){
                    for(int i = 0; i < 4; i++){
                        possibility1[i] = p2[i];
                    }
                }
                else if(condition1 == "q"){
                    for(int i = 0; i < 4; i++){
                        possibility1[i] = q2[i];
                    }
                }
                else if(condition1 == "np"){
                    for(int i = 0; i < 4; i++){
                        possibility1[i] = np2[i];
                    }
                }
                else if(condition1 == "nq"){
                    for(int i = 0; i < 4; i++){
                        possibility1[i] = nq2[i];
                    }
                }
                else{
                    Console.Clear();
                    Console.WriteLine("Invalid option....");
                    Thread.Sleep(1500);
                    ExpressionCalculator();
                }

                Console.Clear();
                Console.WriteLine("Whatch Operator Will You Use ?");
                Console.WriteLine("1 - ^\n2 - v\n3 - v_\n4 - ->\n5 - <->\n\n");
                operators = int.Parse(Console.ReadLine());


                ShowTable2();

                Console.WriteLine("Enter The 2nd Proposition:");
                Console.WriteLine("p, q, np, nq\n");
                condition2 = Console.ReadLine();

                int[] possibility2 = new int[4];
                if(condition2 == "p"){
                    for(int i = 0; i < 4; i++){
                        possibility2[i] = p2[i];
                    }
                }
                else if(condition2 == "q"){
                    for(int i = 0; i < 4; i++){
                        possibility2[i] = q2[i];
                    }
                }
                else if(condition2 == "np"){
                    for(int i = 0; i < 4; i++){
                        possibility2[i] = np2[i];
                    }
                }
                else if(condition2 == "nq"){
                    for(int i = 0; i < 4; i++){
                        possibility2[i] = nq2[i];
                    }
                }
                else{
                    Console.Clear();
                    Console.WriteLine("Invalid option....");
                    Thread.Sleep(1500);
                    ExpressionCalculator();
                }  

                //-----------Calculation---------------

                int[] result1Return = new int[4];
                if(operators == 1){
                    stringOperators = "^";
                    for(int i = 0, j = 0, k = 0; i < p2.Length; i++, j++, k++) 
                    {
                        condition1value = possibility1[i];
                        condition2value = possibility2[j];
                        result1Return[k] = and(condition1value, condition2value);
                    }
                }
                else if(operators == 2){
                    stringOperators = "v";
                    for(int i = 0, j = 0, k = 0; i < p2.Length; i++, j++, k++) 
                    {
                        condition1value = possibility1[i];
                        condition2value = possibility2[j];
                        result1Return[k] = or(condition1value, condition2value);
                    }
                }
                else if(operators == 3){
                    stringOperators = "v_";
                    for(int i = 0, j = 0, k = 0; i < p2.Length; i++, j++, k++) 
                    {
                        condition1value = possibility1[i];
                        condition2value = possibility2[j];
                        result1Return[k] = xor(condition1value, condition2value);
                    }
                }
                else if(operators == 4){
                    stringOperators = "->";
                    for(int i = 0, j = 0, k = 0; i < p2.Length; i++, j++, k++) 
                    {
                        condition1value = possibility1[i];
                        condition2value = possibility2[j];
                        result1Return[k] = ifthen(condition1value, condition2value);
                    }
                }
                else if(operators == 5){
                    stringOperators = "<->";
                    for(int i = 0, j = 0, k = 0; i < p2.Length; i++, j++, k++) 
                    {
                        condition1value = possibility1[i];
                        condition2value = possibility2[j];
                        result1Return[k] = ifonlyif(condition1value, condition2value);
                    }
                }
                else{
                    Console.Clear();
                    Console.WriteLine("Invalid option....");
                    Thread.Sleep(1500);
                    ExpressionCalculator();
                }
                
                //-----------Show Result of Calcule-----------

                Console.Clear();
                Console.WriteLine("+------+ +------+  +--------+");
                Console.WriteLine($"¦   {condition1}  ¦ ¦   {condition2}  ¦  ¦  {condition1} {stringOperators} {condition2} ¦");
                Console.WriteLine("+------+ +------+  +--------+");
                Console.WriteLine("+------+ +------+  +--------+");
                for(int i = 0; i < result1Return.Length; i++)
                {
                    Console.WriteLine("¦   {0}  ¦ ¦   {1}  ¦  ¦    " + result1Return[i] + "   ¦", possibility1[i], possibility2[i]);
                }
                Console.WriteLine("+------+ +------+  +--------+\n");

                Console.WriteLine("Press ENTER to Continue...");
                Console.ReadKey();
                ExpressionCalculator();
            }
            #endregion
            #region ThreePropositions
            else if(amount == 3){

                ShowTable3();

                Console.WriteLine("Enter The 1st Proposition:");
                Console.WriteLine("p, q, r, np, nq, nr\n");
                condition1 = Console.ReadLine();

                int[] possibility1 = new int[8];
                if(condition1 == "p"){
                    for(int i = 0; i < 8; i++){
                        possibility1[i] = p3[i];
                    }
                }
                else if(condition1 == "q"){
                    for(int i = 0; i < 8; i++){
                        possibility1[i] = q3[i];
                    }
                }
                else if(condition1 == "r"){
                    for(int i = 0; i < 8; i++){
                        possibility1[i] = r3[i];
                    }
                }
                else if(condition1 == "np"){
                    for(int i = 0; i < 8; i++){
                        possibility1[i] = np3[i];
                    }
                }
                else if(condition1 == "nq"){
                    for(int i = 0; i < 8; i++){
                        possibility1[i] = nq3[i];
                    }
                }
                else if(condition1 == "nr"){
                    for(int i = 0; i < 8; i++){
                        possibility1[i] = nr3[i];
                    }
                }
                else{
                    Console.Clear();
                    Console.WriteLine("Invalid option....");
                    Thread.Sleep(1500);
                    ExpressionCalculator();
                }

                Console.Clear();
                Console.WriteLine("Whatch Operator Will You Use ?");
                Console.WriteLine("1 - ^\n2 - v\n3 - v_\n4 - ->\n5 - <->\n\n");
                operators = int.Parse(Console.ReadLine());


                ShowTable3();

                Console.WriteLine("Enter The 2nd Proposition:");
                Console.WriteLine("p, q, r, np, nq, nr\n");
                condition2 = Console.ReadLine();

                int[] possibility2 = new int[8];
                if(condition2 == "p"){
                    for(int i = 0; i < 8; i++){
                        possibility2[i] = p3[i];
                    }
                }
                else if(condition2 == "q"){
                    for(int i = 0; i < 8; i++){
                        possibility2[i] = q3[i];
                    }
                }
                else if(condition2 == "r"){
                    for(int i = 0; i < 8; i++){
                        possibility2[i] = r3[i];
                    }
                }
                else if(condition2 == "np"){
                    for(int i = 0; i < 8; i++){
                        possibility2[i] = np3[i];
                    }
                }
                else if(condition2 == "nq"){
                    for(int i = 0; i < 8; i++){
                        possibility2[i] = nq3[i];
                    }
                }
                else if(condition2 == "nr"){
                    for(int i = 0; i < 8; i++){
                        possibility2[i] = nr3[i];
                    }
                }
                else{
                    Console.Clear();
                    Console.WriteLine("Invalid option....");
                    Thread.Sleep(1500);
                    ExpressionCalculator();
                }  

                //-----------Calculation---------------

                int[] result1Return = new int[8];
                if(operators == 1){
                    stringOperators = "^";
                    for(int i = 0, j = 0, k = 0; i < p3.Length; i++, j++, k++) 
                    {
                        condition1value = possibility1[i];
                        condition2value = possibility2[j];
                        result1Return[k] = and(condition1value, condition2value);
                    }
                }
                else if(operators == 2){
                    stringOperators = "v";
                    for(int i = 0, j = 0, k = 0; i < p3.Length; i++, j++, k++) 
                    {
                        condition1value = possibility1[i];
                        condition2value = possibility2[j];
                        result1Return[k] = or(condition1value, condition2value);
                    }
                }
                else if(operators == 3){
                    stringOperators = "v_";
                    for(int i = 0, j = 0, k = 0; i < p3.Length; i++, j++, k++) 
                    {
                        condition1value = possibility1[i];
                        condition2value = possibility2[j];
                        result1Return[k] = xor(condition1value, condition2value);
                    }
                }
                else if(operators == 4){
                    stringOperators = "->";
                    for(int i = 0, j = 0, k = 0; i < p3.Length; i++, j++, k++) 
                    {
                        condition1value = possibility1[i];
                        condition2value = possibility2[j];
                        result1Return[k] = ifthen(condition1value, condition2value);
                    }
                }
                else if(operators == 5){
                    stringOperators = "<->";
                    for(int i = 0, j = 0, k = 0; i < p3.Length; i++, j++, k++) 
                    {
                        condition1value = possibility1[i];
                        condition2value = possibility2[j];
                        result1Return[k] = ifonlyif(condition1value, condition2value);
                    }
                }
                else{
                    Console.Clear();
                    Console.WriteLine("Invalid option....");
                    Thread.Sleep(1500);
                    ExpressionCalculator();
                }
                
                //-----------Show Result of Calcule-----------

                Console.Clear();
                Console.WriteLine("+------+ +------+  +--------+");
                Console.WriteLine($"¦   {condition1}  ¦ ¦   {condition2}  ¦  ¦  {condition1} {stringOperators} {condition2} ¦");
                Console.WriteLine("+------+ +------+  +--------+");
                Console.WriteLine("+------+ +------+  +--------+");
                for(int i = 0; i < result1Return.Length; i++)
                {
                    Console.WriteLine("¦   {0}  ¦ ¦   {1}  ¦  ¦    " + result1Return[i] + "   ¦", possibility1[i], possibility2[i]);
                }
                Console.WriteLine("+------+ +------+  +--------+\n");

                Console.WriteLine("Press ENTER to Continue...");
                Console.ReadKey();
                ExpressionCalculator();
            }
            #endregion
            else if(amount == 0){
                Main();
            }
            else{
                Console.Clear();
                Console.WriteLine("Invalid option....");
                Thread.Sleep(1500);
                ExpressionCalculator();
            }
        }
        #endregion
        
        #region Table
        public static void Table(){
            Console.Clear();

            Console.WriteLine("How Many Propositions Will You Use ? (0 - Return)");
            option = int.Parse(Console.ReadLine());

            if(option == 2){
                ShowTable2();

                Console.WriteLine("Press Enter to Continue...");
                Console.ReadKey();

                Main();
            }
            else if(option == 3){
                ShowTable3();

                Console.WriteLine("Press Enter to Continue...");
                Console.ReadKey();

                Main();
            }
            else if(option == 0){
                Main();
            }
            else{
                Console.Clear();
                Console.WriteLine("Invalid option....");
                Thread.Sleep(2000);
                Table();
            }
        }

        public static void ShowTable2(){
            Console.Clear();

            Console.WriteLine("+------+ +------+ +------+ +------+");
            Console.WriteLine("¦   p  ¦ ¦   q  ¦ ¦  ~p  ¦ ¦  ~q  ¦");
            Console.WriteLine("+------+ +------+ +------+ +------+");
            Console.WriteLine("+------+ +------+ +------+ +------+");
            for (int i = 0, j = 0, h = 0, k = 0; i < p2.Length; i++, j++, h++, k++)
            {
                int condition = p2[i];
                int condition2 = q2[j];
                int condition3 = np2[h];
                int condition4 = nq2[k];
                Console.WriteLine("¦   {0}  ¦ ¦   {1}  ¦ ¦   {2}  ¦ ¦   {3}  ¦", condition, condition2, condition3, condition4);
            }
            Console.WriteLine("+------+ +------+ +------+ +------+\n");
        }

        public static void ShowTable3(){
            Console.Clear();

            Console.WriteLine("+------+ +------+ +------+ +------+ +------+ +------+");
                Console.WriteLine("¦   p  ¦ ¦   q  ¦ ¦   r  ¦ ¦  ~p  ¦ ¦  ~q  ¦ ¦  ~r  ¦");
                Console.WriteLine("+------+ +------+ +------+ +------+ +------+ +------+");
                Console.WriteLine("+------+ +------+ +------+ +------+ +------+ +------+");
            for (int i = 0, j = 0, h = 0, k = 0, l = 0, m = 0; i < p3.Length; i++, j++, h++, k++, l++, m++)
            {
                int condition1 = p3[i];
                int condition2 = q3[j];
                int condition3 = r3[h];
                int condition4 = np3[k];
                int condition5 = nq3[l];
                int condition6 = nr3[m];
                Console.WriteLine("¦   {0}  ¦ ¦   {1}  ¦ ¦   {2}  ¦ ¦   {3}  ¦ ¦   {4}  ¦ ¦   {5}  ¦", condition1, condition2, condition3, condition4, condition5, condition6);
            }
            Console.WriteLine("+------+ +------+ +------+ +------+ +------+ +------+\n");
        }
        #endregion
        
        #region CreateProposition
        public static void CreateProposition(){
            Console.Clear();
            
            Console.WriteLine("Option In Development...");
            Thread.Sleep(2000);
            Main();
        }
        #endregion

        public static void Exit() //funcao exit
        {
            Console.Clear();
            Console.WriteLine("Exiting The Program.");
            Thread.Sleep(500);
            Console.Clear();
            Console.WriteLine("Exiting The Program..");
            Thread.Sleep(500);
            Console.Clear();
            Console.WriteLine("Exiting The Program...");
            Thread.Sleep(700);
            Console.Clear();
            Console.WriteLine("Exiting The Program....");
            Thread.Sleep(800);
            Console.Clear();
            Console.WriteLine("Exiting The Program.....");
            Thread.Sleep(800);
            Console.Clear();
            System.Environment.Exit(1); //sai do programa
        }
    }
}