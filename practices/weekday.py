def week_day(weekday,vaction):
    if not weekday or vaction:
        return True
    else:
        return False
    
print(week_day(True,False))
print(week_day(False,True))