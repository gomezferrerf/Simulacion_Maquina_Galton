import random
import numpy as np
import matplotlib.pyplot as plt

steps = 60
results = np.zeros(steps + 1)



for balls in range(0, 5000):
    ball_location = 0
    for nodes in range(1, steps + 1):
        ball_location = random.randint(ball_location, ball_location + 1)
    results[ball_location] = results[ball_location] + 1
print(results)

plt.bar(range(len(results)), results)
plt.gca().axes.get_xaxis().set_visible(False)
plt.gca().axes.get_yaxis().set_visible(False)
plt.show()






