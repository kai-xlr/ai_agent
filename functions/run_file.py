import os
import subprocess

def run_python_file(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    _, file_extension = os.path.splitext(file_path)
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if file_extension != ".py":
        return f'Error: "{file_path}" is not a Python file.'
    try:
        result = subprocess.run(['python3', file_path], capture_output=True, text=True, timeout=30)
    except subprocess.TimeoutExpired:
        print("The command timed out after 30 seconds.")
    