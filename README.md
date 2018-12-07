# Django Backend to Support the Tablet Application

# Development Installation
**These install guidelines assume you are using
an up-to-date OS with Python 3.5, GNU Make, and git installed**

First clone the repo:

`git clone git@gitlab.com:besi/tablet-backend.git` (if using ssh auth)

or

`git clone https://gitlab.com/besi/tablet-backend.git` (if using https auth)

Then `cd` into the repo:

`cd tablet-backend`

----

To setup the python virtual environment and dependencies run:

`make install`

To upgrade installed packages run:

`make upgrade`

To update the requirements.txt file with the currently installed packages run:

`make update-requirements`

To remove the pyvenv run:

`make uninstall`

----

After you have installed the required packages, ensure you are using the pyvenv by running:

`source env/bin/activate`

You can deactivate the pyvenv by running:

`deactivate`
