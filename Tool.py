# 2022-04-26

from socket import gethostbyname
from sys import argv

if(len(argv) < 2):
  print("Please Select A File [python3 Tool.py File.txt]")
  exit()
  
try:
  with open(argv[1], "r") as File:
    Domains = File.readlines()
except:
  print("Not Able To Read The File")
  exit()

for Domain in Domains:
  try:
    Domain = Domain.lower().strip()
    gethostbyname(Domain.replace("*.",""))
    with open("Working.txt","a") as File:
      File.write(Domain + "\n")
    print("Working: ", Domain)
  except Exception:
    print("Not Working: ", Domain)
else:
  print("Done")
