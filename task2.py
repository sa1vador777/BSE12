#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def is_valid_parentheses(s: str) -> bool:
    def is_valid_helper(s: str, left_count: int, right_count: int) -> bool:
        if not s:
            return left_count == right_count

        if s[0] == '(':
            return is_valid_helper(s[1:], left_count + 1, right_count)
        elif s[0] == ')':
            if left_count > 0:
                return is_valid_helper(s[1:], left_count - 1, right_count)
            return False
        return is_valid_helper(s[1:], left_count, right_count)

    return is_valid_helper(s, 0, 0)


def main() -> None:
    inp = input("Введите выражение: ")
    if is_valid_parentheses(inp):
        print("Скобки расставлены правильно")
    else:
        print("Скобки расставлены неправильно")

if __name__ == "__main__":
    main()
