import pandas as pd
from skimage.color import rgb2hed
import skimage
import numpy as np
from skimage.io import imread
from skimage.color import rgba2rgb
from skimage.transform import resize

data=pd.read_excel('generated_dataframe.xlsx')
