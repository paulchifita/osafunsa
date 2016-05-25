# fibo.py
# This program determines the value of the nth term in the finbonacci sequence.
# Paul Chifita

def main():
    while True:
            
        print("This program determines the value of the current term in the Fibonacci sequence.")
        print()
        n = eval(input("enter the value of n: "))
        print()
        current = 1
        prev = 1
        fiboseq = []
        fibo = []
        if n == 1 or n == 2:
            for i in range(n):
                fiboseq.append(current)
            print(current)
            print(fiboseq)
        elif n > 2:
            fibo.append(1)
            fibo.append(1)
            for i in range(n-2):
                nxt = prev + current
                prev = current
                current = nxt
                fibo.append(current)
            print(current)
            print(fibo)


            

main()
