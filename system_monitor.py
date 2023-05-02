import psutil
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up figure and axis objects
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlabel('Time (s)')
ax.set_ylabel('Usage (%)')
ax.set_ylim(0, 100)
ax.set_title('System Monitor')

# Initialize empty line objects for each metric
cpu_line, = ax.plot([], [], label='CPU')
mem_line, = ax.plot([], [], label='Memory')
disk_line, = ax.plot([], [], label='Disk')
net_line, = ax.plot([], [], label='Network')

# Initialize x and y data lists for each metric
cpu_x, cpu_y = [], []
mem_x, mem_y = [], []
disk_x, disk_y = [], []
net_x, net_y = [], []

# Define function to update plot with new data
def update_plot(frame):
    # Get current CPU, memory, disk, and network usage
    cpu_usage = psutil.cpu_percent()
    mem_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    net_usage = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

    # Add current usage to x and y data lists
    cpu_x.append(frame)
    cpu_y.append(cpu_usage)
    mem_x.append(frame)
    mem_y.append(mem_usage)
    disk_x.append(frame)
    disk_y.append(disk_usage)
    net_x.append(frame)
    net_y.append(net_usage)

    # Update line data with new x and y data
    cpu_line.set_data(cpu_x, cpu_y)
    mem_line.set_data(mem_x, mem_y)
    disk_line.set_data(disk_x, disk_y)

    net_line.set_data(net_x, net_y)

    # Set x-axis limit to show last 50 seconds of data
    ax.set_xlim(max(0, frame-50), frame)

    # Update legend to show current metric values
    ax.legend(loc='upper left', fontsize='small', ncol=2,
              labels=['CPU: {:.1f}%'.format(cpu_usage),
                      'Memory: {:.1f}%'.format(mem_usage),
                      'Disk: {:.1f}%'.format(disk_usage),
                      'Network: {:.2f} kB'.format(net_usage/1024)])

# Start animation with 1 second interval
ani = animation.FuncAnimation(fig, update_plot, interval=1000)

# Show plot
plt.show()
plt.savefig('/var/www/html/system_monitor.png')


