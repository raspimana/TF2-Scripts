--------------
tr_walkway_rc2 by Washipato and Wiseguy149
--------------

This is a practice map focused on bots walking in straight lines, useful for training general aim 
or special techniques, like airshots, airblast and airstabs... or just fooling around

For playing the map, you MUST JOIN THE RED TEAM

If it's your first time with the map, read the "Just starting" section and the "Notes" section
at the end of the file. Both have very useful information about the map that you should know
when playing. Read "Special options" to know about strange buttons and options in the map.

It's recommended to have the developer console open for this map. You can find how to open it in the
next section.

This map has sv_cheats turned on, so your stats won't be saved :)

***********************************************************************************************
Just starting
***********************************************************************************************

-----------------------------------------------------------------------------------------------
INSTALLING THE MAP
-----------------------------------------------------------------------------------------------

**Skip this section if you already know how to install the map and open the console**

Copy the .bsp file from this rar into 

C:\Program Files\Steam\steamapps\<youraccoutname>\team fortress 2\tf\maps

Replace <YOURSTEAMID> with your steamID, the one you log in with

Also copy this readme file too, in case you want to know extra information about the map

To play it, open TF2, press "Create server" and in map choose "tr_walkway_rc2". Be sure to
choose to have more than 17 players slots so the bots can join. 
JOIN THE RED TEAM

-----------------------------------------------------------------------------------------------
OPENING THE CONSOLE
-----------------------------------------------------------------------------------------------

It's very important to have the console opened for binding keys and loading aliases. This section
explains how to open it, in case you don't know how to. 

Go to the "My games" tab in steam and right-click the "Team Fortress 2" game. From the menu,
choose "Properties" and then click the "Set launch options..." button. In the text box, add
"-console" without the quotes. The next time you open the game, the console will be open.

-----------------------------------------------------------------------------------------------
CONTROL ROOM
-----------------------------------------------------------------------------------------------

It's possible to customize several options, like which classes spawn, how fast they walk, how long
it takes to deploy more bots in the map, etc. Those options can be changed inside the "control room"
firing or hitting the buttons. There are 5 kind of buttons, all of them intuitive.

1 light: Stand in front of it to know what it does. Shoot or hit the button to activate it.
2 lights: Stand in front of it to know what it changes. The feature can be turned off and on. Green
light means that the feature is activated, red that it's deactivated.
3 lights: Stand in front to know what option is actually selected. Shoot or hit the button to switch
between the different options. Doing this changes the text to show the actual state.
Plus button: raises a certain variable (movement speed, deploy time or launch-pad power)
Minus button: lowers a certain variable (movement speed, deploy time or launch-pad power)

-----------------------------------------------------------------------------------------------
TELEPORTING AROUND
-----------------------------------------------------------------------------------------------

The players can teleport around the map using the console command "tr_teleport". Hit or shoot the
yellow and black blocks around the map to change the teleport destination. Bind tr_teleport to a 
key of your keyboard to help you to move faster and lose less time walking. To do it, write
in the console:

bind <KEY> "tr_teleport"

Replace <KEY> to any key you want and then press enter to load it. Press the selected key 
to activate the teleport.

There are more commands for the map that can be useful to bind, like "tr_attackonce"
and "tr_stop". More information about these in the console commands section.

***********************************************************************************************
I want to know more
***********************************************************************************************

-----------------------------------------------------------------------------------------------
SPECIAL OPTIONS
-----------------------------------------------------------------------------------------------
In this section I will explain uses for some features in the map that are not so obvious
like the rest

**Invisible walls**
Those are the walls at the sides of the track to make the bots stay on the walkway. You can turn
them off to practice airshots. The first option of turning the walls off is to hurt every bot outside
the walkway. The seconds turns the walls off, but don't damage bots that escaped from the walkway.

**Headshot training spawn button**
The bots and the way they move are not perfect. They play the "run" animation when moving, but their
hitbox (the part of them that detects when they are shot) stay in the "standing" animation.
There is no known way to fix this, but the impact that it has on gameplay can be lowered using
the "Spawn bots for headshot training" button. The bots will be facing a way so their heads will
match better with their hitbox. Only engineers, snipers, spies and demomen work and it's not perfect 

**Aim up + attack**
Useful for practicing long range pipebombs airblast or airstabs with pyros

**Aim down + attack**
Real soldiers aim for your feet, you can choose to simulate that behavior. Aim down can 
also be used to practice "airblast jumps"

**Bots ammount**
If your computer can't manage the map, change the maximum ammount of bots,
increasing the overall performance

**tr_stop and no speed option+tr_attackonce**
Stopping the bots can be useful to practice airblast and airblast jumps.

**Resupply off**
Turn it off to practice ammo management or if you want to play little games where there
is a chance of dying

**Resupply off+attack**
This will make the bots attack, to add some "realism" and challenge to your practice
Note* Stay away from pyros...

**Hurt bots**
One of the most useful options. Light classes will spawn with 1 hp when you enable it.
Pyros will have 26 HP. This can be very useful to know how much damage are you doing
with every shot. It’s also great for fooling around.

**Launch pad random power and trajectory**
By default, the launchpad changes his power (how strong it pushes the bots) and his
trajectory (the initial strength’s angle) in small lapses of time. Airshooting becomes
more realistic with these features on, but the random power can be turned off to select
which one you want and the random trajectory can be disabled too to get the same flying
pattern for every bot.

**Raise and lower the hill**
Lower the hill if it's bothering you when training airshots or you want the bots to run
in a straight line.

**Slope change**
Useful for training stairstabs.

**...***
Just for fun

-----------------------------------------------------------------------------------------------
EXAMPLE GAMEMODES
-----------------------------------------------------------------------------------------------

**Rocket+shotgun training**
Configuration:
- Spawn light classes
- Play soldier

Fire one rocket under a bot. When they are flying in the air shoot him with the shotgun. Try approaching the bots from 
different angles and distances. This is a useful technique that can be used in real servers. It's possible to use scouts,
spies or medics too to practice.


**Airstab training**
Configuration:
- Bind tr_teleport to any key (for example, bind f tr_teleport)
- Play spy

