mname = ["Jan", "Feb", "Mar", "Apr",
         "May", "Jun", "Jul", "Aug",
         "Sep", "Oct", "Nov", "Dec"]


def read_date():
    x = input()
    x = x[0::].split(" ")
    for i in mname:
        if i == x[1]:
            x[1] = (mname.index(i)) + 1
            break
    for i in range(len(x)):
        x[i] = int(x[i])
    return x


def zodiac(d, m):
    if d >= 22 and m == 3 or d <= 21 and m == 4:
        z1 = "Aries"
    elif d >= 22 and m == 4 or d <= 21 and m == 5:
        z1 = "Taurus"
    elif d >= 22 and m == 5 or d <= 21 and m == 6:
        z1 = "Gemini"
    elif d >= 22 and m == 6 or d <= 21 and m == 7:
        z1 = "Cancer"
    elif d >= 22 and m == 7 or d <= 21 and m == 8:
        z1 = "Leo"
    elif d >= 22 and m == 8 or d <= 21 and m == 9:
        z1 = "Virgo"
    elif d >= 22 and m == 9 or d <= 21 and m == 10:
        z1 = "Libra"
    elif d >= 22 and m == 10 or d <= 21 and m == 11:
        z1 = "Scorpio"
    elif d >= 22 and m == 11 or d <= 21 and m == 12:
        z1 = "Sagittarius"
    elif d >= 22 and m == 12 or d <= 20 and m == 1:
        z1 = "Capricorn"
    elif d >= 21 and m == 1 or d <= 20 and m == 2:
        z1 = "Aquarius"
    elif d >= 21 and m == 2 or d <= 21 and m == 3:
        z1 = "Pisces"
    return z1


def days_in_feb(y):
    y1 = y
    days_in_feb1 = 28
    if y1 % 400 == 0 or y1 % 100 != 0 and y1 % 4 == 0:
        days_in_feb1 = 29
    return days_in_feb1


def days_in_month(m1, y):
    days_in_m1 = 31
    if m1 == 4 or m1 == 6 or m1 == 9 or m1 == 11:
        days_in_m1 = 30
    elif m1 == 2:
        days_in_m1 = days_in_feb(y)
    return days_in_m1


def days_in_between(d1, m1, y1, d2, m2, y2):
    if days_in_feb(y1) == 28:
        a = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        m1 = a[m1-1]
        daysleft = 365-(m1+d1)
    else:
        a = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
        m1 = a[m1-1]
        daysleft = 366-(m1+d1)

    if days_in_feb(y2) == 28:
        a = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        m2 = a[m2-1]
        dayspass = m2 + d2
    else:
        a = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
        m2 = a[m2-1]
        dayspass = m2 + d2

    dy = int(365.25*((y2-y1)-1))

    days = daysleft + dayspass + dy
    return(days)


def main():
    d1, m1, y1 = read_date()
    d2, m2, y2 = read_date()
    zo1 = zodiac(d1, m1)
    zo2 = zodiac(d2, m2)
    days = days_in_between(d1, m1, y1, d2, m2, y2)
    print(zo1, zo2)
    print(days)


exec(input().strip())
