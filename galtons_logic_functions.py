import random
import numpy as np
import matplotlib.pyplot as plt

def ball_trajectory(steps):
    ball_location = 0
    for nodes in range(1, steps + 1):
        ball_location = random.randint(ball_location, ball_location + 1)
    return ball_location


def various_balls(steps = 12, balls = 5000):
    results = np.zeros(steps + 1)
    for ball in range(0, balls):

        ball_location = ball_trajectory(steps)
        results[ball_location] = results[ball_location] + 1
    return results

def creates_graph(results):
    plt.bar(range(len(results)), results)
    plt.gca().axes.get_xaxis().set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)
    plt.show()

creates_graph(various_balls())




