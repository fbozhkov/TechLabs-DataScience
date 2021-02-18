def max_month_days(m) :
    if m in [1,3,5,7,8,10,12] :
        #print('m is max 31')
        return 31

    elif m in [4,6,9,11] :
        return 30
    else : return 28

    #return max

def date_to_str(year,month,day) :
    if month < 10 :
        month_str = '0' + str(month)
    else : month_str = str(month)

    if day < 10 :
        day_str = '0' + str(day)
    else: day_str = str(day)
    year = str(year)
    date = year + '-' + month_str + '-' + day_str
    return date

def next_date(date):
    #date_list = list(date)
    year_str = date[0:4]
    month_str = date[5:7]
    day_str = date[8:10]
    year_int = int(year_str)
    month_int = int(month_str)
    day_int = int(day_str)
    next_day_int = 0
    next_month_int = 0
    next_year_int = 0
    if (day_int == max_month_days(month_int)) and (month_int==12) :
        next_year_int = year_int+1
    elif day_int == max_month_days(month_int) :
        next_year_int = year_int
        next_month_int = month_int + 1
        next_day_int = 1
    elif day_int < max_month_days(month_int) :
        next_day_int = day_int + 1
        next_month_int = month_int
        next_year_int = year_int

    else : print("Date error: Out of bound!")

    next_date_str = date_to_str(next_year_int,next_month_int,next_day_int)

    return next_date_str