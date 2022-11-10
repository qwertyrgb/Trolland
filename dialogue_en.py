# Fichier de traduction, différent pour dialogue_fr.py et dialogue_es.py

# Tiers des armes
Common_Tier='Common'
Rare_Tier='Rare'
Hero_Tier='Heroic'
Relic_Tier='Relic'
Arcanic_Tier='Arcanic'
Easter_Egg_Tier='Easter Egg'
Monster_Tier='Monster'

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
Faith_shield_fun_desc='Defence has a 10% chance to be doubled'
Michael_Sword_Name="Michael's Sword"
Michael_Sword_Description="A beautiful sword, made with a solid white metal, and decorated with gold. It's said to have belonged to an archangel."
Michael_sword_fun_desc='Attack has a 10% chance to be doubled'
Dantalion_Anti_Bible_Name="Dantalion's Anti-Bible"
Dantalion_Anti_Bible_Description="A book filled with unreadable ancient characters written in blood. It's said to have been written by a powerful demon, in exchange for the lives of 7 humans."
Troll_King_Shield_Name="Troll King's Shield"
Troll_King_Shield_Description="A shield, resembling more a hunk of red mana-condensed Trollium, seemingly indestructible, which was used by the former Troll King."
Trollking_fun_desc='Damage has a 25% chance to be ignored'
Conquerer_Sword_Name="Conquerer's Sword"
Conquerer_Sword_Description="A beautiful white sword crafted with holy metal into a seemingly perfect sword. It is beautifully engraved and decorated with perfectly balanced gems and red metal."
Conquerer_Sword_fun_desc='If there is a single enemy, damage is doubled.'
Elf_King_Epitome_Name="Elf King's Epitome"
Elf_King_Epitome_Description="A manuscript containing all the magical knowledge of the Elven Kingdom, condensed into a single gray stone tablet, with a mana-responsive enchanted screen. It lights up with red pure mana to display the seal of the spell about to be used."
Elfking_Epitome_fun_desc='If there are multiple enemies, all enemies in battle have a 25% chance to be stunned'
Purgatory_Door_Name="Purgatory's Door"
Purgatory_Door_Description="An extremely powerful divine relic. This shield is said to have been crafted by higher forces when creating Purgatory to keep the vacant souls within, it is said to have been broken down by Satan during the Clash of the Above."
Purgatory_Door_fun_desc='Will return 20% of the damage to the attacker'
Divine_Light_Blade_Name='Divine Blade of Light'
Divine_Light_Blade_Description="An extremely powerful divine relic. The legends say this sword was created from God's left ring finger, it can cut through any non-divine material."
Divine_Light_Blade_fun_desc='Damage is doubled if attacker has more than 50% HP left'
Satan_Profecy_Name="Satan's Profecy"
Satan_Profecy_Description="An extremely powerful divine relic. It contains half of Satan's knowledge within it, and contains an eternity of dark knowledge and magic."
Satan_Profecy_fun_desc='Inflicts curse on attacked that drains 20% of their MAX_HP per turn'
Justice_Sword_Name='Sword of Justice'
Justice_Sword_Description='The sword of the Troll'

Welcome="Welcome to Trolland, this is a solely console high fantasy game with a cool storyline and a bunch of fights."


#ACTION TYPES :

#"Desc" - Description - (x) - console talking to player, decribing environment
#"OSay" - Other Say - (a,b) - character talking, content 
#"PSay" - Player Say - (a) - main character speaking 
#"Cmbt" - Combat - (a, b, [c]) - fight description, XP gained if fight is won, opponent list
#"AskP" - Ask Player - (a, b, c, d, e) - prompt description, options (1:4) : can be undefined

#"QOut" - Question Output - (a, b, c, d) - outputs (1:4) of question w same desc and index

#VAR NAME : (act-type + chapter + global index + action description) - ex : PSay1_12_artur-nul="artur est VRAIMENT nul"

# /copy 
#AskP1_x_y=[Default_ask, "a", "b", "c", "d"]
#QOut1_x_y=[a, b, c, d]

Default_ask="What do you chose to do?"

#ARC 1 : Tutorial Village 
Desc1_1_room="You wake up in a dark room, you light a candle. You are home in your room, there are old books in the library on your left, and a staircase going down on your right."
AskP1_room=[Default_ask, "Go downstairs", "Look at the books"]

Desc1_4_books="You see three heavy books"
AskP1_books=[Default_ask,'Read "The Holy Guide"', 'Read "History of Trolland"', 'Read "The Science of Magic"', "Exit"]
Desc1_5_holyGuide="You have to kill the Troll king"
Desc1_6_history="One day, a troll more intelligent than the others created the elves Sylvain Durif in order to destroy the earth"
Desc1_7_magicScience="For magic stuff, go buy mana"

QOut1_books=["Desc1_5_holyGuide", "Desc1_6_history", "Desc1_7_magicScience", "AskP1_room"]

