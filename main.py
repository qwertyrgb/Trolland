## ! WELCOME TO TROLLAND !
## 🄯 Copyleft 2022 - All wrongs reversed to Lamereary Industries - ширАко and SoulTaker

lang=input('Language, Langue, Lengua? ').lower() #demande la langue, logique, puis la met en minuscule
if lang in ['es','español','espanol']:
  from dialogue_es import * #si c'est espa, importe les dialogues espa
elif lang in ['fr','français','fr']:
  from dialogue_fr import *
else: 
  from dialogue_en import * #Anglais par défaut

class Weapons: # définit toutes les armes du jeu
  def __init__(self,tier,name,description,bonus=''): # Pas forcément de bonus, d'ou le bonus='' (si aucune valeur n'est donnée, bonus sera '')
    '''Initialise ( __init__ ) les armes du jeu'''
    self.tier=tier
    self.name=name
    self.description=description
    self.bonus=bonus

  def info(self):# ex: Rare tier: Magical Tome {MP +5, ATQ +10} \n this weapon does emotional damage
    '''Donne les informations sur l'arme sous forme de GUI'''
    print(self.name,', Tier: ',self.tier,', '.join(tuple(': +'.join((i,str(self.bonus[i]))) for i in self.bonus)), self.description)

MS_T=Weapons('Rare','Magical Tome','This weapon does emotional damage',{'MP':5, 'ATQ':10}) #voir power-system.txt
# Pour les nuls:
# Dans la ligne 14, ce que je fais c'est initialiser une nouvelle arme
# J'appelle donc la fontion __init__ (ligne 5)
# J'ais mis self commme paramètre, dans ce cas self c'est MS_T
# tier, name, description, bonus
# tier: 'Rare'
# name: 'Magical tome'
# description: 'This weapon does emotional damage'
# bonus: {'MP':5, 'ATQ':10}
# Si on demande print(MS_T.bonus) ça met {'MP':5}    print(MS_T.tier) affiche 'Rare'  etc.
# Puis ligne 12, info
# S'utilise sous la forme MS_T.info()    (C'est une fonction)
# MS_T.info() donne:
'''
Magical Tome, tier: Rare
This weapon does emotional damage
MP: +5  ATQ:+10
'''
#Simon fait d'autres armes pour voir si t'as compris

try: #import basique de sauvegarde
  from saves import *
  Weapon=eval(Weapon)
except ModuleNotFoundError: #si non sauvegardé, pas de fichier de sauvegarde
  Weapon=''
