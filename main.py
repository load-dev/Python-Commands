import colorama
import random
import json
import yaml
import time
import os
import re

def sendprompt():
  print("")
  command = input(f"{colorama.Fore.YELLOW}Command: {colorama.Fore.GREEN}/{colorama.Fore.WHITE}")
  checkcmd(command)

def sendpromptfirst():
  command = input(f"{colorama.Fore.YELLOW}Command: {colorama.Fore.GREEN}/{colorama.Fore.WHITE}")
  checkcmd(command)

def checkcmd(command):
  input_arr = command.split(" ")
  filename = input_arr[0] + ".cmd"
  setting_value = input_arr[1] if len(input_arr) > 1 else None
  directory = "commands/"
  sendpatern = r'send\("([^"]+)"\)'
  waitpatern = r'wait\((.*?)\)'
  matching_files = []
  
  for file in os.listdir(directory):
    if file.endswith(".cmd") and file == filename:
      matching_files.append(os.path.join(directory, file))

  if matching_files:
    for file in matching_files:
        with open(file, "r") as f:
            file_contents = f.read()
            if 'setting = {"text" : string}' in file_contents:
                if setting_value:
                    file_contents = file_contents.replace('{setting.text}', str(setting_value))
                else:
                    print(f"{colorama.Fore.RED}Usage: /{input_arr[0]} [text]")
                    sendprompt()
                  
            if 'then' in file_contents:
                text = file_contents.split('then\n')[1].split('\n')[0]
                match = re.search(sendpatern, file_contents)
                match2 = re.search(waitpatern, file_contents)
                matches = re.findall(sendpatern, file_contents)
                if matches:
                  for match in matches:
                    print(match)
                sendprompt()
  else:
      print(f"{colorama.Fore.RED}Unknown command!")
      sendprompt()


sendpromptfirst()