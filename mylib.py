# Import some modules... (I have to)
from random import *
from string import *
from msvcrt import getwch
import curses; import string; from time import *
from sys import *; import keyboard as kb
import os; from winsound import Beep;

# Global variables:
# Remember to create a Filename variable!
Numbers = tuple("0123456789")
Alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-<> '
DictW = {
  10: 'A', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f', 16: 'g', 17: 'h', 
  18: 'i', 19: 'j', 20: 'k', 21: 'l', 22: 'm', 23: 'n', 24: 'o', 25: 'p',
  26: 'q', 27: 'r', 28: 's', 29: 't', 30: 'u', 31: 'v', 32: 'w', 33: 'x',
  34: 'y', 35: 'z'
}
NoteDict = {
    'C2':  65,'C#2':  69,
    'D2':  73,'D#2':  78,
    'E2':  82,
    'F2':  87,'F#2':  93,
    'G2':  98,'G#2': 104,
    'A2': 110,'A#2': 117,
    'B2': 123,
    'C3': 131,'C#3': 139,
    'D3': 147,'D#3': 156,
    'E3': 165,
    'F3': 175,'F#3': 185,
    'G3': 196,'G#3': 208,
    'A3': 220,'A#3': 233,
    'B3': 247,
    'C4': 262    
}

###          My "Classes":          ###
# ----------------------------------- #
class Format:
  def OUT(hex: str,text: str):
    leng = len(hex)
    if hex.startswith('#') and leng == 7: hex = hex.removeprefix('#')
    else: raise TypeError('Not a hexcode.')

    for char in Alphabet[6:26]+Alphabet[32:]:
      if char in hex: raise TypeError('Not a hexcode.')

    r,g,b = hex_to_rgb(hex)
    return "\x1b[38;2;{};{};{}m{}\x1B[0m".format(r, g, b, text)
    
  class synhl:
    """Short for syntaxhighlight."""
    def run(dict: dict,ioro: str):
      str = ''
      for string,hex in dict.items():
        str += Format.OUT(hex,string)
      if ioro in ['o','out','print']:
        return print(str)
      elif ioro in ['i','in','input']:
        return input(str)

  red = '#C91B1B'; orange = '#F34421'; yellow = '#FFD622'
  lime = '#91E630'; green = '#07BD0D'; teal = '#1DC25F'
  aqua = '#97ECFF'; blue = '#3C71D3'; violet = '#411CAE'
  magenta = '#B519AD'; rose = '#BD2D54'; black = '#000000'
  white = '#FFFFFF'; grey = '#6E6E6E'
    
###         My "Functions":         ###
# ----------------------------------- #

def isPrime(num1):
  for i in range(2,num1):
    if num1 % i == 0: return False
    elif num1 % i != 0: pass
  return True

def mFib(num1):
  if num1 <= 2: return 1
  res = mFib(num1-1) + mFib(num1-2)
  return res

def mStsquad(num1):
  if num1 < 1: raise ValueError('Number is too small.')
  elif num1 == 1: return 1
  else: res = num1*(num1+1)/2
  return res

def mWaitingTxt(text,times,dur):
  print("\r" + text + "   ", end="")
  sleep(dur)
  for i in range(0,times):  
    print("\r" + text + ".  ", end="")
    sleep(dur)
    print("\r" + text + ".. ", end="")
    sleep(dur)
    print("\r" + text + "...", end="")
    sleep(dur)

def mPrimeTable(start,end,col):
  count = 0
  for i in range(start,end+1):
    if i > 1 and i < 10 and isPrime(i) == True: 
      print("0"+str(i)+"  ",end='')
      count += 1
    elif i > 10 and isPrime(i) == True: 
      print(str(i)+"  ",end='')
      count += 1

    if count % (col+1) == 0: print(''); count = 1

def spam(numberOfCharacters: int,characterToSpam: str):
  output = characterToSpam*numberOfCharacters
  return output

def rhg():
  out = lambda: randint(0,255)
  print( "#%06X" % (out()) )
  return out

def check(string: str,checkval: tuple | str):
  '''Check if a tuple of characters are in str (you will not understand this)'''
  if isinstance(checkval,str):
    for char in string:
      if char not in tuple(checkval):
        return False
    return True
  elif isinstance(checkval,tuple):
    for char in string:
      if char not in checkval:
        return False
    return True

def isint(*args: str):
  for arg in args:
    try:
      int(arg)
    except ValueError:
      return False
  return True

def isfloat(*args: str):
  for arg in args:
    try:
      float(arg)
    except ValueError:
      return False
  return True

def ishex(*args: str):
  for arg in args:
    if arg.startswith('#'):
      if check(arg[1:],('0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f')): continue
      return False
    else: return False
  return True  

def red(text: str):
  """This function turns text red."""
  return Format.OUT(Format.red,text)
def blue(text: str):
  """This function turns text blue."""
  return Format.OUT(Format.blue,text)
def green(text: str):
  """This function turns text green."""
  return Format.OUT(Format.green,text)

def hex_to_rgb(hexc: str):
  try:
    hexc = hexc.lstrip('#')
    leng = len(hexc); le3 = leng//3
    return tuple(int(hexc[i:i+le3],16) for i in range(0,leng,le3))
  except: print("You're wrong!")

