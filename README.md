# VolleyballTeamGenerator
Volleyball Team Generator that creates a list of all available players and randomizes them, places them into teams.

It requires using Python3.9 and Flask2.1.2.

## Package Manager
Packages and modules required to run this application are managed in virtual environments `venv`. Once the virtual environment is activated, packages can be installed, upgraded, and removed into it using `pip`. 

For more information, please refer to [Python3 - Venv introduction](https://docs.python.org/3/tutorial/venv.html#introduction)

### Creating a Virtual Environment
To create a virtual environment, run the following commmand at the project root:
```
python3 -m venv .venv/<user provided directory>
```
> To avoid committing the virtual environment to Git, the `.venv` directory has been included in the .gitignore file.

### Using Virtual Environments
To activate the virtual environment on Windows, run the following in the project root:
```
.\.venv\activate.bat
``` 

To activate the virtual environment on Unix/MacOS, run the following in the project root:
```
source .venv/bin/activate
```

To deactivate the virtual environment, run the following:
```
deactivate
```

### Installing Packages to Virtual Environment
`requirements.txt` contains all of the required packages to run this application.
With the virtual environment activated, run the following at the project root to install required packages into the virtual environment:
```
python3 -m pip install -r requirements.txt
```

### Adding Packages to Requirements.txt
To add new dependencies to `requirements.txt`, run the following command:
```
pip3 freeze > requirements.txt
```

## TODO: plan out MVP

## TODO: set up CI/CD with github
## TODO: add system diagram for the project

## TODO: include steps on how to run locally

## TODO: see if we can leverage venv for python dependencies and other standard python practices to follow

## TODO: research design patterns for a Flask/Django app.

## TODO: add ways to running application (locally, on server, etc)