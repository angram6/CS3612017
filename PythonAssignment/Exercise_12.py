def fibo_recursion(n):
   if n <= 1:
       return n
   else:
       return(fibo_recursion(n-1) + fibo_recursion(n-2))

value = 12

if value <= 0:
   print("Enter a positive integer")
else:
   for i in range(value):
       print(fibo_recursion(i))