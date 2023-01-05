# OpenClassroom - Python Developer Path

**Project 4:** Develop a Software Program Using Python

**Student:** Abdoul Baki Seydou

**Date:** 11/06/2022

# Abstract
This project consists of creating a standalone tournament management application for a local chess club, 
Castle Chess, that allows the tournament managers to run the entire events offline.

The following features are included in the application:

    - Add and save players. 
    
    - Update player ratings.
    
    - Create and save tournaments.
    
    - Start, postpone and resume tournament rounds.
    
    - Input match scores.
    
    - Display player and tournament reports.

# Structure
The application follows the Model-View-Controller (MVC) design pattern and uses TinyDb, 
a document oriented database, to store the data.


# Basic flow
1. Create a new tournament.
2. Add eight players.
3. The application generates the pairings automatically using the Swiss tournament system.
4. Start the tournament and run the rounds.
5. Input match scores: the winner receives 1 point, the loser 0 points, and 0.5 each for a tie.


# PEP 8 adherence
The folder "flake_report" contains an HTML report generated by flake8-html which displays no errors.
A new report can be generated by running the following command in the terminal (Unix, macOS) 
or command line (Windows): flake8

The file setup.cfg in the root of the repository contains the settings used to generate the report.


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
