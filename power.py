class Power:
    def pow(self, x: float, n: int)-> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        if n % 2 == 0:
            return self.pow(x * x, n // 2)
        else:
            return x * self.pow(x * x, n // 2)
p = Power()
x = int(input("Enter value of x: "))
n = int(input("Enter value of n: "))
ans = p.pow(x,n)
print(f" {x} to the power of {n} is {ans} ")  
