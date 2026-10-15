# Problem: No Idea!
# HackerRank: https://www.hackerrank.com/challenges/no-idea/problem

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    a = set(map(int, input().split()))
    b = set(map(int, input().split()))
    happiness = sum((x in a) - (x in b) for x in arr)
    print(happiness)
