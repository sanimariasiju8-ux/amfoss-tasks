import os
import time
import curses


INTERVAL = 0.5
CPU_CORES = os.cpu_count() or 1


def get_process_info(pid):
    try:
        # Read process name and memory
        with open(f"/proc/{pid}/status", "r") as file:
            name = "Unknown"
            memory = 0

            for line in file:
                if line.startswith("Name:"):
                    name = line.split(":", 1)[1].strip()

                elif line.startswith("VmRSS:"):
                    memory = int(line.split()[1])

        # Read process CPU time
        with open(f"/proc/{pid}/stat", "r") as file:
            data = file.read().split()

        user_time = int(data[13])
        kernel_time = int(data[14])

        cpu_time = user_time + kernel_time

        return name, memory, cpu_time

    except (FileNotFoundError, PermissionError, ValueError):
        return None


def get_all_processes():
    processes = {}

    for entry in os.listdir("/proc"):
        if entry.isdigit():
            info = get_process_info(entry)

            if info:
                processes[entry] = info

    return processes


def get_system_cpu_time():
    with open("/proc/stat", "r") as file:
        values = file.readline().split()[1:]

    return sum(int(value) for value in values)


def guardian_screen(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.keypad(True)

    previous_processes = get_all_processes()
    previous_system_cpu = get_system_cpu_time()

    selected = 0

    while True:

        time.sleep(INTERVAL)

        current_processes = get_all_processes()
        current_system_cpu = get_system_cpu_time()

        system_change = current_system_cpu - previous_system_cpu

        process_rows = []

        for pid, info in current_processes.items():

            name, memory, current_cpu = info

            if pid in previous_processes and system_change > 0:

                previous_cpu = previous_processes[pid][2]

                process_change = current_cpu - previous_cpu

                cpu_percent = (
                    process_change / system_change
                ) * CPU_CORES * 100

            else:
                cpu_percent = 0.0

            process_rows.append(
                (pid, name, cpu_percent, memory)
            )

        # Highest CPU first
        process_rows.sort(
            key=lambda row: row[2],
            reverse=True
        )

        # Make sure selection is still valid
        if process_rows:
            selected = min(selected, len(process_rows) - 1)
        else:
            selected = 0

        stdscr.erase()

        height, width = stdscr.getmaxyx()

        # Header
        title = "GRAND LINE GUARDIAN"

        try:
            stdscr.addstr(
                1,
                max(0, (width - len(title)) // 2),
                title,
                curses.A_BOLD
            )

            stdscr.addstr(
                3,
                2,
                f"CPU Cores: {CPU_CORES} | "
                f"Total Active Processes: {len(current_processes)}"
            )

            stdscr.addstr(
                5,
                2,
                "PID      PROCESS NAME             CPU %       MEMORY"
            )

            stdscr.addstr(
                6,
                2,
                "-" * max(1, width - 4)
            )

            max_rows = height - 9

            for index, row in enumerate(
                process_rows[:max_rows]
            ):

                pid, name, cpu_percent, memory = row

                line = (
                    f"{pid:<8}"
                    f"{name[:24]:<25}"
                    f"{cpu_percent:<10.2f}"
                    f"{memory / 1024:.1f} MB"
                )

                if index == selected:
                    stdscr.attron(curses.A_REVERSE)

                stdscr.addstr(
                    7 + index,
                    2,
                    line[:width - 3]
                )

                if index == selected:
                    stdscr.attroff(curses.A_REVERSE)

            # Footer
            footer = "↑ ↓ Navigate    Q Quit"

            stdscr.addstr(
                height - 2,
                2,
                footer[:width - 3]
            )

        except curses.error:
            pass

        stdscr.refresh()

        # Keyboard input
        key = stdscr.getch()

        if key in (ord("q"), ord("Q")):
            break

        elif key == curses.KEY_UP:
            if selected > 0:
                selected -= 1

        elif key == curses.KEY_DOWN:
            if selected < len(process_rows) - 1:
                selected += 1

        previous_processes = current_processes
        previous_system_cpu = current_system_cpu

curses.wrapper(guardian_screen)
