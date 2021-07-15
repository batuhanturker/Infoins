#!/bin/env python3

import os, sys
sys.path.append(os.getcwd()+"/.lib/")
import argparse
from api import *

ap = argparse.ArgumentParser()
ap.add_argument("-u", "--kullanıcı", required=True, help="username of account to scan")
ap.add_argument("-p", "--post", action="store_true", help="image info of user uploads")
args = vars(ap.parse_args())
	
os.system("clear")

if args['kullanıcı']:
	user_info(usrname=args["kullanıcı"])

if args['post']:
	post_info()
