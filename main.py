## ! WELCOME TO TROLLAND !
## 🄯 Copyleft 2022 - All wrongs reversed to Lamereary Industries - ширАко and SoulTaker

from random import randint

lang=input('Language, Langue, Lengua? ').lower() #demande la langue, puis met l'input en minuscule
if lang in ['es','español','espanol']:
  from dialogue_es import * #si c'est espa, importe les dialogues espa
elif lang in ['fr','français','francais']:
  from dialogue_fr import *
else: 
  from dialogue_en import * #Anglais par défaut


class Entities: # définit toutes les entités du jeu (joueur, enemis..)
	def __init__(self,defe,atq,hp,mp,sta,lvl):
		self.defe=defe
		self.atq=atq
		self.hp=hp
		self.mp=mp
		self.sta=sta
		self.lvl=lvl

Troll1=Entities(1,2,3,4,5,6)#commence à defe (pas def car non enft) donc defe=1,atq=2..
Troll2=Entities(1,2,3,4,5,6)
High_Elf1=Entities(1,2,3,4,5,6)
Your_Mum=Entities(1,2,3,4,5,6)

#Exemple de la variable Enemies, les enemis actuellement présents en combat
Enemies=[Troll1,Troll2,High_Elf1,Your_Mum]

# Définition des fonctions qui affectent les stats avec les armes
# Comme par exemple 'defence has a 10% chance to be doubled'

def faith_shield_fun(): #voir power-system.txt
  if randint(1,10)==1: # 10% de chance de doubler la défense
    Player.defe*=2

def michael_sword_fun():
  if randint(1,10)==1: #10% de chance de doubler l'attaque
    Player.atq*=2

def trollking_shield_fun():
  if randint(1,4)==1: #25% de chance de ne pas recevoir de dégats <=> def=100
    Player.defe=100

def conquerer_sword_fun(): # Conquerer's sword
  if len(Enemies)==1: #Si il n'y a qu'un seul ennemi
    Player.off_pow*=2
  return 'zizi'

def elfking_epitome_fun():
  if len(Enemies)>1: #plusieurs enemis
    for i in Enemis:
      if randint(1,4)==1: # 25% de chance de stun
        i.stun()

def purgatory_door_fun():pass
def divine_light_blade_fun():pass
def satan_profecy_fun():pass
def paul_cum_shield_fun():pass
def mael_schlong_fun():pass
def arty_pride_book_fun():pass


def write(x):
  if type(x)==int:
    return '+'+str(x)
  if type(x)==list:# Si c'est une liste, c'est une fonction logique ahahahahahahahahahahahahahahahahahaha
    return x[1]
  else:print('''
	WTF
	c'est''',x,'\n\n')

class Weapons: # définit toutes les armes du jeu
  def __init__(self,tier,name,description,bonus={}): # Pas forcément de bonus, d'ou le bonus={} (si aucune valeur n'est donnée, bonus sera {})
    '''Initialise ( __init__ ) les armes du jeu'''
    self.tier=tier
    self.name=name
    self.description=description
    self.bonus=bonus

  def info(self):# ex: Rare tier: Magical Tome {MP +5, ATQ +10} \n this weapon does emotional damage
    '''Donne les informations sur l'arme sous forme de GUI'''
    print(self.name+', Tier:',self.tier+'\n'+', '.join(tuple(': '.join((i,write(self.bonus[i]))) for i in self.bonus))+'\n'+self.description)

Magical_Tome=Weapons(Rare_Tier,Magical_Tome_Name,Magical_Tome_Description,{'MP':5, 'ATQ':10}) #voir power-system.txt + dialogue_en.py
# Pour les nuls:
# Dans la ligne 77, une nouvelle arme est initialisée
# On appelle donc la fontion __init__ (ligne 66)
# self commme paramètre, dans ce cas self c'est Magical_Tome
# tier, name, description, bonus
# tier: Rare_Tier, variable importée par dialogue_en, dialogue_es ou dialogue_fr 'Rare', ou 'Raro' dépendant de la langue choisie
# name: variable de langue, 'Magical tome', 'Tome magique' ou 'Tomo mágico'
# description: variable de langue
# bonus: {'MP':5, 'ATQ':10}
# Si on demande print(Magical_Tome.bonus) ça met {'MP':5}    print(Magical_Tome.tier) affiche 'Rare' ou 'Raro' etc.
# Puis ligne 73, la fonction info
# S'utilise sous la forme Magical_Tome.info()    (C'est une fonction)
# Magical_tome.info() en anglais donne:
'''
Magical Tome, tier: Rare
This weapon does emotional damage
MP: +5  ATQ: +10
'''

