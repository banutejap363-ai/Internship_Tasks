# Problem: Set .add()
# https://www.hackerrank.com/challenges/py-set-add/problem

if __name__ == '__main__':
    n = int(input())
    stamps = set()

    for _ in range(n):
        stamps.add(input().strip())

    print(len(stamps))
