import requests

class Player:
    def __init__(self, name):
        payload = {"name":name,"order":"fame","limit":1}
        response = requests.post("https://hordes.io/api/playerinfo/search", json=payload)

        if (response.status_code == 200):
            r = response.json()[0]
            self.playerName = r["name"]
            self.playerClass = r["pclass"]
            self.playerFaction = r["faction"]
            self.playerPrestige = r["prestige"]
            self.playerLevel = r["level"]
            self.playerFame = r["fame"]
            self.playerClan = r["clan"]
            self.playerELO = r["elo"]
            self.playerGearScore = r["gs"]
            self.playerID = r["id"]


    def Name(self):
        return self.playerName
    
    def Class(self):
        return self.playerClass

    def Faction(self):
        return self.playerFaction

    def Prestige(self):
        return self.playerPrestige

    def Level(self):
        return self.playerLevel

    def Fame(self):
        return self.playerFame

    def Clan(self):
        return self.playerClan

    def Elo(self):
        return self.playerELO

    def GearScore(self):
        return self.playerGearScore

    def Id(self):
        return self.playerID



class Clan:
    def __init__(self, clan):

        if len(clan) < 4:
            self.tag = clan
            payload = {"tag":clan}
            response = requests.post("https://hordes.io/api/claninfo/info", json=payload)
            
        else:
            payload = {"name":clan,"order":1}
            self.tag = requests.post("https://hordes.io/api/claninfo/info", json=payload).json()[0]["tag"]

            payload = {"tag":self.tag}
            response = requests.post("https://hordes.io/api/claninfo/info", json=payload)

        if (response.status_code == 200):
            r = response.json()

            self.ID = r["id"]
            self.tag = r["tag"]
            self.name = r["name"]
            self.level = r["level"]
            self.exp = r["exp"]
            self.gold = r["gold"]
            self.tax = r["tax"]
            self.created = r["time_created"]
            self.prestige = r["prestige"]
            self.members = r["members"]
            self.memberCount = len(r["members"])
            self.applications = r["applications"]
            if int(r["faction"]) == 0:
                self.faction = "Vanguard"
            else:
                self.faction = "BloodLust"


    def NameToTag(self, name):
        payload = {"name":name,"order":1}
        return requests.post("https://hordes.io/api/claninfo/list", json=payload).json()[0]["tag"]

    def TagToName(self, tag):
        payload = {"tag":tag}
        return requests.post("https://hordes.io/api/claninfo/info", json=payload)

    def Id(self):
        return self.ID

    def Tag(self):
        return self.tag

    def Name(self):
        return self.name

    def Level(self):
        return self.level

    def Exp(self):
        return self.exp

    def Gold(self):
        return self.gold

    def Tax(self):
        return self.tax

    def CreatedAt(self):
        return self.created

    def Prestige(self):
        return self.prestige

    def Members(self):
        return self.members

    def MemberCount(self):
        return self.memberCount

    def Faction(self):
        return self.faction