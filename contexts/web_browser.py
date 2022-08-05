import logging

from dragonfly import AppContext

logger = logging.getLogger('app_debug')

class WebBrowserContext(AppContext):
    def matches(self, executable, title, handle):
        match = executable == "Google Chrome" \
            or executable == "firefox"

        logger.debug(f'WebBrowserContext: {match}')

        return match