Stand in a catwalk or somewhere high where bots walk (preferably near a black and yellow square). When a bot comes nearby,
drop or jump over him, crouch and stab him as soon as you touch his back. If it's done well, you will do a backstab. For
trying again, instead of walking to the spot where you started, shoot the yellow and black square and press the key you
bound to tr_teleport. This will teleport you to that position (note that the teleport don't change after using it, this
means that you don't need to shoot the square again every time you want to teleport to that place). The airstab technique
is very useful to all spies, so its recommended that you know the timing for using it in real games.

Notice that you can change the speed to scout to make the training more difficult. You can also use the teleporters located
on the beams in the roof for airstabing.

NOTE: airstabs has many names, like overhead stab, height advantage, etc. Some peoples says that they don't even need a name.
I used airstab and stairstab to differentiate the gamemodes.


**Sniper training**
Configuration:
- Spawn bots for headshot training
- Any dodging option (jump, strafe or back and forth)
- Play sniper

Find a good spot and practice. The bots spawned for headshot training work quite well for shooting them from the side,
compared to normal spawns. Find a quiet place and shoot them to the head. You can also stand on the track and do twitch-shots.

**Basic air-strafing**
Configuration:
- Remove all bots
- Launch-pad
- No random power
- High launch-pad power

Air strafing is useful for increasing rocket jump distance and decreasing the chances of being hit
while flying. This readme will not go deep in this move but basically, you need to press the strafe key
without pressing neither "w" or "a" and slowly move the mouse in the direction of the strafe key 
(if you are strafing with "a", move slowly the mouse to the left). Normally, to practice this 
technique you need to to rocket jump to get the initial impulse. With the launch pad, you can get
the initial impulse easier and practice airstrafing after being launched. For example, try to get
to the catwalks BEHIND of the launchpad or disable the random trajectory and using air strafe,
get a bigger distance when traveling in a straight line.


**Stairstab training**
Configuration:
- Play spy

Stand on the slope where the bots walk uphill. When one of them is coming, jump over him, crouch, spin 180º and hit him
with the knife when he is below you. Hopefully you will land a backstab. This is a famous trick, hard to pull off
but really rewarding, especially when it’s done to a real player. You can change the movement speed to scout to increase
the difficulty. Don't forget to change the slope too!


**ULTIMATE Sniper training**
Configuration:
- Spawn bots for headshot training
- Bots move back and forth
- Bots jump
- Bots strafe
- Short strafe time
- Scout speed
- Play sniper

Gamemode designed to make snipers cry (or feel godlike)


**Airblast training**
Configuration:
- Spawn airblast training classes
- Make bots attack
- Hurt bots (optional)
- Bots aim down (optional)
- Play pyro with default flamethrower

Practice rockets and pipebombs reflection. Hurt bots will make them easier to kill and bots 
aim down gives soldiers a more realistic behavior.

**Revolver training**
Configuration:
- Random bots
- Bots move back and forth
- Bots strafe
- Long strafe timer
- Play spy

Train aim with the revolver. Snipe with the revolver low health classes. Jump around a move
like crazy for making the practice more realistic


**Airblast jump**
Configuration:
- Spawn soldiers
- Bots aim down
- Stop movement button or tr_stop
- tr_attackonce bound to any key (for example, bind f tr_attackonce)
- Critical hits off (optional)
- Play pyro with default flamethrower

Use the stop movement button after some soldiers are in the track to make them stop. You can
also use tr_stop console command. Find a soldier with an open space in front of him, preferably
at the beginning of the walkway and press the key binded to tr_attackonce. Position yourself
near the rocket hit and closer to the soldier. To airblast jump, make the bot fire, when the
rocket is about to hit you, jump, crouch and airblast the rocket under you. Try to reach high
places, like catwalks. Critical hits are turned off just in case you receive a critical rocket
to your face, but it can be turned on to perform high jumps. Use bot_refill to give the soldiers
ammo and health.


**Hard airstab**
Configuration:
- Spawn pyros
- Bots aim up
- Make bots attack
- Resupply off
- Play spy

It's just like stairstabs, but it makes them a lot more challenging. This also simulates real
pyros behaviour and let you see the real area of effect from the flame. Fail once and you will
be on fire, rushing to the medkit. NOTE: sometimes the pyro's flame will be invisible. To fix
it you need to turn on and off the bot's attack (binding tr_attack to some key helps too)

-----------------------------------------------------------------------------------------------
EXTRA BOTS
-----------------------------------------------------------------------------------------------

The map will always spawn 16 bots. More bots can be spawned manually and will be teleported to the map.
If you want more bots, spawn them using:

bot -team 0 -name <name>
For kicking them, use

kick <name>

-----------------------------------------------------------------------------------------------
BOT COMMANDS
-----------------------------------------------------------------------------------------------

Valve included some bot commands inside the game. Here I list some of those commands that can
be used inside the map.

******************************
Add more bots:
bot -team <teamname/number> -class <classname> -name <botname>
<teamname/number>: 0 blu, 1 red
<classname>: Demoman, Engineer, HeavyWeapons, Medic, Pyro, Scout, Soldier, Sniper, or Spy
<botname>: name of the bot
******************************

******************************
kick <bot>: kick bot with <bot> name
******************************

******************************
bot_teleport <botname> <X> <Y> <Z> <Pitch> <Yaw> <Roll>
Teleports a specified bot to a given coordinate. Map coordinates of where you are standing
can be found by typing getpos in the console. 
Example: getpos output
setpos -418.444855 3314.872070 -94.027405;setang 13.508876 -2.970791 0.000000
To use it in bot_teleport to teleport mybot there:
bot_teleport mybot -418.444855 3314.872070 -94.027405 13.508876 -2.970791 0.000000
******************************

******************************
bot_refill: Refills ammo, health and metal to bots
******************************

******************************
bot_selectweaponslot <botname> <n>
This makes specified bot select a specified weapon. 0 = primary; 1 = secondary; 2 = melee
******************************

Source and more info: http://tf2wiki.net/wiki/Bots

-----------------------------------------------------------------------------------------------
CONSOLE COMMANDS
-----------------------------------------------------------------------------------------------

All the options inside the control room can be accessed by console commands. With this
feature you can create your own configurations and load them on the map at any time without
looking for all the buttons that you need. Some of them are mirrors from the default TF2
commands, don't use valve ones here because it can make buttons to malfunction.

--- Console only commands ---
tr_teleport                ||  Teleports the player to the last teleport destination selected
tr_help                    ||  Shows the tr_ cvar list
tr_loadcvars               ||  Enables all cvars (for clients)
tr_attackonce              ||  Makes all bots attack once (turns off constant attack)
tr_deployonce              ||  Deploy one bot in the track

--- Bots management ---
tr_kill                    ||  Kill all bots
tr_kick                    ||  Kick all bots

tr_maxbots_up              ||  Raises maximum ammount of bots on the walkway
tr_maxbots_down            ||  Lowers maximum ammount of bots on the walkway

tr_default                 ||  Reset map configurations (except "less bots", hill height and slope)

tr_maxbots_16              ||  Set the maximum ammount of bots to 16 (default)
tr_maxbots_14              ||  Set the maximum ammount of bots to 14
tr_maxbots_12              ||  Set the maximum ammount of bots to 12
tr_maxbots_10              ||  Set the maximum ammount of bots to 10
tr_maxbots_08              ||  Set the maximum ammount of bots to 8
tr_maxbots_05              ||  Set the maximum ammount of bots to 5
tr_maxbots_03              ||  Set the maximum ammount of bots to 3
tr_maxbots_01              ||  Set the maximum ammount of bots to 1
tr_maxbots_00              ||  Do not spawn bots

tr_firewall                ||  Toggles the firewall
tr_firewall_ON             ||  Kill the bots when they reach the middle of the track
tr_firewall_OFF            ||  Do not kill the bots (default)

--- Spawn options ---
tr_spawn_random            ||  Spawn random classes (starting bots)
tr_spawn_all               ||  Spawn 2 bots of every class
tr_spawn_light             ||  Spawn engineers, scouts, snipers and spies
tr_spawn_headshot          ||  Spawn engineers, spies, snipers and demomen with headshot correction
tr_spawn_comp              ||  Spawn scouts, soldiers, demomen and medics
tr_spawn_airblast          ||  Spawn soldiers and demomen

tr_spawn_pyros             ||  Spawn pyros
tr_spawn_scouts            ||  Spawn scouts
tr_spawn_heavies           ||  Spawn heavies
tr_spawn_medics            ||  Spawn medics
tr_spawn_spies             ||  Spawn spies
tr_spawn_demomen           ||  Spawn demomen
tr_spawn_soldiers          ||  Spawn soldiers
tr_spawn_engineers         ||  Spawn engineers
tr_spawn_snipers           ||  Spawn snipers

tr_spawn_1pyro             ||  Spawn one pyro
tr_spawn_1scout            ||  Spawn one scout
tr_spawn_1heavy            ||  Spawn one heavy
tr_spawn_1medic            ||  Spawn one medic
tr_spawn_1spy              ||  Spawn one spy
tr_spawn_1demoman          ||  Spawn one demoman
tr_spawn_1soldier          ||  Spawn one soldier
tr_spawn_1engineer         ||  Spawn one engineer
tr_spawn_1sniper           ||  Spawn one sniper
tr_spawn_1random           ||  Spawn one random bot

--- Movement speed ---
tr_speed_up                ||  Raises movement speed
tr_speed_down              ||  Lowers movement speed

tr_speed_no                ||  Stops movement
tr_speed_snail             ||  Snail movement speed
tr_speed_heavy             ||  Heavy movement speed
tr_speed_soldier           ||  Soldier movement speed
tr_speed_demoman           ||  Demoman movement speed
tr_speed_normal            ||  Average movement speed (default)
tr_speed_medic             ||  Medic movement speed
tr_speed_scout             ||  Scout movement speed
tr_speed_jet               ||  Jet movement speed
For chosing other speeds, use:
ent_fire walk addoutput "speed xxx"

tr_stop                    ||  Stops spawns and movement. Enter this command again to resume spawning and movement (turns off all dodge options)

--- Deploy time ---
tr_deploy_up               ||  Raises deploy time
tr_deploy_down             ||  Lowers deploy time

tr_deploy_no               ||  Stops deploy
tr_deploy_05               ||  Set 0.5 seconds between bots spawns in the map
tr_deploy_10               ||  Set 1 second between bots spawns in the map
tr_deploy_15               ||  Set 1.5 seconds between bots spawns in the map
tr_deploy_20               ||  Set 2 seconds between bots spawns in the map
tr_deploy_30               ||  Set 3 seconds between bots spawns in the map (default)
tr_deploy_40               ||  Set 4 seconds between bots spawns in the map
tr_deploy_60               ||  Set 6 seconds between bots spawns in the map
tr_deploy_120              ||  Set 12 seconds between bots spawns in the map
For choosing other times, use:
ent_fire spawntimer refiretime <time>

--- Bots dodge options ---
tr_jump                    ||  Toggles bots jump
tr_jump_ON                 ||  Forces the bots to jump
tr_jump_OFF                ||  Makes the bots stop jumping  (default)
You can modify the time between jumps using (default 1.75):
ent_fire jump_timer refiretime <time>

tr_back                    ||  Toggles bots "back and forth" movement
tr_back_ON                 ||  Turns "back and forth" movement on
tr_back_OFF                ||  Turns "back and forth" movement off (default)

tr_strafe                  ||  Toggles bots strafe movement
tr_strafe_ON               ||  Make bots strafe left and right
tr_strafe_ONR              ||  Make bots strafe randomly
tr_strafe_OFF              ||  Turns bots strafe movement off (default)

tr_strafe_timer            ||  Switch between the different strafe times
tr_strafe_timer_default    ||  Set the strafe time to 1 second (default)
tr_strafe_timer_long       ||  Set the strafe time to 2 seconds
tr_strafe_timer_short      ||  Set the strafe time to 0.5 seconds
For chosing other times, use:
ent_fire strafe_timer refiretime <time>

tr_crouch                  ||  Toggles bots crouch option
tr_crouch_ON               ||  Make bots crouch
tr_crouch_ONR              ||  Make bots crouch randomly
tr_crouch_OFF              ||  Bots don't crouch (default)

--- Bots actions ---
tr_attack                  ||  Toggles bots attack
tr_attack_ON               ||  Forces the bots to attack (same effect as bot_forceattack 1)
tr_attack_ON3              ||  Forces the bots to attack once every 3 seconds
tr_attack_ONR              ||  Forces the bots to attack randomly
tr_attack_OFF              ||  Forces bots to stop attacking (same effect as bot_forceattack 0 ) (default)

tr_hurt                    ||  Toggles bots hurting
tr_hurt_ON                 ||  Hurt the bots by 124 damage at the beginning of the track
tr_hurt_ONlow              ||  Hurt the bots by 75 damage at the beginning of the track
tr_hurt_OFF                ||  Stop hurting bots (default)

tr_aim                     ||  Switchs between the bots aim direction options
tr_aim_default             ||  Makes bots aim forward (default)
tr_aim_up                  ||  Makes bots aim up
tr_aim_down                ||  Makes bots aim down 
For more customization in bot aiming, go to the "Customize" section

tr_botresupply             ||  Toggles bot resupply
tr_botresupply_ON          ||  Bots regenerate health and ammo constantly
tr_botresupply_OFF         ||  Disables the bot resupply (default)

tr_spam                    ||  Try it
tr_spam_none               ||  Nothing (default)
tr_spam_dispenser          ||  Try it
tr_spam_spy                ||  Try it

--- Map options ---
tr_crits                   ||  Toggles crits
tr_crits_ON                ||  Turn critical hits on (same effect as tf_weapon_criticals 1) (default)
tr_crits_OFF               ||  Turn critical hits off (same effect as tf_weapon_criticals 0)

tr_resupply                ||  Toggles resupply
tr_resupply_ON             ||  Enables the resupply (default)
tr_resupply_OFF            ||  Disables the resupply

tr_panic                   ||  Toggles panic mode
tr_panic_ON                ||  Enables panic mode
tr_panic_OFF               ||  Disable panic mode

tr_grav                    ||  Switches between the gravity options
tr_grav_default            ||  Changes to 800 gravity (default)
tr_grav_low                ||  Changes to 600 gravity 
tr_grav_verylow            ||  Changes to 400 gravity 

tr_walls                   ||  Toggles invisible walls at the sides of the track
tr_walls_ON                ||  Turn walls on (default)
tr_walls_OFF               ||  Turn walls off and damage bots that fall outside the walkway
tr_walls_OFFnd             ||  Turn walls off, don't damage bots outside the walkway

tr_deploy_rand             ||  Toggles random deploy position
tr_deploy_rand_ON          ||  Deploy bots in a random position in the walkway (default)
tr_deploy_rand_OFF         ||  Don't deploy bots randomly

tr_deploy_left             ||  Move the deploy position to the left
tr_deploy_right            ||  Move the deploy position to the right
tr_deploy_stop             ||  Stop the deploy position is movement
To choose a specific deploy position, you need first to set a speed to the
deployer entity using:
ent_fire mytrain setspeed 200
Then, it's possible to move it to a position between 0.0 and 1.0 with:
ent_fire mytrain setposition X

tr_deployonlp              ||  Toggle bots being deployed on the launch-pad
tr_deployonlp_ON           ||  Deploy bots on the launch-pad
tr_deployonlp_OFF          ||  Deploy bots at the start of the track (default)

--- Retractable platform ---
tr_platform                ||  Toggles retractable platform
tr_platform_ON             ||  Extend the retractable platform
tr_platform_OFF            ||  Hide the retractable platform

tr_platform_up             ||  Move the platform up
tr_platform_down           ||  Move the platform down
tr_platform_left           ||  Move the platform left
tr_platform_right          ||  Move the platform right
tr_platform_stop           ||  Stop the platform movement

--- Hill and ramp ---
tr_hill_up                 ||  Move hill up
tr_hill_down               ||  Move hill down

tr_ramp_up                 ||  Move ramp up
tr_ramp_down               ||  Move ramp down

tr_ramp_full               ||  Hide or lift the ramp
tr_ramp_full_up            ||  Lift the ramp fully
tr_ramp_full_down          ||  Hide the ramp

--- Launchpad ---
tr_lp                      ||  Toggles the launch-pad on and off
tr_lp_ON                   ||  Turns the launchpad on
tr_lp_OFF                  ||  Turns the launchpad off (default)

tr_lp_randpow              ||  Toggles launch-pad random power
tr_lp_randpow_ON           ||  Changes the launchpad power 2 times per second (default)
tr_lp_randpow_OFF          ||  Turns random launchpad power off

tr_lp_randtraj             ||  Toggles launch-pad random trajectory
tr_lp_randtraj_ON          ||  Turns on random trajectory, overrides the power meter configuration (default)
tr_lp_randtraj_OFF         ||  Turns off random trajectory

tr_lp_traj_up              ||  Raises the trajectory of the launch-pad
tr_lp_traj_down            ||  Lowers the trajectory of the launch-pad
tr_lp_traj_stop            ||  Stops the trajectory change of the launch-pad

tr_lp_pow_up               ||  Raises launch-pad power
tr_lp_pow_down             ||  Lowers launch-pad power

tr_lp_pow_1                ||  Set launch-pad power to 1000
tr_lp_pow_2                ||  Set launch-pad power to 1100
tr_lp_pow_3                ||  Set launch-pad power to 1250
tr_lp_pow_4                ||  Set launch-pad power to 1350
tr_lp_pow_5                ||  Set launch-pad power to 1500 (default)
tr_lp_pow_6                ||  Set launch-pad power to 1600
tr_lp_pow_7                ||  Set launch-pad power to 1700
tr_lp_pow_8                ||  Set launch-pad power to 1850
tr_lp_pow_9                ||  Set launch-pad power to 1950
For choosing other powers, enter:
ent_fire launchpad_power addoutput "speed xxxx" (this only works when the random power is not selected)

--- Sentry room ---
tr_sentry1                 ||  Create a level 1 sentry
tr_sentry2                 ||  Create a level 2 sentry
tr_sentry3                 ||  Create a level 3 sentry
tr_disp1                   ||  Create a level 1 dispenser
tr_disp2                   ||  Create a level 2 dispenser
tr_disp3                   ||  Create a level 3 dispenser
tr_blocks                  ||  Create a small block
tr_blockl                  ||  Create a large block
tr_deploengi               ||  Deploy an engineer
tr_changeteam              ||  Change the team of the deployed buildings
tr_eraseone                ||  Destroy everything under the spawner
tr_eraseall                ||  Destroy everything in the sentry room
tr_sr_up                   ||  Move spawner up
tr_sr_down                 ||  Move spawner down
tr_sr_left                 ||  Move spawner to the left
tr_sr_right                ||  Move spawner to the right
tr_sr_cw                   ||  Turn the spawner clockwise
tr_sr_ccw                  ||  Turn the spawner counter-clockwise

tr_sr                      ||  Toggle sentry room
tr_sr_ON                   ||  Activate sentry room
tr_sr_OFF                  ||  Deactivate sentry room (default)

tr_wrench                  ||  Toggle wrench attack
tr_wrench_ON               ||  Forces all engineers to attack with the wrench
tr_wrench_OFF              ||  Makes the engineers stop attacking with the wrench (default)

--- Teleport destinations ---
tr_tele_0                  ||  Changes the teleport destination
tr_tele_1                  ||  Changes the teleport destination
tr_tele_2                  ||  Changes the teleport destination
tr_tele_3                  ||  Changes the teleport destination
tr_tele_4                  ||  Changes the teleport destination
tr_tele_5                  ||  Changes the teleport destination
tr_tele_6                  ||  Changes the teleport destination
tr_tele_7                  ||  Changes the teleport destination
tr_tele_8                  ||  Changes the teleport destination
tr_tele_9                  ||  Changes the teleport destination
tr_tele_10                 ||  Changes the teleport destination

By the way, you can use the cheat command tr_iwantmyhoovy to disable the restriction for one 
of the easter eggs ;)

