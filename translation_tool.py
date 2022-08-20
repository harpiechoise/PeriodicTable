import urllib.request as uReq
from i18n import I18nString
import wikipedia as W
from deep_translator import GoogleTranslator as GT
import os
import json
import simplelogging
from bs4 import BeautifulSoup as soup
import itertools
import re
from lib import read_elements as read_lib

log = simplelogging.get_logger(file_name="./logs/translation_log.txt")


STRINGS = I18nString()
translator = GT(source="en", target=STRINGS.lang)
W.set_lang(STRINGS.lang)


def translation_confirmation(args):
    if args[0] is None:
        return None
    print("Original String:")
    print("\t" + args[0])
    print("Translation")
    print("\t" + args[1])
    op = input("Is correct (Y/n)? ")
    translation = args[1]
    if op == "n":
        translation = input("Enter the correct translation: ")
    return translation


def read_dict(main_s):

    translated = map(translator.translate, main_s.values())
    correct = map(translation_confirmation, zip(main_s.values(), translated))
    return dict(zip(main_s.keys(), correct))


def save_dict(result, filename):
    file = os.path.join(os.getcwd(), "i18n", STRINGS.lang, filename)
    with open(file, 'w', encoding=STRINGS.encoding) as f:
        json.dump(result, f, indent=4)
    log.info(f"{filename} saved")


def read_elements():
    url = f"https://elements.vanderkrogt.net/language.php?language={STRINGS.lang}"
    response = uReq.urlopen(url)
    s = soup(response.read(), 'html.parser')
    page_elements = s.find_all('a')
    elements = filter(
        lambda x: True if "sym=" in x['href'] else False,
        page_elements
    )

    name_symbol = map(
        lambda x: (x['href'].split("=")[-1], x.text),
        elements
    )

    return dict(name_symbol)


def wikipedia_extract(x):
    r = re.compile(r"(\[(?:\[??[^\[]*?\]))")
    try:
        page = W.page(x)
        return re.sub(r, "", page.summary), page.url
    except (W.DisambiguationError, W.PageError):
        try:
            page = W.page(x + " (Elemento)")
            return re.sub(r, "", page.summary), page.url

        except (W.DisambiguationError, W.PageError):
            print("Missing Summary for element:\n\t" + x)
            summary = input("Enter the manual summary\n")
            url = input("Enter the summary URL\n")
            return re.sub(r, "", summary), url


def translate_or_none(e):
    if e is None:
        return None
    return translator.translate(e)


def get_subdict(x):
    return {
        "name": x[0],
        "summary": x[1],
        "appareance": x[2],
        "category": x[3]
    }


def scrape_elements():
    def get_appears():
        items = itertools.islice(STRINGS.elements, 10, None)
        apareance = map(
            lambda x: STRINGS.elements[x]['appareance'],
            items
        )
        return apareance

    elems = STRINGS.elements
    k = elems.keys()
    k = itertools.islice(k, 10, None)

    elems = read_elements()
    names = map(
        lambda x: elems[x], k
    )

    names = list(names)

    resultado = map(wikipedia_extract, names)

    apareance = get_appears()
    t_appearence = map(translate_or_none, apareance)

    k = itertools.islice(STRINGS.elements, 10, None)
    category = map(
        lambda x: STRINGS.elements[x]['category'],
        k
    )

    subdicts = map(get_subdict, zip(names, resultado, t_appearence, category))
    k = itertools.islice(STRINGS.elements, 10, None)
    return dict(zip(k, subdicts))


def add_value():
    translations = STRINGS.elements
    elements = read_lib('elements.json')

    # Convert to tuple list
    tl = zip(translations.keys(), translations.values())

    # Advancing 10
    elements_translated = itertools.islice(tl, 10, None)

    elements_translated = dict(elements_translated)
    print(elements["H"])

    def __add_phase(x):
        translations[x]["phase"] = translator.translate(elements[x].phase).capitalize()

    list(map(
        __add_phase,
        elements_translated
    ))

    save_dict(translations, "elements.json")

def add_value_2():
    translations = STRINGS.elements
    elements = read_lib('elements.json')

    # Convert to tuple list
    tl = zip(translations.keys(), translations.values())

    # Advancing 10
    elements_translated = itertools.dropwhile(
        lambda x: x[0] != "H", tl
    )

    elements_translated = dict(elements_translated)
    print(elements["H"])

    def __add_phase(x):
        translations[x]["category_t"] = translator.translate(elements[x].category).capitalize()

    list(map(
        __add_phase,
        elements_translated
    ))

    save_dict(translations, "elements.json")


if __name__ == "__main__":
    # ms = read_dict(STRINGS.main_screen)
    # save_dict(ms, 'main_screen.json')

    # ct = itertools.islice(STRINGS.elements.values(), 10)
    # dk = itertools.islice(STRINGS.elements, 10)
    # ds = read_dict(dict(zip(dk, ct)))
    # ds.update(scrape_elements())
    # save_dict(ds, 'elements.json')
    # add_value()
    add_value_2()
