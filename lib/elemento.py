import json
from decimal import Decimal
from i18n import I18nString
import os
import itertools

STRINGS = I18nString()


class Elemento:
    def __init__(self, registro):
        # self.name = registro["name"],
        symbol = registro["symbol"]
        self.name = STRINGS.elements[symbol]['name']
        # self.appareance = registro["appearance"],
        self.appareance = STRINGS.elements[symbol]['appareance']
        self.atomic_mass = registro["atomic_mass"]
        self.boil = registro["boil"]
        self.category = STRINGS.elements[symbol]['category']
        self.density = registro["density"]
        self.discovered_by = registro["discovered_by"]
        self.melt_point = registro["melt"]
        self.molar_heat = registro["molar_heat"]
        self.named_by = registro["named_by"]
        self.number = registro["number"]
        self.period = registro["period"]
        self.phase = registro["phase"]
        self.source = registro["source"]
        self.spectral_img = registro["spectral_img"]
        self.summary = STRINGS.elements[symbol]['summary']
        self.symbol = symbol
        self.xpos = registro["xpos"]
        self.ypos = registro["ypos"]
        self.shells = registro["shells"]
        self.electron_configuration = registro["electron_configuration"]
        self.electron_configuration_semantic = registro["electron_configuration_semantic"]
        self.electron_afffinity = registro["electron_affinity"]
        self.electronegativity_pauling = registro["electronegativity_pauling"]
        self.ionization_energies = registro["ionization_energies"]
        self.cpk_hex = None
        self.font_color = None
        self.valency_electrons = self.__compute_valency()
        self.__back_color()

    def __repr__(self):
        return f"Elemento(name={self.name}))"

    def __str__(self):
        return self.__repr__()

    def __compute_valency(self):
        elec = self.electron_configuration.split(" ")
        electron_value = map(self.__check_orbital, elec)
        last_layer_value = elec[-1][0]
        last_layer = filter(lambda x: x[0] == last_layer_value, electron_value)
        return sum(map(lambda x: x[1], last_layer))

    def __check_orbital(self, orb_value):
        layer = orb_value[0]
        orb_value = orb_value[1:]
        orbital = orb_value[0]
        value = int(orb_value[1:])
        match orbital:
            case "s":
                result = value
            case "p":
                result = value
            case "d":
                result = 0
            case "f":
                result = 0
        return layer, result

    def __back_color(self):
        if self.symbol == "Nh"\
           or self.symbol == "Mc"\
           or self.symbol == "Lv":
            self.cpk_hex = "#781E77"
            self.font_color = "#FFFFFF"
            return

        if self.symbol == "Po":
            self.cpk_hex = "#ED1944"
            self.font_color = "#FFFFFF"
            return

        if self.symbol == "At" or self.symbol == "Ts":
            self.cpk_hex = "#A2B427"
            self.font_color = "#000000"
            return

        if self.symbol == "Lu" or self.symbol == "Lr":
            self.cpk_hex = "#0088CE"
            self.font_color = "#FFFFFF"
            return

        match self.category:
            case "alkali metal":
                self.cpk_hex = "#002A4E"
                self.font_color = "#FFFFFF"
            case "noble gas" | "unknown, predicted to be noble gas":
                self.cpk_hex = "#006A36"
                self.font_color = "#FFFFFF"
            case "diatomic nonmetal":
                self.cpk_hex = "#A2B427"
                self.font_color = "#000000"
            case "polyatomic nonmetal":
                self.cpk_hex = "#F58021"
                self.font_color = "#000000"
            case "alkaline earth metal":
                self.cpk_hex = "#FDBA12"
                self.font_color = "#000000"
            case "metalloid":
                self.cpk_hex = "#ED1944"
                self.font_color = "#FFFFFF"
            case "transition metal" | "unknown, probably transition metal":
                self.cpk_hex = "#0088CE"
                self.font_color = "#FFFFFF"
            case "lanthanide":
                self.cpk_hex = "#CBD48E"
                self.font_color = "#000000"
            case "actinide":
                self.cpk_hex = "#67A484"
                self.font_color = "#000000"
            case "post-transition metal":
                self.cpk_hex = "#781E77"
                self.font_color = "#FFFFFF"


def read_elements(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.loads(f.read(), parse_int=int, parse_float=Decimal)["elements"]
        elements = map(lambda x: Elemento(x), data)
        symbols = map(lambda x: x["symbol"], data)
        return dict(zip(symbols, elements))


def find_element_names(elements):
    path = os.path.join(os.getcwd(),
                        "i18n",
                        STRINGS.lang,
                        "elements.json")

    with open(path, "r", encoding=STRINGS.encoding) as f:
        data = json.load(f)

    data = dict(itertools.islice(zip(data.keys(), data.values()), 10, None))

    def __find_elements_names(element: Elemento):

        symbol = element.symbol
        name = data[symbol]['name']
        appareance = data[symbol]['appareance']
        summary = data[symbol]['summary']
        element.name = name
        element.appareance = appareance
        element.summary = summary
        return element
    elemens = map(__find_elements_names, elements.values())
    return dict(zip(elements.keys(), elemens))


if __name__ == "__main__":
    elems = read_elements("./elements.json")
    print(elems["P"].valency_electrons)
