from dragonfly import MappingRule, Key, Text

class RestartProgramRule(MappingRule):
    mapping = {
        "control (C | see) restart (program | app)": Key('c-c, c-c, c-c, up, enter'),
        "control D restart (program | app)": Key('c-d, up, enter')
    }

    extras = []
    defaults = {}

class RestartProgramRule(MappingRule):
    mapping = {
        "control (C | see) restart (program | app)": Key('c-c, c-c, c-c, up, enter'),
        "control D restart (program | app)": Key('c-d, up, enter')
    }

    extras = []
    defaults = {}

class GitRule(MappingRule):
    mapping = {
        "get branch": Text("git branch") + Key('enter'),
        "get pull": Text("git pull") + Key('enter'),
        "make a new branch": Text("git checkout -b "),
    }

    extras = []
    defaults = {}
