from dragonfly import MappingRule, Function, Text, Key, Literal

from utils.elixir_enum_function_choice import elixir_enum_choice

class CodeShortcutRule(MappingRule):
    mapping = {
        "[do some] (parenthesis | arguments | parameters)": Text("()") + Key("left"),
        "[do a | make a] map": Text("\%{}") + Key("left"),
        "[do a | make a] (braces | to pull)": Text("{}") + Key("left"),
        "[do a | make a] string": Text("\"\"") + Key("left"),
        "[do a | make a] pipe": Text("|> "),
    }

class KeywordsRule(MappingRule):
    mapping = {
        "E numb [<dot> [<enum_function>]]": Text("Enum%(dot)s%(enum_function)s"),
        "map [<dot>]": Text("Map%(dot)s"),
        "echo [<dot>]": Text("Ecto%(dot)s"),
    }

    extras = [
        Literal("dot", "dot", ".", ""),
        elixir_enum_choice("enum_function"),
    ]


