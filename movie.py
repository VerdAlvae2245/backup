import time
import os

frameList= ['''
  +---+
   o  |
  /|\ |
  / \ |
  ===
''',
'''
    +---+
 \\o/    |
  |     |
  \\\\    |
     ===
''',
'''
 o   +---+
  \o     |
   |\    |
   \\\\    |
      ===
''',
'''
|_o      +---+
|  \o        |
|   |\       |
|   \\\\       |
          ===
''']

while True:
	os.system("cls")
	for frame in frameList:
		print(frame)
		time.sleep(1)
		os.system("cls")
		