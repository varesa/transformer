#!/bin/env python

import os
from os import listdir
from os import path

import subprocess
from time import sleep

from config import *

def encrypt(infile, outfile):
    return subprocess.call(["gpg", "--encrypt", "--armor", "--recipient", "hakemukset@alrekry.fi", "--output", outfile, infile]) == 0

for pair in PAIRS:
    print("Starting to poll " + path.join(BASE, pair[0]))

while True:
    for pair in PAIRS:
        src = path.join(BASE, pair[0])
        dst = path.join(BASE, pair[1])

        files = listdir(src)
        if len(files):
            print("Found files: " + str(files))
        sleep(1)
        for file in files:
            srcfile = path.join(src, file)
            dstfile = path.join(dst, file)

            print("Processing " + srcfile)
            encrypt(srcfile, dstfile)
            if os.path.isfile(dstfile):
                os.remove(srcfile)
            else:
                raise Exception("Something went wrong")

    sleep(30)
