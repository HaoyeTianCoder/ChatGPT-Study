def unique_day(day, possible_birthdays):
    return len(filter(lambda x:x[1]==day, possible_birthdays)) == 1