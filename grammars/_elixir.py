from dragonfly import Grammar

from contexts.elixir import ElixirContext

grammar = Grammar("elixir", context=ElixirContext())
grammar.load()

def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
