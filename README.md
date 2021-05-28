Hasanabbas Momin

Sooraj Sathish



# IAS_arch
Simulating the IAS architecture in python

C program:
main () {
int a=1, b=15, c;
if (a == b)
c = a – b;
else
c = a + b;
}

Assembly code:

#0x100 contains a=1,0x101->b,0x102->c.
#ALL NUMBERS ARE IN HEXADECIMAL

1 LOAD M(100) , SUB M(101) #AC=a-b

2 STOR M(103) , LOAD -|M(103)| 

3 JUMP+ M(6,0:19) # AC will be non-negative only if m(103) is 0 => a-b=0 => a=b

4 LOAD M(100) , ADD M(101)#This is the else part c=a+b

5 STOR M(102) , HALT

6 LOAD M(100) , SUB M(101)#if part c=a-b

7 STOR M(102) , HALT

Explanation of code:

The main() function calls all the other functions and also itself, recursively, to simulate the continuous fetch,decode,execute cycles of the IAS machine.

The fetch() function fetches the various values required for execution and stores them in variables like mar,ibr,etc(all self explanatory variable names have neen used).

The left() function executes left instruction, if it exists.

The right() instruction executes the right instruction of a word.

The program instructions and data are stored in a 2D array mm[]. 

The instructions start from position 0 of mm.

Data is stored from position 0x100 onwards.


