from dragonfly import Grammar

from rules.sleep_and_awake import SleepRule, AriseRule

sleep_grammar = Grammar("sleep")

sleep_grammar.add_rule(AriseRule())
sleep_grammar.add_rule(SleepRule())

sleep_grammar.load()

def unload():
    global sleep_grammar
    if sleep_grammar:
        sleep_grammar.unload()
    sleep_grammar = None
