#coding=utf-8

import os
def dir_path():
    return os.path.split(os.path.realpath(__file__))[0]
