import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy
import time

start_time = time.time()

img = plt.imread("ungthunao.png")

print(img.shape)
height = img.shape[0]
width = img.shape[1]

img = img.reshape(height * width, 3)

kmeans = KMeans(n_clusters=15, init="random").fit(img)
lables = kmeans.predict(img)
clusters = kmeans.cluster_centers_
# error = kmeans.inertia_
# print(error)
print(lables)
print(clusters)
img2 = numpy.zeros_like(img)  # create a new img like "img"

for i in range(len(img2)):
    img2[i] = clusters[lables[i]]

img2 = img2.reshape(height, width, 3)

# img2 = numpy.zeros((height, width, 3), dtype=numpy.uint8)

# index = 0
# for i in range(height):
#     for j in range(width):
#         lable_of_pixel = lables[index]
#         img2[i][j] = clusters[lable_of_pixel]
#         index += 1
end_time = time.time()

elapsed_time = end_time - start_time
print("elapsed_time:{0}".format(elapsed_time) + "[sec]")

plt.imshow(img2)
plt.show()
