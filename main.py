## ! WELCOME TO TROLLAND !
## 🄯 Copyleft 2022 - All wrongs reversed to Lamereary Industries - ширАко and SoulTaker

try: #import basique de sauvegarde
  from saves import *
  Weapon=eval(Weapon)
except ModuleNotFoundError: #si non sauvegardé, pas de fichier de sauvegarde
  Weapon=''

class Weapons: #définit toutes les armes du jeu
  def __init__(self,tier,name,description,bonus=''): #Pas forcément de bonus
    self.tier=tier
    self.name=name
    self.description=description
    
  def info(self):# ex: Rare tier: Magical Tome {MP +5, ATQ +10} \n\t this weapon does emotional damage
    print(self.tier,' tier: ',self.name,', '.join(tuple(': +'.join((i,str(a[i]))) for i in a)), description) #flemme de commenter + peut être optimisé

 Magical_Tome=Weapons('Rare','Magical Tome','this weapon does emotional damage',{'MP':5, 'ATQ':10}) #voir power-system.txt
