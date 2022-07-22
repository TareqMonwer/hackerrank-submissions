import re

n = int(input())
card_numbers = [input().strip() for _ in range(n)]

card_starting_regx = re.compile(r'^[4-6]')
only_digits_regx = re.compile(r'^[0-9+]*$')
hiphen_group_regx = re.compile(
    r"^\d\d\d\d-\d\d\d\d-\d\d\d\d-\d\d\d\d$")
repeating_nums_regx = re.compile(r'(\d)\1{3,}')


def valid_card(cardStr):
    if card_starting_regx.search(cardStr) != None:
        # if only_digits_n_hyphens_regx.match(cardStr) == None:
        #     return False
        if '-' in cardStr:
            if hiphen_group_regx.search(cardStr) == None:
                return False
            if repeating_nums_regx.search(cardStr.replace('-', '')) != None:
                return False
        else:
            if len(cardStr) != 16:
                return False
            if only_digits_regx.search(cardStr) == None:
                return False
            if repeating_nums_regx.search(cardStr) != None:
                return False
        return True
    else:
        return False


for card in card_numbers:
    if valid_card(card):
        print('Valid')
    else:
        print('Invalid')