def caesar(shift: int, encstr: str):
  Alphabet = string.ascii_lowercase
  sh_Alphabet = Alphabet[shift:] + Alphabet[:shift]
  print(sh_Alphabet+'\n'+Alphabet)
  table = str.maketrans(Alphabet,sh_Alphabet)
  return encstr.translate(table)

def base(num: int, base: int):
  """Convert only POSITIVE integers to any base."""
  temp = ''
  if num > -1:
    if num == 0:
      return [0]

    digits = []
    while num:
      digits.append(num % base)
      num //= base
      pass
    for digit in digits:
      if digit < 10:
        temp += f'{digit}'
      else:
        match digit:
          case 10: temp += 'A'
          case 11: temp += 'B'
          case 12: temp += 'C'
          case 13: temp += 'D'
          case 14: temp += 'E'
          case 15: temp += 'F'
          case 16: temp += 'G'
          case 17: temp += 'H'
          case 18: temp += 'I'
          case 19: temp += 'J'
          case 20: temp += 'K'
          case 21: temp += 'L'
          case 22: temp += 'M'
          case 23: temp += 'N'
          case 24: temp += 'O'
          case 25: temp += 'P'
          case 26: temp += 'Q'
          case 27: temp += 'R'
          case 28: temp += 'S'
          case 29: temp += 'T'
          case 30: temp += 'U'
          case 31: temp += 'V'
          case 32: temp += 'W'
          case 33: temp += 'X'
          case 34: temp += 'Y'
          case 35: temp += 'Z'
    return temp[::-1]
  else: raise ValueError('Number is not positive.')

def menu(title, classes, char, color='white', title_color='white'):
  # define the curses wrapper
  def character(stdscr,):
    attributes = {}
    icol = {
      1:'blue',
      2:'green',
      3:'cyan',
      4:'red',
      5:'magenta',
      6:'yellow',
      7:'white'
    }
    # Now I can understand this wow :O It makes this easier to read!
    col = {v: k for k, v in icol.items()}

    # DC the background color
    bc = curses.COLOR_BLACK

    # Make the normal format
    curses.init_pair(1, 7, bc)
    attributes['normal'] = curses.color_pair(1)

    # Make the highlighted format
    curses.init_pair(2, col[color], bc)
    attributes['highlighted'] = curses.color_pair(2)

    # Make the title format
    curses.init_pair(3, col[title_color], bc)
    attributes['title'] = curses.color_pair(3)
    attr2 = attributes['title']
    # Handle da menu
    c = 0
    option = 0
    while c != 10:
      
        stdscr.erase() # Clear da screne

        # Add the title
        stdscr.addstr(f'{title}\n', attr2)

        # Add the options
        for i in range(len(classes)):
            # Handle da colora
            if i == option:
                attr = attributes['highlighted']
            else:
                attr = attributes['normal']
            
            # Add the options 2: Electric Boogaloo
            stdscr.addstr(f'{char}', attr)
            stdscr.addstr(f'{classes[i]}' + '\n', attr)
        c = stdscr.getch()

        # Handle da arrow keyz
        if c == curses.KEY_UP and option > 0:
            option -= 1
        elif c == curses.KEY_DOWN and option < len(classes) - 1:
            option += 1
    return option
  return curses.wrapper(character)

def rdanimat(*seq: str,fps: float,LoopMode: bool,LoopTime: int):
  os.system('cls')
  if LoopMode is False:
    for str in seq:
      if str == 'cls':
        sleep(1/fps)
        os.system('cls')
      else:
        print(str,end='\n')
  else:
    for i in range(0,LoopTime):
      for str in seq:
        if str == 'cls':
          sleep(1/fps)
          os.system('cls')
        else:
          print(str,end='\n')

def beep2(freq: str | int,leng: str):
    if not leng.endswith('s'):
      raise ValueError("The length parameter must end with 's'.")
    else:
      if leng.endswith('ms'):
        leng = leng.strip('ms')
        tim = 1
      else:
        leng = leng.strip('s')
        tim = 1000
        
      if isint(leng):
          if int(leng) > 0:
              if isinstance(freq,int):
                  Beep(freq,int(leng)*tim)
              elif isinstance(freq,str):
                if freq in NoteDict.keys():
                  for k,v in NoteDict.items():
                      if freq == k:
                        Beep(v,int(leng)*tim)
                      else:
                        pass
                else:
                  raise ValueError("The frequency parameter have to be in Western music System (only sharp, no flat). For more info, read: "+blue("https://en.wikipedia.org/wiki/Scale"))
              else:
                raise TypeError("The frequency parameter have to be type <str> or <int>.")
          else:
            raise ValueError("The length parameter have to be positive")
      else:
          raise ValueError("The length parameter have to be able to convert to <integer> type.")
    
def eval2(arg: str):
  list = []; number = ''
  arg = arg.replace(' ','')
  if arg != '' and arg != None and not check(arg,'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$^&_[]\\|{};\'"?`~'):
    print(eval(arg))
  else:
      raise ValueError("Can't calculate this string bruh.")

def progbar(quote: str='\n',prefix = '',suffix = '',length = 100,fill = '▮'):
    os.system('cls')
    filled = ''
    unfilled = '-'*length
    bar = filled + unfilled
    for i in range(length+1):
        filled = fill*i
        unfilled = '-'*(length-i)
        bar = filled + unfilled
        print(f'{prefix} {bar} {i}% {suffix}',end='')
        print('\n'+quote,end='\033[F\r')
        sleep(0.005)
    print('\n')

# print('~ Prepare for the mylib.py experience! ~')