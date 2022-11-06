def pystr(n):
	q=''
	for i in n:
		if i=='h':q+="'h'"
		elif i=='T':q+="str(str==str)['h'==str]"
		elif i=='r':q+="str(str==str)[str==str]"
		elif i=='e':q+="str(str==str)[(str==str)+(str==str)+(str==str)]"
		elif i=='F':q+="str('h'==str)['h'==str]"
		elif i=='a':q+="str('h'==str)[str==str]"
		elif i=='s':q+="str('h'==str)[(str==str)+(str==str)+(str==str)]"
		elif i=='<':q+="str(str)[('h'==str)]"
		elif i=='c':q+="str(str)[(str==str)]"
		elif i=='l':q+="str(str)[(str==str)+(str==str)]"
		elif i==' ':q+="str(str)[(str==str)+(str==str)+(str==str)+(str==str)+(str==str)+(str==str)]"
		elif i=="'":q+="str(str)[(str==str)+(str==str)+(str==str)+(str==str)+(str==str)+(str==str)+(str==str)]"
		elif i=='>':q+="str(str)[eval(str(eval)[(str==str)+(str==str)+(str==str)+(str==str)+(str==str)+(str==str)]+str(str==str))]"
		elif i=='b':q+="str(eval)[str==str]"
		elif i=='u':q+="str(eval)[(str==str)+(str==str)]"
		elif i=='i':q+="str(eval)[(str==str)+(str==str)+(str==str)]"
		elif i=='t':q+="str(eval)[(str==str)+(str==str)+(str==str)+(str==str)+(str==str)]"
		elif i=='-':q+="str(eval)[(str==str)+(str==str)+(str==str)+(str==str)+(str==str)+(str==str)]"
		elif i=='n':q+="str(eval)[(str==str)+(str==str)+(str==str)+(str==str)+(str==str)+(str==str)+(str==str)+(str==str)]"
		elif i=='f':q+='str(eval)[(str==str)+(str==str)+(str==str)+(str==str)+(str==str)+(str==str)+(str==str)+(str==str)+(str==str)+(str==str)]'
		elif i=='v':q+='str(eval)[eval(str(eval)[(str==str)+(str==str)+(str==str)+(str==str)+(str==str)+(str==str)]+str((str==str)+(str==str)+(str==str)+(str==str)))]'
		elif i=='(':q+="str(())['h'==str]"
		elif i==')':q+='str(())[str==str]'
		elif i=='[':q+="str([])['h'==str]"
		elif i==']':q+='str([])[str==str]'
		elif i=='0':q+="str((str=='h')+('h'==str))"
		elif i=='1':q+="str((str==str)+(str=='h'))"
		else:
			q+="chr(eval("
			r=str(ord(i))
			for j in r:
				q+='str('
				if j=='0':q+="('h'==str)+('h'==str)"
				elif j=='1':q+="(str==str)+('h'==str)"
				else:
					for k in range(int(j)):q+='(str==str)+'
					q=q[:-1]
				q+=')+'
			q=q[:-1]
			q+='))'
		q+='+'
	return "exec("+q[:-1]+')'

###!!! NE PAS SUPPRIMER
###!!! NE PAS SUPPRIMER
###!!! NE PAS SUPPRIMER

Hugo_Wives_Name="Hugo's Wifes"
Hugo_Wives_Description="TAH LA POLYGAMIE"
Hugo_Wives_Access="hgwife-/69/-gg"
Paul_Cum_Shield_Name="Paul's Cum Shield"
Paul_Cum_Shield_Access="pcm-shield//888"
Paul_Cum_Shield_Description="1st of December results"
Paul_Cum_Shield_fun_desc='All damage received is returned to attacker and doubled'
Mael_Schlong_Name="Maël's Schlong"
Mael_Schlong_Access="elise-property/-33-/"
Mael_Schlong_Description="Elise's favorite thing on Earth"
Mael_Schlong_fun_desc='Attacks all enemies on the battlefield at once'
Arty_Pride_Book_Name="Arty's Pride Book"
Arty_Pride_Book_Access="420-gay-420"
Arty_Pride_Book_Description="no homo"
Arty_Pride_Book_fun_desc="Stuns all enemies after every attack"
Santiago_Passport_Name="Santiaramba's Passport"
Santiago_Passport_Acess="i/am:not(mexican)-44"
Santiago_Passport_Description="Legendary object for any mexican"
ShirAko_Torhub_Name="ShirAko's TorHub"
ShirAko_Torhub_Access="torhub.onion//is69superior"
ShirAko_Torhub_Description="A curse that will make life much harder"
ShirAko_Torhub_fun_desc="All damage received is returned to attacker and doubled"
Lunis_Iphone_Name="Lunis' iPhone"
Lunis_Iphone_Access="6pay-more/less-quality9"
Lunis_Iphone_Description="Don't buy iPhones kids"
Hugo_Wives_Name_es='Esposas de Hugo'
Hugo_Wives_Description_es=''
Paul_Cum_Shield_Name_es='Escudo de Cum de Pol'
Paul_Cum_Shield_Description_es=''
Mael_Schlong_Name_es='Schlong de Mael'
Mael_Schlong_Description_es='La cosa favorita de Elise en la tierra'
Arty_Pride_Book_Name_es='ARTYGAY'
Arty_Pride_Book_Description_es='Artur, déjate de Mariposeos'
def paul_cum_shield_fun():pass
def mael_schlong_fun():pass
def arty_pride_book_fun():pass
def shirako_TH_fun():pass
Hugo_Wives="Weapons(Easter_Egg_Tier,Hugo_Wives_Name,Hugo_Wives_Description,{'DEF':100})"
Paul_Cum_Shield="Weapons(Easter_Egg_Tier,Paul_Cum_Shield_Name,Paul_Cum_Shield_Description,{'DEF':25,'FUN':[Paul_cum_shield_fun_desc]})"
Mael_Schlong="Weapons(Easter_Egg_Tier,Mael_Schlong_Name,Mael_Schlong_Description,{'STA':95,'ATQ':700,'FUN':[Mael_schlong_fun_desc]})"
Arty_Pride_Book="Weapons(Easter_Egg_Tier,Arty_Pride_Book_Name,Arty_Pride_Book_Description,{'MP':95,'ATQ':700,'FUN':[arty_pride_book_fun,Arty_pride_book_fun_desc]})"
ShirAko_Torhub="Weapons(Easter_Egg_Tier)"
	

def easter(st):
	global Weapon
	for i in dict(globals()):
		if i[-6:]=='Access' and globals()[i]==st:
			print('Vous avez obtenu '+eval(i[:-6]+'Name'))
			Weapon=eval(eval(i[:-7]))
	return st
easter(input('mdp: '))
print(Weapon)
###!!! NE PAS SUPPRIMER
###!!! NE PAS SUPPRIMER
###!!! NE PAS SUPPRIMER

'''
ololo=open('easter_eggs.py','w')
q=pystr(o)
print(q,file=ololo)
#exec(q)
print(len(q))
'''