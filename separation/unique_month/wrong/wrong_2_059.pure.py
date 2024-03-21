def unique_month(month, pb):
    n = len(pb)
    for i in range(n):
        if month == pb[i][0]:
            k = pb[i+1:]
            for j in range(len(k)):
                if month == k[j][0]:
                    return False
    return True