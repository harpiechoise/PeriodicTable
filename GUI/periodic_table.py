from tkinter import ttk, Toplevel
import tkinter as tk
from PIL import Image, ImageTk
from numpy import imag
from lib import read_elements, find_element_names
from i18n import I18nString
from lib.elemento import Elemento
from lib import get_asset_path
from tktooltip import ToolTip

STRINGS = I18nString()

RIGHT = 50
DOWN = 120


class ElementInformationPanel(tk.Frame):
    def __init__(self, parent, factor=1):
        tk.Frame.__init__(self, parent, width=350, height=150)
        self.atomic_mass_text = tk.StringVar(value="1252.0")
        self.electronegativity_text = tk.StringVar(value="12.222")
        self.category_text = tk.StringVar(value="Alcalinotérreo")
        self.phase_text = tk.StringVar(value="Solid")
        self.semantic_config = tk.StringVar(value="[Kr] 4d10 5s2 5p4")
        # Widget Start
        self.image_atom = ImageTk.PhotoImage(Image.open(get_asset_path("atomic.png", 'img' )).resize((16,16)))
        self.image_atom_element = ttk.Label(self, image=self.image_atom)
        self.image_atom_element.image = self.image_atom
        
        self.value = ttk.Label(self, textvariable=self.atomic_mass_text, font=("Helvetica", 11 * factor))

        self.label_sup = ttk.Label(self, text=STRINGS.elements["prop1"], font=("Helvetica", 8 * factor))
        
        self.image_atom_element.place(relx=0, rely=.1)
        self.value.place(relx=.06, rely=.105)
        self.label_sup.place(relx=0, rely=0)
        
        # Widget Start
        self.image_magnets = ImageTk.PhotoImage(Image.open(get_asset_path("magnets.png", 'img')).resize((16,16)))
        self.image_magnets_element = ttk.Label(self, image=self.image_magnets)
        self.image_magnets_element.image = self.image_magnets
        
        self.value_electronegativity = ttk.Label(self, textvariable=self.electronegativity_text, font=("Helvetica", 11 * factor))

        self.label_sup2 = ttk.Label(self, text=STRINGS.elements["prop2"], font=("Helvetica", 8 * factor))

        self.image_magnets_element.place(relx=0, rely=.35)
        self.value_electronegativity.place(relx=.06, rely=.355)
        self.label_sup2.place(relx=0, rely=.25)


        # Widget Start
        self.image_diag = ImageTk.PhotoImage(Image.open(get_asset_path("diagram.png", 'img')).resize((16,16)))
        self.image_diag_element = ttk.Label(self, image=self.image_diag)
        self.image_diag_element.image = self.image_diag
        
        self.value_category = ttk.Label(self, textvariable=self.category_text, font=("Helvetica", 11 * factor))

        self.label_sup3 = ttk.Label(self, text=STRINGS.elements["prop3"], font=("Helvetica", 8 * factor))

        self.image_diag_element.place(relx=0, rely=.59)
        self.value_category.place(relx=.06, rely=.595)
        self.label_sup3.place(relx=0, rely=.49)

        # Widget Start
        self.image_cube = ImageTk.PhotoImage(Image.open(get_asset_path("solid.png", 'img')).resize((16,16)))
        self.image_cube_element = ttk.Label(self, image=self.image_cube)
        self.image_cube_element.image = self.image_cube
        
        self.value_phase = ttk.Label(self, textvariable=self.phase_text, font=("Helvetica", 11 * factor))

        self.label_sup4 = ttk.Label(self, text=STRINGS.elements["prop4"], font=("Helvetica", 8 * factor))

        self.image_cube_element.place(relx=0, rely=.85)
        self.value_phase.place(relx=.06, rely=.855)
        self.label_sup4.place(relx=0, rely=.73)

        # Widget Start
        self.image_gear = ImageTk.PhotoImage(Image.open(get_asset_path("gear.png", 'img')).resize((16,16)))
        self.image_gear_element = ttk.Label(self, image=self.image_gear)
        self.image_gear_element.image = self.image_gear
        
        self.value_config = ttk.Label(self, textvariable=self.semantic_config, font=("Helvetica", 11 * factor))

        self.label_sup5 = ttk.Label(self, text=STRINGS.elements["prop5"], font=("Helvetica", 8 * factor))
        
        self.image_gear_element.place(relx=.4, rely=.1)
        self.value_config.place(relx=.46, rely=.105)
        self.label_sup5.place(relx=.4, rely=0)
    
    def update(self, element: Elemento):
        masa_atomica = element.atomic_mass
        electronegatividad = element.electronegativity_pauling
        category = STRINGS.elements[element.symbol]["category_t"]
        fase_t = STRINGS.elements[element.symbol]["phase"]

        if electronegatividad is None:
            electronegatividad = "-"

        self.atomic_mass_text.set(masa_atomica)
        self.electronegativity_text.set(electronegatividad)
        self.category_text.set(category)
        self.phase_text.set(fase_t)
        self.semantic_config.set(element.electron_configuration_semantic)


