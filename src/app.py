import sys
import os


def prime(s):
    s = int(s)
    if  s % 2 != 0:
        return('it is a prime')
    else:
        return('it is not a prime')

def solution(s):
    return prime(s)

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argument required"))

    print(solution(sys.argv[1]))
