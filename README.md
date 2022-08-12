## Setup

Create a Python virtual environment if setting up for the first time.

```
python3 -m venv ./env
```

Activate the virtual environment.

```
source env/bin/activate
```

Install required Python dependencies.

```
pip3 install -r ./requirements.txt
pip3 install 'dragonfly2[kaldi]'
pip3 install nltk
```

```
mkdir language_models
```

Download the [Kaldi language model](https://github.com/daanzu/kaldi-active-grammar/releases), and place within `language_models/`.

Try running the program.

```
python run.py
```
