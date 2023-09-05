#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib
import os
import re

drive_letter = "H"
drive_path = drive_letter + ":\\"


def calculate_hash(file_path):
    hash_obj = hashlib.sha3_512()
    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()


def download_box_art(file_path):
    url = "https://openretro.org/browse/gb"


def clean_file_name(file_root, file_name):
    print(file_root + "\\" + file_name)
    pattern = re.compile(r'^([0-9]{3,4})[\w ]{1}(.*)')
    match = pattern.search(file_name)
    if match:
        if not is_special_numbers(match.group(1)): # if not special numbers
            print("\t" + match.group(1))
            if os.path.exists(file_root + "\\" + match.group(2)):
                return
                #if calculate_hash(file_root + "\\" + file_name) == calculate_hash(file_root + "\\" + match.group(2)):
                    #os.remove(file_root + "\\" + file_name) # remove duplicate file
            else:
                os.rename(file_root + "\\" + file_name, file_root + "\\" + match.group(2))


def is_special_numbers(number):
    if number == "007":
        return True
    if len(number) == 4:
        if number.startswith("19") or number.startswith("20"):
            return True
    return False


def read_drive(drive_path):
    for root, dirs, files in os.walk(drive_path):
        if "Roms\\GB\\GBC" in root:
            for file in files:
                if file.endswith(".gbc") or file.endswith(".jpg"):
                    clean_file_name(root, file)


read_drive(drive_path)
