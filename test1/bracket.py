def is_balanced_brackets(s):
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in bracket_map.values():  # opening brackets
            stack.append(char)
        elif char in bracket_map:  # closing brackets
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
    return len(stack) == 0


if __name__ == "__main__":
    # Sample input
    test_strings = [
        "()", "()[]{}", "(]", "([)]", "{[]}", "((({[]})))", "[(])", ""
    ]

    for s in test_strings:
        result = is_balanced_brackets(s)
        print(f"{s:12} -> {'Balanced' if result else 'Not Balanced'}")
