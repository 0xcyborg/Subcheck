# 2022-04-26

from socket import gethostbyname

with open("List.txt","r") as File:
  Domains = File.readlines()

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
