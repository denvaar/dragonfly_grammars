from dragonfly import MappingRule, Mouse


class ClickRule(MappingRule):
    mapping = {
        "click": Mouse("left"),
        "right click": Mouse("right"),
        "double click": Mouse("left:2"),
        "triple click": Mouse("left:3"),
    }

    extras = []

    defaults = {}

