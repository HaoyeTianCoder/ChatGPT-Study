def unique_day(day, possible_birthdays):
    birthday_with_day = list(filter(lambda birthday: birthday[1] == day                                 , possible_birthdays))
    if len(birthday_with_day) >= 2:
        return False
    return True