import numpy as np

# 1. Tạo ma trận ngẫu nhiên
def create_random_matrix(rows = 4, cols = 4, low = 0, high = 100):
    return np.random.randint(low, high, size=(rows, cols))

# 2. Tổng 2 ma trận
def matrix_sum(a, b):
    return a + b

# 3. Hiệu 2 ma trận
def matrix_diff(a, b):
    return a - b

# 4. Tích từng phần tử
def matrix_product_elementwise(a, b):
    return a * b

# 5. Nhân ma trận (theo đại số tuyến tính)
def matrix_dot(a, b):
    return np.dot(a, b)

# 6. Chia từng phần tử
def matrix_div(a, b):
    return a * (1 / b)

# 7. Ma trận chuyển vị
def matrix_transpose(a):
    return a.T

# 8. Định thức ma trận
def matrix_determinant(a):
    return np.linalg.det(a)

# 9. Ma trận nghịch đảo
def matrix_inverse(a):
    return np.linalg.inv(a)

# 10. Hạng của ma trận
def matrix_rank(a):
    return np.linalg.matrix_rank(a)

# 11. Giá trị riêng & vector riêng
def matrix_eig(a):
    vals, vecs = np.linalg.eig(a)
    return vals, vecs

# 12. Chuẩn Frobenius (độ lớn ma trận)
def matrix_norm(a):
    return np.linalg.norm(a)

# 13. Trace (tổng đường chéo chính)
def matrix_trace(a):
    return np.trace(a)

# 14. Nối ma trận (theo chiều ngang)
def matrix_concat_h(a, b):
    return np.hstack((a, b))

# 15. Nối ma trận (theo chiều dọc)
def matrix_concat_v(a, b):
    return np.vstack((a, b))