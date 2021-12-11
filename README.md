# team-4-hackathon
Team 4's Repository for the December 2021 Code Institute Hackathon

# Prerequisists
- Python3 installed

# Setup Project

1. Create a `env.py` file in the `covidxmas` folder. See example of the file contents below.

```
import os

os.environ.setdefault('ALLOWED_HOST', '*')

```

2. If you have a virtual environment, then start it

3. Install dependencies

For Bash (Linux/Mac) execute the following line of code from the terminal:

```
pip3 install -r requirements.txt

```

For Windows execute the following line of code from Powershell

```
pip install -r requirements.txt
```

4. Run migrations

For Bash (Linux/Mac) execute the following line of code from the terminal:

```
python3 covidxmas/manage.py migrate

```

For Windows execute the following line of code from Powershell

```
python covidxmas/manage.py migrate
```

5. Run project

For Bash (Linux/Mac) execute the following line of code from the terminal:

```
./run.sh

# or 

python3 covidxmas/manage.py runserver 0.0.0.0:8000

```

For Windows execute the following line of code from Powershell

```
python covidxmas/manage.py runserver 0.0.0.0:8000
```

