# Battleships 

[Live project can be viewed here.](https://battle-ships-cs.herokuapp.com/)

## Table of Content
1. [Introduction](#introduction)
2. [How To Play](#how-to-play)
3. [Features](#features)
4. [User Stories](#user-stories)
5. [Planning](#planning)
6. [Testing](#testing)
7. [Deployment](#deployment)
8. [Credits](#credits)


## Introduction 

This project is for a Battleship game using Python. It allows the player to play a single-player version against a computerized player.

## How To Play

## Features

## User Stories
As a user I want to: 
* Clearly and instantly see what the game is. 
* Easy way to read game instructions. 
* Play a fun game. 

## Planning 

## Testing

## Deployment

The game was deployed through Heroku, by the steps below:

- Make sure your code is up to date and pushed to Github 

- Log onto Heroku

- Select create new app

- Write an app name and add an app region

- Press the 'Create app' button

- Press the Settings tab that can be found at the top

- Then go to 'Config Vars' and select 'Reveal Config Vars'

- You will see 'key' and 'value'. Add 'PORT' under key and '8000' under value. 

- Under 'Buildpacks' select 'Add buildpack' and choose Python. Repeat this with Nodejs but only after Python

- Once done, go back to the top and choose 'Deploy'

- Under 'Deployment method', select 'Github', it should say 'connected' once it's done 

- Write your Github repository name, click 'Search'

- Pick the repository by pressing 'Connect', it will link up with your app

- Go to 'Automatic deploys', pick 'Enable Automatic Deploy'

- Once any new code has been pushed to Github, it can be viewed on the Heroku platform

- Select the app once you are on your home screen

- Click 'Open app' on the right hand side of the screen

- A new tab on the web browswe should appear with your app

## Credits 
* [Code Institute](https://github.com/Code-Institute-Org/python-essentials-template) for providing the template. The template gave me a mock terminal to display my game via a webpage.
* [Knowledge Mavens](https://www.youtube.com/watch?v=tF1WRCrd_HQ&t=0s&ab_channel=freeCodeCamp.org) Youtube video tutorial on how to build a single player Battleship game. 
