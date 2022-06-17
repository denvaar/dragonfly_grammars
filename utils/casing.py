from dragonfly import Text, Choice
from utils.format import (default_case, snake_case, pascal_case, kebab_case,
                          camel_case, capslock_case)

def text_casing_choice(name):
    return Choice(name, {
        "all caps": "all caps",
        "snake": "snake",
        "pascal": "pascal",
        "(kebab | skewer)": "kebab",
        "camel": "camel",
    }, default="")


def format_dictation(format_style, freeform_text):
    transformation_functions = {
        'snake': snake_case,
        'pascal': pascal_case,
        'kebab': kebab_case,
        'camel': camel_case,
        'all caps': capslock_case,
        '': default_case,
    }

    transformation = transformation_functions.get(
        format_style, lambda default: default)(freeform_text)

    return Text(f'{transformation}').execute()

