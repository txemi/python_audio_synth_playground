# https://pytuning.readthedocs.io/en/0.7.2/scales.html#the-pythagorean-scale

from pytuning import scales
from pytuning import utilities

a = scales.create_edo_scale(12)

pythag = scales.create_pythagorean_scale()
names = [utilities.ratio_to_name(x) for x in pythag]

print(1)
