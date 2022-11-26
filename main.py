## ! WELCOME TO TROLLAND !
## © Copyright 2022 - All rights reserved to Lamereary Industries - ширАко and SoulTaker

from random import randint
from continuity import *

try:
  from pygame import mixer
  playmusic=True
  mixer.init()
  mixer.Channel(0).play(mixer.Sound('lol.mp3'))
  import os
  os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
except ModuleNotFoundError:
  print("Vous jouerez sans la musique, c'est dommage, installez le module pygame pour avoir la musique')
  playmusic=False

decobar='----------------------------------------'
print(decobar)
print('                SETUP')
try: #import basique de sauvegarde
  from saves import *
  print('Loading save...')
except ModuleNotFoundError: #si non sauvegardé, pas de fichier de sauvegarde
	print('No save detected')

lang=input('Enter language: ').lower() #demande la langue, puis met l'input en minuscule
if lang in ['es','español','espanol']:
  from dialogue_es import * #si c'est espa, importe les dialogues espa
elif lang in ['fr','français','francais']:
  from dialogue_fr import *
elif lang=='troll':
  from troll_fr import *
else: 
  from dialogue_en import * #Anglais par défaut

Username=input('Enter username: ')
print(decobar)

def center(q,what):
	'''centre un texte horizontalement'''
	while len(q)<10:
		q.append('')
		if len(q)<10:
			q.insert(0,'')#met des espaces avant et après le texte pour centrer
	for i in range(10):
		while len(q[i])<29+((i==8)*2+(i in [7,8,9]))*(what!=desc):
			q[i]+=' '
			if len(q[i])<29+((i==8)*2+(i in [7,8,9]))*(what!=desc):
				q[i]=' '+q[i]#rectifie par rapport au fait que les bulles ne soient pas carrées
	return q

def psay(who,msg):#bulle du Player say, on aurait pu faire ''' ''' mais si c'est reservé aux docstrings
	print(who+"\n       ⊏＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝⊐\n       ∥{0[0]}∥\n       ∥{0[1]}∥\n       ∥{0[2]}∥\n       ∥{0[3]}∥\n       ∥{0[4]}∥\n       ∥{0[5]}∥\n       ∥{0[6]}∥\n   ⊏＝＝{0[7]}∥\n    ＼{0[8]}∥\n      ＼{0[9]}∥\n        ⊏＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝⊐".format(msg))

def osay(who,msg):#other say
	print(who+"\n⊏＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝⊐\n∥{0[0]}∥                                  \n∥{0[1]}∥                                   \n∥{0[2]}∥                                   \n∥{0[3]}∥                                   \n∥{0[4]}∥ \n∥{0[5]}∥\n∥{0[6]}∥\n∥{0[7]}＝＝＝⊐\n∥{0[8]}ノ\n∥{0[9]}ノ \n⊏＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝⊐".format(msg))

def desc(who,msg):#description
	print('⊏＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝⊐\n∥{0[0]}∥                                  \n∥{0[1]}∥                                   \n∥{0[2]}∥                                   \n∥{0[3]}∥                                   \n∥{0[4]}∥ \n∥{0[5]}∥\n∥{0[6]}∥\n∥{0[7]}∥\n∥{0[8]}∥\n∥{0[9]}∥ \n⊏＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝＝⊐\n'.format(msg))

def say(msg,what,who=''):#dire des messages avec une décoration
	q=[]
	i=30
	prev=0
	while i<len(msg):
		while msg[i]!=' ':i-=1#ne pas couper un texte au milieu d'un mot
		q.append(msg[prev:i])
		prev=i+1
		i+=30
	q.append(msg[prev:i])#centre un texte verticalement
	j=0
	while j<len(q):
		what(who,center(q[j:j+10],what))#Faire plusieurs bulles en cas de texte trop long
		j+=10

def exit_game():
  '''Sort du jeu et sauvegarde dans saves.py''' 
  save=open('saves.py','w')
  print('currentAction='+str(currentAction),file=save)
  if Weapon!='':
    print('Weapon="'+list(globals())[list(globals().values()).index(Weapon)]+'"',file=save)
    print('Attack_Slots='+str([i.name for i in eval(list(globals())[list(globals().values()).index(Attack_Slots)])]),file=save)
  else:
    print("Weapon=''",file=save)
    print("Attack_Slots=''",file=save)
  quit()
  
def load():
  '''Charge le jeu comme PCB'''
  from saves import Weapon,Attack_Slots,currentAction
  global Weapon,Attack_Slots,currentAction
  if Weapon!='':
    Weapon=eval(Weapon)#de string à objet
  if Attack_Slots!='':
    Attack_Slots=[eval(i) for i in Attack_Slots]
  for i in Next:
    if 'Desc1_'+str(currentAction)+'_' in i:
      say(eval(i),desc)


def stats():
  '''Affiche les statistiques'''
  print(decobar)
  if Weapon!='':
    Weapon.info()#voir fonction info
    print(Generic_attackslots,'\t'.join([i.name for i in Attack_Slots]))
    print(decobar)
  else:
    print(Generic_weapon, Generic_none)
    print(Generic_attackslots, Generic_none)
    
def combat(desc,xp,enemies):
  '''Le nom n'explique pas son utilité?'''
  ennemy_bar='{0.name} | LVL: {0.LVL} | HP: {0.HP}/{0.HPMAX} \n----------------------------------\n|{1}| \n----------------------------------'
  print(desc)
  enemies=[eval(i) for i in enemies]#chaque ennemi converti de string en objet
  def turn():#combat au tour par tour, surement pas en temps réel
    for Enemy in enemies:#pour tous les ennemis:
      if Enemy.HP>0:
        print(ennemy_bar.format(Enemy,'■'*int(32*(Enemy.HP/Enemy.HPMAX))+'□'*int(32-32*(Enemy.HP/Enemy.HPMAX))))#lignes longues,on n'aime pas la PEP 8
        Player.HP-=Enemy.attack.fight(Player)#L'ennemi attaque
        if Player.HP<=0:
          print(Generic_youdied)#si votre HP<=0, vous êtes mort
          print(Generic_gameover)
          exit_game()
      else:print(Enemy.name,Generic_dead)#Si son HP<=0, l'ennemi est mort
      print(Enemy.name,Generic_attacks,Player.name,Generic_with,Enemy.attack.name,'!')#shirAko attacks PEP 8 with very long lines!
    print(ennemy_bar.format(Player,'■'*int(32*(Player.HP/Player.HPMAX))+'□'*int(32-32*(Player.HP/Player.HPMAX))))
    print('{0[0].name} | {0[1].name} | {0[2].name} |\n----------------------------------\n'.format(Attack_Slots))#slots d'attaques
    if len(enemies)>1:#S'il y a plus d'un ennemi, faire choisir au joueur la cible
      rep=input(Generic_target)
      while rep=='stats':#le joueur à tout de même le droit de voire ses statistiques
        stats()
        rep=input(Generic_target)
      if rep=='exit':#Le joueur peut quitter le jeu en le sauvegardant
        exit_game()
      while not rep.isdigit():
        rep=input(Generic_target)
      target=enemies[int(rep)-1]#choisit la cible
    else:
      target=enemies[0]#si il y a un seul ennemi, le joueur n'aura pas le choix
    pickattack='Attack: '+'\t'.join(['. '.join([str(i),Attack_Slots[i-1].name]) for i in range(1,len(Attack_Slots)+1)])+'\n'
    rep=input(pickattack)
    while rep=='stats':
      stats()
      rep=input(pickattack)
    if rep=='exit':
      exit_game()
    while not rep.isdigit() or int(rep)<1 or int(rep)>3:
      rep=input(pickattack)
    target.HP-=Attack_Slots[int(rep)-1].fight(target)#Finalement, vous attaquez
    print(Player.name,Generic_attacks,Enemy.name,Generic_with,Attack_Slots[int(rep)].name,'!')
    if all(i.HP<=0 for i in enemies):
      if playmusic:mixer.Channel(0).play(mixer.Sound('hall.mp3'))
      print(Generic_win)#GG
      return
    return 1
  while turn():
    pass
		
class Attacks:
	def __init__(self,name,fight):#fight est une function
		self.name=name
		self.fight=fight

Flame=Attacks('Flame',lambda x:x.HPMAX//2)#Fait des dégats de la moitié de l'HPMAX
Slash=Attacks('Slash',lambda x:x.HPMAX//2)
Smash=Attacks('Smash',lambda x:3*x.HPMAX//10)#fait 30% de l'HPMAX de dégats

class Entities: # définit toutes les entités du jeu (joueur, enemis..)
	def __init__(self,name,DEF,ATQ,HPMAX,MP,STA,LVL,attack=''):#certaines entités n'ont pas d'attaque prédéfinie
		self.name=name
		self.DEF=DEF
		self.ATQ=ATQ
		self.HP=HPMAX
		self.HPMAX=HPMAX
		self.MP=MP
		self.STA=STA
		self.LVL=LVL
		self.attack=attack

Player=Entities(Username,0,10,20,0,0,1)#Vous
Troll1=Entities(Troll1_name,0,6,100,0,0,'??',Smash)#Premier ennemi
Troll1.HP=6#affaiblissement

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

def writebonus(x):# écrit les bonus
  if type(x)==int:
    return '+'+str(x)
  if type(x)==list:
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

Wooden_Shield=Weapons(Common_Tier,Wooden_Shield_Name,Wooden_Shield_Description) #pas de bonus
Wooden_Sword=Weapons(Common_Tier,Wooden_Sword_Name,Wooden_Sword_Description)
Old_Grimoire=Weapons(Common_Tier,Old_Grimoire_Name,Old_Grimoire_Description)
Priest_Shield=Weapons(Rare_Tier,Priest_Shield_Name,Priest_Shield_Description,{'DEF':10})
Blacksmith_Sword=Weapons(Rare_Tier,Blacksmith_Sword_Name,Blacksmith_Sword_Description,{'STA':5,'ATQ':10})
Magical_Tome=Weapons(Rare_Tier,Magical_Tome_Name,Magical_Tome_Description,{'MP':5, 'ATQ':10})
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
Justice_Sword=Weapons(Monster_Tier,Justice_Sword_Name,Justice_Sword_Description)

#from easter_eggs import *

try: #import basique de sauvegarde
  load()
except ModuleNotFoundError: #si non sauvegardé, pas de fichier de sauvegarde
  print(Welcome)
  Weapon=''
  Attack_Slots=['']*3
  currentAction=0

Generic_gameover="   _____                                                              _ \n  / ____|                                                            | |\n | |  __    __ _   _ __ ___     ___      ___   __   __   ___   _ __  | |\n | | |_ |  / _` | | '_ ` _ \\   / _ \\    / _ \\  \\ \\ / /  / _ \\ | '__| | |\n | |__| | | (_| | | | | | | | |  __/   | (_) |  \\ V /  |  __/ | |    |_|\n  \\_____|  \\__,_| |_| |_| |_|  \\___|    \\___/    \\_/    \\___| |_|    (_)"

def analyse(q):
    '''Analyse les types d'action de dialogue.py'''
    global currentAction
    if q[:4]=='Desc':
        say(eval(q),desc)
        currentAction=int(q.split('_')[1])#voir continuity.py
    elif q[:4]=='AskP':
        print()
        print(eval(q)[0],end='\t')#la question
        rep=input('\t'.join(['. '.join([str(i),eval(q)[i]]) for i in range(1,len(eval(q)))])+'\n').lower()#met des nombres avec les options
        #easter(rep)
        while rep=='stats':
          print('Your stats:')
          stats()
          return 1
        if rep in ['exit','quit','quitter','sortir','salir']:
          exit_game()
        if rep in ['load','charger','cargar']:
          try:
            print(Generic_loading)
            load()
          except ModuleNotFoundError:
            print(Generic_nosave)
        else:
          try:
            return analyse(eval('QOut'+q[4:])[int(rep)-1])
          except:
            print(Not_Accepted)
    elif q[:4]=='PSay':
      currentAction=int(q.split('_')[1])
      say(eval(q),psay,Player.name)
    elif q[:4]=='OSay':
      currentAction=int(q.split('_')[1])
      say(eval(eval(q)[1]),osay,eval(q)[0])
    elif q[:4]=='Cmbt':
      if playmusic:mixer.Channel(0).play(mixer.Sound('raid.mp3'))
      combat(*eval(q))
      currentAction=int(q.split('_')[1])
    elif q[:4]=='SetV':
      currentAction=int(q.split('_')[1])
      exec(eval(q)[0]+'='+eval(q)[1],globals())
    elif q[:4]=='EndG':
      print(eval(q))
      print(Generic_gameover)
      return
    return 1

while analyse(Next[currentAction]):
  input()#attendre l'input de l'utilisateur pour continuer
