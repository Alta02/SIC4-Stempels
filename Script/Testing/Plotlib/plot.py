import matplotlib.pyplot as plt
import random
import time

# Create empty lists for x and y values
x_values = []
y_values = []

# Set up the plot
fig, ax = plt.subplots()
line, = ax.plot(x_values, y_values, 'ro', label='Random Number')
ax.set_xlabel('Time')
ax.set_ylabel('Random Number')
ax.set_title('Random Number Visualization')
ax.legend()

# Set the time interval (in seconds)
interval = 2

# Start the loop to update and display the random number
try:
    while True:
        # Generate a random number
        random_number = random.randint(1, 100)
        
        # Append the current time and random number to the lists
        x_values.append(time.time())
        y_values.append(random_number)

        # Update the plot data
        line.set_data(x_values, y_values)

        # Adjust the plot limits
        ax.relim()
        ax.autoscale_view()

        # Redraw the plot
        fig.canvas.draw()

        # Pause for the specified interval
        time.sleep(interval)

except KeyboardInterrupt:
    # Close the plot on keyboard interrupt
    plt.close()