-----------------------------------------------------------------------------------------------
ALIASES
-----------------------------------------------------------------------------------------------

You can enter a string of these commands using a simple alias and change between different
ways of playing the map. Alias are used to call a group of commands and are very useful for
general scripting in the source engine.

Example:
Enter this string in the console to create the "tr_airblast" alias:

alias tr_airblast "tr_default; wait 10; tr_spawn_airblast; tr_deploy_4; tr_attack_ON; tr_speed_heavy; tr_hurt_ON"

Copy and paste the whole sentence in the console and press enter. This will create the 
"tr_airblast" alias, which you can use anytime until you close TF2.

Entering this alias in the console (that is, writing "tr_airblast" without the quotes and
pressing enter) will set every option to default, then spawn soldiers and demomen and
force them to attack and move slower. It will also make them appear every 4 seconds and hurt
them by 124 (soldiers will start with 76 hitpoints and demomen with 51). Go pyro and you
will have a perfect setup for practicing airblast.

Another example would be:

alias tr_hardstab "tr_default; wait 10; tr_spawn_pyros; tr_resupply_OFF; tr_attack_ON; tr_aim_up"

You can practice stairstabs (or how you like to call them) with any class or speed, but with this
alias pyros will spawn firing their flamethrowers aiming upwards and resupply will be turned off, making
the practice a bit more challenging.

