import logging
from datetime import datetime
from calendar import monthrange


def parse_str(text: str):
    week, day, month = text.split()
    week = int(week[0])
    day = parse_day(day)
    month = parse_month(month)
    year = datetime.now().year
    days_count = monthrange(year, month)[1]
    week_counter = 0
    for i in range(1, days_count + 1):
        data = datetime(day=i, month=month, year=year)
        if data.weekday() == day:
            week_counter += 1
            if week_counter == week:
                return data


def parse_month(month: str) -> int:
    months = {'Jan': 1, 'Feb': 2, 'Mar': 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9,
              "Okt": 10, "Nov": 11, "Dec": 12}
    return months.get(month[:3], None)


def parse_day(day: str) -> int:
    match day:
        case "Monday":
            return 0
        case "Tuesday":
            return 1
        case "Wednesday":
            return 2
        case "Thursday":
            return 3
        case "Friday":
            return 4
        case "Saturday":
            return 5
        case "Sunday":
            return 6


if __name__ == '__main__':
    print(parse_str("1-st Thursday November"))
    print(parse_str("3-rd Wednesday May"))
