s = str(input("Nhập vào chuỗi s: "))
print(s)
print(f"\nĐộ dài của chuỗi s: {len(s)}")
print("\n Xóa bỏ khoảng trắng thừa trong chuỗi s")
st = s.strip()
print("\n Chuỗi s sau khi bỏ khoảng trắng")
print(st)
print("\nĐếm số từ của chuỗi s")
word = st.split()
print(f"\nSố từ của chuỗi s là: {len(word)}")
left = 0
right = 0
k = int(input("Nhập số tự nhiên k: "))
print("\nSố kí tự bên trái: ")
for i in range(0, k):
    print(f"{st[i]}", end = " ")  
    left += 1
print(f"\nSố kí tự bên trái là: {left}")

print("\nSố kí tự bên phải:")
for j in range(len(st) - 1, len(st) - 1 - k, -1):
    print(f"{st[j]}", end = " ")
    right += 1
print(f"\nSố kí tự bên phải là: {right}")

n = int(input("Nhập só nguyên n: "))

count = 0
for i in range(k, len(st)):
    print(f"{st[i]}", end = " ")
    count += 1
    if count == n:
        break