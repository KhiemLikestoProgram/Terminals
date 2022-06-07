from webbrowser import open_new_tab
from mylib import Format as F,menu,isint,ishex,check,progbar,Alphabet,mWaitingTxt
from games import pong,hangman
from getpass import getuser
from msvcrt import getwch
from rich.table import Table; from rich.console import Console
from rich.tree import Tree
import platform, os, keyboard as kb, time

""" DOC: KShell.py 
    This is kShell, an program that is easy to understand and to use (but only run on Windows). If you want it to run on OSX or *nix, call some Bash programmer to help you or something. I'm not even an adult XD. OK I'll documented this later.
"""
# Renaming functions to read more easier
h = F.OUT; gotofaw = open_new_tab

# Variables (sort dictionaries)
SYS_COLOR = ''; SYS_PROMPTNAME = ''
SUPPORTED_EXT = ['.py','.html','.python','txt','img','snd','vid']
COMMAND_DICT = {
  'q': 'Exits the shell',
  'sound': 'Play a sound (use open will open cmd at the directory)',
  'info': 'Get this machine or this shell\'s info',
  'open':'Open a file or website',
  'cls':'Clears the screen',
  'games':'Show all shell\'s games',
  'code': 'Simple built-in editor for typing',
  'shell': 'Do changes to the shell itself',
  'help': 'Help users (but usually me)',
  '$[str]': 'Create a variable',
  '@[str]': 'Go to [str] directory',
  'time': 'Get current location\'s time.'}
HOST_LIST = ['100','110','120','130','140','150','160','170','180','190','250']
INVALID_NAMES = ['kkk','KKK','$$$','','q']
TEMPVARS = {'$SHELLNAME':os.path.basename(__file__.removesuffix('.py'))}
SYS_COLORS = [attr for attr in dir(F()) if not callable(getattr(F(),attr)) and not attr.startswith("__")]
SYS_VER = 'Alpha 1.3.5'

# Functions
def invalid(name: str):
    return h(F.red,f'Bad {name}.')
def typename():
    mode = menu('Choose a mode:',['Hangman','Input','Preset'],'❯ ','yellow','green')
    print(h(F.aqua,'Enter your name (Maximum 32 characters long):'))
    while 1:
      try:
        if mode == 0:
          unfilled = '_'*12; filled = ''; res = filled+unfilled
          while True:
            print(res,end='\r')
            char = getwch()
            match char:
                case '\r':
                    new_name = res.removesuffix(unfilled)
                    break
                case '\x08':
                    if len(filled) > 0:
                        print('\x1b[2K',end='')
                        filled = filled[:-1]
                        unfilled = '_'+unfilled
                case _:
                    if len(filled) < 12:
                      print('\x1b[2K',end='')
                      unfilled = unfilled[1:]
                      if char in Alphabet:  
                        filled += char
                      else: filled += ' '
            res = filled + unfilled
        elif mode == 1:
          new_name = input(h(F.lime,'?SYS_PROMPTNAME = '))
          for char in new_name:
            if char not in Alphabet[:-1]:
              new_name = new_name.replace(char,'',1)
        elif mode == 2:
          SYS_PROMPTNAME = 'qwertyuiop'; SYS_COLOR = F.aqua; HOST = 'lemon'
          break
        g = SYS_PROMPTNAME = new_name
        if len(g) <= 12 and g not in INVALID_NAMES:
            print(h(F.grey,'OK, your name is '+g+', right?'),end=' ')
            yn = input().lower()
            if yn == 'y':
                while True:
                  m = menu('Choose a color:',SYS_COLORS,'❯ ','yellow','green')
                  SYS_COLOR = getattr(F,SYS_COLORS[m])
                  print(h(F.grey,'OK, you choose '+SYS_COLORS[m]+', right?'),end=' ')
                  yn = input().lower()
                  if yn == 'y':
                    while True:
                      g = menu('Choose a port:',HOST_LIST+['Other'],'❯ ','yellow','green')
                      try:
                        HOST = HOST_LIST[g]
                      except IndexError:
                        HOST = input('Choose a port: ').split()[0]
                        if isint(HOST):
                          if int(HOST) > 0:
                            print(h(F.grey,'OK, port:'),h(F.yellow,HOST)+h(F.grey,'.'),end=' ')
                            yn = input().lower()
                            if yn == 'y':
                              break
                            elif yn != 'n': print(h(F.red,"Can't handle other characters."))
                          else:
                            print(h(F.red,'HOST must be a positive integer.'))
                        else:
                          print(h(F.red,'HOST must be a positive integer.'))
                  elif yn != 'n': print(h(F.red,"Can't handle other characters."))
                break
            elif yn != 'n': print(h(F.red,"Can't handle other characters."))
        else: print(h(F.red,'Illegal name.\n'))
      except IndexError:
        print(h(F.red,'You are missing some arguments!'))
    return SYS_PROMPTNAME,SYS_COLOR,HOST
