## Contents
[CovidXmas Calendar](#covidxmas-calendar)

[UX](#ux)
+ [User Stories](#user-stories)
+ [Wireframes](#wireframes)

[Features](#features)
+ [Navbar](#navbar)
+ [Home Page](#home-page)
+ [Login In Page](#signin-page)
+ [Login Out Page](#signout-page)

[Technologies Used](#technologies-used)
+ [Languages Used](#languages-used)
+ [Frameworks, Libraries & Programs Used](#frameworks-libraries-and-programs-used)

[Code Validation](#code-validation)
+ [Automated Tests](#automated-tests)

[Project Bugs and Solutions](#project-bugs-and-solutions)

[Deployment](#deployment)
+ [Forking the GitHub Respository](#forking-the-github-repository)
+ [Making a Local Clone](#making-a-local-clone)

[Setup Project] (#setup-project)
+ [Create a .py file] (#create-a-.py-file)

[Run Project] (#run-project)
+ [Execute] (#execute)


[Credits](#credits)
+ [Content](#content)
+ [Media](#media)

# CovidXmas Calendar
+ We offer a personalized advent calendar with the theme of Happy Holidays with coXmas touch! This was built by team THE CALENDERERS for the Code Institute December 2021 Hackathon.
It was built to reflect the merry season spirit to our audience, with a simple but effective design that consists of animated combination on each day of December, 
specifically picked to inspire and uplift the user after COVID-19, global restrictions and two years of hardship.

<img src="#"> 


Click [here](https://covidxmas.herokuapp.com/) to live site.  

## UX

### User Stories

+ As a user, I would like to be able to …
1. Register my own account, login and logout.
2. Create, edit, share or delete multiple customized Advent Calendars;
3. Each day of the calendar has an option to either enter an image, youtube video or a text quote;
4. Listen to songs from the playlist that can be accessed from the navbar option named "Play Music".

+ As a site owner, I want…

1. The website be easy to navigate;
2. The functions to be easy accessible;
3. Cherish each day of the calendar with the users;


### Wireframes 

Wireframes created with Balsamique. The project was developed from initial wireframes and some modifications were made during the development process to assure better usability. 

[Wireframes](https://github.com/alissatroiano/team-4-hackathon/tree/master/assets/wireframes)


## Features 


### Navbar 

+ Fixed Navbar with Home, About, Login In and Log Out buttons to simplify accessibility to all pages. 
+ Collapsed navbar on smaller devices to wrap in all options to ensure smoooth adjustment of menu being displayed.



### Home page 

+ Placeholder text
+ Placeholder text
+ Placeholder text

### About Page 

+ Placeholder text
+ Placeholder text
+ Placeholder text


### Log In page 

+ This page is dedicated for handling user login;
+ Remember Me:
 ‘Remember Me’ feature checkbox will allow the user to preserve their logged in status. When the user checks the Remember Me option, then the logged in status is stored in the browser cookies.
+ Forgotten my password:
If user forgotten the password - user may click link named "I've forgotten my password". Once clicked - user will be redirected to the Reset Password page to input their email address so  the system will send you an e-mail allowing you to reset password.

+ Don't have an account?:
If user does not have an account yet, user may click the link named "Don't have an account?". Once clicked - user will be redirected to the Account creation page.

### Log Out Page 

+ This page is dedicated for handling user log out;
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
+ Bootstrap 5:
    Bootstrap was used to add style to the website.
+ Git
    Git was utilised for version control by operating the Gitpod terminal to commit to Git and Push to GitHub.
+ GitHub:
    GitHub is used to lay in the project's code upon being pushed from Git.


## Code Validation

### Automated tests

+ HTML

  Passing through the HTML from all templates and base into the W3C Markup Validator no errors or warnings have been found [W3C validator](https://validator.w3.org/).

HTML validation results can be viewed on links:

| Pages  |  
| ------------------- | 
|  [Index](https://covidxmas.herokuapp.com/) |  
|  [About](https://covidxmas.herokuapp.com/#about)|
|  [Log In](https://covidxmas.herokuapp.com/accounts/login/) |
|  [Log Out](https://covidxmas.herokuapp.com/accounts/logout/) |

+ CSS

No errors were found when passing through the official [W3C validator](https://jigsaw.w3.org/css-validator/). 


[Css](URL)
+ JavaScript

Javascript files were tested with the jshint and no errors were been found. 


## Deployment

 The site was deployed to GitHub pages. 
 
 * The steps to deploy are as follows: 

  - In the GitHub repository, navigate to the Settings tab; 
  - From the source section drop-down menu, select the Master Branch;
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 

The live link can be found [here](https://github.com/alissatroiano/team-4-hackathon/).

### Forking the GitHub Repository

By forking the GitHub Repository you will be able to make a copy of the original repository on your own GitHub account allowing you to view and/or make changes without affecting the original repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/alissatroiano/team-4-hackathon/)
2. At the top of the Repository (not top of page) just above the "Settings" button on the menu, locate the "Fork" button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

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











