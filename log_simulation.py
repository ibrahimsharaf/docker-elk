#import sys
import argparse
from time import sleep

parser = argparse.ArgumentParser()
parser.add_argument("log")
args = parser.parse_args()

f0_bufsize = 0

with open(args.log) as f1:

    with open("/home/hefnawi/Yaoota/BELK_BETA/docker-belk/logs/ariika/10092017.log", "ab", f0_bufsize) as f0:
        lines = f1.readlines()
        for line in lines:
            f0.write(line)
            #print(line.strip())
            sleep(15)