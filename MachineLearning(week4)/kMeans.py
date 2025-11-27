import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

class KMeanAlg:
    def __init__(self, cluster=3, random_state=42):
        self.clusters = cluster
        self.random_state = random_state
        self.kmeans = KMeans(n_clusters=self.clusters, init='random', n_init=1, max_iter=1, random_state=self.random_state)
        self.X = None
        self.central_history = []
        self.labels_history = []

    def load_data(self):
        dataset = load_iris()
        self.X = dataset.data[: , :2] # Xài 2 thuộc tính đầu tiên để dễ hiển thị

    def fit(self, max_iter=10):
        # Huấn luyện từng bước và lưu lại trạng thái tâm cụm
        X = self.X
        for i in range(max_iter):
            self.kmeans.fit(X)
            self.kmeans.max_iter = 1
            self.central_history.append(self.kmeans.cluster_centers_.copy())
            self.labels_history.append(self.kmeans.labels_.copy())
            self.kmeans.max_iter += 1
        
    def animation(self):
        fig, ax = plt.subplots(figsize=(10, 5))
        scatter = ax.scatter(self.X[:, 0], self.X[:, 1], c=self.labels_history[0], cmap='viridis', s=50)
        centrals_plot, = ax.plot([], [], 'rX', markersize=12, markeredgewidth=3)

        ax.set_xlim(self.X[:, 0].min() - 0.5, self.X[:, 0].max() + 0.5)
        ax.set_ylim(self.X[:, 1].min() - 0.5, self.X[:, 1].max() + 0.5)
        ax.set_title("Biểu đồ hiển thị cách hoạt động của thuật toán K-Means")
        ax.set_xlabel("Chiều dài đài hoa (sepal length)")
        ax.set_ylabel("Chiều rộng đài hoa (sepal width)")

        def update(frame):
            labels = self.labels_history[frame]
            central = self.central_history[frame]
            scatter.set_offsets(self.X)
            scatter.set_array(labels)
            centrals_plot.set_data(central[:, 0], central[:, 1])
            ax.set_title(f"Iteration: {frame + 1}")
            return scatter, centrals_plot
        
        self.anim = FuncAnimation(fig, update, frames=len(self.central_history), interval=500, repeat=False)
        plt.show()
        