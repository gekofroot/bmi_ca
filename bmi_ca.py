#    Copyright (C) 2022 gekofroot
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    any later version.
#
#    This program is distributed WITHOUT ANY WARRANTY; 
#    See the GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see <https://www.gnu.org/licenses/>.



# modules
from tkinter import *
from os import sys


def main():

    # variables
    main_window = Tk()
    window_width = 700
    window_height = 400
    main_window.geometry(f"{window_width}x{window_height}")
    FONT = ("Helvetica", 14)
    FG = "#ffffff"
    BG = "#000000"
    BD = 0
    RLF_1 = FLAT

    # functions
    def bmi_button_pressed():
        height = float(get_height.get())
        weight = float(get_weight.get())
        height = height / 100
        bmi_index = (weight / (height * height))
        display_weight.configure(text = f"{bmi_index:.2f}")
        
    def clear_cmd():
        get_height.delete(0, END)
        get_weight.delete(0, END)
        display_weight.configure(text = "")

    def close_cmd():
        sys.exit()

    # widgets
    title = Label(text = "BMI", font = FONT, fg = FG, bg = BG, bd = BD, relief = RLF_1)
    get_height = Entry(font = FONT, fg = FG, bg = BG, bd = BD, relief = RLF_1, justify = CENTER)
    get_weight = Entry(font = FONT, fg = FG, bg = BG, bd = BD, relief = RLF_1, justify = CENTER)
    display_weight = Label(font = FONT, fg = FG, bg = BG, bd = BD, relief = RLF_1)
    bmi_button = Button(text = "[ Enter ]", font = FONT, fg = FG, bg = BG, bd = BD, relief = RLF_1,
            command = bmi_button_pressed)
    clear_button = Button(text = "[ Clear ]", font = FONT, fg = FG, bg = BG, bd = BD, relief = RLF_1,
            command = clear_cmd)

    # set widgets
    x_pos = window_width / 2
    y_pos = window_height / 4

    title.place(x = 0, y = 0, width = x_pos * 2, height = y_pos)

    get_height.place(x = 0, y = y_pos, width = x_pos, height = y_pos)
    get_weight.place(x = x_pos, y = y_pos, width = x_pos, height = y_pos)
    display_weight.place(x = 0, y = y_pos * 2, width = x_pos * 2, height = y_pos)
    bmi_button.place(x = 0, y = y_pos * 3, width = x_pos, height = y_pos)
    clear_button.place(x = x_pos, y = y_pos * 3, width = x_pos, height = y_pos)

    # menu
    top_menu = Menu(main_window)
    settings_menu = Menu(top_menu)
    settings_menu.add_command(label = "Close", command = close_cmd)
    top_menu.add_cascade(label = "Settings", menu = settings_menu)
    main_window.config(menu = top_menu)

    main_window.mainloop()


if __name__ == '__main__':
    main()
