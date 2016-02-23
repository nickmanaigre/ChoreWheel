# ChoreWheel
A project for Human Computer Interaction 2 at the University of Manitoba

### Getting Started
- We're going to be using the Flask web server framework. Installation is extremely easy using pip and virtualenv
- Install the Python package manager, pip [HERE](https://pip.pypa.io/en/stable/installing/)

#### Setting up virtualenv (Optional, but recommended) 
  - By setting up a Python virtualenv, you can install packages without constantly installing them on your actual system
  - Visit the [installation page](https://virtualenv.readthedocs.org/en/latest/installation.html) for instructions on how to install virtualenv
    - You can usually do this with pip by typing `[sudo] pip install virtualenv`
  - Create the virtualenv
    - `virtualenv [NAME OF VIRTUAL ENV]` 
      - e.g., `virtualenv venv`
  - Activate the env:
    - On Linux/Mac: `source [FOLDER CONTAINING ENV]/bin/activate` 
      - e.g., `source venv/bin/activate`
      - `deactivate` exits the virtualenv
    - On windows: `\path\to\env\Scripts\activate`
      - e.g., `venv\Scripts\activate`
  - *DO NOT COMMIT YOUR VIRTUALENV TO THE REPOSITORY*
    - There is a HUGE amount of files in a virtualenv. It's essentially a whole Python installation.
    - Add it to the `.gitignore` if you'd like

#### Installing and running a Flask server
- If using a virtualenv, activate it
- `pip install Flask`
- once flask is installed, you can start the server: `python server.py`
- unless someone explicitly changes the port, you can access the webapp by browsing to `localhost:5000`

#### Frameworks used
- [Python package manager PIP](https://pip.pypa.io/en/stable/)
- [Flask](http://flask.pocoo.org/docs/0.10/)
- [Bootstrap front-end framework](http://getbootstrap.com)
