from geopy.geocoders import Nominatim

def getweather(weatherCode):
    weatherCode = str(weatherCode)
    if weatherCode == '1000':
        weather = 'helder'
    elif weatherCode == '1001':
        weather = 'bewolkt'
    elif weatherCode == '1100':
        weather = 'overwegend helder'
    elif weatherCode == '1101':
        weather = 'gedeeltelijk bewolkt'
    elif weatherCode == '1102':
        weather = 'overwegend bewolkt'
    elif weatherCode == '2000':
        weather = 'mist'
    elif weatherCode == '2100':
        weather = 'ligte mist'
    elif weatherCode == '3000':
        weather = 'zachte wind'
    elif weatherCode == '3001':
        weather = 'wind'
    elif weatherCode == '3002':
        weather = 'sterke wind'
    elif weatherCode == '4000':
        weather = 'motregen'
    elif weatherCode == '4001':
        weather = 'regen'
    elif weatherCode == '4200':
        weather = 'ligte regen'
    elif weatherCode == '4201':
        weather = 'harde regen'
    elif weatherCode == '5000':
        weather = 'sneeuw'
    elif weatherCode == '5001':
        weather = 'vlagen'
    elif weatherCode == '5100':
        weather = 'ligte sneeuw'
    elif weatherCode == '5101':
        weather = 'zware sneeuw'
    elif weatherCode == '6000':
        weather = 'aanvriezende motregen'
    elif weatherCode == '6001':
        weather = 'aanvriezende regen'
    elif weatherCode == '6200':
        weather = 'ligte aanvriezende regen'
    elif weatherCode == '6201':
        weather = 'zware aanvriezende regen'
    elif weatherCode == '7000':
        weather = 'hagel'
    elif weatherCode == '7101':
        weather = 'zware hagel'
    elif weatherCode == '7102':
        weather = 'zware hagel'
    elif weatherCode == '8000':
        weather = 'omweer'
    else:
        weather = 'geen weer vandaag'
    return weather

def getmoonphase(phasecode):
    phasecode = str(phasecode)
    if phasecode == "0":
        moonphase = "nieuwe maan"
    elif phasecode == "1":
        moonphase = "beginnende halve maan"
    elif phasecode == "2":
        moonphase = "eerste kwartier"
    elif phasecode == "3":
        moonphase = "opgaande maan"
    elif phasecode == "4":
        moonphase = "volle maan"
    elif phasecode == "5":
        moonphase = "Afnemende maan"
    elif phasecode == "6":
        moonphase = "derde kwartier"
    elif phasecode == "7":
        moonphase = "afnemende halve maan"
    else:
        moonphase = "onbekend (maan loes)"
    return moonphase


def getcoordinates(Location):
    geolocator = Nominatim(user_agent="eentpy")
    location = geolocator.geocode(Location)
    return f"{location.latitude},{location.longitude}"

