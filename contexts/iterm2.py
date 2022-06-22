import logging

from dragonfly import AppContext

logger = logging.getLogger('app_debug')

class ITerm2Context(AppContext):
    def matches(self, executable, title, handle):
        # iTerm Appearance settings:
        #
        #   Window & Tab Titles
        #   -------------------
        #   [ ] Show window number
        #   [ ] Show current job name
        #   [ ] Show profile name

        # .bash_profile
        #
        # if [ $ITERM_SESSION_ID ]; then
        #     # set title right before executing a command
        #     trap 'printf "\033]0;bash%s\007" " ($BASH_COMMAND)"' DEBUG
        #     # set title back to just "bash" after completion
        #     export PROMPT_COMMAND='printf "\033]0;bash\007"'
        # fi


        match = title.startswith("bash") or title.endswith("(bash)")
        logger.debug(f'ITerm2Context: {match}')

        return match
