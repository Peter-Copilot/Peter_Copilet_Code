import subprocess
import random
import os

def open_terminal_with_code(file_path, delay=0.03):
    # Create a temporary bash script
    bash_script_path = "/tmp/print_file_slowly.sh"
    with open(bash_script_path, "w") as bash_script:
        bash_script.write("#!/bin/bash\n")
        bash_script.write("while IFS= read -r line\n")
        bash_script.write("do\n")
        bash_script.write("  echo \"$line\"\n")
        bash_script.write("  sleep {}\n".format(delay))
        bash_script.write("done < \"{}\"\n".format(file_path))
        bash_script.write("exit\n")  # Add exit command
    os.chmod(bash_script_path, 0o755)

    # Generate random position
    x = random.randint(0, 1152)
    y = random.randint(0, 812)

    script = """
    tell application "Terminal"
        activate
        do script "{0}"
        set number of columns of front window to 80
        set number of rows of front window to 24
        set position of front window to {{{1}, {2}}}
    end tell
    """.format(bash_script_path, x, y)
    subprocess.call(["osascript", "-e", script])

def open_terminal_with_message(message, width=1152, height=812):
    # Create a temporary bash script
    bash_script_path = "/tmp/print_message.sh"
    with open(bash_script_path, "w") as bash_script:
        bash_script.write("#!/bin/bash\n")
        bash_script.write("echo '{}'\n".format(message))  # Print the message
        bash_script.write("exit\n")  # Add exit command
    os.chmod(bash_script_path, 0o755)

    # Calculate columns and rows from pixel size (assume 8x8 pixel per character)
    columns = width // 8
    rows = height // 8

    script = """
    tell application "Terminal"
        activate
        do script "{0}"
        set number of columns of front window to {1}
        set number of rows of front window to {2}
    end tell
    """.format(bash_script_path, columns, rows)
    subprocess.call(["osascript", "-e", script])

# Call the function multiple times
for i in range(random.randint(4,20)):
    code_file_path = "/Users/peter/Documents/Peter_Code/Python_self/550W/textwrap.txt"  # Replace with your file path
    open_terminal_with_code(code_file_path)

# After all the small terminal windows have finished, open the final window
open_terminal_with_message("system is overwrite", 1252, 722)
