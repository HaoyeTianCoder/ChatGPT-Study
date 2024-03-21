def contains_unique_day(month, possible_birthdays):
    temp_days = tuple(map(lambda x: x[1] ,filter(lambda x: x[0]==month,possible_birthdays)))
    for temp_day in temp_days:
        if unique_day(temp_day, possible_birthdays):
            return True
    return False