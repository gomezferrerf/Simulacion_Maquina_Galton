import numpy as np
#import seaborn as sb
from galtons_logic_functions import various_balls
from galtons_logic_functions import creates_graph


ball_distribution_1 = (various_balls(balls = 100000))
ball_distribution_2 = (various_balls(balls = 100000))

# Creates a new function that relates the fase with the distribution
def fase_ball_distribution(ball_distribution):

    center = int((len(ball_distribution) - 1)/2)
    fase = np.zeros(len(ball_distribution))
    fase[center] = 1
    for i in range(1,center+1):
        if fase[center + i -1] == 1:
            fase[center + i] = 0
        elif fase[center + i -1] == -1:
            fase[center + i] = 0
        elif fase[center + i -1] == 0:
            if fase[center + i -2] == 1:
                fase[center + i] = -1
            else:
                fase[center + i] = 1

        if fase[center - i +1] == 1:
            fase[center - i] = 0
        elif fase[center - i +1] == -1:
            fase[center - i] = 0
        elif fase[center - i +1] == 0:
            if fase[center - i +2] == 1: 
                fase[center - i] = -1
            else:
                fase[center - i] = 1

    fase_distribution_dic = [[fase[i], ball_distribution[i]] for i in range(len(fase))]
    return fase_distribution_dic

fase_ball_1 = fase_ball_distribution(ball_distribution_1)
fase_ball_2 = fase_ball_distribution(ball_distribution_2)



print(fase_ball_1)
print(fase_ball_2)

separation = 8
final_distribution = np.zeros(len(fase_ball_1) + separation)
print(final_distribution)

for cup in range(len(ball_distribution_1) + separation):

    if cup - separation < 0:
        final_distribution[cup] = fase_ball_1[cup][1]
    elif cup + separation > len(ball_distribution_1):
        final_distribution[cup] = fase_ball_2[cup - separation][1]

    elif fase_ball_1[cup][0] + fase_ball_2[cup - separation][0] == 0 and fase_ball_1[cup][0] != 0:
        final_distribution[cup] = abs(fase_ball_1[cup][1] - fase_ball_2[cup - separation][1])
    elif fase_ball_1[cup][0] == fase_ball_2[cup - separation][0]:
        final_distribution[cup] = fase_ball_1[cup][1] + fase_ball_2[cup - separation][1]
    elif fase_ball_1[cup][0] != fase_ball_2[cup - separation][0]:
        final_distribution[cup] = (fase_ball_1[cup][1] + fase_ball_2[cup - separation][1])/2

creates_graph(final_distribution)