#!"C:\Users\dastidarr\AppData\Local\Programs\Python\Python37"
import configparser

config = configparser.ConfigParser()
config.read("config_input.ini")
src_filepath = (config.get("Configuration Inputs","src_filepath"))
dst_filepath = (config.get("Configuration Inputs","dst_filepath"))
