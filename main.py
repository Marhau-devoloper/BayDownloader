import requests as rq
import re
import json
import subprocess as sub
import pathlib
import os



def get_data(FileName:str):

    FileName = FileName.replace("-","+")
    URL = f"https://apibay.org/q.php?q={FileName}&cat=100"
    Response = rq.get(URL)
    Data = Response.text
    jsn = json.loads(Data)
    #,'Name','size'
    i = 0
    os.system("clear")
    print( "======================================================") 
    for i in range(30):
        try:
            print(f"| Num {i} ",jsn[i]['id'],jsn[i]['name'],str(round(int(jsn[i]['size'])/1000000)) + "mb")
            
            i += 1
        except:
            if jsn[0]['name'] == "No results returned" :
                
                exit()
    print( " ======================================================")           
    print(f"|Pls Choose with songs to download by Num like 0 . . . |")
    print( " ======================================================") 
    User_choice = int(input("Num ==> "))
    if User_choice > 29 : User_choice = 29
    return jsn[User_choice]['info_hash']




def Download(Hash:str):
    Download_Path = str(pathlib.Path().resolve()) + "/Downloads/"
    if os.path.isdir(Download_Path) == False:
        os.makedirs(Download_Path)
    os.system("clear")
    print(f'''
          
          | Downloading begins and gonna stored in|
          | {Download_Path} |
          ''')
    magnet = (
    f"magnet:?xt=urn:btih:{Hash}"
    "&tr=udp://tracker.opentrackr.org:1337/announce"
    "&tr=udp://tracker.openbittorrent.com:80/announce"
    "&tr=udp://tracker.torrent.eu.org:451/announce"
)
    sub.run([
    "aria2c",
    magnet,
    "-d", "/home/marhau/Music/MusicBay/Downloads/",
    "--seed-time=0",
    "--enable-dht=true",
    "--max-overall-download-limit=0",
    "--bt-max-peers=100"
])
"https://apibay.org/q.php?q={Song_Name}&cat=100"








os.system("clear")
print("""
 /$$$$$$$                      /$$$$$$$                                    /$$                           /$$                    
| $$__  $$                    | $$__  $$                                  | $$                          | $$                    
| $$  \ $$  /$$$$$$  /$$   /$$| $$  \ $$  /$$$$$$  /$$  /$$  /$$ /$$$$$$$ | $$  /$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$   /$$$$$$ 
| $$$$$$$  |____  $$| $$  | $$| $$  | $$ /$$__  $$| $$ | $$ | $$| $$__  $$| $$ /$$__  $$ |____  $$ /$$__  $$ /$$__  $$ /$$__  $$
| $$__  $$  /$$$$$$$| $$  | $$| $$  | $$| $$  \ $$| $$ | $$ | $$| $$  \ $$| $$| $$  \ $$  /$$$$$$$| $$  | $$| $$$$$$$$| $$  \__/
| $$  \ $$ /$$__  $$| $$  | $$| $$  | $$| $$  | $$| $$ | $$ | $$| $$  | $$| $$| $$  | $$ /$$__  $$| $$  | $$| $$_____/| $$      
| $$$$$$$/|  $$$$$$$|  $$$$$$$| $$$$$$$/|  $$$$$$/|  $$$$$/$$$$/| $$  | $$| $$|  $$$$$$/|  $$$$$$$|  $$$$$$$|  $$$$$$$| $$      
|_______/  \_______/ \____  $$|_______/  \______/  \_____/\___/ |__/  |__/|__/ \______/  \_______/ \_______/ \_______/|__/      
                     /$$  | $$                                                                                                  
                    |  $$$$$$/                                                                                                  
                     \______/                                                                                                   """)


print("""
This software is a generic BitTorrent utility.
It is intended for downloading and sharing legal, freely distributable content only.
The author does not host, distribute, or promote copyrighted material.
Users are responsible for complying with their local laws.
      
Use this app only on education pruposes
""")


print("""
     <=================>
      |Enter File Name|
     <=================>  
      """)
user_query = input("Name ==>  ")
Download(get_data(user_query))

