from dragonfly import MappingRule, Mouse, Key

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

        # broken
        # "triple click": Mouse("left:3"),

        "hold click": Mouse("left:down"),
        "release click": Mouse("left:up"),
    }

    extras = []

    defaults = {}

