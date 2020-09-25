import requests
import os
import sys

NTFURL_KEYINFO = "https://nitroflare.com/api/v2/getKeyInfo"
NTFURL_FILEINFO = "https://nitroflare.com/api/v2/getFileInfo"
NTFURL_DOWNLOADLINK = "https://nitroflare.com/api/v2/getDownloadLink"


PARAMS = {"user": sys.argv[1], "premiumKey": sys.argv[2]}

LISTOFDOWNLOAD = sys.argv[3]
PATH = sys.argv[4];

r = requests.get(url=NTFURL_KEYINFO, params=PARAMS)
data = r.json()
print("Premium Account : " + data["type"])

with open(LISTOFDOWNLOAD) as fp:
    line = fp.readline()
    cnt = 1
    while line:
        print("File {}: {}".format(cnt, line.strip()))
        _url = line.strip()
        _file_id = _url.split("/")[4]
        print(_file_id)
        
        params = {"files": _file_id}
        r = requests.get(url=NTFURL_FILEINFO, params=params)
        data = r.json()
        print("getFileInfo : " + str(data))
        print(
            "File ID : "
            + _file_id
            + " -> "
            + data["result"]["files"][_file_id]["status"]
        )
        
        params = PARAMS
        params["file"] = _file_id
        r = requests.get(url=NTFURL_DOWNLOADLINK, params=params)
        data = r.json()
        print("getDownloadLink : " + str(data))
        _dl_url = data["result"]["url"]
        os.system("wget -P "+PATH+" " + _dl_url + "")
        line = fp.readline()
        cnt += 1
