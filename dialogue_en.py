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
Wooden_Shield_Description="A wooden shield, doesn't seem very resistant."
Wooden_Sword_Name='Wooden Sword'
Wooden_Sword_Description="A wooden sword, it's shape is imperfect and it seems rough to use."
Old_Grimoire_Name='Old Grimoire'
Old_Grimoire_Description="A grimoire with unreadable characters an odd looking illustations. You feel a slight magical aura emanate from it."
Priest_Shield_Name="Priest's Shield"
Priest_Shield_Description="A shield with a cross on it and the church's emblem, it feels sturdy."
Blacksmith_Sword_Name="Blacksmith's sword"
Blacksmith_Sword_Description="A handforged sword engraved with the name of it's creator 'Hallburg Lyonkul'."
Magical_Tome_Name='Magical Tome'
Magical_Tome_Description="A book containing magic seals with their description, as well as multiple pages full of ancient texts. You feel strong magic on certain pages."
Faith_Shield_Name='Shield of Faith'
Faith_Shield_Description="A heavy shield made of wood and an unknown mineral, it seems like it could easily stop a blade. It's said to be stronger if your faith is strong."
Michael_Sword_Name="Michael's Sword"
Michael_Sword_Descripion="A beautiful sword, made with a solid white metal, and decorated with gold. It's said to have belonged to an archangel."
Dantalion_Anti_Bible_Name="Dantalion's Anti-Bible"
Dantalion_Anti_Bible_Description="A book filled with unreadable ancient characters written in blood. It's said to have been written by a powerful demon, in exchange for the lives of 7 humans."
Troll_King_Shield_Name="Troll King's Shield"
Troll_King_Shield_Description="A shield, ressembling more a hunk of red mana-condensed Trollium, seemingly indestructible, which was used by the former Troll King."
Conquerer_Sword_Name="Conquerer's Sword"
Conquerer_Sword_Description="A beautiful white sword crafted with holy metal into a seemingly perfect sword. It is beautifully engraved and decorated with perfectly balanced gems and red metal."
Elf_King_Epitome_Name="Elf King's Epitome"
Elf_King_Epitome_Description="A manuscript containing all the magical knowledge of the Elven Kingdom, condensed into a single gray stone tablet, with a mana-responsive enchanted screen. It lights up with red pure mana to display the seal of the spell about to be used."
Purgatory_Door_Name="Purgatory's Door"
Purgatory_Door_Description="An extremely powerful divine relic. This shield is said to have been crafted by higher forces when creating Purgatory to keep the vacant souls within, it is said to have been broken down by Satan during the Clash of the Above."
Divine_Light_Blade_Name='Divine Blade of Light'
Divine_Light_Blade_Description="An extremely powerful divine relic. The legends say this sword was created from God's left ring finger, it can cut through any non-divine material."
Satan_Profecy_Name="Satan's Profecy"
Satan_Profecy_Description="An extremely powerful divine relic. It contains half of Satan's knowledge within it, and contains an eternity of dark knowledge and magic."
Hugo_Wives_Name="Hugo's Wifes"
Hugo_Wives_Description="TAH LA POLYGAMIE"
Paul_Cum_Shield_Name="Paul's Cum Shield"
Paul_Cum_Shield_Description="1st of December results"
Mael_Schlong_Name="Maël's Schlong"
Mael_Schlong_Description="Elise's favorite thing on Earth"
Arty_Pride_Book_Name="Arty's Pride Book"
Arty_Pride_Book_Description="no homo"

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
