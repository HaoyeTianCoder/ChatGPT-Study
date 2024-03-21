def unique_month(month, possible_birthdays):
    birthday_with_month = list(filter(lambda birthday: birthday[0] == month                                 , possible_birthdays))
    if len(birthday_with_month) >= 2:
        return False
    return True