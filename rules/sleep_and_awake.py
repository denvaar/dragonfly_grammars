import logging

from dragonfly import MappingRule, Function, get_engine

logger = logging.getLogger('app')

class AriseRule(MappingRule):
    def process_recognition(self, node):
        self.grammar.set_exclusiveness(False)
        logger.info("👂 Listening...")
        logger.setLevel(logging.INFO)

    mapping = {
        "(arise | rise from your grave | wake up)": Function(lambda: get_engine().start_saving_adaptation_state()),
    }


class SleepRule(MappingRule):
    def process_recognition(self, node):
        self.grammar.set_exclusiveness(True)
        logger.info("💤 Sleeping...")
        logger.setLevel(logging.WARNING)

    mapping = {
        "(go to sleep | quiet you | stop listening)": Function(lambda: get_engine().stop_saving_adaptation_state())
    }

    
