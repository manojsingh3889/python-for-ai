##module are like toolbox or single file containing loosely held tools or function
## some module comes with python called built in modules while other called externals

#you can install the entire module such as
import math #this will bring all functions but need to be reffered as math.function(..)
print (math.pow(4,2))
#or import specific functions
from math import sqrt, sin # now sqrt and sin are imported directlty can be called directly
print(sqrt(16))
print (sin(60))


import random

print(random.randint(1,10))
print(random.choice(["apple", "banana"]))

import datetime
print(datetime.date.today())

import filecmp as fc #import by alias
fc.clear_cache()