***********************************************************************************************
The hard part of the walkway
***********************************************************************************************

-----------------------------------------------------------------------------------------------
CODING SYSTEM
-----------------------------------------------------------------------------------------------
The map features programming tools. Though it's hard to use and counter-intuitive, it's a 
more powerful version of the scripts that come with TF2 by default and let you create simple testing
tools and mini-games inside the walkway. It has 5 variables that can be increased, decrease, compared
and reset. It also has 3 timers, a customizable buttons and text. All of these can be manipulated
using console commands.

The code is case sensitive. Most commands are aliases, but some others are ent_fire commands

*************************************************************************
Events
*************************************************************************

Events are the response of the coding system. They are commands that are loaded in the console.
There is an event after comparing 2 variables, when a bot walks to the end of the walkway, when
a timer reach zero and so on. All of them have the form:

==================
tr_ON<event>
==================

For example, tr_ONEQUAL is loaded in the console every time 2 variables are compared and they are equal
All events don't have any effect in the game. The user must program them. To do this, use:

==================
alias tr_ON<event> "<action>" // Will do <action> every time the <event> happens
alias tr_ON<event> // Will do nothing when the <event> happens
==================

For example, every time the timer A reaches zero, deploy a bot in the walkway

==================
alias tr_ONTIMERA "tr_deployonce"
==================

