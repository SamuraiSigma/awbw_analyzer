Advance Wars by Web Analyzer
=============================
Created by: Leonardo Pereira Macedo

### Introduction

  - I'm a big fan of the Advance Wars franchise from Intelligent Systems on Nintendo. Searching around the Internet, I was delighted on finding a website in which you can play it online: **Advance Wars by Web**! For those who're interested, here's the website: http://awbw.amarriner.com

  - I've had my share of fun playing it. Only thing that bugged me was checking the website daily to see if one of my games had been updated. Sure, there's an option to recieve an e-mail when your turn arrives in a game, but I was thinking of something a little more practical.

  - So, here's when this program comes in handy! At the moment, it only has a terminal option mostly for Linux users, but I'll try expanding it whenever possible with more features. Feel free to give me any advice, suggestion or constructive criticism, as I'm not that strong in Python or programming yet. :P

### Usage (mostly Linux)

  I'll consider that you are on this project's root (the *awbw* folder) when executing these commands.

  **1.** I recommend running the **pyenv** script first. It creates three folders necessary for the virtual environment (*bin*, *lib*, *include*) and installs dependencies so you can run the program with ease (hopefully...).

  ***$ ./pyenv***

  **2.** Next, while on the root of this project, activate the virtual environment:

  ***$ source bin/activate***

  **3.** To execute the main program, just run **src/main.py** as if it were a script (*username* is your name on the awbw website):

  ***./src/main.py <username>***

### Folders

  Here goes an explanation on the current folders of the project:

###### doc/

  - ***requirements.txt***: Contains all dependencies of the program. **pyenv** uses this when creating a virtual environment.

###### src/

  - ***main.py***: Main module of the project. Treats command line arguments (see them with the *-h* option).
  - ***output.py***: Organizes the output for the user. Only terminal for now, but I'm thinking of adding a window interface later...
  - ***wars.py***: Contains the Wars class, responsible for getting info on the awbw website.

### Special Thanks

  - *Intelligent Systems* and *Nintendo*, for making Advance Wars possible in the first place.
  - *amarriner*, for making Advance Wars by Web!
