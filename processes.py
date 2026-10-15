
running_processes = {}
next_pid = 1

def run_process(name):
    global next_pid
    running_processes[next_pid] = {"name": name, "status": "RUNNING"}
    print("\nProcess started.\n")
    print(f"PID: {next_pid}")
    print(f"Name: {name}")
    print("Status: RUNNING\n")
    next_pid += 1

def list_processes():
    # Use exact column widths (<7 means left-aligned, 7 spaces wide)
    print(f"\n{'PID':<7}{'NAME':<15}{'STATUS'}")
    if not running_processes:
        print("  (No running processes)")
    else:
        for pid, info in running_processes.items():
            print(f"{pid:<7}{info['name']:<15}{info['status']}")
    print()

def kill_process(pid_str):
    try:
        pid = int(pid_str)
        if pid in running_processes:
            del running_processes[pid]
            print(f"\nProcess {pid} terminated.\n")
        else:
            print("\nError: Process does not exist.\n")
    except ValueError:
        print("\nError: PID must be a number.\n")