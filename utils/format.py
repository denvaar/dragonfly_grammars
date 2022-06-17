def snake_case(text):
    return text.lower().replace(" ", "_")

def pascal_case(text):
    return text.title().replace(" ", "")

def kebab_case(text):
    return text.lower().replace(" ", "-")

def camel_case(text):
    pascal_formatted = list(pascal_case(text))
    pascal_formatted[0] = pascal_formatted[0].lower()
    return "".join(pascal_formatted)

def capslock_case(text):
    return text.upper()

def default_case(text):
    return text
