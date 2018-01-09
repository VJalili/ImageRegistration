import os
import sys
from image_registration import *

"""
call syntax: python run.py CONFIG_FILE NUCLEI_FILE

CONFIG_FILE: is an xml file containing ... 

NUCLEI_FILE: is a SVS file containing ...
"""

if __name__ == "__main__":
    config = sys.argv[1]
    if os.path.isfile(config) is False:
        sys.exit("First argument is expected to be a valid configuration file; received `{}` instead. ".format(config))

    nuclei_file = sys.argv[2]
    if os.path.isfile(config) is False:
        sys.exit("Second argument is expected to be a valid nuclei file; received `{}` instead. ".format(config))

    ImageRegistration(config=config, nuclei_file=nuclei_file)