class ElementFullSize(tk.Frame):
    def __init__(self, parent, factor=1):
        tk.Frame.__init__(self,
                          parent, bg="#FF0000",
                          width=int(100 * factor),
                          height=int(125 * factor))
        self.symbol_text = tk.StringVar(self, "H")
        self.symbol_label = ttk.Label(self, textvariable=self.symbol_text,
                                      font=("Helvetica", 40 * factor))
        self.symbol_label.place(relx=.5, rely=.55, anchor="c")
        self.z_text = tk.StringVar(self, "1")
        self.z_label = ttk.Label(self, textvariable=self.z_text,
                                 font=("Helvetica", 12 * factor))
        self.z_label.place(relx=.15, rely=.1, anchor="c")
        self.a_text = tk.StringVar(self, "1.0")
        self.a_label = ttk.Label(self, textvariable=self.a_text,
                                 font=("Helvetica", 12 * factor))

        self.a_label.place(relx=.80, rely=.1, anchor="c")

        self.name_text = tk.StringVar(self, "Hydrogen")
        self.name_label = ttk.Label(self, textvariable=self.name_text,
                                    font=("Helvetica", 12 * factor))

        self.name_label.place(relx=.5, rely=.85, anchor="c")

    def update(self, element: Elemento):
        self['bg'] = element.cpk_hex
        self.symbol_label['background'] = element.cpk_hex
        self.symbol_text.set(element.symbol)
        self.symbol_label["foreground"] = element.font_color
        self.z_text.set(element.number)
        self.z_label["foreground"] = element.font_color
        self.z_label['background'] = element.cpk_hex
        self.a_text.set(round(element.atomic_mass))
        self.a_label["foreground"] = element.font_color
        self.a_label['background'] = element.cpk_hex
        self.name_text.set(element.name)
        self.name_label["foreground"] = element.font_color
        self.name_label["background"] = element.cpk_hex


