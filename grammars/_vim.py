from dragonfly import Grammar

from contexts.vim import VimNormalMode, VimInsertMode, VimTerminalMode
from rules.vim_normal_mode import Movement, Editing, Misc
from rules.vim_insert_mode import InsertModeRule, DictationRule
from rules.vim_terminal_mode import FzfFinderWindowRule

terminal_mode_grammar = Grammar("vim terminal mode",
                              context=VimTerminalMode())

terminal_mode_grammar.add_rule(FzfFinderWindowRule())
terminal_mode_grammar.load()

normal_mode_grammar = Grammar("vim normal mode",
                              context=VimNormalMode())

normal_mode_grammar.add_rule(Movement())
normal_mode_grammar.add_rule(Editing())
normal_mode_grammar.add_rule(Misc())

normal_mode_grammar.load()


insert_mode_grammar = Grammar("vim insert mode",
                              context=VimInsertMode())

insert_mode_grammar.add_rule(InsertModeRule())
insert_mode_grammar.add_rule(DictationRule())

insert_mode_grammar.load()


def unload():
    global terminal_mode_grammar
    global insert_mode_grammar
    global normal_mode_grammar

    if insert_mode_grammar:
        insert_mode_grammar.unload()

    if terminal_mode_grammar:
        terminal_mode_grammar.unload()

    if normal_mode_grammar:
        normal_mode_grammar.unload()

    terminal_mode_grammar = None
    insert_mode_grammar = None
    normal_mode_grammar = None
