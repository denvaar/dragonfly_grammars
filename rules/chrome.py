from dragonfly import MappingRule, Mouse


class ClickRule(MappingRule):
    mapping = {
        "click": Mouse("left")
    }

    extras = []

    defaults = {}

