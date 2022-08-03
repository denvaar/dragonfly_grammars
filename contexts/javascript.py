from dragonfly import AppContext

class JavascriptContext(AppContext):
    def matches(self, executable, title, handle):
        match = "ext:js" in title \
            or "ext:ts" in title \
            or "ext:jsx" in title \
            or "ext:tsx" in title

        return match
