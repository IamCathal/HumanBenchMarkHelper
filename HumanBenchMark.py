from pynput.mouse import Button, Controller
from PIL import Image
import pyscreenshot
import pytesseract
import sys
import re


def getWord(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    if re.search('(See how you compare)+', text):
        print('Error: Unexpected end of game.')
        exit()
    else:
        return text


def screenshot():
    region = pyscreenshot.grab(bbox=(700,390,1250,450))
    region.save('currentWord.png')


def isNew(currentWord, allWords):
    if currentWord in allWords:
        return 0
    else:
        allWords.append(currentWord)
        return 1

    
def playGame(allWords, userLevel):
    mouse = Controller()
    seenWords = 0
    for i in range(1,userLevel):
        screenshot()
        subject = getWord('currentWord.png')
        # if new
        if isNew(subject, allWords):
            mouse.position = (1030,505)
            mouse.click(Button.left, 1)
        # if seen
        else:
            seenWords += 1
            mouse.position = (870, 505)
            mouse.click(Button.left, 1)
        percentage = 0
        percentage = float(seenWords/i)*100
        sys.stdout.write('\r{:.2f}% overall duplicates'.format(percentage))
        sys.stdout.flush()
            

def main():
    allWords = list()
    mouse = Controller()
    userLevel = int(input('What level would you like to reach: '))
    if userLevel < 2:
        print('Error: defaulting to 10')
        userLevel = 10
    mouse.position = (950, 610)
    mouse.click(Button.left, 1)
    try:
        playGame(allWords, userLevel)
    except KeyboardInterrupt:
        exit()
    
   
if __name__ == '__main__':
    main()
