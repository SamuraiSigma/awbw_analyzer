Advance Wars by Web Analyzer
=============================
Created by: Leonardo Pereira Macedo

### Introduction

  - I'm a big fan of the Advance Wars franchise from Intelligent Systems on Nintendo. Searching around the Internet, I was delighted on finding a website in which you can play it online: **Advance Wars by Web**! For those who're interested, here's the [website](http://awbw.amarriner.com "awbw").

  - I've had my share of fun playing it. Only thing that bugged me was checking the website daily to see if one of my games had been updated. Sure, there's an option to recieve an e-mail when your turn arrives in a game, but I was thinking of something a little more practical.

  - So, here's when this program, created for Linux, comes in handy! It's possible to recieve a window GUI message with information about your game rooms.

  - Feel free to give me any advice, suggestion or constructive criticism, as I'm trying my best to hone my coding skills. :P

### Usage (Linux)

  **1.** Run the **pyenv** script first. It creates three folders necessary for the virtual environment (*bin*, *lib*, *include*) and installs dependencies so you can run the program with ease (hopefully...).  

  **2.** To start the main program, just run the **execute** script:

  ***./execute <username> [-a] [-w] [-h]***  
  *-username*: Your name on the awbw website.  
  *-a*: Show all rooms.  
  *-w*: Show data in a window GUI.  
  *-h*: Shows how to use the program, closing it afterwards.  

  **3.** To execute the script periodically, add it to your **crontab**.

### Folders

  Here goes an explanation on the current folders of the project:

###### doc/

  - ***requirements.txt***: Contains all dependencies of the program. **pyenv** uses this when creating a virtual environment.

###### src/

  - ***main.py***: Main module of the project. Treats command line arguments.
  - ***output.py***: Organizes the output for the user. Can be through terminal or a window GUI.
  - ***wars.py***: Contains the Wars class, responsible for getting info on the awbw website.

### Special Thanks

  - *Intelligent Systems* and *Nintendo*, for making Advance Wars possible in the first place.
  - *amarriner*, for making Advance Wars by Web!
