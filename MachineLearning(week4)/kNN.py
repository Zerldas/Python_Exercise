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

        scatter = ax.scatter(self.X[:, 0], self.X[:, 1], c=self.y, cmap='viridis', s=70)

        test_dot, = ax.plot([], [], 'ko', markerfacecolor='none', markeredgewidth=1, markersize=5, label="Test Point")

        highlight, = ax.plot([], [], 'kx', color='red', markersize=5, markeredgewidth=1, label='Neighbors')

        ax.set_xlim(self.X[:, 0].min() - 0.5, self.X[:, 0].max() + 0.5)
        ax.set_ylim(self.X[:, 1].min() - 0.5, self.X[:, 1].max() + 0.5)
        ax.set_xlabel("Sepal length")
        ax.set_ylabel("Sepal width")
        ax.set_title("KNN")
        ax.legend()

        # test point
        tx, ty = self.test_point
        test_dot.set_data([tx], [ty])

        # thứ tự index theo khoảng cách
        sorted_idx = self.sorted_indices

        def update(frame):
            # frame chạy từ 0 → k-1
            if frame < self.k:
                hit = sorted_idx[:frame+1]  # tăng dần số neighbors
            else:
                hit = sorted_idx[:self.k]

            neighbors = self.X[hit]
            highlight.set_data(neighbors[:, 0], neighbors[:, 1])

            ax.set_title(f"Tìm neighbor {len(hit)} / {self.k}")

            return scatter, test_dot, highlight

        self.anim = FuncAnimation(fig, update, frames=self.k, interval=600, repeat=False)

        plt.show()