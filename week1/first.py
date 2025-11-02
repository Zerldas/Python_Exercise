a = float(input("Nhập số nguyên a: "))
b = float(input("Nhập số ngueyen b: "))

print(f"Tổng của 2 số nguyên/thực nhập vào là: {a + b:.2f}")
print(f"Hiệu của 2 số nguyên/thực nhập vào là: {a - b:.2f}")
print(f"Tích của 2 số nguyên/thực nhập vào là: {a * b:.2f}")
if b != 0:   
    print(f"Thương của 2 số nguyên/thực nhập vào là: {a / b:.2f}")
else:
    print("Mẫu số b bằng 0 không thể thực hiện phép Thương")
