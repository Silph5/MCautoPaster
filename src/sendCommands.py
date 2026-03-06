import argparse
import time
import pyautogui
import pyperclip

class CommandFileProcessor:
    def __init__(self, filePath):
        self.filePath = filePath
        self.fileContents = None
    
    def readFile(self):
        with open(self.filePath, "r") as cmdFile:
            self.fileContents = cmdFile.read()
        return self.fileContents
    
    def buildCommandsList(self):
        lines = self.fileContents.splitlines()
        commands = []

        for line in lines:
            line = line.strip()
            if line[0] == '#':
                continue
            if line[0] == '/':
                line = line[:1]
            commands.append(line)

        return commands
    
class AutoPaster:
    def __init__(self, commands):
        self.commandList = commands
        self.interMenuDelay = 0.5 #MC has an annoying delay on opening and closing the chat menu where you can't type or toggle the menu again

    def openCommandMenu(self):
        pyautogui.press("/")
        time.sleep(self.interMenuDelay)
    
    def copyCommand(self, command):
        pyperclip.copy(command)

    def paste(self):
        pyautogui.hotkey("ctrl", "v")
        time.sleep(0.05)

    def runCommand(self):
        pyautogui.press("enter")
        time.sleep(self.interMenuDelay)

    def runFullCommandList(self):
        
        for command in self.commandList:
            self.copyCommand(command)
            self.openCommandMenu()
            self.paste()
            self.runCommand()

        

def main(args:argparse.Namespace):
    builder = CommandFileProcessor(filePath=args.file_path)
    builder.readFile()
    builder.buildCommandsList()
    commandList = builder.buildCommandsList()
    
    time.sleep(args.start_delay)

    paster = AutoPaster(commands=commandList)
    paster.runFullCommandList()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file-path", type=str, help="path to text file containing commands", required=True)
    parser.add_argument("-d", "--start-delay", type=float, help="delay before commands start to run, to give yourself enough time to tab into the minecraft window. Default is 3s", default=3)
    args=parser.parse_args()
    main(args)

    