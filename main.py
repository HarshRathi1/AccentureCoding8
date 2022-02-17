'''A carry is a digit that is transferred to left if sum of digits exceeds 9 while adding two numbers from right-to-left one digit at a time
You are required to implement the following function.
Int NumberOfCarries(int num1 , int num2);
The functions accepts two numbers ‘num1’ and ‘num2’ as its arguments. You are required to calculate and return  the total number of carries generated while adding digits of two numbers ‘num1’ and ‘ num2’.
Assumption: num1, num2>=0
Example:
Input
Num 1: 451
Num 2: 349
Output
2
Explanation:
Adding ‘num 1’ and ‘num 2’ right-to-left results in 2 carries since ( 1+9) is 10. 1 is carried and (5+4=1) is 10, again 1 is carried. Hence 2 is returned.'''
num1=23
num2=563
def NumberOfCarries(num1,num2):
    n1 = str(num1)[::-1]
    n2 = str(num2)[::-1]
    c = 0
    if len(n1) < len(n2):
        for i in range(len(n1)):
            if (int(n1[i]) + int(n2[i])) > 9:
                print(n1[i], n2[i], i)
                c += 1
    else:
        for i in range(len(n2)):
            if (int(n1[i]) + int(n2[i])) > 9:
                print(n1[i], n2[i], i)
                c += 1
    return c
print(NumberOfCarries(num1,num2))