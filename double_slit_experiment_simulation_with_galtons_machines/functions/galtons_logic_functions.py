import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline


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
    balls_final_distribution = balls_final_distribution / balls
    return balls_final_distribution


# Creates and shows graph of the distribution of the balls
def creates_graph(results):

    plt.bar(range(len(results)), results, alpha=0.6, label='Resultados')

    x = np.arange(len(results))
    y = np.array(results)
    x_smooth = np.linspace(x.min(), x.max(), 300)  # Crear puntos adicionales para suavizar la línea
    y_smooth = make_interp_spline(x, y)(x_smooth)

    plt.plot(x_smooth, y_smooth, color='red', linewidth=2, label='Distribución')

    plt.gca().axes.get_xaxis().set_visible(True)
    plt.gca().axes.get_yaxis().set_visible(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    results = various_balls()
    creates_graph(results)




