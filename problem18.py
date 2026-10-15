# Problem: The Minion Game
# HackerRank: https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    vowels = set("AEIOU")
    kevin = 0
    stuart = 0
    n = len(string)
    for i, char in enumerate(string):
        if char in vowels:
            kevin += n - i
        else:
            stuart += n - i
    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)
