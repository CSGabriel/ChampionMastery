import json
import requests
import itertools
with open('champion.json') as f:
    champdata = json.load(f)

names = []
keys = []
champData = {}
num = 0
apiK = "RGAPI-7cc5cbcc-59c0-4a86-9a20-6e26d4986d9c"

def getKeyWithValue(dict, value):
    for k, v in dict.iteritems():
        if v == value:
            yield k

for name in champdata['data']:
    names.append(str(name))

for i in names:
    for items in champdata['data'][i]['key']:
        keys.append(str(champdata['data'][i]['key']))
        break

for g in keys:
    champData[g] = names[num]
    num += 1

def getChampionName(champData, dictKey):
    keyFromDict = dictKey['championId']
    champName = champData[str(keyFromDict)]
    return champName

def getSummonerId(summonerName):
    try:
        summonerReq = requests.get('https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{}?api_key={}'.format(summonerName, apiK))
        print(summonerReq.json()['id'])
    except Exception as e:
        summonerReq.json()['id'] = ""
        return
    return summonerReq.json()['id']

def getMastery(encryptedSummonerId):
    masteryReq = requests.get('https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{}?api_key={}'.format(encryptedSummonerId,apiK))
    jsonFile = masteryReq.json()
    return jsonFile

def getChampionData(name):
    summonerid = getSummonerId(name)
    mastery = getMastery(summonerid)
    count = len(mastery) - 1
    championDic = {}
    for e in range(count):
        champname = getChampionName(champData, mastery[e])
        championLvL = mastery[e]['championLevel']
        championExp = mastery[e]['championPoints']
        championDic[champname] = [championLvL, championExp]

    return championDic
