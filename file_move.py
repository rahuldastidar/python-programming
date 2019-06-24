#!"C:\Users\dastidarr\AppData\Local\Programs\Python\Python37"
# -*- coding: utf-8 -*-
# __author__: Rahul.Dastidar@Teoco.com
#__version__: 1.0.1
from pathlib import Path
import arrow
import shutil
import os
import configparser

config = configparser.ConfigParser()
config.read("config_input.ini")
src_filepath = (config.get("Configuration Inputs","src_filepath"))
dst_filepath = (config.get("Configuration Inputs","dst_filepath"))
file_limit = int((config.get("Configuration Inputs","file_limit")))
minutes_limit = int((config.get("Configuration Inputs","minutes_limit")))
seconds_limit = int((config.get("Configuration Inputs","seconds_limit")))

#src_filepath = r"D:\EMTEL\sample_files"

criticalTime = arrow.now().shift(minutes=+minutes_limit).shift(seconds=+seconds_limit)
#dst_filepath = r"D:\EMTEL\Logs_Out"
if not os.path.exists (dst_filepath):
    os.makedirs(dst_filepath)
onlyfiles_in_dst = next ( os.walk ( dst_filepath ) ) [ 2 ]
file_count_indst = len ( onlyfiles_in_dst )
print ('Files in destination', file_count_indst)
for item in Path(src_filepath).glob('*'):
    if item.is_file():
        files_in_source = (str(item.absolute()))
        print (files_in_source)
        itemTime = arrow.get(item.stat().st_mtime)
        if itemTime < criticalTime and file_count_indst < file_limit:
            shutil.move(files_in_source,dst_filepath)



