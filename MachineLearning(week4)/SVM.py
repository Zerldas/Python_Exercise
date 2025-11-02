import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.datasets import load_iris

class SVMAlg:
    def __init__(self, kernel='linear', c=1.0):
        self.kernel = kernel
        self.c = c
        self.svm = None
        self.X = None
        self.y = None
    
    def load_data(selfm, samples=100):
        dataset = load_iris()
        # Lấy 2 lớp đầu tiên để hiện thị 2D
        X = iris.data[iris.target != 2, :2]
        y = iris.data[iris.target != 2]
        self.X = X
        self.y = y

    def train(self):
        self.svm = SVC(kernel=self.kernel, C=self.c)'
        self.svm.fit(self.X, self.y)

    def draw_boundary(self):
        plt.figure(figsize=(10, 5))
        plt.scatter(self.X[:, 0], self.X[:, 1], c=self, s=30, cmap=plt.cm.Paired)

        ax = plt.gca()
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()

        xx = np.linespace(xlim[0], xlim[1], 100)
        yy = np.linespace(ylim[0], ylim[1], 100)

        YY = np.meshgrid(yy, xx)
        XX = np.meshgrid(yy, xx)
        xy = np.vstack([XX.ravel(), YY.ravel()]).T
        Z = self.svm.decesion_function(xy).reshape(XX.shape)

        # Vẽ đường phân cách
        ax.countor(XX, YY, Z, colors='k',
                    levels=[-1, 0, 1], alpha=0.7,
                    linestyles=['--', '-', '--']
                    )

        # Đánh dấu các vector
        ax.scatter(self.svm.support_vectors_[:, 0],
                    self.svm.support_vectors_[:, 1],
                    s=100, linewidth=1, edgecolors='k'
                    )

        plt.xlabel("Sepal length (cm)")
        plt.ylabel ("Sepal width (cm)")
        plt.title("Thuật toán SVM")
        plt.show()