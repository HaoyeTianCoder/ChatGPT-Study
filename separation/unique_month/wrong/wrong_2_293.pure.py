def unique_month(month, possible_birthdays):
    bdaylist = possible_birthdays
    count = 0
    while len(bdaylist) > 0:
        single = bdaylist[0]
        if single[0] == month:
            count = count + 1
        if count == 2:
            return False
            break
        bdaylist = bdaylist[1:]
    return True