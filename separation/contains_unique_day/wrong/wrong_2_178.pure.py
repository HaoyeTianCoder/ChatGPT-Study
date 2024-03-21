def contains_unique_day(month, possible_birthdays):
    filtered = tuple(filter(lambda x: x[0] == month, possible_birthdays))
    tup1 = tuple(filter(lambda x: x[0] != month, possible_birthdays)) 
    tup2 = tuple(map(lambda x: x[1], tup1)) 