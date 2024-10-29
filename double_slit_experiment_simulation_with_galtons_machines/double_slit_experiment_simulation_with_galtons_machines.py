from double_slit_experiment_simulation_with_galtons_machines.functions.galtons_logic_functions import creates_graph, various_balls
from double_slit_experiment_simulation_with_galtons_machines.functions.two_galtons_interference import fase_ball_distribution, interference

steps = 12
balls = 100000
separation = 2

ball_distribution_1 = (various_balls(steps = steps, balls = balls))
ball_distribution_2 = (various_balls(steps = steps, balls = balls))

distribution_fase_1 = fase_ball_distribution(ball_distribution_1)
distribution_fase_2 = fase_ball_distribution(ball_distribution_2)

final_distribution = interference(separation, ball_distribution_1, distribution_fase_2)

creates_graph(final_distribution)