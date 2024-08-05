#!/usr/bind/env python
#_*_ coding: utf8 _*_

import os


#COLORS
RED = '\033[1;31m'
BLUE = '\033[1;34m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
MAGENTA = '\033[1;35m'
WHITE = '\033[1;37m'
CYAN = '\033[1;36m'
END = '\033[0m'
RED_NORMAL = '\033[0;31m'
GREEN_NORMAL = '\033[0;32m'


def banner():
	print(f"""
{RED_NORMAL} ____             _        {WHITE} _   _           _     
{RED_NORMAL}| __ ) _ __ _   _| |_ ___  {WHITE}| | | | __ _ ___| |__  
{RED_NORMAL}|  _ \| '__| | | | __/ _ \ {WHITE}| |_| |/ _` / __| '_ \ 
{RED_NORMAL}| |_) | |  | |_| | ||  __/ {WHITE}|  _  | (_| \__ \ | | |
{RED_NORMAL}|____/|_|   \__,_|\__\___| {WHITE}|_| |_|\__,_|___/_| |_|


\t\t\t\033[1;31m----<\033[0;m \033[1;37mGithub: \033[1;41;37mYoga913\033[0;m \033[1;31m>----\033[0;m
""")

banner()
