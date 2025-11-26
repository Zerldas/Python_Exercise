import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

class KNNAlg:
    def __init__(self, k=5):
        self.k = k
        self.knn = KNeighborsClassifier(n_neighbors=k)
        self.X = None
        self.y = None
        self.test_point = None
        self.distances = None
        self.sorted_indices = None
        self.anim = None  # giữ animation sống

    def load_data(self):
        dataset = load_iris()
        self.X = dataset.data[:, :2]
        self.y = dataset.target

    def fit(self):
        self.knn.fit(self.X, self.y)

    def set_test_point(self, point=None):
        if point is None:
            min_val = self.X.min(axis=0)
            max_val = self.X.max(axis=0)
            self.test_point = np.random.uniform(min_val, max_val)
        else:
            self.test_point = np.array(point)

        # Chỉ cần 1D array cho plot
        self.distances = np.linalg.norm(self.X - self.test_point, axis=1)
        self.sorted_indices = np.argsort(self.distances)

    def animation(self):
        fig, ax = plt.subplots(figsize=(10, 5))

        # scatter cho dữ liệu gốc
        scatter = ax.scatter(self.X[:, 0], self.X[:, 1], c=self.y, cmap='viridis', s=50)

        # test point và neighbors
        test_dot, = ax.plot([], [], 'ro', markersize=10, label="Test Point")
        highlight, = ax.plot([], [], 'kx', markersize=12, markeredgewidth=3, label='Neighbors')

        ax.set_xlim(self.X[:, 0].min() - 0.5, self.X[:, 0].max() + 0.5)
        ax.set_ylim(self.X[:, 1].min() - 0.5, self.X[:, 1].max() + 0.5)
        ax.set_title("Thuật toán KNN")
        ax.legend()

        def update(frame):
            k_now = frame + 1
            neighbor_indices = self.sorted_indices[:k_now]
            neighbors = self.X[neighbor_indices]

            # Cập nhật vị trí test point
            test_dot.set_data([self.test_point[0]], [self.test_point[1]])

            # Cập nhật vị trí neighbors
            highlight.set_data(neighbors[:, 0], neighbors[:, 1])

            ax.set_title(f"Tìm {k_now} / {self.k} Nearest Neighbors")
            return scatter, test_dot, highlight
        
        self.anim = FuncAnimation(fig, update, frames=self.k, interval=800, repeat=False)

        plt.show()