System Monitoring Tool
The system monitoring tool project is a Python program that periodically monitors the system's resources such as CPU usage, memory usage, and disk usage, and displays the data in a user-friendly way on the terminal. It also logs the data to a file for future reference.

The program uses various Python libraries such as psutil, which provides an easy-to-use interface to retrieve information on system utilization (CPU, memory, disks, network, sensors) in a portable way, and prettytable, which allows you to display the data in a well-formatted table.

Moreover, this project provides a way to run the program as a service using systemd in Linux. This ensures that the program is automatically started when the system boots up and is always running in the background.


Installation and Execution:

1. Download the project code from the GitHub repository.
2. Open a terminal and navigate to the directory where you downloaded the code.
3. Create a new systemd service file using the following command: 
         sudo nano /etc/systemd/system/system_monitor.service
4.Copy and paste the following code into the file:

        [Unit]
        Description=System Monitor

        [Service]
        ExecStart=/usr/bin/python3 /path/to/system_monitor.py
        Restart=always
        User=<your_username_here>

        [Install]
        WantedBy=multi-user.target
        
  Replace /path/to/system_monitor.py with the path to your system_monitor.py script, and replace <your_username_here> with your username.
5. Save and close the file.
6. Start the service using the following command:
         sudo systemctl start system_monitor.service
7. Check that the service is running:
          sudo systemctl status system_monitor.service
8. Execute the following command to start the script:
          python3 system_monitor.py
9. To stop the systemd service, execute the following command:
          sudo systemctl stop system_monitor.service
10. To stop the application press Ctrl + C on the terminal.
