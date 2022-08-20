from tkinter import Tk, ttk
from GUI.periodic_table import PeriodictTable
from i18n import I18nString

RIGHT = 50
DOWN = 120

STRINGS = I18nString()


class MainScreen:
    def __init__(self):
        self.window = Tk()
        self.window.resizable(False, False)
        self.window.geometry(f"340x720+{RIGHT}+{DOWN}")
        self.__configure_font("Helvetica", 18)

        self.__make_label(STRINGS.main_screen["title"], 0, 0)

        self.__make_button(STRINGS.main_screen["main_button"], 38, 0, 1)
        self.window.mainloop()

    def __make_label(self, text, gridx, gridy):
        label = ttk.Label(self.window, text=text)
        label.grid(column=gridx, row=gridy, padx=10, pady=20)

    def __invoke_periodic(self):
        PeriodictTable(self.window)

    def __make_button(self, text, width, gridx, gridy):
        button = ttk.Button(self.window, text=text, width=width, command=self.__invoke_periodic)
        button.grid(column=gridx, row=gridy, padx=10, pady=5)

    def __configure_font(self, name, size):
        self.window.option_add("*Font", f"{name} {size}")


if __name__ == "__main__":
    MainScreen()
