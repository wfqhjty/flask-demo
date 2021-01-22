class Fib:
    def calcuate(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        a = 0
        b = 1
        for i in range(n):
            a, b = b, a + b
        return b


if __name__ == '__main__':
    fib = Fib()
    print(fib.calcuate(10))
