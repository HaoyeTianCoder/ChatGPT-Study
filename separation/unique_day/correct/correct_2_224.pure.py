def unique_day(day, possible_birthdays):
    bag = []
    for birthdays in possible_birthdays:
        if birthdays[1] == day:
            bag.append(day)
    n = len(bag)
    if n == 1:
        return True
    else:
        return False