More than one commands can be issued to a single event. This can be used to modify the event that
just happened. Here, after the timer A is activated, wait and make every bot attack once and 
then set the next activation to do nothing:
==================
alias tr_ONTIMERA "wait 120; tr_attackonce; alias tr_ONTIMERA"
==================

Events are the core of the system. If you want or need, you can activate them like any command using
==================
tr_ON<event>
==================

Complete list of events and when they trigger:
==================
Bot positions:
tr_ONSTART: a bot enters the start part of the walkway
tr_ONMID: a bot enters the middle part of the walkway
tr_ONEND: a bot enters the end of the walkway
tr_ONLEAVE: a bot leaves the walkway

Timers:
tr_ONTIMERA: timer A runs out
tr_ONTIMERB: timer B runs out
tr_ONTIMERC: timer C runs out
tr_ONTIMERD: timer D runs out

Comparer:
tr_ONCMPEQUAL: X=Y after calling tr_CMP
tr_ONCMPNOTEQUAL: X=/=Y after calling tr_CMP
tr_ONCMPGREATERTHAN: X>Y after calling tr_CMP
tr_ONCMPLESSTHAN: X<Y after calling tr_CMP

Variables:
tr_ONAEQUAL: A is equal than his compare value after changing the value of A
tr_ONANOTEQUAL: A is not equal than his compare value after changing the value of A
tr_ONAGREATERTHAN: A is greater than his compare value after changing the value of A
tr_ONALESSTHAN: A is less than his compare value after changing the value of A
tr_ONBEQUAL: B is equal than his compare value after changing the value of B
tr_ONBNOTEQUAL: B is not equal than his compare value after changing the value of B
tr_ONBGREATERTHAN: B is greater than his compare value after changing the value of B
tr_ONBLESSTHAN: B is less than his compare value after changing the value of B
tr_ONCEQUAL: C is equal than his compare value after changing the value of C
tr_ONCNOTEQUAL: C is not equal than his compare value after changing the value of C
tr_ONCGREATERTHAN: C is greater than his compare value after changing the value of C
tr_ONCLESSTHAN: C is less than his compare value after changing the value of C
tr_ONDEQUAL: D is equal than his compare value after changing the value of D
tr_ONDNOTEQUAL: D is not equal than his compare value after changing the value of D
tr_ONDGREATERTHAN: D is greater than his compare value after changing the value of D
tr_ONDLESSTHAN: D is less than his compare value after changing the value of D
tr_ONEEQUAL: E is equal than his compare value after changing the value of E
tr_ONENOTEQUAL: E is not equal than his compare value after changing the value of E
tr_ONEGREATERTHAN: E is greater than his compare value after changing the value of E
tr_ONELESSTHAN: E is less than his compare value after changing the value of E
tr_ONBUFFEREQUAL: BUFFER is equal than his compare value after changing the value of BUFFER
tr_ONBUFFERNOTEQUAL: BUFFER is not equal than his compare value after changing the value of BUFFER
tr_ONBUFFERGREATERTHAN: BUFFER is greater than his compare value after changing the value of BUFFER
tr_ONBUFFERLESSTHAN: BUFFER is less than his compare value after changing the value of BUFFER

