from dragonfly import AppContext

class ElixirContext(AppContext):
    def matches(self, executable, title, handle):
        match = "ext:ex" in title \
            or "ext:eex" in title
        return match

