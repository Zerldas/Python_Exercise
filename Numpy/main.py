import vector
import matrix

def vector():
    vector_a = vector.create_random_vector()
    vector_b = vector.create_random_vector()

    print("Vector a:", vector_a)
    print("Vector b:", vector_b)

    print("1. Tổng:", vector.vector_sum(vector_a, vector_b))
    print("2. Hiệu:", vector.vector_diff(vector_a, vector_b))
    print("3. Tích từng phần tử:", vector.vector_product(vector_a, vector_b))
    print("4. Tích có hướng:", vector.vector_cross(vector_a, vector_b))
    print("5. Tích vô hướng:", vector.vector_dot(vector_a, vector_b))
    print("6. Thương:", vector.vector_div(vector_a, vector_b))
    print("7. Khoảng cách:", vector.vector_distance(vector_a, vector_b))
    cos_theta, angle = vector.vector_angle(vector_a, vector_b)
    print("8. cos(θ):", cos_theta)
    print("   Góc giữa 2 vector:", angle, "radian")
    print("9. Quan hệ:", vector.check_relation(vector_a, vector_b))
    vector_c = vector.vector_concat(vector_a, vector_b)
    print("10. Nối:", vector_c)
    print("11. Đảo ngược vector a:", vector.vector_reverse(vector_a))
    print("12. Giá trị duy nhất trong vector c:", vector.vector_unique(vector_c))
    print("13. Độ dài vector c:", vector.vector_length(vector_c))
    print("14. Một phần tử bất kì trong vector c:", vector.vector_random_element(vector_c))


def matrix():
    A = matrix.create_random_matrix(3, 3, 0, 10)
    B = matrix.create_random_matrix(3, 3, 0, 10)

    print("Ma trận A:\n", A)
    print("Ma trận B:\n", B)

    print("\n1. Tổng A+B:\n", matrix.matrix_sum(A, B))
    print("\n2. Hiệu A-B:\n", matrix.matrix_diff(A, B))
    print("\n3. Tích từng phần tử A*B:\n", matrix.matrix_product_elementwise(A, B))
    print("\n4. Nhân ma trận A.B:\n", matrix.matrix_dot(A, B))
    print("\n5. Chia từng phần tử A/B:\n", matrix.matrix_div(A, B))
    print("\n6. Chuyển vị A^T:\n", matrix.matrix_transpose(A))
    print("\n7. Định thức det(A):", matrix.matrix_determinant(A))
    print("\n8. Nghịch đảo A^-1:\n", matrix.matrix_inverse(A))
    print("\n9. Hạng rank(A):", matrix.matrix_rank(A))
    vals, vecs = matrix.matrix_eig(A)
    print("\n10. Giá trị riêng:", vals)
    print("    Vector riêng:\n", vecs)
    print("\n11. Norms ||A||:", matrix.matrix_norm(A))
    print("\n12. Trace (A):", matrix.matrix_trace(A))
    print("\n13. Nối ngang [A | B]:\n", matrix.matrix_concat_h(A, B))
    print("\n14. Nối dọc [A ; B]:\n", matrix.matrix_concat_v(A, B))

if __name__ == "__main__":
    vector()