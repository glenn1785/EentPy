from discord.ext import commands
client = commands.Bot


async def update_data(users, user, xp):
    users.update_one(filter={'_id': user.id, }, update={'$setOnInsert': {"name": user.name,'xp': 5,'level':1,'b-day':'NaN',"b-month":'NaN',"b-year":"NaN"  }, }, upsert=True, )
    users.update_one({"_id": user.id}, {"$inc": {"xp": xp}})


async def level_up(users, user):
    results = users.find({"_id": user.id})
    for result in results:
        experience = result['xp']
        lvl_start = result['level']

    lvl_end = int(experience ** (1 / 4))

    if lvl_start < lvl_end:
        users.update_one({"_id": user.id}, {"$set": {"level": lvl_end}})
        return True
