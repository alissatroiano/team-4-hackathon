# team-4-hackathon
Team 4's Repository for the December 2021 Code Institute Hackathon

# Prerequisists
- Python3 installed

# Setup Project

1. Create a `env.py` file in the `covidxmas` folder. See example below.

```
import os

os.environ.setdefault('ALLOWED_HOST', '*')

```

2. Run migrations
3. Run project


# Run Project

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

