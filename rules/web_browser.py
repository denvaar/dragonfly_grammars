from dragonfly import MappingRule, Mouse, Key, Function

from pynput.mouse import Controller, Button

controller = Controller()

def left_click(n):
    controller.click(Button.left, n)

class CopyPasta(MappingRule):
    mapping = {
        "copy": Key("w-c"),
        "paste": Key("w-v")
    }

class ClickRule(MappingRule):
    mapping = {
        "click": Mouse("left"),
        "right click": Mouse("right"),

        # broken
        # "double click": Mouse("left:2"),
        "double click": Function(lambda: left_click(2)),

        # broken
        # "triple click": Mouse("left:3"),
        "triple click": Function(lambda: left_click(3)),

        "hold click": Mouse("left:down"),
        "release click": Mouse("left:up"),
    }

    extras = []

    defaults = {}

