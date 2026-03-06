# Mass command pasting script for MC:BE

This script reads the commands in a text file, and pastes and runs them one-by-one in the minecraft chat. This will probably work in java as well as bedrock edition, but i haven't tested it so i can't technically say for certain. There's definitely better ways of doing this in JE regardless without this weirdness.

## Usecase/Purpose

If you just want to know how to use the script, skip this section, it's not important.

The specific problem i encountered that made me in need of this script was porting minecraft structure blocks onto a friend's minecraft world. Structure blocks are local to specific worlds, so this cannot be done without accessing the files of the world. In this situation, my friend played on console and either didn't have the means to or didn't understand how to access these files, meaning that i couldn't send a structure across, or install a datapack.

Instead, I found [a website](https://mcbe-essentials.github.io/structure-to-function/) that allowed me to convert structure block NBT data to a .mcfunction text file. The specific output of this website is what this script is designed around. What that actually means for the use of this script is detailed in How To Use, but a simple text file with nothing but ordinary commands separated by newlines will work fine, it just has a tiny bit of extra support for those files.

Anyway, now thanks to that website, i had a sequence of commands to generate the structure. Unfortunately, BE commands blocks do not support having multiple commands in one command block, and using chain commands would be tedious, to say the least. So instead I simply wrote this script to do all the command running for me. Voila.

## How To Use

If you do not have them already, install pyautogui and pyperclip using 
```
pip install pyautogui pyperclip
```
I'm under the impression that these should work on Mac on Linux (i'm on windows).
 
Open a minecraft world and tab out to the command line. If you are on a server and tab out while in full screen mode, you may disconnect, so first switch to windowed mode through the ingame settings. 

Important: do not open the chat before running the script, or the first command will be skipped.

Call the script with the required argument:
```
py sendCommands.py --file-path [path_to_command_text_file]
```
<sup><sub>(short: -f)</sub></sup>
This argument expects a path to a text file containing a sequence of commands separated by newlines.
The script will ignore comments made using the # symbol, and will assume that every uncommented line is a command. Commands are not required to be prefixed with / in the text file (This script is designed with mc functions in mind).

The script also takes the optional argument:
```
--start-delay [time_in_seconds]
```
<sup><sub>(short: -d)</sub></sup>
This is set to 3 seconds by default, giving you enough time to tab into the minecraft window and do any other quick things.

Once you run the script and wait, all the commands in the text file will run in sequence. Very complex script, I know, but it works and hopefully it will help you someday if you end up in the same situation as me.

IF SOMETHING GOES WRONG: slam your mouse into the upper right corner of the screen. This is a failsafe built into pyautogui that will terminate the script immediately.
