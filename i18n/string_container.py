import json
import os


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class I18nString(metaclass=Singleton):

    def __init__(self) -> None:
        self.elements = None
        self.main_screen = None
        self.lang = None
        self.encoding = None
        self.load_strings()

    def load_strings(self):
        with open("config.json", "r") as f:
            data = json.loads(f.read())
            self.lang = data['lang']
            self.encoding = data['encoding']

        base_dir = os.path.join(
            os.getcwd(),
            "i18n",
            self.lang
        )

        elems_path = os.path.join(base_dir, "elements.json")
        main_src_path = os.path.join(base_dir, "main_screen.json")

        with open(elems_path, "r", encoding=self.encoding) as f:
            self.elements = json.load(f)

        with open(main_src_path, 'r', encoding=self.encoding) as f:
            self.main_screen = json.load(f)
