import requests as rq
import re
import json
import subprocess as sub
import pathlib




def get_data(FileName:str):


    URL = f"https://apibay.org/q.php?q={FileName}&cat=100"
    Response = rq.get(URL)
    Data = Response.text
    jsn = json.loads(Data)
    #,'Name','size'
    i = 0
    d = 10
    for i in range(10):

        print(f"Num {i} ",jsn[i]['id'],jsn[i]['name'],str(round(int(jsn[i]['size'])/1000000)) + "mb")
        i += 1
    print("Pls Choose with songs to download by Num from 0 to 9")
    User_choice = int(input("Num: "))
    return jsn[User_choice]['info_hash']




def Download(Hash:str):
    import os 
    Download_Path = str(pathlib.Path().resolve()) + "/Downloads/"
    if os.path.isdir(Download_Path) == False:
        os.makedirs(Download_Path)
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
print("""
This software is a generic BitTorrent utility.
It is intended for downloading and sharing legal, freely distributable content only.
The author does not host, distribute, or promote copyrighted material.
Users are responsible for complying with their local laws.
""")
print("Enter File Name")
Download(get_data("Nirvana"))

