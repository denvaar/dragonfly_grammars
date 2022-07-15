import logging

from dragonfly import AppContext

logger = logging.getLogger('app_debug')

class ChromeContext(AppContext):
    def matches(self, executable, title, handle):
        match = executable == "Google Chrome"
        logger.debug(f'ChromeContext: {match}')

        return match
