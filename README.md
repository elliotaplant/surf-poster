# Surf Poster
Backend for a live updating surf poster.
- Fetches surf data from surfline.com (currently only for Tourmaline Beach)
- Converts that data into signals to adjust the angle on servo controllers
- Runs on a raspberry pi (zero w)

## Runs on Python 2 (system python)
Why? Getting things running with python3 was a pain.
For some reason it took 10s+ to get a virtualenv setup with pipenv, so I ditched it in favor of the system python2

## Getting setup
- Get your pi
- Install these dependencies:
  - `python-requests`
  - `python-RPI.GPIO`
- Hook up your servo wires according to the pin numbers in `actuate.py`
- Run the script with `python main.py` to get live data OR
`python manual.py <surf_height> <water_temp> <surf_quality>` to put in your own data
