
def extract_equation(operand1, operator, operand2):
    if operator == "+":
        return operand1 + operand2
    elif operator == "-":
        return operand1 - operand2
    elif operator == "*":
        return operand1 * operand2
    elif operator == "/":
        return operand1 / operand2
    elif operator == "**":
        return operand1 ** operand2
    elif operator == "%":
        return operand1 % operand2
    else:
        return None
