from dragonfly import Grammar

from contexts.chrome import ChromeContext

from rules.chrome import ClickRule

chrome_grammar = Grammar("chrome",context=ChromeContext())

chrome_grammar.add_rule(ClickRule())

chrome_grammar.load()

def unload():
    global chrome_grammar

    if chrome_grammar:
        chrome_grammar.unload()
    chrome_grammar = None
