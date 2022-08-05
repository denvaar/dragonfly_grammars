from dragonfly import (MappingRule, Dictation, Integer, Key, Function, Text,
                       Choice, CompoundRule, IntegerRef, RuleRef, Alternative,
                       Repetition, CompoundRule, FuncContext)

from utils.letters import singleLetter
from utils.casing import format_dictation, text_casing_choice
from rules.vim_insert_mode import _SpellingRule as InsertModeSpellingRule
from rules.vim_insert_mode import DictationRule as InsertModeDictationRule

from rules.vim_command_mode import FileOperations as CommandModeFileOperations
from rules.vim_command_mode import CommandModeMisc
from rules.vim_command_mode import SearchAndReplace as CommandModeSearchAndReplace


movement_mapping = {
    "[<n>] jury": Text("%(n)dj"),
    "[<n>] kite": Text("%(n)dk"),
    "[<n>] harp": Text("%(n)dh"),
    "[<n>] look": Text("%(n)dl"),

    "[<n>] (word | whale)": Text("%(n)dw"),
    "[<n>] big (word | whale)": Text("%(n)dW"),

    "[<n>] each": Text("%(n)de"),
    "[<n>] big each": Text("%(n)dE"),

    "[<n>] bat": Text("%(n)db"),
    "[<n>] big bat": Text("%(n)dB"),

    "(guest guest | top)": Text("gg"),
    "(big guest | bottom)": Text("G"),

    "[<n>] fine <letter>": Text("%(n)df%(letter)s"),
    "[<n>] big fine <letter>": Text("%(n)dF%(letter)s"),

    "page down": Key('c-d'),
    "page up": Key('c-u'),

    "dollar": Key("$"),
    "carrot": Key("^"),
}

movement_extras = [
    singleLetter("letter"),
    IntegerRef("n", 1, 900),
]

movement_defaults = {
    "n": 1,
}

editing_mapping = {
    "big sit": Key("I"),

    "(air | append)": Key("a"),
    "big (air | append)": Key("A"),

    "odd": Key("o"),
    "big odd": Key("O"),

    "undo": Key("u"),
    "redo": Key("c-r"),

    "big jury": Key("J"),

    "(yank yank | yankee yankee)": Text("yy"),
    "(yank | yankee)": Key("y"),
    "pit": Key("p"),

    "[<n>] plex": Text("%(n)dx"),

    "[<n>] drum": Text("%(n)dd"),
    "[<n>] drum (until | trap) <letter>": Text(
        f"%(n)ddt%(letter)s"),
    "drum whale": Text("dw"),

    "drum drum": Text("dd"),

    "(clear inner | cap sit) <letter>": Text("ci%(letter)s"),

    "(red | replace) <letter>": Text("r%(letter)s"),

    "insert [<format_style>] <freeform_text>": Key('i') + Function(format_dictation) + Key('escape'),
}

editing_extras = [
    singleLetter("letter"),
    IntegerRef("n", 1, 900),
    text_casing_choice("format_style"),
    Dictation("freeform_text"),
]

editing_defaults = {
    "n": 1,
}

misc_mapping = {
    "insert mode": Key("i"),
    "(visual | vest) line": Key("shift:down, v, shift:up"),
    "(visual | vest) block": Key("control:down, v, control:up"),
    "command mode": Key("colon"),

    "escape": Key("escape"),

    "(vest sit sit | select inner indent)": Text("vii"),
    "(cap sit trap | clear inner tag)": Text("cit"),
     

    "(next tab | guest trap)": Text("gt"),
    "(previous tab | guest big trap)": Text("gT"),
    "([go to] tab | guest trap) <n>": Text("%(n)dgt"),

    "file search": Key("control:down, p, control:up"),
    "code search": Key("control:down, i, control:up"),
    "code search for this": Key("control:down, k, control:up"),

    "option <n>": Key('c-n:%(n)d'),
    "option down <n>": Key('c-n:%(n)d'),
    "option up <n>": Key('c-p:%(n)d'),

    "search for this word": Key("#"),
    "search for [<format_style>] <freeform_text>": Text("/") + Function(
        format_dictation) + Key("enter"),

    "(next [match] | near)": Key('n'),
    "(previous [match] | big near)": Key('N'),

    "(no harp look | no harp | no highlight)": Text(":nohl") + Key("enter"),

    "(control whale whale | next window)": Key("c-w, c-w"),
    "previous window": Key("c-w, c-p"),

    "current path expand": Key("percent, colon, h, tab")
}

misc_extras = [
    IntegerRef("n", 1, 900),
    Dictation("freeform_text"),
    text_casing_choice("format_style")
]

misc_defaults = {}

class Movement(MappingRule):
    exported = False
    mapping = movement_mapping
    extras = movement_extras
    defaults = movement_defaults

class Editing(MappingRule):
    exported = False
    mapping = editing_mapping
    extras = editing_extras
    defaults = editing_defaults

class Misc(MappingRule):
    exported = False
    mapping = misc_mapping
    extras = misc_extras
    defaults = misc_defaults

misc_rule_ref = RuleRef(rule=Misc())
movement_rule_ref = RuleRef(rule=Movement())
editing_rule_ref = RuleRef(rule=Editing())
insert_mode_spelling_ref = RuleRef(rule=InsertModeSpellingRule())

sequence = Repetition(
    Alternative([
        movement_rule_ref,
        misc_rule_ref,
        editing_rule_ref,
    ]),
    min=1,
    max=20,
    name="sequence"
)

insert_spell_it_seq = Repetition(Alternative([insert_mode_spelling_ref, ]),
                                 min=1, max=16, name="insert_spell_it_seq")

class SequenceRule(CompoundRule):
    spec = "<sequence>"
    extras = [
        sequence,
    ]

    def _process_recognition(self, node, extras):
        sequence = extras["sequence"]
        for action in sequence:
            action.execute()


class InsertSpellItRule(CompoundRule):
    spec = "<mode> spell it <insert_spell_it_seq>"
    extras = [
        insert_spell_it_seq,
        Choice("mode", {
            "insert": "i",
            "append": "a",
            "big (insert | I | eye)": "I",
            "big (append | A)": "A",
        })
    ]

    def _process_recognition(self, node, extras):
        sequence = [Key(extras["mode"])] \
            + extras["insert_spell_it_seq"] \
            + [Key('escape')]

        for action in sequence:
            action.execute()

class InsertDictateRule(CompoundRule):
    spec = "<mode> <insert_dictate_ref>"
    extras = [
        RuleRef(rule=InsertModeDictationRule(), name="insert_dictate_ref"),
        Choice("mode", {
            "insert": "i",
            "append": "a",
            "big (insert | I | eye)": "I",
            "big (append | A)": "A",
        })
    ]

    def _process_recognition(self, node, extras):
        sequence = [Key(extras["mode"])] \
            + [extras["insert_dictate_ref"]] \
            + [Key('escape')]

        for action in sequence:
            action.execute()

class QuickCommand(CompoundRule):
    """execute a single command-mode rule"""

    spec = "command <x>"
    extras = [
        Alternative(
            children=[
                RuleRef(rule=CommandModeFileOperations()),
                RuleRef(rule=CommandModeMisc()),
                RuleRef(rule=CommandModeSearchAndReplace()),
            ],
            name="x"
        )
    ]

    def _process_recognition(self, node, extras):
        seq = [Key("colon")] + [extras["x"]]
            
        for action in seq:
            action.execute()

