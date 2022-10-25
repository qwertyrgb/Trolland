## ! WELCOME TO TROLLAND !
## 🄯 Copyleft 2022 - All wrongs reversed to Lamereary Industries - ширАко and SoulTaker

lang=input('Language, Langue, Lengua? ').lower() #demande la langue, puis met l'input en minuscule
if lang in ['es','español','espanol']:
  from dialogue_es import * #si c'est espa, importe les dialogues espa
elif lang in ['fr','français','francais']:
  from dialogue_fr import *
else: 
  from dialogue_en import * #Anglais par défaut

class Weapons: # définit toutes les armes du jeu
  def __init__(self,tier,name,description,bonus={}): # Pas forcément de bonus, d'ou le bonus={} (si aucune valeur n'est donnée, bonus sera {})
    '''Initialise ( __init__ ) les armes du jeu'''
    self.tier=tier
    self.name=name
    self.description=description
    self.bonus=bonus

  def info(self):# ex: Rare tier: Magical Tome {MP +5, ATQ +10} \n this weapon does emotional damage
    '''Donne les informations sur l'arme sous forme de GUI'''
    print(self.name,', Tier: ',self.tier,', '.join(tuple(': +'.join((i,str(self.bonus[i]))) for i in self.bonus)), self.description)

Magical_Tome=Weapons(Rare_Tier,Magical_Tome_Name,Magical_Tome_Description,{'MP':5, 'ATQ':10}) #voir power-system.txt + dialogue_en.py
# Pour les nuls:
# Dans la ligne 14, ce que je fais c'est initialiser une nouvelle arme
# J'appelle donc la fontion __init__ (ligne 5)
# J'ais mis self commme paramètre, dans ce cas self c'est Magical_Tome
# tier, name, description, bonus
# tier: Rare_Tier, variable importée par dialogue_en, dialogue_es ou dialogue_fr 'Rare', ou 'Raro' dépendant de la langue choisie
# name: variable de langue, 'Magical tome', 'Tome magique' ou 'Tomo mágico'
# description: variable de langue
# bonus: {'MP':5, 'ATQ':10}
# Si on demande print(Magical_Tome.bonus) ça met {'MP':5}    print(Magical_Tome.tier) affiche 'Rare' ou 'Raro' etc.
# Puis ligne 12, la fonction info
# S'utilise sous la forme Magical_Tome.info()    (C'est une fonction)
# Magical_tome.info() en anglais donne:
'''
Magical Tome, tier: Rare
This weapon does emotional damage
MP: +5  ATQ:+10
'''

Wooden_Shield=Weapons(Tier_Common,Wooden_Shield_Name,Wooden_Shield_Description) #pas de bonus


try: #import basique de sauvegarde
  from saves import *
  Weapon=eval(Weapon)
except ModuleNotFoundError: #si non sauvegardé, pas de fichier de sauvegarde
  Weapon=''
