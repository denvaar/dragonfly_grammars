from dragonfly import AppContext

class VimContext(AppContext):
    def matches(self, executable, title, handle):
        match = "app:nvim" in title
        print(f'VimContext: {match}')

        return match

class VimNormalMode(AppContext):
    def matches(self, executable, title, handle):
        match = "mode:n" in title \
            or "mode:V" in title \
            or "mode:^V" in title

        print(f'VimNormalMode: {match}')

        return match

class VimInsertMode(AppContext):
    def matches(self, executable, title, handle):
        match = "mode:i" in title
        print(f'VimInsertMode: {match}')

        return match

class VimTerminalMode(AppContext):
    def matches(self, executable, title, handle):
        match = "mode:t" in title
        print(f'VimTerminalMode: {match}')

        return match
