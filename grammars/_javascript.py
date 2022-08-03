from dragonfly import Grammar

from contexts.javascript import JavascriptContext
from rules.javascript import CodeShortcutRule, KeywordsRule

javascript_grammar = Grammar("javascript",
                             context=JavascriptContext())

javascript_grammar.add_rule(CodeShortcutRule())
javascript_grammar.add_rule(KeywordsRule())
javascript_grammar.load()

def unload():
    global javascript_grammar

    if javascript_grammar:
        javascript_grammar.unload()

    javascript_grammar = None

