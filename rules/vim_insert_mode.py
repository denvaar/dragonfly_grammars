from dragonfly import (MappingRule, Key, IntegerRef, Function, Dictation,
                       Text, CompoundRule, Alternative, Repetition, RuleRef)

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
        "back space": Key('backspace'),
        "(tab | tabby)": Key('tab'),
        "escape": Key('escape'),

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

class _SpellingRule(MappingRule):
    exported = False

    mapping = {
        "<letter>": Text("%(letter)s"),
    }

    extras = [
        singleLetter("letter"),
    ]

spelling_ref = RuleRef(rule=_SpellingRule())
sequence = Repetition(Alternative([
    spelling_ref,
]),
                      min=1, max=16, name="spelling_sequence")

class SpellingRule(CompoundRule):
    spec = "spell it <spelling_sequence>"
    extras = [
        sequence,
    ]

    def _process_recognition(self, node, extras):
        sequence = extras["spelling_sequence"]
        for action in sequence:
            action.execute()