Desc1_2_downstairs="You go down the old, creaky wooden stairs as a warm, welcoming living room reveals itself to your eyes. It's small, yet full of benevolance. You notice your mother isn't there. You see a note on the table, next to a fresh pot of blood colored lilies"
Desc1_3_note="The note reads : \"Finally up :D ? I'm going to buy mana charges downtown, be back home soon. Love, Mom <3\""
AskP1_downstairs=[Default_ask, "Go outside", "Go back upstairs", "Look around"]
Desc1_10_backUpstairs="You go back up the stairs, and arrive in your bedroom"
Desc1_11_lookAround="To your right is stone fireplace, with, above it a brick chimnee, and no fire within it, in front of it is a leather sofa, facing towards it with a low table. The house is decorated with sketches of trees hung up on the wall, one catches your attention, it shows a deer walking through the dense forest, you seem to percieve a faint silhouette drawn behind it, though it may just be your imagination. On your left is the kitchen, with next to it the door to your mother's bedroom."
Desc1_12_backInside="You go back inside, but the house is shaking, it seems very unsafe, you exit the house for now. You come back outside and the screams continue."
AskP1_backOutside=[Default_ask, "Run towards the screams", "Run in the direction opposite to the screams"]

QOut1_room=["Desc1_2_downstairs", "Desc1_4_books"]

Desc1_8_outside="You go through the large, dark, oak door and arrive on a gravel field, surrounded with tall green grass. You take a deep breath as you feel the grass-odored air freshen your lungs. Around yours are a number of similar looking houses, with small houses and bright flowers in their lawn. You see a child playing in the house in front of yours, how innocent he looks..."
Desc1_9_boom="A sudden flash of light blinds your eyes, followed by a deafening detonation and shock wave, making you lose balance and fall back. You hear screams through the ringing of your ears coming from South-East : that's where the mana store is !"
AskP1_boom=[Default_ask, "Go back inside the house", "Run towards the mana store", "Run in the direction opposite to the sound"]

QOut1_downstairs=["Desc1_8_outside", "Desc1_10_backUpstairs", "Desc1_11_lookAround"]

Desc1_13_runScreams="You run towards the screams, and seem to distinguish a silhouette towards the end of the street."
OSay1_14_momScream=["Unknown","'AAAAAAAAAAAAHHH, SOMEONE, ANYONE HELP ME PLEASE, I BEG OF YOU!'"]
Desc1_15_isThat="That's your mother voice! As you run closer, you distinguish her more clearly, there's no doubt, that's her."
PSay1_16_mom="MOM !"
OSay1_17_dontCome=["Mom",'"NO !!! {0} don\'t come near me!".format(Player.name)']
Desc1_18_momDead="Another person appears behind her, wait, no, that's no person... THAT'S A TROLL ! He raises his giant fist, and crushes your agonising mother under it, without even using his sword."
OSay1_19_trollSpeak=["Troll", "'GWWWWA-HWA-HWA-HWA, HOOMAN SPRLOOF! OH! HOOMAN!!'"]
Desc1_20_chased="The troll sees you, and starts walking towards you."
AskP1_chased=[Default_ask, "Run away", "Face the troll"]
EndG1_troll="The troll crushes you with his fist."
Desc1_21_runTroll="You run in the opposite direction as fast as you can. The vision of a pool of blood with what you could assume to be human remains strikes your eyes despite their shield of tears. In an attempt to lose the beast slowly approaching behind you, you take a turn left. You see an old man, still, but completely undamaged."

Desc1_22_runOpposite="You run in a direction, turning everytime you hear the screams get louder, left, and then left again. You see an old man, standing still, unphased, and completely undamaged."

OSay1_23_kamisaGo=["Kamisa", "Child. Go inside this house, choose a weapon for your adventure. And fight."]
Desc1_24_Insinct="For an odd reason, you do not question him a second. You enter the house and see three weapons : an old Grimoire, a wooden sword, a wooden shield. You have a feeling once you chose a weapon, you can never go back."
AskP1_weaponChoice=["Which one do you prefer ?", "The Sword", "The Shield", "The Magical Book"]

SetV1_25_sword=["WEAP", "Wooden_Sword"]
SetV1_26_shield=["WEAP", "Wooden_Shield"]
SetV1_27_book=["WEAP", "Old_Grimoire"]

OSay1_28_kamisaFight=["Kamisa", "Trolls may be, in normal times, the most dangerous being within this realm, but you can beat him. I'll help you, hero. He cannot kill you, his weapon will only take a fraction of your life, terrifying if you possess much, but for a weakling like you, it is a blessing. I'll weaken him, you finish it off."
Desc1_29_preFight="A bright flash of light forces your eyes closed, and once you open them, the troll seems near death."
Cmbt1_30_troll=['You rush towards the troll, and engage combat.',10,['Troll1']]
Desc1_31_hide="The troll is dead. No old man. Old man dead ? You must hide. Hide within the house. You are hidden within the house."
Desc1_32_wait="You wait for minutes, hours, or even maybe days. You hide until you hear nothing, nothing but silence. Then you open the door, and see ashes, nothing left of such a grand city but ashes. Except the single house you were staying in, completely untouched. You go out, look around, nothing but the smell of burnt blood. You look behind you, the house is gone. You drop down on your knees."
PSay1_33_alone="Why..? Why am I alive ? WHY AM I ALIVE ?? I hate them. I'll kill all of them. Every single one of them. I'LL OBLITERATE EVERY TROLL ON THIS PLANET !"
EndG1_demoOver="END, for now. The rest coming soon"

QOut1_weaponChoice=["SetV1_25_sword", "SetV1_26_shield", "SetV1_27_book"]
QOut1_chased=["Desc1_21_runTroll", "EndG1_troll"]
QOut1_boom=["Desc1_12_backInside", "Desc1_13_runScreams", "Desc1_22_runOpposite"]
QOut1_backOutside=["Desc1_13_runScreams", "Desc1_22_runOpposite"]


