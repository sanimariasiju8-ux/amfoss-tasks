# Grand Line Guardian

Grand Line Guardian is a terminal-based system monitoring tool built with
Python for Linux systems.

It is inspired by tools such as `htop` and `btop++` and provides a live view
of running processes, including their Process ID (PID), process name, CPU
usage, memory usage, and the total number of active processes.

The project uses the Linux `/proc` virtual filesystem to obtain process and
system information instead of relying on third-party process-monitoring
libraries.

## Features

- Displays Process ID (PID)
- Displays process name
- Displays CPU usage
- Displays memory usage
- Displays total active process count
- Updates information every 0.5 seconds
- Sorts processes by CPU usage
- Interactive terminal interface using `curses`
- Supports process navigation using:
  - `↑` Up Arrow
  - `↓` Down Arrow
- Press `Q` to quit
- Uses Linux `/proc` virtual filesystem

## Technologies Used

- Python3
- Linux
- `/proc` virtual filesystem
- `os` module
- `time` module
- `curses` module

## Approach

The application continuously reads process information from the Linux
`/proc` virtual filesystem.

The basic workflow is:

                 Linux System
                      │
                      ▼
                    /proc
                      │
             ┌────────┴────────┐
             ▼                 ▼
        Process data       System CPU data
             │                 │
             ▼                 ▼
       /proc/<PID>/       /proc/stat
          status
          stat
             │
             └────────┬────────┘
                      ▼
               Calculate CPU %
                      │
                      ▼
                Sort processes
                      │
                      ▼
              Display with curses
                      │
                      ▼
                 Wait 0.5 sec
                      │
                      └──────► Repeat

## Process Discovery

Linux exposes information about running processes through the /proc virtual filesystem.
Inside /proc, directories with numeric names represent running processes.
For example:
/proc/1
/proc/2
/proc/3
/proc/10
/proc/100
The directory name is the Process ID (PID).
The program scans /proc and selects only entries whose names are numeric.

## Reading Process Information

For every discovered PID, the program reads:
/proc/<PID>/status
This file contains information about the process.
The program uses it to obtain: Process Name
Example:
Name:   systemd

Memory Usage
The VmRSS: field provides the amount of resident memory currently used by the process.
Example:
VmRSS:   17144 kB
The program converts this value from KB to MB before displaying it.

## CPU Usage Calculation

CPU usage is not obtained directly as a percentage from /proc.
The CPU time stored in: /proc/<PID>/stat
is cumulative.
The program reads:
User CPU time
Kernel CPU time
and adds them together.
Process CPU time = User CPU time + Kernel CPU time
A single reading cannot tell us how much CPU the process is currently using.
Therefore, the program takes two measurements separated by 0.5 seconds.

First reading
      │
      ▼
Wait 0.5 seconds
      │
      ▼
Second reading
      │
      ▼
Calculate difference
      │
      ▼
CPU usage %

The system-wide CPU counter is obtained from: /proc/stat
The change in the process CPU time is compared with the change in the system CPU time to estimate the process CPU usage.
The number of logical CPU cores detected by Python is also taken into account.

## Real Time Monitoring

The monitor continuously repeats the following process:
Read all currently running processes.
Read system CPU information.
Wait for 0.5 seconds.
Read the information again.
Calculate CPU usage.
Sort processes according to CPU usage.
Update the terminal display.
Repeat.
The 0.5-second interval keeps the displayed information close to real time while avoiding unnecessary updates.

## Terminal Interface

The application uses Python's curses module to create an interactive terminal interface.
The interface displays information in columns:

PID      PROCESS NAME             CPU %       MEMORY
---------------------------------------------------------
6011     python3                  12.39       10.8 MB
4537     ptyxis                    5.31      127.6 MB
3430     gnome-shell               3.54      239.2 MB

Only the number of processes that fit inside the terminal window are displayed.
The process list is sorted by CPU usage so that the most CPU-intensive processes appear first.

## Controls

Key  Action
↑    Move selection up
↓    Move selection down
Q    Quit the application
The currently selected process is highlighted in the terminal.

## Project Structure

Task-05/
├── guardian.py
├── requirements.txt
└── README.md

guardian.py
Contains the complete Grand Line Guardian implementation.
requirements.txt
The project does not use third-party Python packages, so this file is intentionally empty.
README.md
Contains the project documentation, approach, resources, and concepts learned

## Resources Used
The following resources were used to understand the concepts required for the project:
Linux /proc virtual filesystem documentation
Linux process information documentation
Python documentation
Python curses documentation
Python os module documentation
Python time module documentation
htop and btop++ for understanding terminal-based system monitors
 

## New Concepts Learned
Through this project, I learned about:

Linux Processes
A process is a running instance of a program. Every process has a unique Process ID (PID).
/proc Virtual Filesystem
Linux provides system and process information through the /proc virtual filesystem.
I learned how to inspect process information using paths such as:
/proc/<PID>/status
/proc/<PID>/stat
/proc/stat

CPU Time vs CPU Percentage
CPU time stored by Linux is cumulative, so it cannot directly be displayed as a current CPU percentage.
I learned how to compare two measurements over a time interval to estimate CPU usage.

Real-Time Monitoring
I learned how repeated measurements can be used to monitor changing system information.
curses
I learned how Python's curses module can be used to build interactive terminal applications and update the display without repeatedly printing new screens.

Keyboard Input
I learned how terminal applications can detect special keys such as the arrow keys and use them to navigate through data.

Process Sorting
I learned how to store process information in Python data structures and sort processes according to their CPU usage.

Handling Dynamic Processes
Processes can start or terminate while the monitor is running. Therefore, the program handles situations where /proc/<PID> disappears between reads.

## Challenges Faced
Understanding /proc
Initially, the /proc filesystem was unfamiliar. By inspecting directories such as /proc/1 and files such as /proc/1/status, I learned how Linux exposes process information.
Calculating CPU Usage
One of the main challenges was understanding that CPU usage requires two measurements rather than a single CPU-time value.
The program therefore compares CPU counters before and after a 0.5-second interval.
Terminal Flickering
The initial implementation repeatedly cleared and printed the entire terminal, which caused visible flickering.
This was improved by using Python's curses module to manage the terminal screen.
Large Number of Processes
A Linux system can have hundreds of active processes. The program therefore checks the terminal size and displays only the processes that fit on the screen.

## Conclusion
Grand Line Guardian demonstrates how a basic Linux system monitoring tool can be built using Python and the /proc virtual filesystem.
The project provides real-time information about running processes while also demonstrating concepts related to Linux process management, CPU monitoring, memory usage, terminal interfaces, and the Linux kernel's virtual filesystem interface.
Building this project helped me understand how system-level information can be accessed from a user-space Python program without depending on third-party process-monitoring libraries.
