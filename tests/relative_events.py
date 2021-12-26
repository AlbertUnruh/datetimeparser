import datetime

today = datetime.datetime.today()

tests = [
    "next christmas",
    "christmas",
    "new years eve",
    "xmas 2025",
    "next friday",
    "next second",
    "last month",
    "next hour",
    "next year",
    "eastern 2010",
    "halloween 2030",
    "next april fools day",
    "thanksgiving",
    "next st patricks day",
    "valentine day 2010",
    "summer",
    "winter 2021",
    "next spring",
    "begin of fall 2010",
    "summer end",
    "end of winter",
    "end of the spring",
    "end of autumn 2020",
    "begin of advent of code 2022",
    "end of aoc 2022",
    "end of the year"
]

validation = [
    datetime.datetime(2022, 12, 25),
    datetime.datetime(2022, 12, 25),
    datetime.datetime(today.year, 12, 31),
    datetime.datetime(2025, 12, 25),
    datetime.datetime(today.year, 12, 31),
    datetime.datetime(today.year, today.month, today.day, today.hour, today.minute, today.second+1),
    datetime.datetime(today.year, today.month-1, today.day, today.hour, today.minute, today.second),
    datetime.datetime(today.year, today.month, today.day, today.hour+1, today.minute, today.second),
    datetime.datetime(today.year+1, today.month, today.day, today.hour, today.minute, today.second),
    datetime.datetime(2010, 4, 4),
    datetime.datetime(2030, 10, 31),
    datetime.datetime(2022, 4, 1),
    datetime.datetime(2022, 11, 25),
    datetime.datetime(2022, 3, 17),
    datetime.datetime(2010, 2, 14),
    datetime.datetime(2022, 6, 1),
    datetime.datetime(2021, 12, 1),
    datetime.datetime(2022, 3, 1),
    datetime.datetime(2010, 9, 1),
    datetime.datetime(2022, 8, 31, 23, 59, 59),
    datetime.datetime(2022, 2, 28, 23, 59, 59),
    datetime.datetime(2022, 5, 31, 23, 59, 59),
    datetime.datetime(2020, 11, 30, 23, 59, 59),
    datetime.datetime(2022, 12, 1, 6),
    datetime.datetime(2022, 12, 26, 6),
    datetime.datetime(today.year, 12, 31, 23, 59, 59),
]