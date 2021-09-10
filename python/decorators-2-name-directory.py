from operator import itemgetter

def sorted_by_age_and_formatted(people, formatter):
    people.sort(key=itemgetter(2))
    formatted_persons = list()
    for person in people:
        formatted_persons.append(formatter(person))
    return formatted_persons

def person_lister(f):
    def inner(people):
        people_with_int_ages = list()
        for person in people:
            person[2] = int(person[2])
            people_with_int_ages.append(person)
        return sorted_by_age_and_formatted(
            people_with_int_ages, formatter=f
        )
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')