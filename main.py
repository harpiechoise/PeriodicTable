from GUI import MainScreen
from urllib.request import urlopen
from os import path
import locale
import json


def download_elements():
    url = ("https://raw.githubusercontent.com" +
           "/Bowserinator/Periodic-Table-JSON/master/PeriodicTableJSON.json")
    with urlopen(url) as f:
        with open('./elements.json', "wb") as e:
            e.write(f.read())


def init_config_file():
    locale_ = locale.getlocale()
    language = locale_[0].split("_")[0]

    with open("./config.json", "w") as f:
        json.dump({"lang": language, "encoding": locale_[1]}, f, indent=4)


if __name__ == "__main__":
    if not path.exists("./elements.json"):
        download_elements()
    if not path.exists("./config.json"):
        init_config_file()
    MainScreen()
