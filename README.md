## Contents
[CovidXmas Calendar](#covidxmas-calendar)

[UX](#ux)
+ [User Stories](#user-stories)
+ [Wireframes](#wireframes)

[Features](#features)
+ [Navbar](#navbar)
+ [Home Page](#home-page) 
+ [Login In Page](#login-page)
+ [Login Out Page](#logout-page)

[Technologies Used](#technologies-used)
+ [Languages Used](#languages-used)
+ [Frameworks, Libraries & Programs Used](#frameworks-libraries-and-programs-used)

[Deployment](#deployment)

[Credits](#credits)
+ [Content](#content)
+ [Media](#media)

# CovidXmas Calendar
+ We offer a personalized advent calendar with the theme of Happy Holidays with coXmas touch! This was built by team THE CALENDERERS for the Code Institute December 2021 Hackathon.
It was built to reflect the merry season spirit to our app users, with a simple but effective design that consists of animated combination on each day of December, 
specifically picked to inspire and uplift the user after COVID-19, global restrictions and two years of hardship.

<img src="#"> 


Click [here](https://covidxmas.herokuapp.com/) to live site.  

## UX

### User Stories

+ As a user, I would like to be able to …
1. Register my own account, login and logout;
2. Create, edit, share or delete multiple customized Advent Calendars;
3. Each day of the calendar has an option to either enter an image, youtube video or a text quote;
4. Listen to songs from the playlist or upload your own. Playlist can be accessed from the navbar option named "Play Music".

+ As a site owner, I want …
1. The website to be easy to navigate;
2. The functions to be easy accessible;
3. User to experience the festive season through interacting with app.


### Wireframes 

Wireframes created with Figma and Balsamiq. The project was developed from initial wireframes and some modifications were made during the development process to assure better usability. 

[Wireframes](https://github.com/alissatroiano/team-4-hackathon/tree/master/assets/wireframes)


## Features 


### Navbar 

+ Fixed Navbar with Home, Public Calendars, Login In and Log Out buttons to simplify accessibility to all pages;
+ Collapsed navbar on smaller devices to wrap in all options to ensure smoooth adjustment of menu being displayed.


### Home page 

+ animated gif of santa claus reindeer climbing across the page to catch the user's attention;
+ navigation bar on top of the page.

### Public Calendars

+ In this page, user can view calendars which are publicly available.

### My Calendars

+ This page is accessible once user has logged in;
+ 

### Log In page 

+ This page is dedicated for handling the user authentication;
+ Username and password box:
 The user is required to input their registered username and password.
+ Remember Me:
 ‘Remember Me’ feature checkbox will allow the user to preserve their logged in status. When the user checks the Remember Me option, then the logged in status is stored in the browser cookies.
+ Forgotten my password:
If user forgotten the password - user may click link named "I've forgotten my password". Once clicked - user will be redirected to the Reset Password page to input their email address so  the system will send you an e-mail allowing you to reset password.

+ Don't have an account?:
If user does not have an account - user may click the link named "Don't have an account? Sign Up". Once clicked - user will be redirected to the signup page.

### Sign Up Page

+ This page is dedicated for handling the registration of a new user;
+ The user is required to input their desired username;
+ The user has the option to input their email address;
+ The user is required to input their password twice;


### Log Out Page 

+ This page is dedicated for handling user log out;
+ It is accessible upon user login.
+ Once "Log out" is clicked from the navbar; user will be prompted if they want to sign out. Once user confirm - system will sign out the user and return to the homepage.

## Technologies Used

### Languages Used

   + HTML5
   + CSS3
   + JavaScript
   + Python3/Django
   + SVG
   + JSON

 ### Frameworks Libraries and Programs Used

+ Balsamiq:
  Balsamiq was used to produce the wireframes throughout the design process.

+ Figma:
  Figma was used to produce the wireframes throughout the design process.

+ Bootstrap 5:
    Bootstrap was used to add style to the website.
+ Git
    Git was utilised for version control by operating the Gitpod terminal to commit to Git and Push to GitHub.
+ GitHub:
    GitHub is used to lay in the project's code upon being pushed from Git.


## Bugs 

No bugs were found.


## Deployment

 The site was deployed to GitHub pages. 
 
 * The steps to deploy are as follows: 

  - In the GitHub repository, navigate to the Settings tab; 
  - From the source section drop-down menu, select the Master Branch;
  - Once the mas  ter branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 

The live link can be found [here](https://github.com/alissatroiano/team-4-hackathon/).

+ Heroku Deployment

 + Prerequisites;
●	A Github repository
●	Your creds.json file open in Gitpod.
●	Ensuring your requirements.txt is up to date. You can do so using by entering the following line in your terminal:
pip3 freeze --local > requirements.txt

  + Step 1 - Creating an account;

●	If you already have a Heroku account, please sign in to your existing account.
●	If you don't, go to Heroku.com and create a free account.

  + Step 2: Create an app;

●	Click on the 'New' drop down in the upper right-hand corner.
●	Select 'Create a new app'.
●	When choosing an app name, it will need to be unique to Heroku.
●	If the Github repository name or project name is not available, choose a name similar by adding other words, dashes, letters or numbers.
●	Enter your chosen 'App name' and select your region.
●	Click the 'Create app' button.

 + Step 3: Add Config Vars;

●	Go to the 'Settings' tab in your app.
●	Scroll down to the 'Config Vars' section and click the 'Reveal Config Vars' button.
●	We are going to add two config vars.
●	From the creds.json file, copy the entire contents.
●	Enter CREDS for KEY and then paste the contents from creds.json into the VALUE field.
●	Then click the 'Add' button.
●	Enter PORT for KEY and then 8000 for VALUE and click the 'Add' button.

+ Step 4: Add Buildpacks;

●	On the same 'Settings' tab in your app, scroll down to the 'Buildpacks' section.
●	The buildpacks need to be listed in your Settings in a specific order.
●	It's best to add Python first, click 'Save Changes and repeat for then Node.js.
●	If the buildpacks don't appear with Python first and Node.js second, you change the order by dragging Python to the top.

+ Step 5 - Select Github Deployment Method;

●	Go to the 'Deploy' tab in your app.
●	In the Deployment method' section, select 'GitHub' and click 'Connect to GitHub'.
●	Search for your Github repository name, which will create a list of repository names.
●	Click the 'Connect' button, and your Heroku app will link to your Github repository.
●	You can choose manual deploys for your app; click 'Deploy Branch' in the 'Manual Deploy' section.
●	Once successfully deployed, a green tick will appear next to Deploy to Heroku
●	Your app will not update/rebuild each time you push to Github, which will conserve your dyno hours in Heroku.
●	You will need to click 'Deploy Branch' each time you want the app to rebuild after pushing your changes to Github.
●	Or you can choose automatic deploys for your app,
●	Your app will update/rebuild each time you push to Github, which will not conserve your dyno hours in Heroku
●	To access your deployed app, scroll to the top and click 'Open app'.


## Forking the GitHub Repository

By forking the GitHub Repository you will be able to make a copy of the original repository on your own GitHub account allowing you to view and/or make changes without affecting the original repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/alissatroiano/team-4-hackathon/)
2. At the top of the Repository (not top of page) just above the "Settings" button on the menu, locate the "Fork" button.
3. You should now have a copy of the original repository in your GitHub account.

## Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/alissatroiano/team-4-hackathon/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/alissatroiano/team-4-hackathon/
```

7. Press Enter. Your local clone will be created.

## Setup Project

### Create a .py file
1. Create a `env.py` file in the `covidxmas` folder. See example below.

```
import os

os.environ.setdefault('ALLOWED_HOST', '*')

```

2. Run migrations
3. Run project


## Run Project
### Execute

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


## Credits 
 
### Content

Quotes (both Christmas-themed and non-Christmas themed) for the advent calendar boxes used in combination with on-theme gifs from [Giphy](https://giphy.com/)

### Media

Images from [Vecteezy](https://www.vecteezy.com)