Switch:
tr_ONCASE00: BUFFER=0 after calling a tr_CASE
tr_ONCASE01: BUFFER=1 after calling a tr_CASE
tr_ONCASE02: BUFFER=2 after calling a tr_CASE
tr_ONCASE03: BUFFER=3 after calling a tr_CASE
tr_ONCASE04: BUFFER=4 after calling a tr_CASE
tr_ONCASE05: BUFFER=5 after calling a tr_CASE
tr_ONCASE06: BUFFER=6 after calling a tr_CASE
tr_ONCASE07: BUFFER=7 after calling a tr_CASE
tr_ONCASE08: BUFFER=8 after calling a tr_CASE
tr_ONCASE09: BUFFER=9 after calling a tr_CASE
tr_ONCASE10: BUFFER=10 after calling a tr_CASE
tr_ONCASE11: BUFFER=11 after calling a tr_CASE
tr_ONCASE12: BUFFER=12 after calling a tr_CASE
tr_ONCASE13: BUFFER=13 after calling a tr_CASE
tr_ONCASE14: BUFFER=14 after calling a tr_CASE
tr_ONCASE15: BUFFER=15 after calling a tr_CASE
tr_ONCASEDEF: tr_CASE do not trigger any of the other cases
==================

*************************************************************************
Timers
*************************************************************************

Timers are an important part of the programming system. They are 4 logic_timer entities, it's possible
to set the refire time for 3 of them (A, B and C), the last one is a random timer. All of them start
disabled, they must be turned on to work with them. When the timers are activated, they start a
countdown of x seconds. When they reach zero, a command is loaded in the console and the timer restart.
x must be a float a value with 2 decimals (5.05, is ok, 5.006 is not)

Timers (entity name):

Timer A
-------
Entity name: custom_timer_a
Event: tr_ONTIMERA
Initial refire time: 0.01 seconds
--COMMANDS
tr_ONTIMERA: event
tr_TIMERA_ON: turn on timer A
tr_TIMERA_OFF: turn off timer A
ent_fire custom_timer_a refiretime x: set x as time for the timer A 
Note: this will be a special timer useful to load and compare variable

Timer B
-------
Entity name: custom_timer_b
Event: tr_ONTIMERB
Initial refire time: 1 second
--COMMANDS--
tr_ONTIMERB: event
tr_TIMERB_ON: turn on timer B
tr_TIMERB_OFF: turn off timer B
ent_fire custom_timer_b refiretime x: set x as time for the timer B

Timer C
-------
Entity name: custom_timer_c
Event: tr_ONTIMERC
Initial refire time: 1 second
--COMMANDS--
tr_ONTIMERC: event
tr_TIMERC_ON: turn on timer C
tr_TIMERC_OFF: turn off timer C
ent_fire custom_timer_c refiretime x: set x as time for the timer B

Timer D
-------
Entity name: custom_timer_D
Event: tr_ONTIMERD
Initial refire time: 5(lower limit) to 10(upper limit) seconds
--COMMANDS--
tr_ONTIMERD: event
tr_TIMERD_ON: turn on timer D
tr_TIMERD_OFF: turn off timer D
ent_fire custom_timer_d addoutput "LowerRandomBound x": set the lower limit of the random timer to x
ent_fire custom_timer_d addoutput "UpperRandomBound x": set the upper limit of the random timer to x
NOTE: It's impossible to use "" inside aliases. The upper limit MUST be bigger than the lower limit

*************************************************************************
Relay
*************************************************************************
The relay is an event that triggers one second after it was called. It's useful
for setting up a program without using a timer, because some commands need other
features activated to work (like moving the trajectory selection for the launch-pad,
first you need to disable trajectory selection)

tr_RELAY: call the relay
tr_ONTRIGGER: event. Triggers one second after calling the relay

*************************************************************************
Position
*************************************************************************
It's possible to detect when a blu bot enters different parts of the walkway,
that is when they enter it (START) are in the middle (MID) or at the end (END).
This will be triggered once per time they enter it. You need to enable the events
before using them

tr_POSEVENT_ON: Enables position events
tr_POSEVENT_OFF: Disables position events
tr_ONSTART: event. Triggered when a bot enters the first part of the walkway
tr_ONMID: event. Triggered when a bot enters the middle part of the walkway
tr_ONEND: event. Triggered when a bot enters the final part of the walkway
tr_ONLEAVE: event. Triggered when a bot leaves the walkway (this includes being killed)

*************************************************************************
Variables
*************************************************************************

All of them are integers, and their starting value is 0. 
Their names are:
======
A
B
C
D
E
BUFFER
======
BUFFER is a special variable. More about it later

You can do 4 operations with variables
==================
INC: increase by 1
DEC: decrease by 1
RESET: reset to 0
LOAD: load the variable in the buffer
ent_fire custom_<VARIABLE>var setvalue x : Set the value of VARIABLE to x
==================

All of these are issued by console commands in the way
==================
tr_<VARIABLE><OPERATION>
==================
For example:

tr_TIMERA_ON
alias tr_ONTIMERA "step1"
alias step1 "tr_ARESET; alias tr_ONTIMERA step2"
alias step2 "tr_AINC; alias tr_ONTIMERA; tr_TIMERA_OFF"

More about this structure in the next section

This lines will reset the variable A, wait 0.01 seconds using the timer A and increase 
the variable A by 1. Final result: A = 1.

You can also do more advanced operations using ent_fire commands:

==================
ent_fire custom_<VARIABLE>var add x : Add x to VARIABLE
ent_fire custom_<VARIABLE>var subtract x : Subtract x to VARIABLE
ent_fire custom_<VARIABLE>var multiply x : Multiply VARIABLE by x
ent_fire custom_<VARIABLE>var divide x : Divide VARIABLE by x
==================

EVENTS FOR VARIABLES:

When a value from a variable is changed, the new value is compared to a special number. By
default, that number is 0. The comparison will output a command depending on what is the
relation between the value in the variable and the one used for comparing it. The compare
value can be changed in any moment.

