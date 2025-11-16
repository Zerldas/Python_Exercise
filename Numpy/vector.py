import numpy as np

# 1. Tạo vector ngẫu nhiên
def create_random_vector(size=100, low=0, high=100):
    return np.random.randint(low, high, size=size)

# 2. Tổng 2 vector
def vector_sum(a, b):
    return a + b

# 3. Hiệu 2 vector
def vector_diff(a, b):
    return a - b

# 4. Tích từng phần tử
def vector_product(a, b):
    return a * b

# 5. Tích có hướng (cross product)
def vector_cross(a, b):
    return np.cross(a, b)

# 6. Tích vô hướng (dot product)
def vector_dot(a, b):
    return np.dot(a, b)

# 7. Thương của 2 vector (chia từng phần tử)
def vector_div(a, b):
    return a * (1 / b)

# 8. Khoảng cách Euclid giữa 2 vector
def vector_distance(a, b):
    return np.linalg.norm(a - b)

# 9. Góc giữa 2 vector
def vector_angle(a, b):
    cos_theta = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
    angle = np.arccos(np.clip(cos_theta, -1.0, 1.0))  # tránh sai số vượt [-1,1]
    return cos_theta, angle

# 10. Kiểm tra quan hệ giữa 2 vector
def check_relation(a, b):
    cos_theta, _ = vector_angle(a, b)
    if np.isclose(cos_theta, 0):
        return "Vuông góc"
    elif np.isclose(abs(cos_theta), 1):
        return "Song song"
    else:
        return "Không vuông góc cũng không song song"

# 11. Nối 2 vector
def vector_concat(a, b):
    return np.concatenate((a, b))

# 12. Đảo ngược vector
def vector_reverse(a):
    return a[::-1]

# 13. Lấy các giá trị duy nhất
def vector_unique(a):
    return np.unique(a)

# 14. Độ dài vector
def vector_length(a):
    return len(a)

# 15. Lấy phần tử ngẫu nhiên
def vector_random_element(a):
    return np.random.choice(a)