# Question 16.10

def most_living_people(people):
    pop_count = {key: 0 for key in range(1900, 2001)}

    for year in range(1900, 2001):
        for person in people: 
            if person[1] <= year and person[2] >+ year:
                pop_count[year] += 1
    
    max_pop = 1900
    for key in pop_count.keys():
        if pop_count[max_pop] < pop_count[key]:
            max_pop = key
    return max_pop


# Potential optimization: loop through people instead of years, and increment year group for each person


people = [("person1", 1901, 1985), ("person2", 1920, 1921)]

actual = most_living_people(people)
expected = 1920
assert actual == expected, f"actual: {actual} expected: {expected}"