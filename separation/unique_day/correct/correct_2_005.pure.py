def unique_day(day, possible_birthdays):
    def dayfilter(birthday):
        if birthday[1] == day:
            return True
        else:
            return False
    possible = tuple(filter(dayfilter,possible_birthdays))
    if len(possible) == 1:
        return True
    else:
        return False