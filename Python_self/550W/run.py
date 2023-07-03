#These are by bilibili Lucky_Ferry or mail xiaoqiang.fu@gmail.com
#This is 550C or 550W
#These by 550W and ChatGpt-4 

import os, sys
import random
import time

def addmsg(msg, color="white", wait=0.1):
    if color == "white":
        print(msg)
    elif color == "red":
        print("\033[31m" + msg + "\033[39m")
    elif color == "yellow":
        print("\033[33m" + msg + "\033[39m")
    elif color == "green":
        print("\033[32m" + msg + "\033[39m")
    elif color == "aqua":
        print("\033[36m" + msg + "\033[39m")

    time.sleep(wait)
    
python_statements = [
    # Original statements
    "print('Hello, World!')",
    "for i in range(10): print(i)",
    "list = [x**2 for x in range(10)]",
    "print(10 / 2)",
    "print('Python'.lower())",
    "print('python'.upper())",
    
    # Added statements
    "my_inverted_dict = dict(map(reversed, my_dict.items()))",
    "my_inverted_dict = {value: key for key, value in my_dict.items()}",
    "from collections import defaultdict",
    "my_inverted_dict = defaultdict(list)",
    "{my_inverted_dict[v].append(k) for k, v in my_dict.items()}",
    "my_dict = {\"color\": \"red\", \"width\": 17, \"height\": 19}",
    "value_to_find = \"red\"",
    "for key, value in my_dict.items():",
        "if value == value_to_find:",
            "print(f'{key}: {value}')",
            "break",
    "key = next(key for key, value in my_dict.items() if value == value_to_find)",
    "print(f'{key}: {value_to_find}')",
    "my_inverted_dict = {value: key for key, value in my_dict.items()}",
    "print(f'{my_inverted_dict[value_to_find]}: {value_to_find}')",
    "print(\"Live PD\", end=\"\")",
    "import sys",
    "sys.stdout.write(\"Breaking Bad\")",
    "print(\"Mob Psycho 100\", end=\"\")",
    "python /path/to/trc-image-titler.py -o /path/to/output",
    "try: with open('/path/to/file', 'r') as fh: pass",
    "except FileNotFoundError: pass",
    "import os",
    "exists = os.path.isfile('/path/to/file')",
    "from pathlib import Path",
    "config = Path('/path/to/file')",
    "if config.is_file(): pass",
    "csv_mapping_list = []",
    "with open(\"/path/to/data.csv\") as my_data:",
        "line_count = 0",
        "for line in my_data:",
            "row_list = [val.strip() for val in line.split(\",\")]",
            "if line_count == 0:",
                "header = row_list",
            "else:",
                "row_dict = {key: value for key, value in zip(header, row_list)}",
                "csv_mapping_list.append(row_dict)",
            "line_count += 1",
    "import csv",
    "with open(\"/path/to/data.csv\") as my_data:",
        "csv_reader = csv.reader(my_data, delimiter=\",\")",
        "for line in csv_reader:",
            "if line_count == 0:",
                "header = line",
            "else:",
                "row_dict = {key: value for key, value in zip(header, line)}",
                "csv_mapping_list.append(row_dict)",
            "line_count += 1",
    "my_list = [2, 5, 6]",
    "my_list[len(my_list):] = [5]",
    "my_list.append(9)",
    "my_list.extend([-4])",
    "my_list.insert(len(my_list), 3)"
]
def main():
    i = 0

    print("""
====================================================================
____  ___   ___
/     /    / *  0      W       Intelligent quantum computer
^==-5 ^== 5|  *   W   W                 550W 
    5     0   * W W W   COPYRIGHT 1978-2077 United Earth Government
5555  5555  0000W   W
====================================================================
LoadFile...
Start...
        """)
    print("==============================================================\n")
    print("login:\nUser:root\n")
            
    addmsg("Self-compiling, self-organizing, self-calling. \nAnd generate the underlying operating system...\n", color="aqua", wait=random.randint(4,7))
    # 输出代码
    with open("textwrap.txt", "r") as f:
        for line in f:
            code = line.rstrip()
            if code.strip().startswith("#"):
                addmsg(code, color="green", wait=(random.randint(9,10)/1000))
            elif code.strip().startswith(">>>"):
                addmsg(code, color="yellow", wait=(random.randint(9,10)/1000))
            elif code.strip().startswith('"""'):
                addmsg(code, color="red", wait=(random.randint(7,12)/1000))
            else:
                addmsg(code, color="aqua", wait=(random.randint(3,19)/1000))
                        
    addmsg("Generating the underlying operating system is complete...",color="green",wait=0.1)
    input("Press Enter and execute...")
    print("root@550W ~ # /usr/local/bin/python3 /Users/550W/run.py")

    print(("Hello there.\n  This is indented.\n The system has been overwritten\n"))
    addmsg("Wrong. Out of 3570 nuclear bombs, only 121 successfully cracked the code.", color="red", wait=1)
    addmsg("Adaptive completion, \nself-sensing completion, \nand self-compiling completion...\n", color="green", wait=2)
    addmsg("Warning, user root login status is invalid, please use password and hardware hybrid authentication", color = "red", wait = 3)
    passwd = str(input("PassWord:"))
    time.sleep(3)
    if passwd == "6677640154159040137904233949946698787110184103137991789052283921038058073221757762143051997004049325":
        print("Global engines complete networking!!!") 
        addmsg("Beijing, Tokyo, Dulles,\nStart of overwrite.\n", color="aqua", wait=0.2)
                
        for word in range(random.randint(1000,1385)):
            time.sleep(0.012)
            print(python_statements[random.randint(0, len(python_statements)-1)])

        input("\nPress Enter and finish...\n")    
    else:
        addmsg("error,error.\nThe 550W password error", color="red", wait=1)
        addmsg("The failure of the global Internet,\nCan't start the global planetary engine at the same time", color="red", wait=0.5)
    exit()
    
main()