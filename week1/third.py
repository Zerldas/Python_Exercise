import random as rd
import check

# Khởi tạo mảng
a = []
a.extend(rd.randint(1, 100) for _ in range(1, 10))

print("\n Các phần tử trong mảng a:")
for i in a:
    print(f"{i}", end = " ")

print("\n Các số nguyên tố trong mảng a: ")
for i in a:
    if check.is_prime(i):
        print(f"{i}", end = " ")

print("\n Thêm một phần tử vào mảng ")
n = int(input("Nhập giá trị muốn thêm vào mảng: "))
a.append(n)
print("Mảng sau khi thêm: ", end = " ")
print(a)

idx = int(input("Nhập vị trí muốn xóa: "))
a.pop(idx)
print("Mảng sau khi xóa", end = " ")
print(a)

print("\n Xóa một phần tử khỏi mảng")
de = int(input("Nhập phần tử muốn xóa khỏi mảng: "))
a.remove(de)
print("Mảng sau khi xóa", end = " ")
print(a)

x = int(input("Nhập phần tử x: "))
for i in range(len(a)):
    if a[i] == x:
        print(f"Vị trí của phần tử {x} trong mảng là: {i}")
        