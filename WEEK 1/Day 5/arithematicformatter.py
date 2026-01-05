def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    first_line = []
    second_line = []
    dash_line = []
    answer_line = []

    for problem in problems:
        parts = problem.split()

        if len(parts) != 3:
            return "Error: Invalid problem format."

        left, op, right = parts
        # 2. Operator must be + or -
        if op not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # 3. Only digits
        if not (left.isdigit() and right.isdigit()):
            return "Error: Numbers must only contain digits."

        # 4. Max 4 digits
        if len(left) > 4 or len(right) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Width = max length of operands + 2 (one for operator, one for space)
        width = max(len(left), len(right)) + 2

        # Build each part right-aligned
        first_line.append(left.rjust(width))
        second_line.append(op + right.rjust(width - 1))
        dash_line.append('-' * width)

        if show_answers:
            if op == '+':
                result = str(int(left) + int(right))
            else:
                result = str(int(left) - int(right))
            answer_line.append(result.rjust(width))

    # Join with 4 spaces between problems
    arranged = '    '.join(first_line) + '\n' + \
               '    '.join(second_line) + '\n' + \
               '    '.join(dash_line)

    if show_answers:
        arranged += '\n' + '    '.join(answer_line)

    return arranged

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')