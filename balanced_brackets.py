#!/bin/python3

# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING brackets as parameter.

# brackets = "{[(])}"


def isBalanced(brackets):
    if len(brackets) % 2 != 0:
        return "NO"

    stack_bracket = list()
    indice = len(stack_bracket) - 1

    for bracket in brackets:
        if bracket in "([{":
            stack_bracket.append(bracket)
        elif bracket == ")" and stack_bracket[indice] == "(":
            stack_bracket.pop()
        elif bracket == "]" and stack_bracket[indice] == "[":
            stack_bracket.pop()
        elif bracket == "}" and stack_bracket[indice] == "{":
            stack_bracket.pop()
        else:
            return "NO"

    return "YES"


# print(isBalanced(brackets))


if __name__ == '__main__':

    t = int(input().strip())

    results = []
    for t_itr in range(t):
        brackets = input()

        results.append(isBalanced(brackets))

    print(*results, sep='\n')
