# Fichier de traduction, différent pour dialogue_fr.py et dialogue_es.py

# Tiers des armes
common_Tier='Common'
rare_Tier='Rare'
hero_Tier='Heroic'
relic_Tier='Relic'
arcanic_Tier='Arcanic'
easter_Egg_Tier='Easter Egg'

# Les armes
wooden_Shield_Name='Wooden Shield'
wooden_Shield_Description="A wooden shield, doesn't seem very resistant."
wooden_Sword_Name='Wooden Sword'
wooden_Sword_Description="A wooden sword, it's shape is imperfect and it seems rough to use."
old_Grimoire_Name='Old Grimoire'
old_Grimoire_Description="A grimoire with unreadable characters an odd looking illustations. You feel a slight magical aura emanate from it."
priest_Shield_Name="Priest's Shield"
priest_Shield_Description="A shield with a cross on it and the church's emblem, it feels sturdy."
blacksmith_Sword_Name="Blacksmith's sword"
blacksmith_Sword_Description="A handforged sword engraved with the name of it's creator 'Hallburg Lyonkul'."
magical_Tome_Name='Magical Tome'
magical_Tome_Description="A book containing magic seals with their description, as well as multiple pages full of ancient texts. You feel strong magic on certain pages."
faith_Shield_Name='Shield of Faith'
faith_Shield_Description="A heavy shield made of wood and an unknown mineral, it seems like it could easily stop a blade. It's said to be stronger if your faith is strong."
faith_shield_fun_desc='Defence has a 10% chance to be doubled'
michael_Sword_Name="Michael's Sword"
michael_Sword_Description="A beautiful sword, made with a solid white metal, and decorated with gold. It's said to have belonged to an archangel."
michael_sword_fun_desc='Attack has a 10% chance to be doubled'
dantalion_Anti_Bible_Name="Dantalion's Anti-Bible"
dantalion_Anti_Bible_Description="A book filled with unreadable ancient characters written in blood. It's said to have been written by a powerful demon, in exchange for the lives of 7 humans."
troll_King_Shield_Name="Troll King's Shield"
troll_King_Shield_Description="A shield, resembling more a hunk of red mana-condensed Trollium, seemingly indestructible, which was used by the former Troll King."
trollking_fun_desc='Damage has a 25% chance to be ignored'
conquerer_Sword_Name="Conquerer's Sword"
conquerer_Sword_Description="A beautiful white sword crafted with holy metal into a seemingly perfect sword. It is beautifully engraved and decorated with perfectly balanced gems and red metal."
elf_King_Epitome_Name="Elf King's Epitome"
elf_King_Epitome_Description="A manuscript containing all the magical knowledge of the Elven Kingdom, condensed into a single gray stone tablet, with a mana-responsive enchanted screen. It lights up with red pure mana to display the seal of the spell about to be used."
purgatory_Door_Name="Purgatory's Door"
purgatory_Door_Description="An extremely powerful divine relic. This shield is said to have been crafted by higher forces when creating Purgatory to keep the vacant souls within, it is said to have been broken down by Satan during the Clash of the Above."
divine_Light_Blade_Name='Divine Blade of Light'
divine_Light_Blade_Description="An extremely powerful divine relic. The legends say this sword was created from God's left ring finger, it can cut through any non-divine material."
satan_Profecy_Name="Satan's Profecy"
satan_Profecy_Description="An extremely powerful divine relic. It contains half of Satan's knowledge within it, and contains an eternity of dark knowledge and magic."
hugo_Wives_Name="Hugo's Wifes"
hugo_Wives_Description="TAH LA POLYGAMIE"
paul_Cum_Shield_Name="Paul's Cum Shield"
paul_Cum_Shield_Description="1st of December results"
mael_Schlong_Name="Maël's Schlong"
mael_Schlong_Description="Elise's favorite thing on Earth"
arty_Pride_Book_Name="Arty's Pride Book"
arty_Pride_Book_Description="no homo"

welcome="Welcome to Trolland, this is a solely console high fantasy game with a cool storyline and a bunch of fights."


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
desc1_9_magicScience=""
desc1_8_history=""
desc1_7_holyGuide=""
qOut1_6_books=[desc1_7_holyGuide, desc1_8_history, desc1_9_magicScience]
askP1_5_books=['Read "The Holy Guide"', 'Read "History of Trolland"', 'Read "The Science of Magic"']
desc1_4_books="You see three heavy books"
qOut1_3_room=[a, desc1_4_books]
askP1_2_room=[default_ask, "Go downstairs", "Look at the books"]
desc1_1_room="You wake up in a dark room, you light a candle. You are home in your room, there are old books in the library on your left, and a staircase going down on your right."
