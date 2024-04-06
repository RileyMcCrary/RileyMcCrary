from pyfiglet import Figlet
import sys

f = sys.argv[1]
type = Figlet(font=f)
user = input('Input: ')
print('Output: \n' + type.renderText(user))