import sys

def check_input(s, type_):
    if type_ == "number":
        if not s.isnumeric():
            print(f"抱歉，您输入的{s}不是数字")
            sys.exit(1)
    elif type_ == "operator":
        operators = ["+", "-", "*", "/", "^"]
        if s not in operators:
            print(f"抱歉，您输入的{s}不是有效的运算符")
            sys.exit(1)

def get_input(type_):
    if type_ == "number":
        s = input("请输入一个数字：")
    elif type_ == "operator":
        s = input("请输入一个运算符（+、-、*、/、^）：")
    check_input(s, type_)
    return s

op1 = float(get_input("number"))
op = get_input("operator")
op2 = float(get_input("number"))

if op == "+":
    print(f"{op1} + {op2} = {op1 + op2:.3f}")
elif op == "-":
    print(f"{op1} - {op2} = {op1 - op2:.3f}")
elif op == "*":
    print(f"{op1} * {op2} = {op1 * op2:.3f}")
elif op == "/":
    if op2 == 0:
        print("抱歉，您输入错误（除数不能为0）")
        sys.exit(1)
    else:
        print(f"{op1} / {op2} = {op1 / op2:.3f}")
elif op == "^":
    print(f"{op1} ^ {op2} = {op1 ** op2:.3f}")
