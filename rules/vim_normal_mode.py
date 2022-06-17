from dragonfly import (MappingRule, Dictation, Integer, Key, Function, Text,
                       Choice, CompoundRule, IntegerRef)

from utils.letters import singleLetter
from utils.casing import format_dictation, text_casing_choice


class Movement(MappingRule):
    mapping = {
        "[<n>] (down | jay | J)": Text("%(n)dj"),
        "[<n>] (up | kay | K)": Text("%(n)dk"),
        "[<n>] (left | H)": Text("%(n)dh"),
        "[<n>] (right | el | L)": Text("%(n)dl"),

        "[<n>] (word | dub | W)": Text("%(n)dw"),
        "[<n>] big (word | dub | W)": Text("%(n)dW"),

        "[<n>] (eee | E)": Text("%(n)de"),
        "[<n>] big (eee | E)": Text("%(n)dE"),

        "[<n>] (bee | be | B)": Text("%(n)db"),
        "[<n>] (big | cap | capital) (bee | be | B)": Text("%(n)dB"),

        "(jee jee | top)": Text("gg"),
        "(big G | big jee | bottom)": Text("G"),

        "[<n>] (find | jump | F) <letter>": Text("%(n)df%(letter)s"),

        "page down": Key('c-d'),
        "page up": Key('c-u'),

        "dollar": Key("$"),
        "carrot": Key("^"),
    }

    extras = [
        singleLetter("letter"),
        IntegerRef("n", 1, 900),
    ]

    defaults = {
        "n": 1,
    }

class Editing(MappingRule):
    mapping = {
        "(eye | I)": Key("i"),
        "big (eye | I)": Key("I"),

        "(A | append)": Key("a"),
        "big (A | append)": Key("A"),

        "(oh | O)": Key("o"),
        "big (oh | O)": Key("O"),

        "undo": Key("u"),
        "redo": Key("c-r"),

        "(yank line | why why)": Text("yy"),
        "(yank | why | Y)": Key("y"),
        "(paste | pea | pee | P)": Key("p"),

        "[<n>] (ex | x)": Key("%(n)dx"),

        "[<n>] (delete | D | dee)": Key("d"),
        "(delete | D | dee) (until | tea | tee | T) <letter>": Text(
            "dt%(letter)s"),
        "(delete | D | dee) (dub | word)": Text("dw"),

        "(clear inner | see eye) <letter>": Text("ci%(letter)s"),
    }

    extras = [
        singleLetter("letter"),
        IntegerRef("n", 1, 900),
    ]

    defaults = {
        "n": 1,
    }

class Misc(MappingRule):
    mapping = {
        "insert [mode]": Key("i"),

        "(visual | V) line": Key("shift:down, v, shift:up"),
        "(visual | V) block": Key("control:down, v, control:up"),

        "(V eye eye | select inner indent)": Text("vii"),

        "escape": Key("escape"),
        "save": Text(":w\n"),
        "save quit": Text(":wq\n"),

        "file search": Key("control:down, p, control:up"),
        "code search": Key("control:down, i, control:up"),
        "option <n>": Key('c-n:%(n)d'),
        "option down <n>": Key('c-n:%(n)d'),
        "option up <n>": Key('c-p:%(n)d'),

        "(find | search) [<format_style>] <freeform_text>": Function(
            format_dictation) + Key("enter")
    }

    extras = [
        IntegerRef("n", 1, 900),
        Dictation("freeform_text"),
        text_casing_choice("format_style")
    ]

    defaults = {}