==================
tr_ON<VARIABLE>EQUAL: <VARIABLE> is equal than his compare value after changing the value of <VARIABLE>
tr_ON<VARIABLE>NOTEQUAL: <VARIABLE> is not equal than his compare value after changing the value of <VARIABLE>
tr_ON<VARIABLE>GREATERTHAN: <VARIABLE> is greater than his compare value after changing the value of <VARIABLE>
tr_ON<VARIABLE>LESSTHAN: <VARIABLE> is less than his compare value after changing the value of <VARIABLE>
ent_fire custom_<VARIABLE>varcomp setcomparevalue x: set the compare value of <VARIABLE> to x
==================

*********
Loading variables
*********
Always after changing the value of a variable, a time lapse is needed before using that
variable with the new value. The best way to be sure of getting the new value is using
the special timer A and creating a line of steps in the form:

==================
alias tr_ONTIMERA "step1"
alias step1 "<action 1>; alias tr_ONTIMERA step2"
alias step2 "<action 2>; alias tr_ONTIMERA step3"
alias step3 "<action 3>; alias tr_ONTIMERA step4"
....

alias laststep "<last action>; alias tr_ONTIMERA; tr_TIMERA_OFF"
==================

All actions will be activated with a 0.01 seconds delay between them. In every step,
tr_ONTIMERA is set to the next step and in the final one, tr_ONTIMERA is set to
nothing. The timer can also be disabled in this point until it's needed again and the
next step can be set to be the initial one.

All actions in a step are done simultaneously, so the order is not really important.

Always:

1) Load variables one step after the value has changed 
2) Change the value of a compare event one step before comparing or changing the variable
3) If it's the last step, disable the timer or change the event of the timer to nothing

==================
alias laststep "<last action>; alias tr_ONTIMERA step1; tr_TIMERA_OFF"
==================

There is a good example in the "Compare" section

*************************************************************************
Buffer
*************************************************************************

To do any operation between two variables, you need to load them in the buffer first. Only one
variable can be buffered at the same time. The buffer is a variable, so you can manipulate it like
one, except it cannot be loaded.

Special operations with the buffer:

==================
tr_LOADX: load the integer in the buffer to the X variable
tr_LOADY: load the integer in the buffer to the y variable
tr_CASE: load the integer in the buffer to a the switch
==================

*************************************************************************
Compare
*************************************************************************

It's possible to compare one variable to another and know if it's equal, not equal,
smaller or bigger. The engine always compares the variable X to Y, their values can be
changed using tr_LOADX and tr_LOADY. Those commands change the variables to the value 
in the buffer.

To compare X and Y, use:
==================
tr_CMP
==================

It will compare them and call the following commands in the console (events):
==================
if X equal to Y: tr_ONCMPEQUAL
if X not equal to Y: tr_ONCMPNOTEQUAL
if X is bigger than Y: tr_ONCMPGREATERTHAN
if X is smaller than Y: tr_ONCMPLESSTHAN
==================

For example, we want to compare variable A with B, if A is bigger than B, stop movement and
deploy. Here, the B variables has an initial value and A increases with the time. Copy this
text in a cfg file and name it var_test.cfg. Put the file in the /tf/cfg folder. Load it inside 
the game using "exec var_test".

////////////////////////////////////////////
// tr_ONGREATERTHAN will stop movement and deploy and then say "A is bigger than B" in the 
// console. It also stops the main timer

alias "tr_ONCMPGREATERTHAN" "tr_stop; echo A is bigger than B; tr_TIMERB_OFF"

ent_fire custom_Bvar setvalue 3 // Initial value of B = 3

tr_ARESET // A is reset to 0

tr_TIMERB_ON // The timer B (1 second) is activated

alias tr_ONTIMERB "tr_AINC; tr_TIMERA_ON;echo O" // Each time the timer B triggers, A
// is increased, timer A is activated (0.01 seconds) and "O" is echoed in the console
// to keep track on the time

alias tr_ONTIMERA "step1" // We set the fast timer to the first step in the line

alias step1 "tr_ALOAD;alias tr_ONTIMERA step2" // A is loaded in the buffer and set the next step to be step 2
alias step2 "tr_LOADX;alias tr_ONTIMERA step3" // X is loaded with the value in the buffer and set the next step to be step 3
alias step3 "tr_BLOAD;alias tr_ONTIMERA step4" // B is loaded in the buffer and set the next step to be step 4
alias step4 "tr_LOADY;alias tr_ONTIMERA step5" // Y is loaded with the value in the buffer and set the next step to be step 5
alias step5 "tr_CMP;alias tr_ONTIMERA step1;tr_TIMERA_OFF" // Compare, set the next step to be the first step and turn off timer A
////////////////////////////////////////////

After loading the code, bots will stop moving and spawning and "A is bigger than B" will
appear in the console.

*************************************************************************
Switch
*************************************************************************

The switch compares the variable in the buffer with numbers between 0 and 15.
To call the switch use

==================
tr_CASE: compares the buffer to numbers between 0 and 15, then it triggers
a case depending on the value.
tr_CASERAND: choose one of the cases randomly
tr_CASERANDSHUF: choose one of the cases randomly. The cases don't repeat until
all cases have been chosen
==================

If the value of the buffer is equal to any of these numbers, an event will 
be triggered in the form

==================
tr_ONCASE00: if buffer is 0
tr_ONCASE01: if buffer is 1
tr_ONCASE02: if buffer is 2
tr_ONCASE03: if buffer is 3
tr_ONCASE04: if buffer is 4
tr_ONCASE05: if buffer is 5
tr_ONCASE06: if buffer is 6
tr_ONCASE07: if buffer is 7
tr_ONCASE08: if buffer is 8
tr_ONCASE09: if buffer is 9
tr_ONCASE10: if buffer is 10
tr_ONCASE11: if buffer is 11
tr_ONCASE12: if buffer is 12
tr_ONCASE13: if buffer is 13
tr_ONCASE14: if buffer is 14
tr_ONCASE15: if buffer is 15
==================

In case of the value not being equal to any of these values, it will trigger another
event

==================
tr_ONCASEDEF
==================

The switch can work like a randomizer using tr_CASERAND and tr_CASERANDSHUF

*************************************************************************
Custom text
*************************************************************************

Text that appears on screen. Can save up to 3 different lines. Only one text can stay on
screen at the same time. Warning: don't use the " symbol inside the message.

