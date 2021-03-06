from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

__author__ = 'wangj'
__date__ = '2018/01/24 16:52'


def main():
    pass


if __name__ == '__main__':
    x, y = datasets.make_blobs(n_samples=150, n_features=2, centers=3, cluster_std=0.5, shuffle=True, random_state=0)
    plt.figure(1)
    plt.scatter(x[:, 0], x[:, 1], c='blue', marker='o', s=50)
    plt.grid()
    plt.show()
    km = KMeans(n_clusters=3, init='random', n_init=10, max_iter=300, tol=1e-4, random_state=0)
    y_km = km.fit_predict(x)
    plt.figure(2)
    plt.scatter(x[y_km == 0, 0], x[y_km == 0, 1], s=50, c='lightgreen', marker='s', label='cluster 1')
    plt.scatter(x[y_km == 1, 0], x[y_km == 1, 1], s=50, c='orange', marker='o', label='cluster 2')
    plt.scatter(x[y_km == 2, 0], x[y_km == 2, 1], s=50, c='lightblue', marker='v', label='cluster 3')
    plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1], s=250, marker='*', c='red', label='centroids')
    plt.legend(loc='best')
    plt.grid()
    plt.show()
