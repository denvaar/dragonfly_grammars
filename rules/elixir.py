from dragonfly import MappingRule, Function, Text, Key, Literal

from utils.elixir_enum_function_choice import elixir_enum_choice

class CodeShortcutRule(MappingRule):
    mapping = {
        "[do some] (parenthesis | arguments | parameters)": Text("()") \
            + Key("left"),
        "[do a | make a] map": Text("%%{}") + Key("left"),
        "[do a | make a] (braces | to pull)": Text("{}") + Key("left"),
        "[do a | make a] string": Text("\"\"") + Key("left"),
        "[do a | make a] pipe": Text("|> "),
        "[do a | make a] [rocket | fat arrow]": Text("=> "),
        "[do an | make an] arrow": Text("-> "),
        "[do a | make a] comment": Text("# "),
        "[do an | make an] embedded elixir variable": Text("<%%=  %%>") + Key('left:3'),
    }

class KeywordsRule(MappingRule):
    mapping = {
        "E numb [<dot> [<enum_function>]]": \
            Text("Enum%(dot)s%(enum_function)s"),
        "map [<dot>]": Text("Map%(dot)s"),
        "echo [<dot>]": Text("Ecto%(dot)s"),

        "(eye oh dot inspect | I O dot inspect)": Text("IO.inspect()") \
            + Key("left"),

        "is (nail | nil)": Text("is_nil()") + Key("left"),

        "when": Text("when "),
        "not": Text("not "),

        "(def | death)": Text("def "),
        "(def | death) (pea | pit)": Text("defp "),
        "(def | death) module": Text("defmodule "),
    }

    extras = [
        Literal("dot", "dot", ".", ""),
        elixir_enum_choice("enum_function"),
    ]

