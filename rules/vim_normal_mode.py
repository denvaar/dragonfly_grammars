from dragonfly import (MappingRule, Dictation, Integer, Key, Function, Text,
                       Choice, CompoundRule, IntegerRef, RuleRef, Alternative,
                       Repetition, CompoundRule)

from utils.letters import singleLetter
from utils.casing import format_dictation, text_casing_choice
from rules.vim_insert_mode import _SpellingRule as InsertModeSpellingRule
from rules.vim_insert_mode import DictationRule as InsertModeDictationRule


movement_mapping = {
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

    "[<n>] (jump | fine) <letter>": Text("%(n)df%(letter)s"),
    "[<n>] (jump (backwards | backward) | big fine) <letter>": \
        Text("%(n)dF%(letter)s"),

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

    "[<n>] (ex | x | exit)": Text("%(n)dx"),

    "[<n>] (delete | D | dee)": Text("%(n)dd"),
    "[<n>] (delete | D | dee) (until | tea | tee | T) <letter>": Text(
        f"%(n)ddt%(letter)s"),
    "(delete | D | dee) (dub | word)": Text("dw"),

    "(dee dee | D D)": Text("dd"),

    "(clear inner | see eye) <letter>": Text("ci%(letter)s"),

    "replace <letter>": Text("r%(letter)s"),

    "insert [<format_style>] <freeform_text>": Key('i') + Function(format_dictation) + Key('escape'),

    # "insert <insert_mode_spelling_rule>": Key('i') + Text('%(insert_mode_spelling_rule)s') + Key('escape')
}

editing_extras = [
    singleLetter("letter"),
    IntegerRef("n", 1, 900),
    text_casing_choice("format_style"),
    Dictation("freeform_text"),
    # RuleRef(rule=InsertModeSpellingRule(), name="insert_mode_spelling_rule"),
]

editing_defaults = {
    "n": 1,
}

misc_mapping = {
    "insert mode": Key("i"),

    "(visual | V) line": Key("shift:down, v, shift:up"),
    "(visual | V) block": Key("control:down, v, control:up"),

    "(V eye eye | select inner indent)": Text("vii"),
    "(see eye (tee | tea) | clear inner tag)": Text("cit"),

    "escape": Key("escape"),
    "command save quit": Text(":wq\n"),

    "command save": Text(":w") + Key("enter"),
    "command quit": Text(":q") + Key("enter"),
    "command quit all": Text(":qa") + Key("enter"),
    "command force quit all": Text(":qa!") + Key("enter"),
    "command force quit": Text(":q!") + Key("enter"),
    "command save [and] quit": Text(":wq") + Key("enter"),

    "next tab": Text("gt"),
    "previous tab": Text("gT"),
    "([go to] (tab | tabby) | G T) <n>": Text("%(n)dgt"),

    "file search": Key("control:down, p, control:up"),
    "code search": Key("control:down, i, control:up"),
    "option <n>": Key('c-n:%(n)d'),
    "option down <n>": Key('c-n:%(n)d'),
    "option up <n>": Key('c-p:%(n)d'),

    "search for this word": Key("#"),

    "search [for] [<format_style>] <freeform_text>": Text("/") + Function(
        format_dictation) + Key("enter"),
    "next [match]": Key('n'),
    "previous [match]": Key('N'),
    "(no H L | no high | no highlight)": Text(":nohl") + Key("enter"),

    "(control dub dub | next window)": Key("c-w, c-w"),
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

misc_sequence = Repetition(
    Alternative([
        movement_rule_ref,
        misc_rule_ref,
        editing_rule_ref,
    ]),
    min=1,
    max=20,
    name="misc_sequence"
)

movement_sequence = Repetition(
    Alternative([
        misc_rule_ref,
        movement_rule_ref,
        editing_rule_ref,
    ]),
    min=1,
    max=20,
    name="movement_sequence"
)

edit_sequence = Repetition(
    Alternative([
        movement_rule_ref,
        editing_rule_ref,
        misc_rule_ref,
    ]),
    min=1,
    max=20,
    name="edit_sequence"
)

insert_spell_it_seq = Repetition(Alternative([insert_mode_spelling_ref, ]),
                                 min=1, max=16, name="insert_spell_it_seq")

class MiscSequenceRule(CompoundRule):
    spec = "<misc_sequence>"
    extras = [
        misc_sequence,
    ]

    def _process_recognition(self, node, extras):
        sequence = extras["misc_sequence"]
        for action in sequence:
            action.execute()


class MovementSequenceRule(CompoundRule):
    spec = "<movement_sequence>"
    extras = [
        movement_sequence,
    ]

    def _process_recognition(self, node, extras):
        sequence = extras["movement_sequence"]
        for action in sequence:
            action.execute()


class EditSequenceRule(CompoundRule):
    spec = "<edit_sequence>"
    extras = [
        edit_sequence,
    ]

    def _process_recognition(self, node, extras):
        sequence = extras["edit_sequence"]
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