Wooden_Shield=Weapons(Common_Tier,Wooden_Shield_Name,Wooden_Shield_Description) #pas de bonus dans power-system.txt
Wooden_Sword=Weapons(Common_Tier,Wooden_Sword_Name,Wooden_Sword_Description)
Old_Grimoire=Weapons(Common_Tier,Old_Grimoire_Name,Old_Grimoire_Description)
Priest_Shield=Weapons(Rare_Tier,Priest_Shield_Name,Priest_Shield_Description,{'DEF':10})
Blacksmith_Sword=Weapons(Rare_Tier,Blacksmith_Sword_Name,Blacksmith_Sword_Description,{'STA':5,'ATQ':10})
# 'FUN': fonction qui s'applique à chaque attaque, dans Faith_Shield la défense à une chance sur 10 de doubler (ligne 21)
Faith_Shield=Weapons(Hero_Tier,Faith_Shield_Name,Faith_Shield_Description,{'DEF':25,'FUN':[faith_shield_fun,faith_shield_fun_desc]})
Michael_Sword=Weapons(Hero_Tier,Michael_Sword_Name,Michael_Sword_Description,{'STA':20,'ATQ':40,'FUN':[michael_sword_fun,michael_sword_fun_desc]})
Dantalion_Anti_Bible=Weapons(Hero_Tier,Dantalion_Anti_Bible_Name,Dantalion_Anti_Bible_Description,{'MP':20,'ATQ':10})
Troll_King_Shield=Weapons(Relic_Tier,Troll_King_Shield_Name,Troll_King_Shield_Description,{'DEF':35,'FUN':trollking_shield_fun})
Conquerer_Sword=Weapons(Relic_Tier,Conquerer_Sword_Name,Conquerer_Sword_Description,{'STA':50,'ATQ':50,'FUN':conquerer_sword_fun})
Elf_King_Epitome=Weapons(Relic_Tier,Elf_King_Epitome_Name,Elf_King_Epitome_Description,{'MP':50,'ATQ':50,'FUN':elfking_epitome_fun})
Purgatory_Door=Weapons(Arcanic_Tier,Purgatory_Door_Name,Purgatory_Door_Description,{'DEF':50,'FUN':purgatory_door_fun})
Divine_Light_Blade=Weapons(Arcanic_Tier,Divine_Light_Blade_Name,Divine_Light_Blade_Description,{'STA':75,'ATQ':100,'FUN':divine_light_blade_fun})
Satan_Profecy=Weapons(Arcanic_Tier,Satan_Profecy_Name,Satan_Profecy_Description,{'MP':75,'ATQ':100,'FUN':satan_profecy_fun})
Hugo_Wives=Weapons(Easter_Egg_Tier,Hugo_Wives_Name,Hugo_Wives_Description,{'DEF':100})
Paul_Cum_Shield=Weapons(Easter_Egg_Tier,Paul_Cum_Shield_Name,Paul_Cum_Shield_Description,{'DEF':25,'FUN':paul_cum_shield_fun})
Mael_Schlong=Weapons(Easter_Egg_Tier,Mael_Schlong_Name,Mael_Schlong_Description,{'STA':95,'ATQ':700,'FUN':mael_schlong_fun})
Arty_Pride_Book=Weapons(Easter_Egg_Tier,Arty_Pride_Book_Name,Arty_Pride_Book_Description,{'MP':95,'ATQ':700,'FUN':arty_pride_book_fun})

try: #import basique de sauvegarde
  from saves import *
  Weapon=eval(Weapon)
except ModuleNotFoundError: #si non sauvegardé, pas de fichier de sauvegarde
  Weapon=''

print(Welcome)#le message de bonsoir dans la langue choisie (input de ligne 6)

def psay(msg):
	print('''

'''.format(msg))

def osay(msg):
	print('''
⊏＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝⊐
∥         {msg1}              ∥                                  
∥         {msg2}              ∥                                   
∥         {msg3}              ∥                                   
∥         {msg4}              ∥ 
∥         {msg5}              ∥
∥         {msg6}              ∥
∥         {msg7}              ＝＝＝⊐
∥         {msg8}                 ノ
∥         {msg9}               ノ 
⊏＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝⊐

'''.format(msg))
