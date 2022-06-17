from dragonfly import AppContext

class ElixirContext(AppContext):
    def matches(self, executable, title, handle):
        match = "ext:ex" in title
        print(f'elixir context match: {match}')

        return match