Commands:

==================
tr_TEXT1: Display text 1 on screen
ent_fire custom_text1 addoutput "message <your message here>": Change the text 1
tr_TEXT2: Display text 2 on screen
ent_fire custom_text2 addoutput "message <your message here>": Change the text 2
tr_TEXT1: Display text 3 on screen
ent_fire custom_text3 addoutput "message <your message here>": Change the text 3
==================

*************************************************************************
Notes
*************************************************************************

- If you want to damage a bot (or a player) by 124 hp using the "hurt bot" option, the player/bot
must be teleported to (1664 566 510)
- To change the damage inflicted by the hurt option, use the following command:

ent_fire hurtstart_trigger SetDamage X

Where X is two times the damage you want to do (by default, it is 248 and will reset to that value
with tr_default)

*************************************************************************
Galaga soldier mini-game
*************************************************************************
The map includes a mini-game showing some of the functions. It's located inside 
tf/cfg/tr_walkway/minigames/gsoldier.cfg
To run it, enter "exec tr_walkway/minigames/gsoldier" in the console.

-----------------------------------------------------------------------------------------------
CUSTOMIZE
-----------------------------------------------------------------------------------------------
There are some options around the map that can be tweaked by the user with commands. Those include the
bot movement speed, timers used for different features and the angle the bots aim. Take in mind that
all of the commands listed use ent_fire and some of them use "addoutput", so handle them with care
and check if they are well written before loading the command in the console.
Commands with "" inside them cannot be used in aliases.

MOVEMENT SPEED
****
ent_fire walk addoutput "speed <speed>"
****
Replace <speed> with the speed you want

AIM DIRECTION
****
ent_fire destination_walkway addoutput "angles x y 0"
****
x: This is the pitch. It goes from -90 to 90. -90 is straight up and 90 is straight down.
y: This is the yaw. It goes from 0 to 360. 270 is forward, 90 is backward,0 and 180 are left and right

DEPLOY TIME
****
ent_fire spawntimer refiretime <time>
****
Replace <time> with the time you want

JUMP TIMER
****
ent_fire jump_timer refiretime <time>
****
Time between jumps. Choosing a small one will make bots accelerate.Replace <time> with
the time you want (default 1.75)

STRAFE TIMER
****
ent_fire strafe_timer refiretime <time>
****
Time it takes for the bots to change strafe direction. Replace <time> with the time you
want (default 1.75)

BACK AND FORTH TIMERS
"Backward timer"
****
ent_fire back_timeron addoutput "LowerRandomBound <lowertime>"
ent_fire back_timeron addoutput "UpperRandomBound <uppertime>"
****
This timer controls when the bots go backwards. It's random, that means the timer changes it's refire
time everytime it ends counting. This time goes from <lowertime> to <uppertime>. Default values are
<lowertime> = 2.5
<uppertime> = 4.5
If you want to change these values, make sure the <uppertime> is bigger than the <lowertime>

"Forward timer"
****
ent_fire back_timeroff refiretime <time>
****
This timer triggers every <time> seconds (default 1.25). Every time it triggers, it makes the bots
go forward

LAUNCH PAD POWER
****
ent_fire launchpad_power addoutput "speed <power>"
****
This changes the power the launchpad pushes the bots. Use this command only when the "random power"
option is not selected or the power will be reset to random after a fraction of a second.

-----------------------------------------------------------------------------------------------
NOTES (Important)
-----------------------------------------------------------------------------------------------

- The bots don't walk, they are pushed using the track, so the behavior when they are pushed (airblast, FaN)
or exploded is a little different from real players walking. That difference is hard to perceive now (rc)
- The hitboxes from the bots behaves in a different way from real walking bots. There is no way to fix this.
- Damage spread is DISABLED by default. Having it enabled breaks the "hurt" function, making the
124 damage done by it suffer the damage spread, sometimes doing more than 124 damage and killing
light classes
- Don't use commands that issue move orders to bots (bot_flipout, bot_mimic). They will break the bots
deploy system
- When playing multiplayer, certain cvars are disabled for clients
- SV_CHEATS in ENABLED. Players can easily abuse this in LOTS of ways, so play with people you 
trust. sv_cheats is turned on automatically after it is turned off.
- The map is a release candidate (rc). If you have any suggestion or find a bug, contact one of the mappers
(Wiseguy149 or Washipato) sending a mail to washipato@gmail.com or by steam (ID: washipato/profile: 76561197995187989)

I hope you enjoy the map and find it fun and useful. Good luck!

****
NOTES FOR SERVER OWNERS
****

The map will set at the start of the round the following configurations:
# sv_cheats 1
# mp_teams_unbalance_limit 0
# mp_disable_respawn_times 1
# mp_waitingforplayers_cancel 1
# tf_damage_disablespread 1
# tf_weapon_criticals 1

sv_cheats is turned on, so it's recommended to use a plugin to disallow player from
using ent_fire commands. Disable any kind of external team-balancer plugin that the
server could be running

-----------------------------------------------------------------------------------------------
Credits and thanks
-----------------------------------------------------------------------------------------------
- Thanks a lot to wiseguy149 for his huge help in the last part of the project, cleaning up the 
map, adding new features, optimizing, general mapping and lots of ideas and bug reports that
made the map work a lot better than it was before.
- Thanks to the ESG (elite spy group) community for his support and ideas. The group gave me
great feedback in many stages of the develpment. The map would not be what now is without 
their help. People from ESG are NOT elitist. They are just a group of people who enjoy a lot
to play the spy class.
- Thanks to Dr. ROCKZO for his great work with the posters and the pacience to deal with my
suggestions
- Thanks to the Argentina community for the early help with the alpha (y disculpen todas las
veces que no pude meterme a mix ni a los pub para terminar esto)
- Thanks to Kakihara, Squible, Dr. ROCKZO, The Big Cheese, Wiseguy149, Fede22 and Arctic Vampire
for their help beta testing the last versions of the beta. Special thanks to Arctic Vampire
for lending me the server to try this map in multiplayer
- Thanks to the following mappers for inspirating this work
   * tr_airshot, by gmannick
   * tr_aim, by metalpiss
   * tr_airstab, by The Ultimate Potato (also thanks to him for the good ideas and tips while I was mapping)
- Thanks to tf2maps.net community for the useful tutorials and answering some difficult
questions about hammer. Special thanks to A Boojum Snark for his useful addon to hammer.