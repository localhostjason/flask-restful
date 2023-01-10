set PYTHONPATH=.;venv/Lib;venv/Lib/site-packages
set PATH=%PATH%;venv/Scripts
twistd -n web --port tcp:5000 --wsgi main.app
