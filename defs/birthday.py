from discord.ext import commands
client = commands.Bot


async def update_birthday(users, member, day, month, year):
    users.update_one({"_id": member.id}, {"$set": {"b-day": str(day), "b-month": str(month), 'b-year': str(year)}})


async def check_day(month, day):
    if month < 1 or month > 12:
        return False
    if day > 31 or day < 1:
        return False
    if month == 2 and day > 29:
        return False
    elif month in [4, 6, 9, 11] and day > 30:
        return False
    else:
        return True
