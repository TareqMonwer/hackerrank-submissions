VOWELS = 'AEIOU'


def minion_game(string):
    stuart = 0
    kevin = 0

    for i in range(len(string)):
        if string[i] in VOWELS:
            kevin += len(string) - 1
        else:
            stuart += len(string) - 1

    if stuart > kevin:
        print("Stuart", stuart)
    elif kevin > stuart:
        print("Kevin", kevin)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)