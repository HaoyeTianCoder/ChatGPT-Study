def unique_day(day, possible_birthdays):
    count = 0
    for birthdays in possible_birthdays:
        if birthdays[1] == day:
            count +=1
            if count == 2:
                return False
    return True