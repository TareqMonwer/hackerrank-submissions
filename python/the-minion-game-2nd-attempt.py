VOWELS = 'AEIOU'
import time

def minion_game(string):
    string = string.upper()
    winner = 'Draw'
    kevin = {'words': [], 'score': 0, 'name': 'Kevin'}
    stuart = {'words': [], 'score': 0, 'name': 'Stuart'}
    word_len = 1
    string_len = len(string)
    print(string_len)
    while word_len <= string_len:
        print(word_len)
        start, end = 0, word_len

        while end <= string_len:
            substr = string[start:end]
            
            if substr[0] in VOWELS and substr not in kevin['words']:
                # Update kevin's score and words
                # counts = sum([
                #     string.startswith(substr, i) for i in range(len(string))
                # ])
                # kevin['score'] += counts
                kevin['words'].append(substr)
                ...
            elif substr[0] not in VOWELS and substr not in stuart['words']:
                # update stuart's score and words
                # counts = sum([
                #     string.startswith(substr, i) for i in range(len(string))
                # ])
                # stuart['score'] += counts
                stuart['words'].append(substr)
                ...
            start += 1
            end += 1
        
        word_len += 1


    if kevin['score'] > stuart['score']:
        winner = kevin
    if stuart['score'] > kevin['score']:
        winner = stuart

    if winner != 'Draw':
        print(f'{winner["name"]} {winner["score"]}')
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    start = time.time()
    minion_game(s)
    end = time.time()
    print(end - start, '......')
