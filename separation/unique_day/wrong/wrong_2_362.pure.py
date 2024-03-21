def unique_day(day, possible_birthdays):
    occur = 0
    for i in possible_birthdays:
            if day == i[1]:
                occur += 1
    if occur == 1:
        return True
    else:
        return False