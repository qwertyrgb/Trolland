#1 - MONSTER ATTACK LIST

#attack - attack stats - [SCA, Attack special effect]

Smash=["20%", "none"]

#2 - MONSTER WEAPON LIST 

#weapon_EL - weapon Effect List - [Stat bonus (1:4, can be undefined)]
#weapon - [[EL], special effect]

Sword_of_justice_EL=["ATQ=+100"]
Sword_of_justice=[Sword_of_justice_EL, "All attacks deal 30% of the target's MAX_HP"]

#3 - BEASTS

#beast_AL - beast Attack List - [Attacks (1:6, can be undefined) of Beast]
#beast - beast stats - [DEF, ATQ, HP, MAX_HP, STA, MP, WEAP, [AL]]

InjuredTroll_AL=["Smash"]
InjuredTroll=["DEF=0",
              "ATQ=800",
              "HP=6",
              "MAX_HP=1750",
              "STA=150",
              "MP=150",
              "WEAP=Sword of Justice",
              InjuredTroll_AL]
