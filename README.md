# Tvde1's TF2 Configs

## Introduction
Hi!
These are my TF2 configs for all classes.
I'll try to comment on what every line does, if there are any questions, just ask.
Feel free to edit the configs to your own liking!

## General information on scripting
From the Official Team Fortress Wiki https://wiki.teamfortress.com/wiki/Scripting
> Scripting is the use of configuration files (.cfg) to create new keybinds and aliases automating complex behaviors and console command sequences. Unlike hacking, scripting is built into Team Fortress 2 and is not banned by VAC (Valve Anti-Cheat). Uses of scripting vary from simply binding a key to a command to self-referential loops and nested aliases that redefine one another. Any functionality that can be created with scripting can also be accomplished without it, but scripting allows these functionalities to be used in the heat of battle.

## List of default keys
This is a list of default keys for the PC version of Team Fortress 2.
https://wiki.teamfortress.com/wiki/List_of_default_keys

## Installation
You can download this GitHub repository as a .zip and extract all the files into
- Windows: C:\Program Files (x86)\Steam\SteamApps\common\Team Fortress 2\tf\cfg\
- OSX: Volume/Users/~username/Library/Application Support/Steam/SteamApps/common/team fortress 2/tf/cfg/
- Linux: ~/.local/share/Steam/steamapps/common/Team\ Fortress\ 2/tf/custom/

You can delete README.md though as it serves no function in game.  
Also make sure you have no scripts in `\Team Fortress 2\tf\cfg` that have the same name as these.
You should update it regularly, and scan through the README.md to see if I have added something.

## Maps
As you can see, I have a few aliasses that start up maps. You can only use them if you've downloaded the maps. It is optional, you don't have to download them.
Those maps are
- tr_walkway_rc2
- tr_aim
- tr_aim_practice

## Keybinds

### All classes: (Some classes may overwrite these)

#### High frequency buttons:
| Button(s) | Function | Extras |
| --- | --- | --- |
| W A S D | Regular movement | I have added a null-movement script. |
| SPACE | Jumps + crouches | This button jumps and crouches at the same time. Still crouches when you hold the spacebar. |
| CTRL | Crouches | |

#### Mouse:
| Button(s) | Function | Extras |
| --- | --- | --- |
| Mouse 1 | Attacks | Just the same as default |
| Mouse 2 | Uses attack 2 | E.g. equipping an invisi-watch, or zooming in as sniper. |
| Mousewheel Up | Primary weapon | Equips the primary weapon. **NOTE: Some classes overwrite this.**|
| Mousewheel Down | Secondary weapon | Equips the secondary weapon. **NOTE: Some classes overwrite this.**|
| Mousewheel Click (Mouse 3) | Melee | Equips the melee weapon and keeps swinging it until you let go if it. It will still be equipped. **NOTE: Some classes overwrite this.**|

#### Special Keys:
| Button(s) | Function | Extras |
| --- | --- | --- |
| E | Call for medic | I shouldn't have to explain this. |
| ALT | Call for spy | Just calls out that there is a spy. |
| F | Inspect | Inspects the player aimed at, or shows an animation of your current reskin weapon. |
| R | Reload and disguise team | Use this to manually reload, or change the disguise team as a spy. |
| SHIFT | Used for class-switching and voice commands | If you hold shift, you can use voice commands and class switching. Some classes will add extra usages to this button. |

###### Shift usage:  
When shift is held down, these buttons will serve diffrent purposes than if shift hadn't been held down. When shift is released, all buttons will be bound to the previous binds again.  
Also, some classes will make use of shift. It'll switch what a button does.

| Button(s) | Function | Extras |
| --- | --- | --- |
| E | Yes! Voice | Says "Yes!" with a voice command. |
| R | No! Voice | Says "No!" with a voice command. |
| F | Thanks! Voice | Says "Thanks!" with a voice command. |
| G | Nice shot! Voice | You have to be nice somethimes. |
| Q | Battlecry voice | Look at enemies with your melee equipped to say something witty. |
| T | Trade binds | These will say your trade binds in chat. (in chat.cfg) |
| C | Noob talk | This will say a noob line (from chat.cfg). |
| 1 to 9 | Class switching | Press 1 - 9 to swich to the desired class. I advise you to use this and not the regular class swiching. |

#### Low frequency buttons:
Most of these stayed the same.

