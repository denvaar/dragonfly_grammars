from dragonfly import (MappingRule, Key, IntegerRef, Function, Dictation,
                       Text, Compound)

from utils.letters import singleLetter
from utils.casing import text_casing_choice, format_dictation

def select_menu_opt(option_n=None):
    if option_n:
        action = Key('c-n:%(option_n)d') + Key("tab")
        return action.execute({"option_n": option_n - 1})

    return Key("tab").execute()

class InsertModeRule(MappingRule):
    mapping = {
        "normal [mode]": Key("escape"),

        "complete": Key('c-n'),
        "option <n>": Key('c-n:%(n)d'),
        "option down <n>": Key('c-n:%(n)d'),
        "option up <n>": Key('c-p:%(n)d'),
        "select option [<option_n>]": Function(select_menu_opt),

        "enter": Key('enter'),
        "(tab | tabby)": Key('tab'),

        "<letter>": Text("%(letter)s"),

    }

    extras = [
        singleLetter("letter"),
        IntegerRef("option_n", 1, 900),
        IntegerRef("n", 1, 900),
        Dictation("dictation"),
    ]

    defaults = {
        "n": 1
    }

class DictationRule(MappingRule):
    mapping = {
        "(type | dictate) [<format_style>] <freeform_text>": Function(
            format_dictation),
    }

    extras = [
        text_casing_choice("format_style"),
        Dictation("freeform_text"),
    ]