class Element(tk.Frame):
    def __init__(self, parent, element: Elemento, factor=1):
        w = int(80 * factor)
        h = int(75 * factor)
        sz = int(24 * factor)
        idx = int(8 * factor)
        self.element = element
        tk.Frame.__init__(self, parent, bg=element.cpk_hex, width=w, height=h,
                          highlightbackground="#D9D9D9", highlightthickness=.5)
        self.symbol = ttk.Label(self, text=element.symbol, font=("Helvetica", sz),
                                background=element.cpk_hex, foreground=element.font_color)

        self.z = ttk.Label(self, text=element.number, font=("Helvetica", idx),
                           background=element.cpk_hex, foreground=element.font_color)

        self.a = ttk.Label(self, text=round(element.atomic_mass), font=("Helvetica", idx),
                           background=element.cpk_hex, foreground=element.font_color)

        self.name = ttk.Label(self, text=element.name, font=("Helvetica", idx),
                              background=element.cpk_hex, foreground=element.font_color)
        self.symbol.place(relx=.5, rely=.5, anchor="c")
        self.z.place(relx=.2, rely=.1, anchor="c")
        self.a.place(relx=.8, rely=.1, anchor="c")
        self.name.place(relx=.5, rely=.9, anchor="c")
        self.grid_propagate(0)

        ToolTip(self, msg=STRINGS.elements['tt1'].format(f"\"{self.element.name}\""),
                delay=.5, 
                parent_kwargs={
                    'bg': 'black', 
                    'padx': 5, 
                    "pady": 5
                }, fg="#ffffff", bg="#1c1c1c", padx=10, pady=10,
                font=("Helvetica", 12))
        self.bind('<Double-Button-1>', self.__get_widget )



    def __get_widget(self, w):
        print(w.widget.element)
    

class ColorLegend(tk.Frame):
    def __init__(self, parent, color, text, factor=1) -> None:
        w = int(256 * factor)
        h = int(64 * factor)
        tk.Frame.__init__(self, parent, width=w, height=h)
        self.patch = tk.Canvas(self, width=int(32 * factor), height=int(32 * factor))
        self.patch.create_rectangle(0, 0, int(34 * factor), int(34 * factor), fill=color)

        self.label = tk.Label(self, text=text, font=("Helvetica", int(18 * factor)))
        self.patch.grid(row=0, column=0, sticky='w')
        self.label.grid(row=0, column=1)


