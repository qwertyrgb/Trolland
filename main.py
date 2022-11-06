## ! WELCOME TO TROLLAND !
## 🄯 Copyleft 2022 - All wrongs reversed to Lamereary Industries - ширАко and SoulTaker

from random import randint
from easter_eggs import *

lang=input('Language, Langue, Lengua? ').lower() #demande la langue, puis met l'input en minuscule
if lang in ['es','español','espanol']:
  from dialogue_es import * #si c'est espa, importe les dialogues espa
elif lang in ['fr','français','francais']:
  from dialogue_fr import *
else: 
  from dialogue_en import * #Anglais par défaut

def change(q):#voir fonction say
	while len(q)<10:
		q.append('')
		if len(q)<10:
			q.insert(0,'')
	for i in range(10):
		while len(q[i])<34+(i==8)*2+(i in [7,8,9]):
			q[i]+=' '
			if len(q[i])<34+(i==8)*2+(i in [7,8,9]):
				q[i]=' '+q[i]
	return q

def psay(msg):
	print("       ⊏＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝⊐\n       ∥{0[0]}∥\n       ∥{0[1]}∥\n       ∥{0[2]}∥\n       ∥{0[3]}∥\n       ∥{0[4]}∥\n       ∥{0[5]}∥\n       ∥{0[6]}∥\n   ⊏＝＝{0[7]}∥\n    ＼{0[8]}∥\n      ＼{0[9]}∥\n        ⊏＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝⊐".format(msg))

def osay(msg):
	print("⊏＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝⊐\n∥{0[0]}∥                                  \n∥{0[1]}∥                                   \n∥{0[2]}∥                                   \n∥{0[3]}∥                                   \n∥{0[4]}∥ \n∥{0[5]}∥\n∥{0[6]}∥\n∥{0[7]}＝＝＝⊐\n∥{0[8]}ノ\n∥{0[9]}ノ \n⊏＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝⊐".format(msg))

def say(msg,what):#dire des messages avec une décoration
	q=[]
	i=30
	prev=0
	while i<len(msg):
		while msg[i]!=' ':i-=1
		q.append(msg[prev:i])
		prev=i+1
		i+=30
	q.append(msg[prev:i])
	j=0
	while j<len(q):
		what(change(q[j:j+10]))
		j+=10

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
    Player.DEF*=2

def michael_sword_fun():
  if randint(1,10)==1: #10% de chance de doubler l'attaque
    Player.ATQ*=2

def trollking_shield_fun():
  if randint(1,4)==1: #25% de chance de ne pas recevoir de dégats <=> def=100
    Player.DEF=100

def conquerer_sword_fun(): # Conquerer's sword
  if len(Enemies)==1: #Si il n'y a qu'un seul ennemi
    Player.off_pow*=2


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


def writebonus(x):
  if type(x)==int:
    return '+'+str(x)
  if type(x)==list:# Si c'est une liste, c'est une fonction logique ahahahahahahahahahahahahahahahahahaha
    return x[1]

class Weapons: # définit toutes les armes du jeu
  def __init__(self,tier,name,description,bonus={}): # Pas forcément de bonus, d'ou le bonus={} (si aucune valeur n'est donnée, bonus sera {})
    '''Initialise ( __init__ ) les armes du jeu'''
    self.tier=tier
    self.name=name
    self.description=description
    self.bonus=bonus

  def info(self):# ex: Rare tier: Magical Tome {MP +5, ATQ +10} \n this weapon does emotional damage
    '''Donne les informations sur l'arme sous forme de GUI'''
    print(self.name+', Tier:',self.tier+'\n'+', '.join(tuple(': '.join((i,writebonus(self.bonus[i]))) for i in self.bonus))+'\n'+self.description)

Magical_Tome=Weapons(Rare_Tier,Magical_Tome_Name,Magical_Tome_Description,{'MP':5, 'ATQ':10}) #voir power-system.txt + dialogue_en.py


Wooden_Shield=Weapons(Common_Tier,Wooden_Shield_Name,Wooden_Shield_Description) #pas de bonus dans power-system.txt
Wooden_Sword=Weapons(Common_Tier,Wooden_Sword_Name,Wooden_Sword_Description)
Old_Grimoire=Weapons(Common_Tier,Old_Grimoire_Name,Old_Grimoire_Description)
Priest_Shield=Weapons(Rare_Tier,Priest_Shield_Name,Priest_Shield_Description,{'DEF':10})
Blacksmith_Sword=Weapons(Rare_Tier,Blacksmith_Sword_Name,Blacksmith_Sword_Description,{'STA':5,'ATQ':10})
# 'FUN': fonction qui s'applique à chaque attaque, dans Faith_Shield la défense à une chance sur 10 de doubler (ligne 21)
Faith_Shield=Weapons(Hero_Tier,Faith_Shield_Name,Faith_Shield_Description,{'DEF':25,'FUN':[faith_shield_fun,Faith_shield_fun_desc]})
Michael_Sword=Weapons(Hero_Tier,Michael_Sword_Name,Michael_Sword_Description,{'STA':20,'ATQ':40,'FUN':[michael_sword_fun,Michael_sword_fun_desc]})
Dantalion_Anti_Bible=Weapons(Hero_Tier,Dantalion_Anti_Bible_Name,Dantalion_Anti_Bible_Description,{'MP':20,'ATQ':10})
Troll_King_Shield=Weapons(Relic_Tier,Troll_King_Shield_Name,Troll_King_Shield_Description,{'DEF':35,'FUN':[trollking_shield_fun,Trollking_fun_desc]})
Conquerer_Sword=Weapons(Relic_Tier,Conquerer_Sword_Name,Conquerer_Sword_Description,{'STA':50,'ATQ':50,'FUN':[conquerer_sword_fun,Conquerer_Sword_fun_desc]})
Elf_King_Epitome=Weapons(Relic_Tier,Elf_King_Epitome_Name,Elf_King_Epitome_Description,{'MP':50,'ATQ':50,'FUN':[elfking_epitome_fun,Elfking_Epitome_fun_desc]})
Purgatory_Door=Weapons(Arcanic_Tier,Purgatory_Door_Name,Purgatory_Door_Description,{'DEF':50,'FUN':[purgatory_door_fun,Purgatory_Door_fun_desc]})
Divine_Light_Blade=Weapons(Arcanic_Tier,Divine_Light_Blade_Name,Divine_Light_Blade_Description,{'STA':75,'ATQ':100,'FUN':[divine_light_blade_fun,Divine_Light_Blade_fun_desc]})
Satan_Profecy=Weapons(Arcanic_Tier,Satan_Profecy_Name,Satan_Profecy_Description,{'MP':75,'ATQ':100,'FUN':[satan_profecy_fun,Satan_Profecy_fun_desc]})

try: #import basique de sauvegarde
  from saves import *
  Weapon=eval(Weapon)
except ModuleNotFoundError: #si non sauvegardé, pas de fichier de sauvegarde
  Weapon=''

from continuity import *

currentAction=0
print(Welcome)
def anal(q):
    global currentAction
    if q[:4]=='Desc':
        print(eval(q))
        currentAction=int(q.split('_')[1])
    elif q[:4]=='AskP':
        print('\t'.join(eval(q)))
        anal(eval('QOut'+q[4:])[int(eval(easter(input())))-1])

while True:
	anal(Next[currentAction])
