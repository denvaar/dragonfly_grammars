from dragonfly import MappingRule, Text, Key


class CodeShortcutRule(MappingRule):
    mapping = {
        "[do some] (parenthesis | arguments | parameters)": Text("()") \
            + Key("left"),
        "[do an | make an] (braces | object)": Text("{}") + Key("left"),
        "[do a | make a] string": Text("\"\"") + Key("left"),
        "[do an | make an] arrow": Text("-> "),
        "[do a | make a] comment": Text("// "),
    }

class KeywordsRule(MappingRule):
    mapping = {
        "const": Text("const "),
    }

    extras = []
