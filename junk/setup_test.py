import numpy as np
from ui import read_human_setup

field = np.zeros([10, 10])
field = read_human_setup(field)

print(field)