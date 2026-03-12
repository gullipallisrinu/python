class MyMath:
    def calculate(self, operation, n):
        if operation == "sum":
            result = sum(range(1, n + 1))
            print("Sum =", result)

        elif operation == "prime":
            print("Prime numbers:")
            count = 0
            num = 2
            while count < n:
                for i in range(2, num):
                    if num % i == 0:
                        break
                else:
                    print(num, end=" ")
                    count += 1
                num += 1
            print()

        elif operation == "fibonacci":
            a, b = 0, 1
            print("Fibonacci Series:")
            for i in range(n):
                print(a, end=" ")
                a, b = b, a + b
            print()

        elif operation == "factorial":
            fact = 1
            for i in range(1, n + 1):
                fact *= i
            print("Factorial =", fact)

        else:
            print("Invalid Operation")

m = MyMath()

print("1.Sum of n numbers")
print("2.First n Prime numbers")
print("3.Fibonacci series")
print("4.Factorial")

choice = int(input("Enter choice: "))
n = int(input("Enter n value: "))

if choice == 1:
    m.calculate("sum", n)
elif choice == 2:
    m.calculate("prime", n)
elif choice == 3:
    m.calculate("fibonacci", n)
elif choice == 4:
    m.calculate("factorial", n)



'''
1.Sum of n numbers
2.First n Prime numbers
3.Fibonacci series
4.Factorial
Enter choice: 2
Enter n value: 10
Prime numbers:
2 3 5 7 11 13 17 19 23 29
PS D:\python> python 3q.py
1.Sum of n numbers
2.First n Prime numbers
3.Fibonacci series
4.Factorial
Enter choice: 3
Enter n value: 5
Fibonacci Series:
0 1 1 2 3
PS D:\python> python 3q.py
1.Sum of n numbers
2.First n Prime numbers
3.Fibonacci series
4.Factorial
Enter choice: 4
Enter n value: 5
Factorial = 120

'''
