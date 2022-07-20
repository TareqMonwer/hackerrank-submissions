VOWELS = 'AEIOU'


def minion_game(string):
    string = string.upper()
    players = {
        'Stuart': {'scores': 0, 'words': []},
        'Kevin': {'scores': 0, 'words': []}
    }

    length = len(string)
    substr_length = 1
    
    while substr_length <= length:
        start_index = 0
        end_index = 0
        while start_index < length:
            end_index = start_index + substr_length
            substr = string[start_index:end_index]

            if substr[0] in VOWELS and substr not in players['Kevin']['words']:
                counts = sum([
                    string.startswith(substr, i) for i in range(len(string))
                ])
                players['Kevin']['scores'] += counts
                players['Kevin']['words'].append(substr)
                print(substr, counts)
            if substr[0] not in VOWELS and substr not in players['Stuart']['words']:
                counts = sum([
                    string.startswith(substr, i) for i in range(len(string))
                ])
                # print(substr, counts)
                players['Stuart']['scores'] += counts
                players['Stuart']['words'].append(substr)
            start_index += 1

        substr_length += 1
    
    if players['Kevin']['scores'] > players['Stuart']['scores']:
        winner = 'Kevin'
    elif players['Stuart']['scores'] > players['Kevin']['scores']:
        winner = 'Stuart'
    else:
        winner = 'Draw'
    
    winning_msg = f'{winner} {players[winner]["scores"]}' if winner != 'Draw' else winner
    print(winning_msg)


if __name__ == '__main__':
    s = input()
    minion_game(s)
