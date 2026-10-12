# MiniOS [Your Assigned Group Name]

**Operating Systems Final Project**

## Group Members
1. [Your Name] - Project Leader + CLI
2. [Member 2 Name] - File Management
3. [Member 3 Name] - Process & Memory Management
4. [Member 4 Name] - User Management, System Info & Testing

## Project Description
MiniOS is a command-line operating system simulator built in Python. It runs directly through the Windows Command Prompt (CMD) and simulates core OS concepts including a file system, background processes, memory allocation, and user authentication.

## Features
- Command-line interface with persistent shell
- Simulated File Management (create, read, delete directories and files)
- Simulated Process Management (run and kill background tasks via PID)
- Simulated Memory Management (allocate and free virtual RAM)
- User Authentication (admin/student login system)
- System Information and Hardware Simulation
- Robust Error Handling for invalid commands and parameters

## Requirements
- Python 3.x
- Windows CMD (or standard terminal)

## How to Run
1. Clone this repository to your local machine.
2. Open Windows Command Prompt (CMD) or your IDE terminal.
3. Navigate to the project folder.
4. Run the following command:
   `python main.py`
5. Login using default credentials (Username: `admin` / Password: `admin123`).

## Available Commands
| Category | Commands |
|----------|----------|
| **General** | `help`, `clear`, `whoami`, `systeminfo`, `exit` |
| **Files** | `dir`, `mkdir <name>`, `create <name>`, `read <name>`, `delete <name>` |
| **Processes** | `process`, `run <name>`, `kill <pid>` |
| **Memory** | `memory`, `allocate <MB>`, `free <MB>` |