import os, sys, time, re
import argparse

parser = argparse.ArgumentParser()
parser.description='Usage: JuiceShop automating attack application'
parser.add_argument("-s", "--s", help="Login through sql injection -s -p(Optional) [SQL payload, dictionary name] -c(Optional) [username]", action="store_true")
parser.add_argument("-p", "--p", help="associated with flag -s, to provide specific SQL injection payload", action="store")
parser.add_argument("-u", "--u", help="associated with flag -s, to provide specific username", action="store")

# # parser.add_argument("-decode", "--decode", help="decode mode -st [steganographed image]", action="store")
# parser.add_argument("-c", "--c", help="cover image include extension", action="store")
#parser.parse_args(['-h'])
# parser.add_argument("-encode", "--encode", help="encode mode -c [cover image name] -s [secret image name] -st [name for new image]", action="store")
# parser.add_argument("-decode", "--decode", help="decode mode -st [steganographed image]", action="store")
# parser.add_argument("-c", "--c", help="cover image include extension", action="store")
# parser.add_argument("-s", "--s", help="secret image include extension", action="store")
# parser.add_argument("-st", "--st", help="steganography image include extension", action="store")

args = parser.parse_args()
if args.h:
    print(args)