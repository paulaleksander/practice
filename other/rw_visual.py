from turtle import color
import matplotlib.pyplot as plt
from random_walks import Randomwalk

# Keep makin new walks, as long as the program is active. 
while True:
    # Make a random walk.
    rw = Randomwalk(5000)
    rw.fill_walk()

    # Plot the points in the walk.
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15,9))
    point_numbers = range(rw.num_points)
    ax.plot(rw.x_values, rw.y_values, color='blue', marker='o', 
        linestyle='dashed', linewidth=2, markersize=5)

    # Emphasize the first and last points.
    ax.plot(0, 0, color='green', marker='o', linestyle='dashed', 
        linewidth=2, markersize=12)
    ax.plot(rw.x_values[-1], rw.y_values[-1], color='red',
        marker='o', linestyle='dashed', linewidth=2, markersize=5)
    
    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running =='n':
        break