| Button(s) | Function | Extras |
| --- | --- | --- |
| L | Dropitem | Drops the intel/other stuff when carrying it. |
| M | Open loadout | Goes directly to the loadout of the class you're in. |
| N | Open backpack | Opens your backpack. |
| X | Voice menu 1 | Opens voice menu 1. |
| C | Voice menu 2 | Opens voice menu 2. |
| V | Voice menu 3 | Opens voice menu 3. |
| Z | Spray | Spray your spray. |
| T | Open chat | Opens server chat. |
| Y | Team chat | Opens chat for your team to see only. |
| K | Die | You kill yourself. |
| G | Taunt | Uses your taunt menu. Press twice to use the item taunt. (Or once if you have no other taunts equipped.) |
| , | Change class | Changes classes. But I advise you to use the SHIFT + 1-9 to change classes. |
| . | Change team | Change teams. |
| J | Accept connect | Press this to accept if you have been asked to join a server (by a server). |
| H | Use | Use the item in your action slot. |
| U | Tauntkill | Press this to use your classes tauntkill weapon and taunt. |
| TAB | Show scoreboard | You should know that screen by now. |
| ESCAPE | Cancel | Regular escape function. |
| PGDN | First/Third person toggle | Toggles the first person world model and taunt. Just for fun. |
| \` | Developer console | You should be familiar with this, if you're on this page. |
| \ | Voice chat | Use your mic. |
| - | Decline notification | |
| = | Accept notification | |
| F1 | Vote option 1 | Usually vote yes in the tf2 voting system (kick, or next map) |
| F2 | Vote option 2 | Usually no ^ |
| F3 | Demo start | Start recording a demo. |
| Shift + F3 | Demo stop | Stop recording a demo. |
| F4 | Toggle ready | Use this to toggle your ready state in MvM and other gamemodes. |
| F5 | Screenshot | |
| F6 | Save replay | |
| F7 | Fill in an abuse report | Use it when you spot a cheater. It is pretty self explanatory. |
| F8 | Bug-fix button | If it's buggy, or something disappeared. Note: this will most likely freese your game for more than 10 seconds. Could disconnect you from game. |
| F9-F12 | Choose between presets. | Also use to quick respawn. |
| ' | Demo bookmark | If you are recording a demo and want a bookmark, use this to bookmark. |

Note: The demos will be stored in `tf\demo_[class]`. The [class] is the class thet you're playing. Also, if you make a bookmark, it'll say `Bookmark: [Class]`.

#### Numpad voice commands:
Press these key on your numpad to send insults/taunts in chat. It'll automatically rebind them to a diffrent one.  
First, select a catagory. `0`, `.` or `ENTER`. And then use the 1-9 buttons.

##### Selection
| Button(s) | Function | Extras |
| --- | --- | --- |
| 1-9 | Classes | Use these for selecting the class. |
| 0 (INS) | Enemies down | Push this to use the 'enemy down' commands. It will write "Enemy ... down" in team chat. |
| . (DEL) | Enemy spy | Push this to enable the spy commands. It will write "Enemy spy disguised as ..." in team chat. |
| ENTER | Other | Push this for other commands. They are listed below. |

So after 0 (INS) and . (DEL), press 1-9 for the class.

##### Other
These take place when the KP enter has been activated.

| Button(s) | Function | Extras |
| --- | --- | --- |
| 1 | Sentry down | Lets your team know that a sentry is down. |
| 2 | Teleporters down | Lets your team know that one or more teleporters are down. |
| 3 | Everything down | Lets your team know the whole nest is down. |
| 4 | Uber pop | Select the class they popped on. |
| 5 | Kritz pop | Select the class they popped on. |
| 6 | Quick fix pop | Select the class they popped on. |
| 7 | Push | Let's all push (go in). |
| 8 | Fall back | We need to fall back. |

When you press 4 or 5 to show an uber pop, press 1-9 to show the class they've popped on.

##### Insulting/Joking
| Button(s) | Function | Extras |
| --- | --- | --- |
| / | LMAOBOX Spam | Push these for a LMAOBOX spam line. (You won't get vac'ed!) |
| * | Insults | Push these when someone is mad. These are whole centances. |
| - | Jokes | These are just nice TF2 related jokes. |

Examples:  
If I'd press `KP 0` (Enemy down commands) and then `KP 4` (demoman), in the team chat "Enemy demoman down!" will appear.  
And if I'd press `KP .` (spy commands) and then `KP 8` (sniper), then it will write "Enemy spy disguised as sniper!" in team chat.  
Or if I'd press `KP ENTER` (other commands) and then `KP 5` and then `KP_4`, it will write "They have popped kritz on the Demoman." in team chat.


### Class specific:

#### Scout:
| Button(s) | Function | Extras |
| --- | --- | --- |
| Mouse 4 | Sandman | Hold it to launch a sandman ball. Let it go to return to last selected weapon. |
| Q | Dispenser here! | Press this to use the "Need a dispenser here!" voice command. |

#### Soldier:
| Button(s) | Function | Extras |
| --- | --- | --- |

#### Pyro:
| Button(s) | Function | Extras |
| --- | --- | --- |
| Mouse 2 | Airblast | It'll switch to your flamethrower and airblast. |
| SHIFT + Mouse 2 | Flare airblast | Swaps to the flare gun after you ariblast. |
| Mouse 4 | Viewmodel off | Click this to turn the flamethrower viewmodel (and flames) on/off. | 

#### Demoman:
| Button(s) | Function | Extras |
| --- | --- | --- |

#### Heavy:
| Button(s) | Function | Extras |
| --- | --- | --- |
| Mouse 4 | Throw sandvich | Hold it to throw the sandvich (on the ground or to a player) and let go if it's thrown. |
| Shift + Mouse 4 | Eat sandvich | Hold to eat sandvich. You can let go if you're eating. |
| Q | Pootispow | Press it. It will pootispow. |
| P | Pootis Spam | Spam it while **in spawn** to keep saying pootis. |

#### Engineer:
| Button(s) | Function | Extras |
| --- | --- | --- |
| Q | Fastbuild Sentry | Quickly builds a sentry. This will destroy you old sentry. **Bug: It may fire your gun once accidentally. Switch to your melee first if you don't want to lose revenge crits.** |
| MOUSE 4 | Build things | Push this to use 1-4 to build equipment. |

When you push mouse 4, the 1, 2, 3 and 4 keys will change into the building menu:
* 1 is for building a sentry.
* 2 is for building a dispenser.
* 3 is for building a teleporter entrance.
* 4 is for building a teleporter exit.  

When you have used a key. It will go back to being the default binds (1 for slot1 etc).

Also, you will say "Dammit!" every time you use left mouse button.

#### Medic:
| Button(s) | Function | Extras |
| --- | --- | --- |
| Mouse 2 | Uber | Switches to medigun and ubers. Also writes it in team chat. |
| Mouse 4 | Fake uber | You will say the Uber Ready voice command while you say that it's fake in your team chat. |
| Shift + Mouse 4 | Mask uber | Press this when you are at 98/99% ubercharge to suppress the voice comm. |
| Q| Radar | Hold this to see all your teammates. |

#### Sniper:
| Button(s) | Function | Extras |
| --- | --- | --- |

You will say "nice shot!" every time you attack.

####Spy:

| Button(s) | Function | Extras |
| --- | --- | --- |
| Mouse 1 | Attack | |
| Mouse 2 | Secondary attack. | Uses invisi watch or dead ringer. It will turn on the viewmodel if you have equpped the revolver. It will also turn the viewmodel off again after undeploying it if you still have the revolver equipped. |
| Mousewheel up | Equip primary | Equips primary weapon and removes viewmodel. Using any other weapon will show the viewmodel again. |
| Mouswheel down | Equip knife | |
| Mouse 3 | Use the disguise menu. | Use 'R' to swap between teams. |
| Mouse 4 | Sap-o-matic | Hold this to bring out your sapper and start sapping. Let go of it to return to your knife. |
| Shift + Mouse 4 | Lastdisguise | Use this to disguise again, or change the weapon your disguise is holding. |
| Q | Zoom script | You will zoom in (low FOV). Press it again to zoom out. |

Note: If the viewmodels are not being hidden, look at spy.cfg. I have explained there what lines to comment and uncomment (with //).

## Console Commands:
| Command | Meaning |
| --- | --- |
| `walkway` | Loads the tr_walkway map and executes some commands to make it work. |
| `aim` | Same as above, but then with the map tr_aim. |
| `aim_training` | Same as above, but then with the map tr_aim_training. |
| `comp_g` | Switches to my comp graphics config. |
| `good_g` | Uses my good graphics config. Usually for playing pubs. This is the default one. |
| `ultra_g` | Swtiches to the ultra graphics. Not advised unless you have a good pc. |

Changing graphics, can (and will) freze your game. But only when changing to `good` or `ultra`.

## Final words.
Feel free to edit this to your own liking. But please refer to me (and this page) if you will upload this code somewhere.
Message me if you encounter any bugs, I'd be glad to help and fix it. You can also message me if you know any improvements.  
Also, check out [my youtube channel](https://www.youtube.com/user/1tvde1) for some cool TF2 videos! (Mostly spy frags and fun related.)

#### P.S.
You can bind a lenny face to KP_PLUS (the plus on the numpad). It won't unbind it.
