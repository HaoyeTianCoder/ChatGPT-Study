def contains_unique_day(month, possible_birthdays):
    d=map(lambda birthday:birthday[1],filter(lambda birthday:birthday[0]==month,possible_birthdays))
    for day in d:
        if unique_day(day,possible_birthdays):
            return True
    return False