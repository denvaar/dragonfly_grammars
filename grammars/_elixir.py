from dragonfly import Grammar

from contexts.elixir import ElixirContext
from rules.elixir import CodeShortcutRule, KeywordsRule

elixir_grammar = Grammar("elixir", context=ElixirContext())

elixir_grammar.add_rule(CodeShortcutRule())
elixir_grammar.add_rule(KeywordsRule())

elixir_grammar.load()

def unload():
    global elixir_grammar
    if elixir_grammar:
        elixir_grammar.unload()
    elixir_grammar = None
