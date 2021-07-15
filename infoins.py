#!/bin/env python3

import os, sys
sys.path.append(os.getcwd()+"/.lib/")
import argparse
import instaloader 
from pyfiglet import Figlet 
from api import *
gr = "\033[0;32m"

ig = instaloader.Instaloader()
dp = input("Kullanıcı Adı Girin : ")
ap = argparse.ArgumentParser()
ap.add_argument(dp , action="store_true")
ap.add_argument(dp , action="store_true")
args = vars(ap.parse_args())
ig.download_profile(dp , profile_pic_only=True)


os.system("clear")

c_text = Figlet(font="slant")
os.system("cols=75 lines=30")
print(c_text.renderText("InfoIns"))


if args[dp]:
	user_info(usrname=dp)
	
if args[dp]:
	post_info()
