import sys
import check

n = int(input("Nhập số nguyên n: "))
    
if check.is_prime(n) == 1:
    print(f"\nSố nguyên {n} là số nguyên tố")

sum = 0
for i in range(1, n + 1):
    sum += i
    print(f"{i}", end = " ")
print(f"\nTổng từ 1 đến {n}: {sum}")

print(f"\nSố số nguyên tố từ 1 -> {n}")
for i in range(1, n):
    if check.is_prime(i) == 1:
        print(f"{i}", end = " ")

print(f"\nIn ra {n} số nguyên tố đầu tiên")
count = 0
for i in range(1, sys.maxsize):
    if check.is_prime(i):
        print(f"{i}", end = " ")
        count += 1
    if count == n:
        break