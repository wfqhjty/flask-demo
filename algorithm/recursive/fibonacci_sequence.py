class Fibo:

    def __init__(self):
        self.num = 0


    def calculate(self, n):
        if n == 0 or n == 1:
            self.num += 1
            return n
        else:
            return self.calculate(n-1)+self.calculate(n-2)


if __name__ == "__main__":
    fibo = Fibo()
    # 斐波那契数列
    print(fibo.calculate(9))
    print(fibo.num)
