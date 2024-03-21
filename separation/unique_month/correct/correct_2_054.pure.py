def unique_month(month, possible_birthdays):
    return len(filter(lambda x:x[0]==month, possible_birthdays)) == 1