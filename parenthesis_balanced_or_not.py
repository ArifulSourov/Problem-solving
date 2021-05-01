def parenthesis_balanced(paren_string):
    index = 0
    is_balanced = True
    s = []

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "({[":
            s.append(paren)
        else:
            if s == []:
                is_balanced = False

            else:
                top = s.pop()

            if not is_match(top, paren):
                is_balanced = False
            
        index += 1
    if s == [] and is_balanced:
        return True
    else:
        return False


def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False


print(parenthesis_balanced("(({{{{}}}})"))

