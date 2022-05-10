#!/usr/bin/env python

import sys, os, xdg, time, argparse
from datetime import datetime, timezone
import colorama
from colorama import Fore, Style
import subprocess

#import requests, argparse, time
#from bs4 import BeautifulSoup
#from prettytable import from_html_one, SINGLE_BORDER, DOUBLE_BORDER

PROG = "DotClean"
VERSION = "0.1.0"
AUTHOR = "Copyright (C) 2022, by Michael John"
DESC = "List old or unused dotfiles/dotdirs."

def main():
    #print(f"{PROG} version {VERSION}, {AUTHOR}")
    start = time.time()

    parser = argparse.ArgumentParser(prog=PROG, description=DESC)
    #parser.add_argument('userid', metavar='userid', type=int, help='user-id')
    parser.add_argument('-f', '--files', help='only apply to files', action='store_true')
    parser.add_argument('-d', '--directories', help='only apply to directories', action='store_true')
    parser.add_argument('-x', '--exclude', metavar='months', type=int, help='exclude files not older than {x} months')
    parser.add_argument('-n', '--nocolor', help='disable colored output', action='store_true')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + VERSION + ' ' + AUTHOR)
    args = parser.parse_args()
    print(str(args).replace("Namespace", "Options"))
    #user_id = args.userid
    home_dir = ""
    config_dir = xdg.xdg_config_home()
    if args.files == False and args.directories == False:
        args.files = True
    if args.files:
        onlyfiles = [f for f in os.listdir(config_dir) if os.path.isfile(os.path.join(config_dir, f))]
        output = onlyfiles
        #print("\n".join(onlyfiles))
    if args.directories:
        onlydirs = [f for f in os.listdir(config_dir) if os.path.isdir(os.path.join(config_dir, f))]
        output = onlydirs
        #print("\n".join(onlydirs))
    #try:
        #home_dir, __file__, __package__, __name__, __)
    #except IndexError:
    #    pass
    for file in output:
        SkipFile = False
        file_info = os.stat(os.path.join(config_dir, file))
        modified = datetime.fromtimestamp(file_info.st_mtime, tz=timezone.utc)
        age_days = (float(start) - float(file_info.st_mtime)) /(60*60*24)
        
        if not args.nocolor:
            if age_days >= 0:
                color = Fore.WHITE
            if age_days > 90:
                color = Fore.GREEN
            if age_days > 300:
                color = Fore.BLUE
            if age_days > 800:
                color = Fore.LIGHTRED_EX
        else:
            color = Fore.RESET

        #if age_days <= 30 and args.exclude:
        if args.exclude is not None and age_days <= args.exclude:
            SkipFile = True

        #print(file, file_info.st_mtime, modified, start, (float(start) - float(file_info.st_mtime)) /(60*60*24))
        if SkipFile == False:
            print(f"{color}{file:50s}{age_days:3.0f} d")

    end = time.time()
    print(f'{Style.RESET_ALL}''[{:2.3} seconds elapsed]'.format((end - start)))
