# Fichier de traduction, différent pour dialogue_fr.py et dialogue_en.py

# Tiers des armes
Common_Tier='Común'
Rare_Tier='Raro'
Hero_Tier='Heroico'
Relic_Tier='Reliquia'
Arcanic_Tier='Arcánico'
Easter_Egg_Tier='Easter Egg'
Monster_Tier='Monstruo'

# Les armes
Wooden_Shield_Name='Escudo de Madera'
Wooden_Shield_Description='Un escudo de madera, no parece muy resistente.'
Wooden_Sword_Name='Espada de Madera'
Wooden_Sword_Description='Una espada de madera, su forma es imperfecta y parece difícil de usar.'
Old_Grimoire_Name='Viejo Grimorio'
Old_Grimoire_Description='Un grimorio con carácterer illegibles e ilustraciones extrañas. Usted siente una ligera aura mágica emanar de esta.'
Priest_Shield_Name='Escudo del Sacerdote'
Priest_Shield_Description='Un escudo con una cruz en él y el emblema de la iglesia, parece robusto.'
Blacksmith_Sword_Name='Espada del Herrero'
Blacksmith_Sword_Description="Una espada forjada a mano grabada con el nombre de su creador 'Hallburg Lyonkul'."
Magical_Tome_Name='Tomo Mágico'
Magical_Tome_Description='Un libro que contiene sellos mágicos con su descripción, así como múltiples páginas llenas de textos antiguos. Usted siente magia fuerte en algunas páginas.'
Faith_Shield_Name='Escudo de la Fe'
Faith_Shield_Description='Un escudo pesado hecho de madera y de un mineral desconocido, parece que podría fácilmente parar una cuchilla. Se dice que cuanto mayor sea su fe, más poderoso será el escudo.'
Faith_shield_fun_desc='Defence has a 10% chance to be doubled'######## OHOH
Michael_Sword_Name='Espada de Michael'
Michael_Sword_Description='Una espada magnífica, hecha con un sólido metal blanco y decorada con oro. Se dice que perteneció a un arcángel.'
Michael_sword_fun_desc='Attack has a 10% chance to be doubled'
Dantalion_Anti_Bible_Name='Anti-Biblia de Dantalión'
Dantalion_Anti_Bible_Description=''
Troll_King_Shield_Name='Escudo del Rey Troll'
Troll_King_Shield_Description=''
Trollking_fun_desc='Damage has a 25% chance to be ignored'
Conquerer_Sword_Name='Espada del Conquistador'
Conquerer_Sword_Description=''
Conquerer_Sword_fun_desc='If there is a single enemy, damage is doubled.'
Elf_King_Epitome_Name='NiReputisimaIdea'
Elf_King_Epitome_Description=''
Elfking_Epitome_fun_desc='If there are multiple enemies, all enemies in battle have a 25% chance to be stunned'
Purgatory_Door_Name='Puerta del Purgatorio'
Purgatory_Door_Description=''
Purgatory_Door_fun_desc='Will return 20% of the damage to the attacker'
Divine_Light_Blade_Name='Cuchilla Divina de Luz'
Divine_Light_Blade_Description=''
Divine_Light_Blade_fun_desc='Damage is doubled if attacker has more than 50% HP left'
Satan_Profecy_Name='Profecía de Satanás'
Satan_Profecy_Description=''
Satan_Profecy_fun_desc='Inflicts curse on attacked that drains 20% of their MAX_HP per turn'
Justice_Sword_Name='Sword of Justice'
Justice_Sword_Description='The sword of the Troll'

#generic messages
Welcome="Bienvenido a Trolland, este es un juego de alta fantasía exclusivo para consola con una historia genial y muchas, muchas peleas."
Generic_youdied='Ha muerto! :('
Generic_dead='Muerto'
Generic_target='Objetivo'
Generic_win='Mató a todos los enemigos y ganó el combate!'
Generic_attacks='attaca a '
Generic_with='con'
Generic_weapon='Armo:'
Generic_attackslots='Espacios de ataque:'
Generic_none='Ninguno'
Generic_loading='Loading last checkpoint...'
Generic_nosave='No se encontró archivo de guardado'

