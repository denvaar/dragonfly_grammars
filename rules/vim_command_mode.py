from dragonfly import MappingRule, Key, Text

class FileOperations(MappingRule):
    mapping = {
        "save": Text(":w") + Key("enter"),
        "quit": Text(":q") + Key("enter"),
        "quit all": Text(":qa") + Key("enter"),
        "force quit all": Text(":qa!") + Key("enter"),
        "force quit": Text(":q!") + Key("enter"),
        "save [and] quit": Text(":wq") + Key("enter"),
    }

    extras = []

    defaults = {}

class SearchAndReplaceRule(MappingRule):
    mapping = {
        "find and replace": Text(":%s///gc") + Key("left:4"),
        "(cancel | escape)": Key("escape")
    }

    extras = []

    defaults = {}
