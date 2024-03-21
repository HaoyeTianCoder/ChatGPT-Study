def contains_unique_day(month, possible_birthdays):
    bdays_in_mth = filter(lambda x:x[0]==month, possible_birthdays)
    for bday in bdays_in_mth:
        if unique_day(bday[1], possible_birthdays):
            return True
    return False