Troll1_name='Troll herido'

Default_ask="Que decide hacer?"
Not_Accepted='Respuesta no acceptada'
#ARC 1 : Tutorial Village 

Desc1_1_room="Usted se levanta en una habitación oscura, enciende una vela. Está en casa en su habitación, hay viejos libros en la estantería a su izquierda y unas escaleras bajando a su derecha."
AskP1_room=[Default_ask, "Bajar por las escaleras", "Mirar los libros"]

Desc1_4_books="Ve tres libros pesados"
AskP1_books=[Default_ask,'Leer "La Guía Sagrada"', 'Leer "Historia de Trolland"', 'Leer "La Ciencia de la Magia"', 'Salir']
Desc1_5_holyGuide="Mate al Troll."
Desc1_6_history="Un día, Sylvain Durif destruirá la Tierra."
Desc1_7_magicScience="Para cosas mágicas, vaya a a comprar maná."

QOut1_books=["Desc1_5_holyGuide", "Desc1_6_history", "Desc1_7_magicScience", "AskP1_room"]

Desc1_2_downstairs="Baja por las viejas escaleras chirriantes de madera mientras una cálida sala de estar acogedora se revela a sus ojos. Es pequeña, pero llena de benevolencia. Usted se da cuenta de que su madre no está. Ve una nota en la mesa, al lado de una maceta fresca de lirios color sangre."
Desc1_3_note="La nota dice: \"¿Al fin te has levantado :D ? Voy a comprar cargas de maná a la ciudad, volveré a casa pronto. Te quiero, Mamá <3\""
AskP1_downstairs=[Default_ask, "Ir fuera", "Volver arriba", "Mirar alrededor"]
Desc1_10_backUpstairs="Sube las escaleras y llega a su cuarto."
Desc1_11_lookAround="A su derecha está un hogar de piedra, con una chimenea de ladrillo encima y sin fuego en su interior, frente a él está un sofá de cuero, mirando hacia él con una mesa baja. La casa está decorada con garabatos de árboles colgados a la pared, uno le llama la atención, muestra un ciervo caminando por el denso bosque, le parece percibir una tenue silueta dibujada detrás de él, aunque puede que solo sea su imaginación. A su izquierda está la cocina, con al lado la puerta del dormitorio de su madre."
Desc1_12_backInside="You go back inside, but the house is shaking, it seems very unsafe, you exit the house for now. You come back outside and the screams continue."
AskP1_backOutside=[Default_ask, "Run towards the screams", "Run in the direction opposite to the screams"]

QOut1_room=["Desc1_2_downstairs", "Desc1_4_books"]

Desc1_8_outside="You go through the large, dark, oak door and arrive on a gravel field, surrounded with tall green grass. You take a deep breath as you feel the grass-odored air freshen your lungs. Around yours are a number of similar looking houses, with small houses and bright flowers in their lawn. You see a child playing in the house in front of yours, how innocent he looks..."
Desc1_9_boom="A sudden flash of light blinds your eyes, followed by a deafening detonation and shock wave, making you lose balance and fall back. You hear screams through the ringing of your ears coming from South-East : that's where the mana store is !"
AskP1_boom=[Default_ask, "Go back inside the house", "Run towards the mana store", "Run in the direction opposite to the sound"]

QOut1_downstairs=["Desc1_8_outside", "Desc1_10_backUpstairs", "Desc1_11_lookAround"]

