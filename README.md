Doughuware
==========

A simple Django-based document organization tool. 


Developmet Environment
======================
Doughuware is developed within a virtualenv. It is probably helpful, but not necessary, to have virtualenvwrapper installed for development (`pip install virtualenvwrapper`). 

1) Create a virtualenv with virtualenvwrapper: mkvirtualenv Doughuware
2) Clone the git repository
3) By default, Doughuware uses the `pscyopg2` Python database adapter. If you intend to use psycopg2 and don't have it installed, you may need to install the following libraries before installing from pip: libpq-dev, python-dev
4) Install the Doughuware requirements: `pip install -r requirements.txt`
