def contains_unique_day(month, possible_birthdays):
     get_possible_months = filter(lambda birthday: birthday[0] == month, possible_birthdays)
     get_possible_days = map(lambda birthday: birthday[1],get_possible_months)
     for days in get_possible_days:
        if unique_day(days, possible_birthdays):
            return True
     return False