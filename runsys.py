import subprocess
import platform
import os
import signal
import sys

# Get the current environment variables
env = os.environ.copy()

# Dynamically add the project root to PYTHONPATH
project_root = os.path.abspath(os.path.dirname(__file__))  # Root directory of your project
env["PYTHONPATH"] = f"{project_root}:{env.get('PYTHONPATH', '')}"

print(project_root)
processes = {}

def open_terminal(script_name, script_path):
    # Detect the current operating system
    system = platform.system()

    if system == "Windows":
        # Use 'start' to open a new terminal window on Windows
        process = subprocess.Popen(
            ["start", "cmd", "/K", f"set PYTHONPATH={project_root} && python {script_path}"], 
            shell=True, env=env
        )
    elif system == "Darwin":  # macOS
        # Use 'osascript' to open a new Terminal window on macOS
        process = subprocess.Popen([
            "osascript", "-e",
            f'tell application "Terminal" to do script "export PYTHONPATH="{project_root}:$PYTHONPATH" python3 {script_path}"'
        ],env=env)
    elif system == "Linux":
        # Use 'gnome-terminal' or an alternative terminal emulator for Linux
        print("Opening file")
        process = subprocess.Popen(["gnome-terminal", "--", "python3", script_path], env=env)
    else:
        print(f"Unsupported operating system: {system}")
        return None
    
    processes[script_name] = process
    print(f"Started script: {script_name} (PID: {process.pid})")
    return process

operations_dict = {
    "open" : open_terminal,
}
while True:
    operation = input("Enter the operation (open <server/client>): ")
    operation = operation.strip()
    oper_list = operation.split(" ")
    path = "a"

    if oper_list[1] == "server":
        path = "server/server.py"
    elif oper_list[1] == "client":
        path = "app/client.py"
    else:
        print("Invalid file name")
        continue
    func = operations_dict.get(oper_list[0], [None])
    if not func:
        print("Invalid operation")
        continue
    func(script_name=oper_list[1],script_path=path)

