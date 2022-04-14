def print_rangoli(size):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    letters = alphabets[0:size]
    reversed_letters = letters[::-1]
    reversed_str = reversed_letters + letters[1:]
    final_str = ''.join([('-' + letter if index != 0 else letter) \
        for index, letter in enumerate(reversed_str)])

    rows = list()

    for index, letter in enumerate(reversed_letters):
        if index == size - 1:
            rows.append(final_str)
        else:
            line_letters = reversed_str[0:index+1]
            edge_letters = letters[-index:]
            if len(line_letters) > 1:
                line_letters += edge_letters
            l = '-'.join(line_letters)
            line = l.center(len(final_str), '-')
            rows.append(line)

    rows.extend(rows[0:-1][::-1])

    for line in rows:
        print(line)


if __name__ == '__main__':
    # n = input()
    # print_rangoli(int(n))
    print_rangoli(10)