def beta_shell(color, prompt):
  while True:
      try:
        print(h(color,prompt+h(F.grey,'-test'))+h(F.lime,'~')+h(F.green,'$ '),end='')
        userin = input('\x1b[38;2;136;247;32m').split()
        if userin[0] in ['quit','q','exit']: break
        elif userin[0] in ['rr','rickroll','nggyu','never_gonna_give_you_up']:
          gotofaw('https://youtube.com/watch?v=dQw4w9WgXcQ')
        elif userin[0] in ['table']:
          os.system('cls'); con = Console()
          table = Table(title='Sample Table')
          table.add_column('Sample 1',style='cyan',justify='center',no_wrap=True)
          table.add_column('Sample 2',style='cyan',justify='center',no_wrap=True)
          table.add_column('Sample 3',style='cyan',justify='center',no_wrap=True)
          table.add_row('69','420','21')
          table.add_row('42','13','morbius')
          table.add_row('Bruh','wot','Sans')
          con.print(table)
        elif userin[0] in ['tree']:
          os.system('cls'); con = Console()
          tree = Tree('Great-Grandfather')
          gr = tree.add('Grandfather')
          gr.add('Father').add('Mother').add('Me!'); gr.add('Aunt'); gr.add('Aunt 2'); gr.add('Uncle')
          tree.add('Granduncle')
          tree.add('Grandaunt')
          con.print(tree)
        elif userin[0] in ['cls','clear','clearscr']:
          os.system('cls')
      except IndexError:
        print(h(F.red,'You are missing some arguments!'))
      except Exception as e:
          print(h(F.red,'Error: ')+str(e))
      
