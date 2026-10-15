# Problem: Lists
# HackerRank: https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    n = int(input())
    items = []
    for _ in range(n):
        command, *args = input().split()
        args = list(map(int, args))
        if command == 'insert':
            items.insert(args[0], args[1])
        elif command == 'print':
            print(items)
        elif command == 'remove':
            items.remove(args[0])
        elif command == 'append':
            items.append(args[0])
        elif command == 'sort':
            items.sort()
        elif command == 'pop':
            items.pop()
        elif command == 'reverse':
            items.reverse()
