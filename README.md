# Hordes.io-API
Unofficial API for hordes.io

## Player Stats


```
import hordesAPI

player = hordesAPI.Player("danziel") # initialize the player

player.Name() # returns the player's name
player.Class() # returns the player's class
player.Faction() # returns the player's faction
player.Prestige() # returns the player's prestige
player.Level() # returns the player's level
player.Fame() # returns the player's fame
player.Clan() # returns the player's clan
player.Elo() # returns the player's ELO
player.GearScore() # returns the player's gear score
player.Id() # returns the player's ID
```

## Clan Stats


```
import hordesAPI

clan = hordesAPI.Clan("Bed") # Initialize the clan with its name or tag however, it's better to use the tag

clan.NameToTag() # returns the clan's tag from its name
clan.TagToName() # returns the clan's name from its tag
clan.Id() # returns the clan's ID
clan.Tag() # returns the clan's tag
clan.Name() # returns the clan's name
clan.Level() # returns the clan's level
clan.Exp() # returns the clan's EXP to the next level
clan.Gold() # returns the clan's amount of gold
clan.Tax() # returns the clan's tax rate
clan.CreatedAt() # returns the date the clan was created at
clan.prestige() # returns the clan's prestige
clan.Members() # returns a list of all the members in a clan
clan.MemberCount() # returns the amount of members in a clan
clan.Faction() # returns what faction the clan is in
```

#### Contact:
###### Discord: KittyCatSlayer1#0354
