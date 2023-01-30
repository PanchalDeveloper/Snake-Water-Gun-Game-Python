# This is a Snake, Water and Gun Game in Python (Without Using Classes)
import random
import json
import time
import sys
#from replit import audio # For Audio on Replit
from colored import fg
from functools import reduce
from os import environ

# Extras for Text Effects
[
  clrGray, clrRed, clrBlue, clrGreen, clrSuccess, clrYellow, clrOrange,
  clrPurple
] = [
  fg('#BDC3C7'),
  fg('#7B241C'),
  fg('#3498DB'),
  fg('#229954'),
  fg('#4BB543'),
  fg('#F5B041'),
  fg('#D35400'),
  fg('#7D3C98'),
]
# Width of Window for setting text-aling to center
lineCenterSpacing = 80

# Gap of time between prints for delay
sleepTime = 0.5

# Check if Old Data is Available on a JSON File
try:
  with open('scoreboard.json') as f:
    scoreboard = json.loads(f.read())
except:
  scoreboard = {}
  with open('scoreboard.json', 'w') as f:
    f.write('')


## Writing mode Effect
def tWrite(str, startSleep=0, endSleep=sleepTime, end='\n', speed=0.01):
  time.sleep(startSleep)
  for i in str:
    time.sleep(speed)
    sys.stdout.write(i)
    sys.stdout.flush()
  if end:
    print(end)
  time.sleep(endSleep)


# Choices Which can be made by the Players
choices = {'1': '🐍 - Snake', '2': '💦 - Water', '3': '🔫 - Gun'}

rules = {
  choices.get('1'): {
    'kills': choices.get('2'),
    'getKilled': choices.get('3')
  },
  choices.get('2'): {
    'kills': choices.get('3'),
    'getKilled': choices.get('1')
  },
  choices.get('3'): {
    'kills': choices.get('1'),
    'getKilled': choices.get('2')
  }
}


# Game Score Checking Functions
def get_result(arr):
  if arr[0] == arr[1]:
    return 0
  elif rules.get(arr[0]).get('kills') == arr[1]:
    return 1
  elif rules.get(arr[0]).get('getKilled') == arr[1]:
    return -1


# Get Total Scores of the Player
def total_score(player, scoreboard=scoreboard):
  if player in scoreboard:
    try:
      res = reduce(lambda a, b: a + b, scoreboard.get(player).get('scores'))
    except:
      res = 'Scores not Found for this player.'
  return res

# Show Centered String within Box of Given Symbol
def inBoxPrint(str, space, clr=clrSuccess, symbol='*'):
  print(clr + f"{''.center(int(space / 2), symbol)}".center(space, ' '))
  print(f"{symbol + ''.center(int(space / 2) - 2, ' ') + symbol}".center(space, ' '))
  print(f"{symbol + str.center(int(space / 2) - 2, ' ') + symbol}".center(space, ' '))
  print(f"{symbol + ''.center(int(space / 2) - 2, ' ') + symbol}".center(space, ' '))
  print(f"{''.center(int(space / 2), symbol)}".center(space, ' '))

# Player Choices
yourChoices = []
botChocies = []

# Total Scores
scores = []

print(
  clrOrange +
  f"\n{' Welcome to The Snake, Water & Gun Game '.center(60, '*').center(82, ' ')}\n"
)

# Game Instructions
print(
  clrBlue, """
 Snake 🐍, Water 💦 & Gun 🔫 game is a game which requires two players 🙎🙎 both have to select something from snake 🐍 or water 💦 or gun 🔫. snake 🐍 wins over water 💦 , gun 🔫 win over snake 🐍 and water 💦 wins over gun 🔫. ultimately the player🧑 with maximum points wins 🏆 the game.
""")

print(clrOrange,
      'NOTE:-',
      clrBlue,
      'Here you will play against The Computer/BOT.',
      end='\n\n\n')

# Ask Player's Name
time.sleep(sleepTime)
tWrite(clrYellow + 'Please Enter Your Name : ' + clrGray, end='')
dialogues = [
  "Let's start the game. Get ready and let the fun begin!",
  "Let's see if you have what it takes to conquer this game!",
  "Are you ready to test your skills and challenge your luck? Let's start the game then."
]
playerName = input('').title()

try:
  # UserName of Replit Account
  username = environ['REPL_OWNER']
except:
  # If not inside Replit
  username = playerName
  

if username in scoreboard:
  tWrite(
    clrGreen +
    f"\nHi {playerName}! It seems you have already played this game here.\nWanna keep the Old Data and continue!?   [Y(Default) | N]"
    + clrGray,
    end='')
  keepData = input(' ') or 'Yes'
  # Stop Playing if Player Doesn't want to play anymore
  if keepData.lower() in ['y', 'yes']:
    pass
  elif keepData.lower() in ['n', 'no', 'erase', 'q', 'quit', 'exit']:
    del scoreboard[username]
    tWrite(clrRed + '\nYour Old Saved Data Has been Deleted Successfully.')
    tWrite(clrGreen + 'Let\'s Get Started.')
else:
  # Greet The Player
  tWrite(clrGray + f"\nHi {playerName}! {random.choice(dialogues)}\n")

# Rules\Instructions for the Game
print(clrGreen, "\nThe Choices Which can be made are: ", end='\n\n')
print(clrBlue,
      ' | '.join(choices.values()).center(lineCenterSpacing, ' '),
      end='\n\n')
