import matplotlib.pyplot as plt
from sklearn import cluster
from sklearn.cluster import KMeans
import numpy
from sklearn.cluster import kmeans_plusplus
import time


start_time = time.time()


img = plt.imread("ungthunao.png")

print(img.shape)
height = img.shape[0]
width = img.shape[1]

img = img.reshape(height * width, 3)

K = []
errors = []
for i in range(2, 20):
    # centers, indices = kmeans_plusplus(img, n_clusters=10, random_state=0)
    kmeans = KMeans(n_clusters=i, init="k-means++").fit(img)
    lables = kmeans.predict(img)
    clusters = kmeans.cluster_centers_
    error = kmeans.inertia_
    errors.append(error)
    K.append(i)
    print(error)

end_time = time.time()

elapsed_time = end_time - start_time
print("elapsed_time:{0}".format(elapsed_time) + "[sec]")

plt.plot(K, errors, "bx-")
plt.plot(K, errors)
plt.show()
