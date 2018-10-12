# -*- coding: utf-8 -*-
# @Time    : 18-9-29 上午10:16
# @Author  : allen.you

import os


class Config(object):
    ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
    SECRET_KEY = 'hard to guess string'
