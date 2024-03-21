def contains_unique_day(month, possible_birthdays):
    occur = 0
    for i in possible_birthdays:
            if month == i[0]:
                occur += 1
    if occur == 1:
        return True
    else:
        return False