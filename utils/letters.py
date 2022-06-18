from dragonfly import Choice

def singleLetter(name="letter"):
    lowers = {
        '(aye | alpha | A)' : 'a',
        '(bee | beta | B)' : 'b',
        '(see | char | C)' : 'c',
        '(dee | delta | D)' : 'd',
        '(echo | E)' : 'e',
        '(fox | foxtrot | F)' : 'f',
        '(jee | G)' : 'g',
        '(hotel | H)' : 'h',
        '(eye | india | I)' : 'i',
        '(jay | J)' : 'j',
        '(kay | K)' : 'k',
        '(el | lima | L)' : 'l',
        '(mike | M)' : 'm',
        '(knot | N)' : 'n',
        '(oh | oscar | O)' : 'o',
        '(pee | pea | prime | P)' : 'p',
        '(queue | quack | Q)' : 'q',
        '(romeo | arr | R)' : 'r',
        '(ess | sierra | S)' : 's',
        '(tee | tea | tango | T)' : 't',
        '(you | yew | U | uni)' : 'u',
        '(vee | victor | V)' : 'v',
        '(double you | W | wet | dub)' : 'w',
        '(ex | X | x ray | xylophone)' : 'x',
        '(why | Y | yankee)' : 'y',
        '(zee | Z | zulu | zed | zap)' : 'z',
    }

    uppers = dict(
        [("(upper | big) " + k, v.upper()) for k, v in lowers.items()])

    symbols = {
        '(left | open) parenthesis': '(',
        '(right | close) parenthesis': ')',

        '(left | open) brace': '{',
        '(right | close) brace': '}',

        '(left | open) bracket': '[',
        '(right | close) bracket': ']',

        'percent': '%',
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
