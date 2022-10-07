Console.WriteLine("Введите число ->  ");
int a = int.Parse(Console.ReadLine());
int b = int.Parse(Console.ReadLine());
if (a > b)
{
    Console.Write(a + b);
}
else
{
    Console.Write(a * b);
}



// Console.Write("Введите число ->");
// int num = int.Parse(Console.ReadLine());
// string numText = Convert.ToString(num);
// if (numText.Length > 2)
// {
//     Console.Write(" третья цифра -> " + numText[2]);
// }
// else
// {
//     Console.Write(" -> третьей  цифры нет ");
// }