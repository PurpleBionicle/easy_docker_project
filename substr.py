import pygame


def lengthOfLongestSubstring(s: str) -> int:
    current, max = 0, 0
    set_char = set()
    shift = 0
    i = 0
    while i < len(s):
        # for i in range(len(s)+shift):
        i -= shift
        if s[i] not in set_char:
            current += 1
            set_char.add(s[i])
            shift = 0
        else:
            if current > max:
                max = current
            set_char.clear()
            shift = current
            current = 0
        i += 1

    if current > max:
        max = current
    return max


if __name__ == '__main__':
    print(lengthOfLongestSubstring("asfga2"))