def shell(color,prompt,host):
    print(h(F.white,
          '\x1b[5mkShell {SYS_VER} @Khiem2773 2022\n'+
          'No Copyright 2022-2022 Nguyen Tran Gia Khiem\x1b[25m'))
    while True:
      try:
        print(h(color,prompt)+h(F.lime,f'@{h(F.yellow,host)}~')+h(F.green,'$ '),end='')
        userin = input('\x1b[38;2;32;242;174m').split()
        if userin[0].lower() in ['quit','q','exit']:
            # mWaitingTxt('\x1b[5;0mShutting down',3,0.8)
            # print('\nBYE!')
            break
        elif userin[0] in ['sound']:
            g = ''
            for i in userin[1:]:
                g += i + ' '
            os.system('start wmplayer '+g)
        elif userin[0] == prompt:
            if prompt not in COMMAND_DICT.keys():
              print(h(F.white,'You are special! If you can dream about it, you definitely can do it!'))
            else: print(h(F.red,'You are trolling me, right?'))
        elif userin[0] in ['time']:
            if userin[1] in ['web','-w']:
                gotofaw('https://time.is')
            elif userin[1] in ['1']:
                print(time.strftime('%d/%m/%Y %H:%M:%S'))
            elif userin[1] in ['2']:
                print(time.strftime('%b %#d %Y %H:%M:%S'))
            elif userin[1] in ['3']:
                print(time.strftime('%d/%m/%Y %I:%M:%S %p'))
            elif userin[1] in ['4']:
                print(time.strftime('%b %#d %Y %I:%M:%S %p'))
            else: print(invalid('parameter'))
        elif userin[0] in ['info']:
            if userin[1] in ['this','machine','-m']:
                uname = platform.uname()
                print(h(F.lime,'\nSYSTEM: ') + uname.system)
                print(h(F.lime,'COMPUTER_NAME: ') + uname.node)
                print(h(F.lime,'RELEASE: ') + uname.release)
                print(h(F.lime,'VERSION: ') + uname.version)
                print(h(F.lime,'MACHINE: ') + uname.machine)
                print(h(F.lime,'PROCESSOR: ') + uname.processor + '\n')
            elif userin[1] in ['program','-p','prog']:
                print(h(F.lime,'\nNAME: ') + os.path.basename(__file__).removesuffix('.py'))
                print(h(F.lime,'VERSION: ') + SYS_VER)
                print(h(F.lime,'AUTHOR: ') + 'Nguyen Tran Gia Khiem')
                print(h(F.lime,'CODE: ') + '5839534345' + '\n')
            else: print(invalid('parameter'))
        elif userin[0] in ['open']:
            g = ''
            for i in userin[1:]:
                g += i + ' '
            g = g.removesuffix(' ')
            os.system('start '+g)
        elif userin[0] in ['cls','clear','clearscr']:
            os.system('cls')
        elif userin[0] in ['games']:
            ch = menu('Choose a game',['Pong','Hangman'],'❯ ','yellow','cyan')
            match ch:
                case 0: pong()
                case 1: hangman()
        elif check(userin[0][1:],'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm_-') and userin[0][0] == '$':
            if userin[1] in ['=']:
              if check(userin[2],'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm_-'):
                temp = userin[0]
                tempval = userin[2]
                TEMPVARS.update({temp: tempval})
              else: print(h(F.red,invalid('variable value')))
            elif userin[1] in ['-o']:
                if userin[0] in TEMPVARS.keys():
                    if TEMPVARS.get(userin[0],None) is not None:
                        print(TEMPVARS.get(userin[0]))
                    else: print(h(F.red,'Variable does not exist.'))
                else: print(h(F.red,'Variable does not exist.'))
            elif userin[1] in ['del','-d']:
                if userin[0] in TEMPVARS.keys():
                    TEMPVARS.pop(userin[0])
                else: print(h(F.red,'Variable does not exist.'))
            else: print(invalid('parameter'))
        elif userin[0] in ['code']:
          if userin[2] in SUPPORTED_EXT:
            if isint(userin[1]):
              if int(userin[1]) > 0:
                os.system('cls')
                lines = ''
                for i in range(1,int(userin[1])+1):
                    lines += input(h(F.white,i)+' ') + '\n'
                fname = input('Save directory: ')
                with open(fname,'w') as f:
                    f.write(lines)
                os.system(f'run {userin[2]} {fname.removesuffix(".py")}')
              else: print(h(F.red,invalid('number of lines'))) 
            else: print(h(F.red,invalid('number of lines')))
          else: print(h(F.yellow,'W: Unsupported extension.'))
        elif userin[0] in ['shell','shl']:
            if userin[1] in ['config','-c']:
              while True:
                ch = menu('Configuration',['Change prompt color','Change prompt name'],'❯ ','yellow','cyan')
                match ch:
                  case 0:
                    a = input(h(F.white,'Choose a color: '))
                    if ishex(a): color = a; break
                    else: print(h(F.red,invalid('color')))
                  case 1:
                    a = input(h(F.white,'Choose a name: '))
                    if a not in INVALID_NAMES:
                      for char in a:
                        if char not in Alphabet[:-1]:
                          a = a.replace(char,'',1)
                      prompt = a; break
                    else: print(h(F.red,invalid('name')))
            elif userin[1] in ['spam']:
                for i in range(943):
                    print('kshell',end=' ')
                print('')
            else:
                print(h(F.red,invalid('parameter')))
        elif userin[0] in ['help','?']:
            os.system('cls')
            print(h(F.white,'This is kShell, a terminal program that you can only run on Windows =) btw it is very cringey'))
            print(h(F.aqua,'---------- COMMAND LIST ----------'))
            for cmd,desc in COMMAND_DICT.items():
                print(f'{cmd:10} - {h(F.lime,desc)}')
            while 1:
                if kb.is_pressed('esc') or kb.is_pressed('q'):
                    os.system('cls')
                    break
        elif userin[0][0] in ['@']:
            match userin[0][1:].lower():
              case 'localappdata':
                os.system('start %LOCALAPPDATA%')
              case 'appdata':
                os.system('start %APPDATA%')
              case 'temp':
                os.system('start %TEMP%')
              case 'user':
                print(h(F.aqua,'User:'),h(F.violet,getuser()))
              case _:
                print(invalid('directory'))
        elif userin[0] in ['test','dev']:
          beta_shell(color,prompt)
        else:
            print(h(F.red,invalid('command name')))
      except IndexError:
        print(h(F.red,'You are missing some arguments!'))
      except Exception as e:
          print(h(F.red,'Error: ')+str(e))

# Program
name,color,host = typename()    
progbar('','Running...','',100)
shell(color,name,host)