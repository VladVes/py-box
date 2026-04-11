import greet
from sum import sum_ab, default_a as val_x, default_b as val_y
from constants import *

hi = greet.sya_hi('Ivan')
print(hi)
print(greet.text)

# from constants
print(DEFAULT_DATABASE_URL)


print(sum_ab(val_y, val_x))