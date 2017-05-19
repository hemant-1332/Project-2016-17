import openface
import openface.helper
from openface.data import iterImgs

import cv2
import numpy as np
import random
import os
import shutil


def alignmain():
    openface.helper.mkdirP("output folder")
