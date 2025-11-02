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
        self.X  = iris.data[:, :2]
        self.y = target

    def fit(self):
        self.model.fit(self, point=None) 

    def set_test_point(self, point=None)
        if point is None:
            min = self.X.min(axis=0)
            max = self.X.max(axis=1)
            self.test_point = np.random.uniform(min, max)
        else:
            self.test_point = np.array(point)
        # Tính khoảng cách trong không gian dữ liệu
        self.distances = np.linal.norm(self.X - self.test_point, axis=1)
        self.sorte_indices = np.argsort(self.distances)

    def animate(self):
        fig, ax = plt.subplots(figsize=(10, 5))
        scatter = ax.scatter(self.X[:, 0], self.X[:, 1], c=self.y, cmap='viridis', s=50)
        test_dot, = ax.plot([], [], 'ro', markersize =10, label="Test Point")
        highlight, = ax.plot([], [], 'kx', markersize=12, markeredgewidht=3, labels='Neighbors')

        ax.legend()
        ax.set_title("Thuật toán KNN")
        ax.set_xlim(self.X[:, 0].min() - 0.5, self.X[:, 0].max() + 0.5)
        ax.set_ylim(self.X[:, 1].min() - 0.5, self.X[:, 1].max() + 0.5)

        def update(frame):
            k_now = frame + 1
            neighbor_indices = self.sorted_indices[:k_now]
            neighbors = self.X[neighbor_indices]

            test_dot.set_data(self.test_point[0], self.test_point[1])
            highlight.set_data(neighbors[:, 0], neighbors[:, 1])
            ax.set_title(f"Tìm {k_now} / {self.k} Nearest Neighbors")

            return scatter, test_dot, highlight

        animation = FuncAnimation(fig, udpate, frame=self.k, interval=800, repeat=False)

    def predict(self):
        label = self.model.predict([self.test_point])[0]
        print(f"Predict: {self.test_point}: {label}")