print(clrGreen, "Rules for Choices are:")
for key in choices:
  print(clrBlue,
        f"[{key}] = [{choices.get(key)}]".center(lineCenterSpacing, ' '),
        end='\n\n')

# Logic for the Game
while True:
  # Give Random Choice to the Bot
  time.sleep(sleepTime * 2)
  print(clrPurple + "\nOne moment, the BOT is making it's decision...")
  time.sleep(sleepTime)
  botChoice = random.choice(list(choices.keys()))
  tWrite("The BOT has made it's Choice.")
  time.sleep(sleepTime)

  print('\n\n')
  # Show Prompt for User's Choice
  tWrite(clrYellow + 'Enter your Choice : ' + clrGray, end='')
  yourChoice = input('')
  print('\n\n')

  # Skip to the next iteration if wrong option entered
  if not yourChoice in list(choices.keys()):
    print(clrRed,
          '\nThis Option is Not Available! Try Choosing Again.',
          end='\n\n')
    continue
  else:
    print(clrGray, f"\nYou Choosed : {choices.get(yourChoice)}", end='\n\n')
    print(f"BOT Choosed : {choices.get(botChoice)}\n")

  # Append Choices and Result
  yourChoices.append(choices.get(yourChoice))
  botChocies.append(choices.get(botChoice))

  # Show Result for This Iteration
  result = get_result([choices.get(yourChoice), choices.get(botChoice)])

  # Append Score to the Score-list
  scores.append(result)

  print('\n\n')
  if (result == 0):
    
    inBoxPrint('It was a Draw', lineCenterSpacing, clrBlue, '⛑')
    # audio.play_file("./sounds/draw.mp3")  # This only works while inside the workbook Otherwise it gives an error from 'Replit Module'
  elif (result == -1):
    inBoxPrint('You Loose', lineCenterSpacing, clrRed, '☠')
    # audio.play_file("./sounds/loose.mp3")  # This only works while inside the workbook Otherwise it gives an error from 'Replit Module'
  elif (result == 1):
    inBoxPrint('Congratulations!!! You Win', lineCenterSpacing, clrSuccess, '🎖')
    # audio.play_file("./sounds/win.mp3")  # This only works while inside the workbook Otherwise it gives an error from 'Replit Module'
  print('\n\n')
  
  continueGame = input(clrGreen + 'Continue The Game!?   [Y(Default) | N]: ' +
                       clrGray) or 'Yes'
  print('\n\n')

  # Stop Playing if Player Doesn't want to play anymore
  if continueGame.lower() in ['n', 'no', 'q', 'quit', 'exit']:
    break
    
  print('\n\n')
  
  print(' [1 - 🐍 Snake | 2 - 💦 Water | 3 - 🔫 Gun] '.center(int(lineCenterSpacing - 15), '-').center(lineCenterSpacing, ' '))
  
  print('\n\n')

# Show Match-Scores
print("Match Scoreboard:-", end='\n\n')

# Headers of the Table

thirdOfSpacing = int(lineCenterSpacing / 3)
print(f"|{''.center(lineCenterSpacing - 2, '-')}|") # Multipal '-' within '|'

print(f"|{'Your Choises'.center(thirdOfSpacing, ' ')}{'BOTs Choises'.center(thirdOfSpacing, ' ')}{'Status'.center(thirdOfSpacing, ' ')}|") # Table Head Content

print(f"|{''.center(lineCenterSpacing - 2, '-')}|") # Multipal '-' within '|'


# Body of the table
for you, bot, score in zip(yourChoices, botChocies, scores):
  print(f"|{''.center(lineCenterSpacing - 2, ' ')}|") # Empty Space Within '|'
  
  match score:
    case 1:
      stat = 'WIN'
    case -1:
      stat = 'LOOSE'
    case _:
      stat = 'DRAW'

  print(f"|{str(you).center(thirdOfSpacing - 1, ' ')}{str(bot).center(thirdOfSpacing, ' ')}{str(stat).center(thirdOfSpacing - 1, ' ')}|") # Table Body Content


print(f"|{''.center(lineCenterSpacing - 2, '-')}|") # Multipal '-' within '|'
print(f"|{''.center(lineCenterSpacing - 2, ' ')}|") # Empty Space Within '|'
print(f"|{''.center(thirdOfSpacing, ' ')}{''.center(thirdOfSpacing, ' ')}{('Match Score : ' + str(reduce(lambda a, b: a + b, scores))).center(thirdOfSpacing, ' ')}|")
print(f"|{''.center(lineCenterSpacing - 2, ' ')}|") # Empty Space Within '|'
print(f"|{''.center(lineCenterSpacing - 2, '-')}|", end="\n\n") # Multipal '-' within '|'

# Create new player if doesn't exists
if not scoreboard.get(username):
  scoreboard[username] = {
    'name': playerName,
    'playerChoices': yourChoices,
    'botChocies': botChocies,
    'allChoices': list(zip(yourChoices, botChocies)),
    'scores': scores
  }
# Update player's scoreboard if already exists
else:
  scoreboard[username]['playerChoices'] += yourChoices
  scoreboard[username]['botChocies'] += botChocies
  scoreboard[username]['allChoices'] += list(zip(yourChoices, botChocies))
  scoreboard[username]['scores'] += scores

print(f"Your Total Score is now: {total_score(username, scoreboard)}".center(lineCenterSpacing, " "))
print("\n\n")
# Save Scores to a JSON File
with open('scoreboard.json', 'w') as f:
  scoreboard = json.dumps(scoreboard)
  f.write(scoreboard)
