def unique_day(date, possible_birthdays):
    bdaylist = possible_birthdays
    count = 0
    while len(bdaylist) > 0:
        single = bdaylist[0]
        if single[1] == day:
            count = count + 1
        if count == 2:
            return False
            break
        bdaylist = bdaylist[1:]
    return True