class PeriodictTable:
    def __init__(self, master):
        self.lantanids = range(57, 71)
        self.actinids = range(89, 103)
        self.window = Toplevel(master)
        self.window.resizable(False, False)
        self.window.geometry(f"{1280}x720+{RIGHT+360}+{DOWN}")
        self.window.title(STRINGS.main_screen["main_button"])
        self.tabla_container = tk.Frame(self.window)
        self.tabla_container.place(relx=.5, rely=.5, relwidth=.98, relheight=.8, anchor='c')
        self.element_full_size = ElementFullSize(self.window, 1)
        self.element_full_size.place(relx=.5, rely=.2, anchor='c')
        elements = read_elements("./elements.json")
        full_size = elements["H"]
        self.element_full_size.update(full_size)
        self.info = ElementInformationPanel(self.window)
        self.info.update(full_size)
        self.info.place(relx=.15, rely=.08)
        
        elements = find_element_names(elements)
        

        self.__make_incomplete_row(elements, 1)
        self.__make_incomplete_row(elements, 2)
        self.__make_incomplete_row(elements, 3)

        self.__make_row(elements, row=4)
        self.__make_row(elements, row=5)
        self.__make_row(elements, row=6)
        self.__make_row(elements, row=7)

        self.__make_lantanids_actinids(elements, row=6)
        self.__make_lantanids_actinids(elements, row=7)
        self.__make_groups()
        self.__make_periods()
        dx = -0.02
        ColorLegend(self.window,
                    "#006A36",
                    STRINGS.elements["category1"],
                    .6).place(relx=.15 + dx, rely=.9)
        ColorLegend(self.window,
                    "#A2B427",
                    STRINGS.elements["category2"],
                    .6).place(relx=.30 + dx, rely=.9)
        ColorLegend(self.window,
                    "#F58021",
                    STRINGS.elements["category3"],
                    .6).place(relx=.45 + dx, rely=.9)
        ColorLegend(self.window,
                    "#ED1944",
                    STRINGS.elements["category4"],
                    .6).place(relx=.60 + dx, rely=.9)
        ColorLegend(self.window,
                    "#781E77",
                    STRINGS.elements["category5"],
                    .6).place(relx=.75 + dx, rely=.9)
        ColorLegend(self.window,
                    "#F58021",
                    STRINGS.elements["category6"],
                    .6).place(relx=.15 + dx, rely=.95)
        ColorLegend(self.window,
                    "#FDBA12",
                    STRINGS.elements["category7"],
                    .6).place(relx=.30 + dx, rely=.95)
        ColorLegend(self.window,
                    "#002A4E",
                    STRINGS.elements["category8"],
                    .6).place(relx=.45 + dx, rely=.95)
        ColorLegend(self.window,
                    "#CBD48E",
                    STRINGS.elements["category9"],
                    .6).place(relx=.60 + dx, rely=.95)
        ColorLegend(self.window,
                    "#67A484",
                    STRINGS.elements["category10"],
                    .6).place(relx=.75 + dx, rely=.95)

    def __elem_information(self, event):
        print(event)

    def __display_full_size(self, event):
        element: Elemento = event.widget.element
        self.element_full_size.update(element)
        self.info.update(element)

    def __make_row(self, elements, row):
        periodos = map(lambda x: (x.period, x, x.number), list(elements.values()))
        periodo4 = filter(lambda x: bool(int(x[0] == row) & ~((int(x[2] in self.lantanids) |
                          int(x[2] in self.actinids)))), periodos)
        elements = map(lambda x: Element(self.tabla_container,
                                         element=x[1],
                                         factor=.8),
                       periodo4)
        elements = list(elements)
        elements1 = map(lambda x: x[1].grid(row=row, column=x[0] + 1), enumerate(elements.copy()))
        elements2 = map(lambda x: x.bind("<Enter>", self.__display_full_size), elements.copy())
        list(elements1)
        list(elements2)

    def __make_incomplete_row(self, elements, row):
        periodos = map(lambda x: (x.period, x, x.number), list(elements.values()))
        periodo1 = filter(lambda x: x[0] == row, periodos)
        elements = map(lambda x: (Element(self.tabla_container,
                                          element=x[1],
                                          factor=.8),
                                  x[1]),
                       periodo1)
        elements = list(elements)
        list(map(lambda x: x[0].bind("<Enter>", self.__display_full_size), elements.copy()))
        list(map(lambda x: x[0].grid(column=x[1].xpos, row=x[1].ypos),
                 elements.copy()))

    def __make_lantanids_actinids(self, elements, row):
        periodos = map(lambda x: (x.period, x, x.number), list(elements.values()))
        periodo4 = filter(lambda x: bool(int(x[0] == row) & ((int(x[2] in self.lantanids) |
                          int(x[2] in self.actinids)))), periodos)
        cols = range(2, 16)
        rows = [row - 1] * len(cols)
        elements = map(lambda x: (Element(self.tabla_container,
                                  element=x[1],
                                  factor=.8)), periodo4)
        elements = list(elements)
        pos = zip(elements.copy(), zip(rows, cols))

        list(map(lambda x: x[0].grid(column=x[1][1] + 1, row=row + 10),
             pos))
        list(map(lambda x: x.bind("<Enter>", self.__display_full_size), elements.copy()))

    def __make_groups(self):
        list(map(
            lambda x: ttk.Label(self.tabla_container, text=str(x),
                                font=("Helvetica", 8)).grid(row=0, column=x),
            [1, 18]))

        list(map(
            lambda x: ttk.Label(self.tabla_container, text=str(x),
                                font=("Helvetica", 8)).grid(row=1, column=x),
            [2, 13, 14, 15, 16, 17]))

        list(map(
            lambda x: ttk.Label(self.tabla_container, text=str(x),
                                font=("Helvetica", 8)).grid(row=3, column=x),
            range(3, 13)))

    def __make_periods(self):
        elems_pos = map(
            lambda x: ttk.Label(self.tabla_container, text=str(x),
                                font=("Helvetica", 8)).grid(row=x, column=0),
            range(1, 8))
        list(elems_pos)
