Doughuware
==========

A simple Django-based document organization tool. 


Developmet Environment
======================
Doughuware is developed within a virtualenv. It is probably helpful, but not necessary, to have virtualenvwrapper installed for development (`pip install virtualenvwrapper`). 

1) Create a virtualenv with virtualenvwrapper: mkvirtualenv Doughuware  
2) Clone the git repository  
3) Install non-pip dependencies: 
   * For psycopg2 support: `libpq-dev, python-dev`  
   * For creating document thumbnails and previews: `imagemagick`  

4) Install the Doughuware requirements: `pip install -r requirements.txt`
