from dragonfly import MappingRule, Key, Text

misc_mapping = {
    "escape": Key("escape")
}

file_op_mapping = {
    "(save quit | whale quench)": Text("wq") + Key("enter"),
    "(save | whale)": Text("w") + Key("enter"),
    "(quit | quench)": Text("q") + Key("enter"),
    "(quit all | quench air)": Text("qa") + Key("enter"),
    "(force quit all | quench air bang)": Text("qa!") + Key("enter"),
    "(force quit | quench bang)": Text("q!") + Key("enter"),
    "(save [and] quit | whale quench)": Text("wq") + Key("enter"),
}

find_replace_mapping = {
    "(search | find) and replace": Text("%%s///gc") + Key("left:4"),
}

class CommandModeMisc(MappingRule):
    mapping = misc_mapping


class FileOperations(MappingRule):
    mapping = file_op_mapping


class SearchAndReplace(MappingRule):
    mapping = find_replace_mapping

