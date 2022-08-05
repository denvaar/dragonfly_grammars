import logging

from dragonfly import AppContext

logger = logging.getLogger('app_debug')

class VimContext(AppContext):
    def matches(self, executable, title, handle):
        match = "app:nvim" in title
        logger.debug(f'VimContext: {match}')

        return match

class VimNormalMode(AppContext):
    def matches(self, executable, title, handle):
        match = "mode:n" in title \
            or "mode:V" in title \
            or "mode:^V" in title

        logger.debug(f'VimNormalMode: {match}')

        return match

class VimInsertMode(AppContext):
    def matches(self, executable, title, handle):
        match = "mode:i" in title
        logger.debug(f'VimInsertMode: {match}')

        return match

class VimTerminalMode(AppContext):
    def matches(self, executable, title, handle):
        match = "mode:t" in title
        logger.debug(f'VimTerminalMode: {match}')

        return match

class VimCommandMode(AppContext):
    def matches(self, executable, title, handle):
        match = "mode:c" in title
        logger.debug(f'VimCommandMode: {match}')

        return match
