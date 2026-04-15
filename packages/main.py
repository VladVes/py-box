import greet
from sum import sum_ab, default_a as val_x, default_b as val_y
from constants import *

import sp
import sp.functions
import sp.constants

from sp.functions import run
from sp.constants import DEFAULT_URL

hi = greet.say_hi("Ivan")
print(hi)
print(greet.text)

# from constants
print(DEFAULT_DATABASE_URL)
print(sum_ab(val_y, val_x))


# -------------
print(sp.NAME)
sp.functions.run()
print(sp.constants.DEFAULT_URL)
run()
print(DEFAULT_URL)
