# main.py
# KMK firmware for Seeed Studio XIAO RP2040
# Matrix: 4 columns x 2 rows

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.modules.macros import Macros
from kmk.keys import KC, Key

keyboard = KMKKeyboard()

keyboard.col_pins = (
    board.D0,
    board.D1,
    board.D2,
    board.D3,
)
keyboard.row_pins = (
    board.D5,
    board.D6,
)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.modules.append(Macros())

# Macro test:
# HELLO = KC.MACRO("WOW")

keyboard.keymap = [
    [
        KC.LCTRL(KC.C), KC.LCTRL(KC.V), KC.LCTRL(KC.X), KC.LCTRL(KC.LALT(KC.DEL)),
        KC.LCTRL(KC.T), KC.LCTRL(KC.W), KC.LSFT(KC.LCTRL(KC.T)), KC.LCTRL(KC.LSFT(KC.LALT(KC.F))),
    ]
]

if __name__ == "__main__":
    keyboard.go()
