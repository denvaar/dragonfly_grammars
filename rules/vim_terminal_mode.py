from dragonfly import MappingRule, Key, IntegerRef, Function, Dictation, Text

from utils.letters import singleLetter
from utils.casing import text_casing_choice, format_dictation

class FzfFinderWindowRule(MappingRule):
    mapping = {
        "[option] down <n>": Key('c-n:%(n)d'),
        "[option] up <n>": Key('c-p:%(n)d'),

        "open split": Key('c-v, enter'),
        "open tab": Key('c-t, enter'),
        "open here": Key('enter'),
        "enter": Key('enter'),

        "(type | dictate) [<format_style>] <freeform_text>": Function(
            format_dictation),

        "<letter>": Text("%(letter)s"),
    }

    extras = [
        singleLetter("letter"),
        IntegerRef("n", 1, 900),
        text_casing_choice("format_style"),
        Dictation("freeform_text"),
    ]

    defaults = {
        "n": 1
    }

