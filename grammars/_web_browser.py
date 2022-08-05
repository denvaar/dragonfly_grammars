from dragonfly import Grammar

from contexts.web_browser import WebBrowserContext

from rules.web_browser import ClickRule
from rules.web_browser import CopyPasta

web_browser_grammar = Grammar("web browser", context=WebBrowserContext())

web_browser_grammar.add_rule(ClickRule())
web_browser_grammar.add_rule(CopyPasta())

web_browser_grammar.load()

def unload():
    global web_browser_grammar

    if web_browser_grammar:
        web_browser_grammar.unload()
    web_browser_grammar = None
