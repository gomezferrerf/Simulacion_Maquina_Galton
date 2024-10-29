import numpy as np
from double_slit_experiment_simulation_with_galtons_machines.functions.galtons_logic_functions import various_balls, creates_graph

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




def interference(separation, fase_ball_1, fase_ball_2):
    final_distribution = np.zeros(len(fase_ball_1) + separation)
    print(len(ball_distribution_1))

    for cup in range(len(ball_distribution_1) + separation):

        if cup - separation < 0:
            final_distribution[cup] = fase_ball_1[cup][1]
        elif cup  >= len(ball_distribution_1):
            final_distribution[cup] = fase_ball_2[cup - separation][1]

        elif fase_ball_1[cup][0] + fase_ball_2[cup - separation][0] == 0 and (fase_ball_1[cup][0] != 0 or fase_ball_2[cup - separation][0]) != 0:
            final_distribution[cup] = 0 #abs(fase_ball_1[cup][1] - fase_ball_2[cup - separation][1])
        elif fase_ball_1[cup][0] == fase_ball_2[cup - separation][0]:
            final_distribution[cup] = fase_ball_1[cup][1] + fase_ball_2[cup - separation][1]
        elif fase_ball_1[cup][0] != fase_ball_2[cup - separation][0]:
            final_distribution[cup] = (fase_ball_1[cup][1] + fase_ball_2[cup - separation][1])/2
    final_distribution = final_distribution/sum(final_distribution)
    return(final_distribution)

