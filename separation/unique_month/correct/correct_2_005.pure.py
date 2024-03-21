def unique_month(month, possible_birthdays):
    def monthfilter(birthday):
        if birthday[0] == month:
            return True
        else:
            return False
    possible = tuple(filter(monthfilter,possible_birthdays))
    if len(possible) == 1:
        return True
    else:
        return False