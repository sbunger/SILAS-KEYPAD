import board

from kmk.scanners import DiodeOrientation
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Press, Release, Tap, Macros

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

# 4x2 matrix
col_pins = (board.A0, board.A1, board.A2, board.A3)
row_pins = (board.SLC, board.TX)
diode_orientation = DiodeOrientation.COL2ROW

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    [KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8]
]

# Start kmk!
if __name__ == '__main__':
    keyboard.go()