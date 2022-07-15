from dragonfly import Choice

def singleLetter(name="letter"):
    lowers = {
        'air' : 'a',
        'bat' : 'b',
        'cap' : 'c',
        'drum' : 'd',
        'each' : 'e',
        'fine' : 'f',
        'guest' : 'g',
        'harp' : 'h',
        'sit' : 'i',
        'jury' : 'j',
        'kite' : 'k',
        'look' : 'l',
        'made' : 'm',
        'near' : 'n',
        'odd' : 'o',
        '(pitt | pit)' : 'p',
        'quench' : 'q',
        '(read | red)' : 'r',
        'sun' : 's',
        'trap' : 't',
        'urge' : 'u',
        'vest' : 'v',
        'whale' : 'w',
        'plex' : 'x',
        '(yankee | yank)' : 'y',
        'zip' : 'z',
    }

    uppers = dict(
        [("(upper | big | capital) " + k, v.upper()) for k, v in lowers.items()])

    symbols = {
        '(left | open) parenthesis': '(',
        '(right | close) parenthesis': ')',

        '(left | open) brace': '{',
        '(right | close) brace': '}',

        '(left | open) bracket': '[',
        '(right | close) bracket': ']',

        'percent': '%',
        '(ampere | ampersand)': '&',
        'dollar [sign]': '$',
        '(tilda | squiggle)': '~',
        '(equal | equals)': '=',
        'colon': ':',
        '(dot | period)': '.',
        '(double quote | dub quote | string)': '"',
        'single quote': '\'',
        '(under | underscore)': '_',
        '(arrow | dash | minus)': '-',
        'space': ' ',
        'comma': ',',
        '(bar | vertical bar)': '|',

        '[forward] slash': '/',
    }

    return Choice(name, {**lowers, **uppers, **symbols})
