# Fichier de traduction, différent pour dialogue_fr.py et dialogue_es.py

# Tiers des armes
Common_Tier='Common'
Rare_Tier='Rare'
Hero_Tier='Heroic'
Relic_Tier='Relic'
Arcanic_Tier='Arcanic'
Easter_Egg_Tier='Easter Egg'

# Les armes
Wooden_Shield_Name='Wooden Shield'
Wooden_Shield_Description=''
Wooden_Sword_Name='Wooden Sword'
Wooden_Sword_Description=''
Old_Grimoire_Name='Old Grimoire'
Old_Grimoire_Description=''
Priest_Shield_Name="Priest's Shield"
Priest_Shield_Description=''
Blacksmith_Sword_Name="Blacksmith's sword"
Blacksmith_Sword_Description=''
Magical_Tome_Name='Magical Tome'
Magical_Tome_Description=''
Faith_Shield_Name='Shield of Faith'
Faith_Shield_Description=''
Michael_Sword_Name="Michael's Sword"
Michael_Sword_Descripion=''
Dantalion_Anti_Bible_Name="Dantalion's Anti-Bible"
Dantalion_Anti_Bible_Description=''
Troll_King_Shield_Name="Troll King's Shield"
Troll_King_Shield_Description=''
Conquerer_Sword_Name="Conquerer's Sword"
Conquerer_Sword_Description=''
Elf_King_Epitome_Name="Elf King's Epitome"
Elf_King_Epitome_Description=''
Purgatory_Door_Name="Purgatory's Door"
Purgatory_Door_Description=''
Divine_Light_Blade_Name='Divine Blade of Light'
Divine_Light_Blade_Description=''
Satan_Profecy_Name="Satan's Profecy"
Satan_Profecy_Description=''
Hugo_Wives_Name="Hugo's Wifes"
Hugo_Wives_Description=''
Paul_Cum_Shield_Name="Paul's Cum Shield"
Paul_Cum_Shield_Description=''
Mael_Schlong_Name="Maël's Schlong"
Mael_Schlong_Description=''
Arty_Pride_Book_Name="Arty's Pride Book"
Arty_Pride_Book_Description=''

Welcome="Welcome to Trolland, this is a solely console high fantasy game with a cool storyline and a bunch of fights."


#ACTION TYPES :

#"desc" - description - (x) - console talking to player, decribing environment
#"oSay" - other Say - (a,b) - character talking, content 
#"pSay" - player Say - (a) - main character speaking 
#"cmbt" - combat - (a,[b]) - fight description, opponent list
#"askP" - ask Player - (a, b, c, d, e) - prompt description, options (1:4) : can be undefined
#"qOut" - question Output - (a, b, c, d) - outputs (1:4) of question w same desc and index

#VAR NAME : (act-type + chapter + global index + action description) - ex : pSay1_12_artur-nul="artur est VRAIMENT nul"

# /copy 
#askP1_x_y=[default_ask, "a", "b", "c", "d"]
#qOut1_x_y=[a, b, c, d]

default_ask="What do you chose to do?"

#ARC 1 : Tutorial Village 

desc1_1_room="You wake up in a dark room, you light a candle. You are home in your room, there are old books in the library on your left, and a staircase going down on your right."
askP1_2_room=[default_ask, "Go downstairs", "Look at the  books"]
qOut1_3_room=[a, desc1_4_books]

desc1_4_books="You see three heavy books"
askP1_5_books=["Read  \"The Holy Guide \"", "Read \"History of Trolland\"", "Read \"The Science of Magic\""]
qOut1_6_books=[desc1_7_holyGuide, desc1_8_history, desc1_9_magicScience]
desc1_7_holyGuide=""
desc1_8_history=""
desc1_9_magicScience=""
