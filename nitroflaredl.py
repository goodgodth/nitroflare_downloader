import requests
import os

URL = "https://nitroflare.com/api/v2/getKeyInfo"

PARAMS = {"user" sys.argv[1], "premiumKey": sys.argv[2]}

PATH = sys.argv[3];

r = requests.get(url=URL, params=PARAMS)
data = r.json()
print("Premium Account : " + data["type"])

with open(sys.argv[4]) as fp:
    line = fp.readline()
    cnt = 1
    while line:
        print("File {}: {}".format(cnt, line.strip()))
        _url = line.strip()
        _file_id = _url.split("/")[4]
        print(_file_id)
        url = "https://nitroflare.com/api/v2/getFileInfo"
        params = {"files": _file_id}
        r = requests.get(url=url, params=params)
        data = r.json()
        print("getFileInfo : " + str(data))
        print(
            "File ID : "
            + _file_id
            + " -> "
            + data["result"]["files"][_file_id]["status"]
        )
        url = "https://nitroflare.com/api/v2/getDownloadLink"
        params = PARAMS
        params["file"] = _file_id
        r = requests.get(url=url, params=params)
        data = r.json()
        print("getDownloadLink : " + str(data))
        _dl_url = data["result"]["url"]
        os.system("wget -P "+PATH+" " + _dl_url + "")
        line = fp.readline()
        cnt += 1
