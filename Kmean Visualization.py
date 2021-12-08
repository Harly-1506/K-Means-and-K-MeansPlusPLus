import pygame
from random import randint
import math
from sklearn.cluster import KMeans


def distance(p1, p2):
    return math.sqrt(
        (p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1])
    )


pygame.init()  # initialize

screen = pygame.display.set_mode((1200, 700))  # Create screen

pygame.display.set_caption("Kmeans Visualization")

running = True

clock = pygame.time.Clock()

BACKGROUND = (214, 214, 214)
BLACK = (0, 0, 0)
BACKGROUND_PANEL = (249, 255, 230)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (147, 153, 35)
PURPLE = (255, 0, 255)
SKY = (0, 255, 255)
ORANGE = (255, 125, 25)
GRAPE = (100, 25, 125)
GRASS = (55, 155, 65)

COLORS = [RED, GREEN, BLUE, YELLOW, PURPLE, SKY, ORANGE, GRAPE, GRASS]

# Create text render 1:
font = pygame.font.SysFont("san", 40)
font_small = pygame.font.SysFont("san", 20)
text_plus = font.render("+", True, WHITE)
text_minus = font.render("-", True, WHITE)

# Create text render 2:
def create_text_render(string):
    font = pygame.font.SysFont("san", 40)
    return font.render(string, True, WHITE)


K = 0
error = 0
points = []
clusters = []
labels = []

while running:
    clock.tick(60)  # tạo fps
    screen.fill(BACKGROUND)
    mouse_x, mouse_y = pygame.mouse.get_pos()  # create click mouse
    # Draw interface
    # Draw panel
    pygame.draw.rect(screen, BLACK, (50, 50, 700, 500))
    pygame.draw.rect(screen, BACKGROUND_PANEL, (55, 55, 690, 490))

    # K button +
    pygame.draw.rect(screen, BLACK, (850, 50, 50, 50))
    screen.blit(text_plus, (860, 50))

    # K button -
    pygame.draw.rect(screen, BLACK, (950, 50, 50, 50))
    screen.blit(create_text_render("-"), (960, 50))

    # K Value
    text_K = font.render("K = " + str(K), True, BLACK)
    screen.blit(text_K, (1050, 50))

    # Run button
    pygame.draw.rect(screen, BLACK, (850, 150, 150, 50))
    screen.blit(create_text_render("Run"), (900, 160))

    # Random button
    pygame.draw.rect(screen, BLACK, (850, 250, 150, 50))
    screen.blit(create_text_render("Random"), (870, 260))

    # Algorithm button
    pygame.draw.rect(screen, BLACK, (850, 450, 150, 50))
    screen.blit(create_text_render("Algorithm"), (860, 460))
    # Reset button
    pygame.draw.rect(screen, BLACK, (850, 550, 150, 50))
    screen.blit(create_text_render("Reset"), (890, 560))

    # Error text
    # text_error = font.render("Error = " + str(error), True, BLACK)
    # screen.blit(text_error, (850, 350))

    # Draw mouse position when mouse is in panel
    if 50 < mouse_x < 750 and 50 < mouse_y < 550:
        text_mouse = font_small.render(
            "(" + str(mouse_x - 50) + "," + str(mouse_y - 50) + ")", True, BLACK
        )
        screen.blit(text_mouse, (mouse_x + 15, mouse_y + 10))

    # End Draw interface

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:  # when mouse click
            # Create point on panals
            if 50 < mouse_x < 750 and 50 < mouse_y < 550:
                labels = []
                point = [mouse_x - 50, mouse_y - 50]  # save point when mouse click
                points.append(point)
            # Change K Button +
            if 850 < mouse_x < 900 and 50 < mouse_y < 100:
                if K < 9:
                    K += 1

            # Change K Button -
            if 950 < mouse_x < 1000 and 50 < mouse_y < 100:
                if K > 0:
                    K -= 1

            # Run button
            if 850 < mouse_x < 1000 and 150 < mouse_y < 200:
                # Assign points to closet clusters
                if clusters != []:
                    labels = []
                    for p in points:
                        distances_to_cluster = []
                        for c in clusters:
                            dis = distance(p, c)
                            distances_to_cluster.append(dis)
                        min_distance = min(distances_to_cluster)
                        label = distances_to_cluster.index(min_distance)
                        labels.append(label)

                    # Update Clusters
                    for i in range(K):
                        sum_x = 0
                        sum_y = 0
                        count = 0
                        for j in range(len(points)):
                            if labels[j] == i:
                                sum_x += points[j][0]
                                sum_y += points[j][1]
                                count += 1
                        if count != 0:
                            new_cluster_x = sum_x / count
                            new_cluster_y = sum_y / count
                            clusters[i] = [new_cluster_x, new_cluster_y]

            # Random button
            if 850 < mouse_x < 1000 and 250 < mouse_y < 300:
                clusters = []
                labels = []
                for i in range(K):
                    random_point = [randint(0, 700), randint(0, 500)]
                    clusters.append(random_point)

            # Algorithm button
            if 850 < mouse_x < 1000 and 450 < mouse_y < 500:
                kmeans = KMeans(n_clusters=K).fit(points)
                labels = kmeans.predict(points)
                clusters = kmeans.cluster_centers_

            # Reset button
            if 850 < mouse_x < 1000 and 550 < mouse_y < 600:
                K = 0
                error = 0
                points = []
                clusters = []
                labels = []

    # Draw points
    for i in range(len(points)):
        pygame.draw.circle(screen, BLACK, (points[i][0] + 50, points[i][1] + 50), 6)

        if labels == []:
            pygame.draw.circle(screen, WHITE, (points[i][0] + 50, points[i][1] + 50), 5)
        else:
            pygame.draw.circle(
                screen, COLORS[labels[i]], (points[i][0] + 50, points[i][1] + 50), 5
            )

    # Draw clusters
    for i in range(len(clusters)):
        pygame.draw.circle(
            screen, COLORS[i], (clusters[i][0] + 50, clusters[i][1] + 50), 10
        )
    # Draw big circle
    # for i in range(len(clusters)):
    #     if labels != []:
    #         pygame.draw.circle(
    #             screen,
    #             COLORS[i],
    #             (clusters[i][0] + 50, clusters[i][1] + 50),
    #             (clusters[i][0] + clusters[i][1]) / 10,
    #             1,
    #         )

    # Calculate and draw error
    error = 0
    if clusters != [] and labels != []:
        for i in range(len(points)):
            error += distance(points[i], clusters[labels[i]])
    text_error = font.render("Error = " + str(int(error)), True, BLACK)
    screen.blit(text_error, (850, 350))
    print(clusters)
    print(points)
    print(labels)
    pygame.display.flip()

pygame.QUIT()
