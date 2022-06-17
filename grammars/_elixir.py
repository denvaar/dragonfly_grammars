from dragonfly import Grammar

sleep_grammar = Grammar("sleep")
sleep_grammar.load()

def unload():
    global sleep_grammar
    if sleep_grammar:
        sleep_grammar.unload()
    sleep_grammar = None
