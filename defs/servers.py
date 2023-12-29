
def updateservers(servers,guild):
    servers.update_one(filter={'_id': guild.id, }, update={'$setOnInsert': {'gm/gn': 'None', "location": 'London',"rules":"None","spamchannel":"None" ,"lastgm":"0","lastgn":"0"}, }, upsert=True, )

def updatesettings(servers,guild,setting,var):
    if setting == 'gm/gn':
        servers.update_one({"_id":guild.id},{"$set":{"gm/gn":var}})

    elif setting == 'location':
        servers.update_one({"_id":guild.id},{"$set":{"location":var}})

    elif setting == 'spam':
        servers.update_one({"_id":guild.id},{"$set":{"spamchannel":var}})

def updaterules(servers,guild,rulenumber,var):
    servers.update_one({"_id": guild.id}, {"$set": {"rules": var}},multi=True)

    '''
    if servers[f'{guild.id}']['rules'] == 'None':
        servers[f'{guild.id}']['rules'] = {}

    if rulenumber in servers[f'{guild.id}']['rules']:
        servers[f'{guild.id}']['rules'][f'{rulenumber}'] = f'{var}'
    else:
        servers[f'{guild.id}']['rules'][f'{rulenumber}'] = f'{var}'
    '''
