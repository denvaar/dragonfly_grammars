from dragonfly import Grammar

from rules.iterm2 import RestartProgramRule, GitRule

iterm2_grammar = Grammar("iterm2")

iterm2_grammar.add_rule(RestartProgramRule())
iterm2_grammar.add_rule(GitRule())

iterm2_grammar.load()

def unload():
    global iterm2_grammar

    if iterm2_grammar:
        iterm2_grammar.unload()
    iterm2_grammar = None
