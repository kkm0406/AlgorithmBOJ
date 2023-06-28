# Java vs C++ S3

import sys

input = sys.stdin.readline
s = input().strip()


def convert_to_java(s):
    result = []
    if "__" in s:
        return 'Error!'
    if s[0] == '_' or s[-1] == '_':
        return 'Error!'
    if not s.islower():
        return 'Error!'

    for word in s.split("_"):
        if not result:
            result.append(word)
        else:
            result.append(word.capitalize())

    return "".join(result)


def convert_to_c(s):
    result = []
    for idx in range(len(s)):
        if s[idx].isupper():
            if idx == 0:
                return 'Error!'
            else:
                result.append("_"+s[idx].lower())
        else:
            result.append(s[idx].lower())

    return "".join(result)


if '_' in s:
    ans = convert_to_java(s)
    print(ans)
else:
    ans = convert_to_c(s)
    print(ans)
