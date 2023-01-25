


#The year can be evenly divided by 4;
#If the year can be evenly divided by 100, it is NOT a leap year, unless;
#The year is also evenly divisible by 400. Then it is a leap year.

# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    if year1 < year2:           #this makes sure year1 is the newer year
        year1, year2 = year2, year1
        month1, month2 = month2, month1
        day1, day2 = day2, day1


    leaps1 = 0                #counts the leap years in the range of a given year not counting the year itself

    for x in range(1,year1):
        if x % 4 == 0 and not x % 100 == 0 or x % 400 == 0:
            leaps1 += 1
                
    nonleaps1 = year1 - leaps1
    totaldays1 = (nonleaps1*365) + (leaps1*366)


    leaps2 = 0

    for y in range(1,year2):
        if y % 4 == 0 and not y % 100 == 0 or y % 400 == 0:
            leaps2 += 1

    nonleaps2 = year2 - leaps2
    totaldays2 = (nonleaps2*365) + (leaps2*366)


    jan, mar, may, jul, aug, octe, dec = 31, 31, 31, 31, 31, 31, 31
    apr, jun, sep, nov = 30, 30, 30, 30
    feb = 28

    january = 0
    february = jan
    march = february + feb
    april = march + mar
    maiy = april + apr
    june = maiy + may
    july = june + jun
    august = july + jul
    september = august + aug
    october = september + sep
    november = october + octe
    december = november + nov

    if month1 == 1:
        month1 = january
    elif month1 == 2:
        month1 = february
    elif month1 == 3:
        month1 = march
    elif month1 == 4:
        month1 = april
    elif month1 == 5:
        month1 = maiy
    elif month1 == 6:
        month1 = june
    elif month1 == 7:
        month1 = july
    elif month1 == 8:
        month1 = august
    elif month1 == 9:
        month1 = september
    elif month1 == 10:
        month1 = october
    elif month1 == 11:
        month1 = november
    else:
        month1 = december

    
    if month2 == 1:
        month2 = january
    elif month2 == 2:
        month2 = february
    elif month2 == 3:
        month2 = march
    elif month2 == 4:
        month2 = april
    elif month2 == 5:
        month2 = maiy
    elif month2 == 6:
        month2 = june
    elif month2 == 7:
        month2 = july
    elif month2 == 8:
        month2 = august
    elif month2 == 9:
        month2 = september
    elif month2 == 10:
        month2 = october
    elif month2 == 11:
        month2 = november
    else:
        month2 = december

    monthndays1 = month1 + day1
    monthndays2 = month2 + day2
    if year1 % 4 == 0 and not year1 % 100 == 0 or year1 % 400 == 0:
        if monthndays1 > 59 and day1 != 29:
            monthndays1 += 1
    if year2 % 4 == 0 and not year2 % 100 == 0 or year2 % 400 == 0:
        if monthndays2 > 59 and day2 != 29:
            monthndays2 += 1


    total1 = monthndays1 + totaldays1
    total2 = monthndays2 + totaldays2

    final = total1 - total2
    if final < 0:
        final = - final
    return final

replay = True

while replay:
    a = int(input('Enter year1: '))
    b = int(input('Enter month1: '))
    c = int(input('Enter day1: '))
    d = int(input('Enter year2: '))
    e = int(input('Enter month2: '))
    f = int(input('Enter day2: '))
    print(daysBetweenDates(a, b, c, d, e, f), 'days between dates or roughly', daysBetweenDates(a, b, c, d, e, f) / 365, 'years' )
    final = input('replay? ')
    if final == 'no':
        replay = False

