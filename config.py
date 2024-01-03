from pymongo import MongoClient
import os

bot_version = '0.2'
bot_id = '988143343559127090'
token = os.environ['token']

tommorowiokey = os.environ['tommorowiokey']
openAIKey = os.environ['openAIKey']

cluster = MongoClient(os.environ['mongoDBCluster'])
db = cluster["discord-data"]


Rules = '1. Do not use forbidden words \n(for a complete list of banned words, type banned words)\n' \
         '2. Only use the bot channels for bot commands\n' \
         '3. nog regels?'
bannedWords = ['fuck', 'fortnite', 'stinkt', '#nocaps']
bannedwords = "'fuck', 'fortnite', 'stinkt'"

greets = ["adios amigos", "yoo", "goodbye", "bye", "yo", "challas", "saluu", "adios", "daag", "adioz", "adiozz", "challaz", "babay", "bay"]
othergreets = ["allow", "allo", "hallo", "bonjorno", "bonjor", "alloww", "allowww", "ellow", "bozoer", "ello", "bonsoir", "bjr", "bonjour"]

clearlimit = 10
botlogo = 'https://i.postimg.cc/MGBY0KBH/logo.png'

# foto's
FotoPeirsman = 'https://i.postimg.cc/YqPgFPfZ/peirsman.png'
FotoSarens = 'https://i.postimg.cc/FFD0rzf9/mnr-sarens.png'
FotoDank = 'https://i.postimg.cc/4d1VhNBQ/dank.png'
FotoChezzi = 'https://i.postimg.cc/PJPJrtcx/chezzi-groot.jpg'
FotoChezziK = 'https://i.postimg.cc/d06V2kc3/chezzi-klein.jpg'
FotoTroch = 'https://i.postimg.cc/x1SfBy0q/troch.jpg'



#emoji's:
Mnrsarens = '<:mnrsarens:820597058837938226>'
mnrpeirsman = '<:mnrpeirsman:821394371081273385>'
darkmemer = '<:darkmemer:818068419429531679>'
eent = '<:eent:841755160531304480>'
Mnrchezzi = '<:mnrchezzi:836954038792486922>'
mvrwtroch = '<:mvrwtroch:837751701955543140>'
mvrwMaetenZZ = '<:mvrMaetenZZ:890231711902871562>'
nibien = '<:nibien:898218023767404585>'
zarenz = '<:mnrZarenZZ:888066813529821184>'
mnrzonderbroeck = '<:mnrzonderbroeck:897815031541014530>'
onsnancy= '<:onsnancy:886663885950701588>'
mvrwLarivier = '<:mvrLarivier:890232049640812574>'
invisible = "<:Invisible:856156846033338378>"


