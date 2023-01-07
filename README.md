# OpenClassroom - Python Developer Path

**Project 4:** Develop a Software Program Using Python

**Student:** Abdoul Baki Seydou

**Date:** 11/06/2022

# Abstract
In this project, as a junior freelance developer presented with the first opportunity of a potential client project,
the task consists of creating a standalone tournament management application for a local chess club, Castle Chess, 
that allows the tournament managers to run the entire events offline.

In meeting the client's requirements, the application include the following features:

    - Add players. 
    
    - Update player ratings.
    
    - Create, start and resume tournaments.
    
    - Save and load tournament statements at any time.
    
    - Perform player pairings using the Swiss tournament system.
    
    - Display reports on players, and all tournament's rounds and matches played.

# Structure
The application follows the Model-View-Controller (MVC) design pattern.

# Database
For storing and loading the data, the application uses TinyDb, a Python based document oriented database.
The database, in json format, will be created and saved automatically in the 'dbase' folder in the root of the 
repository, upon lunching the application the first time.

# Basic flow
1. Create a new tournament.
2. Add eight players in the tournament.
3. Start the tournament created and run the rounds.
4. The application generates the pairings automatically.
5. Input match scores: the winner receives 1 point, the loser 0, and 0.5 each for a tie.

# Requirement

Latest version of Python must be installed.

You can download the latest version for your system from : https://www.python.org/downloads/

# Installation

The following commands rely on the knowledge of how to use the terminal (Unix, macOS) or the command line (Windows).

**1 - Get the code**

  * $ git clone https://github.com/Afudu/P4_OpenClassroom.git

**2 - Move to the folder**

  * Unix/macOS/Windows: cd P4_OpenClassroom

**3 - Create a virtual environment**

  * Unix/macOS: $ python3 -m venv pythonenv
  * Windows: py -m venv pythonenv
  
    * Note: you can create the virtual environment in another folder, then move to that folder to run the command above.
    * Example: in the above command, our virtual environment created is called pythonenv - you can give a different name.

**4 - Activate the virtual environment created**

  * Unix/macOS: $ source pythonenv/bin/activate

  * Windows: pythonenv\Scripts\activate

**5 - Securely upgrade pip**

 * Unix/macOS/Windows: pip install --upgrade pip

**6 - Install all dependencies**

 * Unix/macOS/Windows: pip install -r requirements.txt

# Running the application

To run the application, in the terminal (Unix, macOS) or command line (Windows):

  python main.py

# PEP 8 adherence
The folder 'flake_report' in the repository contains an HTML report generated by flake8-html which displays no errors.
A new report can be generated by running the following command in the terminal (Unix, macOS) 
or command line (Windows): flake8

The file setup.cfg in the root of the repository contains the settings used to generate the report.