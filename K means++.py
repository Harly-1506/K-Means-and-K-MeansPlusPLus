import matplotlib.pyplot as plt
from numpy.core.numeric import indices
from sklearn import cluster
from sklearn.cluster import KMeans
import numpy
from sklearn.cluster import kmeans_plusplus
import math


def distance(p1, p2):
    return math.sqrt(
        (p1[0] - p2[0]) * (p1[0] - p2[0])
        + (p1[1] - p2[1]) * (p1[1] - p2[1])
        + (p1[2] - p2[2]) * (p1[2] - p2[2])
    )


img = plt.imread("Test.jpg")

print(img.shape)
height = img.shape[0]
width = img.shape[1]

img = img.reshape(height * width, 3)

centers, indices = kmeans_plusplus(img, n_clusters=25, random_state=0)
kmeans = KMeans(n_clusters=5, init="k-means++").fit(img)
lables = kmeans.predict(img)

# img = img.reshape(height, width, 3)


img2 = numpy.zeros_like(img)  # create a new img like "img"


# labels = []
# for p in new_img:
#     distances_to_cluster = []
#     for c in clusters:
#         dis = distance(p, c)
#         distances_to_cluster.append(dis)
#     min_distance = min(distances_to_cluster)
#     label = distances_to_cluster.index(min_distance)
#     labels.append(label)

for i in range(len(img2)):
    img2[i] = centers[lables[i]]

img2 = img2.reshape(height, width, 3)


plt.imshow(img2)
plt.show()