Desc1_13_runScreams="You run towards the screams, and seem to distinguish a silhouette towards the end of the street."
OSay1_14_momScream=["Unknown","'AAAAAAAAAAAAHHH, SOMEONE, ANYONE HELP ME PLEASE, I BEG OF YOU!'"]
Desc1_15_isThatSooo="That's your mother voice! As you run closer, you distinguish her more clearly, there's no doubt, that's her."
PSay1_16_mom="MOM !"
OSay1_17_dontCome=["Mom",'"NO !!! {0}, don\'t come near me!".format(Player.name)']
Desc1_18_momDead="Another person appears behind her, wait, no, that's no person... THAT'S A TROLL ! He raises his giant fist, and crushes your agonising mother under it, without even using his sword."
OSay1_19_trollSpeak=["Troll", "'GWWWWA-HWA-HWA-HWA, HOOMAN SPRLOOF! OH! HOOMAN!!'"]
Desc1_20_chased="The troll sees you, and starts walking towards you."
AskP1_chased=[Default_ask, "Run away", "Face the troll"]
EndG1_troll="The troll crushes you with his fist."
Desc1_21_runTroll="You run in the opposite direction as fast as you can. The vision of a pool of blood with what you could assume to be human remains strikes your eyes despite their shield of tears. In an attempt to lose the beast slowly approaching behind you, you take a turn left. You see an old man, still, but completely undamaged."

Desc1_22_runOpposite="You run in a direction, turning every time you hear the screams get louder, left, and then left again. You see an old man, standing still, unphased, and completely undamaged."

OSay1_23_kamisaGo=["Kamisa", '"Child. Go inside this house, choose a weapon for your adventure. And fight."']
Desc1_24_Insinct="For an odd reason, you do not question him a second. You enter the house and see three weapons : an old Grimoire, a wooden sword, a wooden shield. You have a feeling once you choose a weapon, you can never go back."
AskP1_weaponChoice=["Which one do you prefer ?", "The Sword", "The Shield", "The Magical Book"]

SetV1_25_sword=["Weapon", "Wooden_Sword"]
SetV1_26_shield=["Weapon", "Wooden_Shield"]
SetV1_27_book=["Weapon", "Old_Grimoire"]
SetV1_34_slash=["Attack_Slots", "[Slash]*3"]
SetV1_35_flame=["Attack_Slots", "[Flame]*3"]

OSay1_28_kamisaFight=["Kamisa", '"Trolls may be, in normal times, the most dangerous being within this realm, but you can beat him. I\'ll help you, hero. He cannot kill you, his weapon will only take a fraction of your life, terrifying if you possess much, but for a weakling like you, it is a blessing. I\'ll weaken him, you finish it off."']
Desc1_29_preFight="A bright flash of light forces your eyes closed, and once you open them, the troll seems near death."
Cmbt1_30_troll=['You rush towards the troll, and engage combat.',10,['Troll1']]
Desc1_31_hide="The troll is dead. No old man. Old man dead ? You must hide. Hide within the house. You are hidden within the house."
Desc1_32_wait="You wait for minutes, hours, or even maybe days. You hide until you hear nothing, nothing but silence. Then you open the door, and see ashes, nothing left of such a grand city but ashes. Except the single house you were staying in, completely untouched. You go out, look around, nothing but the smell of burnt blood. You look behind you, the house is gone. You drop down on your knees."
PSay1_33_alone="Why..? Why am I alive ? WHY AM I ALIVE ‽‽ I hate them. I'll kill all of them. Every single one of them. I'LL OBLITERATE EVERY TROLL ON THIS PLANET !"
EndG1_demoOver="END, for now. The rest coming soon"

QOut1_weaponChoice=["SetV1_25_sword", "SetV1_26_shield", "SetV1_27_book"]
QOut1_chased=["Desc1_21_runTroll", "EndG1_troll"]
QOut1_boom=["Desc1_12_backInside", "Desc1_13_runScreams", "Desc1_22_runOpposite"]
QOut1_backOutside=["Desc1_13_runScreams", "Desc1_22_runOpposite"]
