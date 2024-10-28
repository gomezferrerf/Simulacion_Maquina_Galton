import random
import numpy as np
import matplotlib.pyplot as plt


# Describes the behaviour of a single ball going through the machine
def ball_trajectory(steps):
    ball_location = 0
    for nodes in range(1, steps + 1):
        ball_location = random.randint(ball_location, ball_location + 1)
    return ball_location

# Describes and creates the final distribution of n number of balls
def various_balls(steps = 12, balls = 5000):
    balls_final_distribution = np.zeros(steps + 1)
    for ball in range(0, balls):

        ball_location = ball_trajectory(steps)
        balls_final_distribution[ball_location] = balls_final_distribution[ball_location] + 1
    return balls_final_distribution


# Creates and shows graph of the distribution of the balls
def creates_graph(results):
    plt.bar(range(len(results)), results)
    plt.gca().axes.get_xaxis().set_visible(False)
    plt.gca().axes.get_yaxis().set_visible(False)
    plt.show()

if __name__ == "__main__":
    results = various_balls()
    creates_graph(results)




