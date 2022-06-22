import os
import logging

from dragonfly import get_engine
from dragonfly.loader import CommandModuleDirectory
from dragonfly.log import setup_log
import nltk

nltk.download('punkt')

logger = logging.getLogger('app')
logger.setLevel(logging.INFO)
# logger.setLevel(logging.DEBUG)

debug_logger = logging.getLogger('app_debug')
debug_logger.setLevel(logging.INFO)
# debug_logger.setLevel(logging.DEBUG)

if False:
    # Debugging logging for reporting trouble
    logging.basicConfig(level=10)
    logging.getLogger('grammar.decode').setLevel(20)
    logging.getLogger('grammar.begin').setLevel(20)
    logging.getLogger('compound').setLevel(20)
    logging.getLogger('kaldi.compiler').setLevel(10)
else:
    setup_log()

def pick_language_model_engine():
    name = os.environ.get('LANGUAGE_MODEL_NAME')
    lang_model_path = {
        'kaldi': 'language_models/kaldi_model'
    }

    return get_engine(name, model_dir=lang_model_path[name],
                      auto_add_to_user_lexicon=True)

def on_begin():
    pass

def on_recognition(words):
    logger.info(u"✅ Recognized: '%s'" % u" ".join(words))

def on_failure():
    logger.info("⛔️ Failed to recognize speech.")


def main():
    try:
        path = os.path.dirname(__file__)
    except NameError:
        path = os.getcwd()
        __file__ = os.path.join(path, "run.py")

    path = os.path.join(os.getcwd(), "grammars")

    engine = pick_language_model_engine()
    engine.connect()

    directory = CommandModuleDirectory(path, excludes=[__file__])
    directory.load()

    engine.prepare_for_recognition()

    try:
        print("👂 Listening...")
        engine.do_recognition(on_begin, on_recognition, on_failure)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
