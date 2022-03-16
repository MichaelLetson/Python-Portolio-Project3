# Python Project - Team Data Automation

![image](https://user-images.githubusercontent.com/93741957/158492239-478fa180-dc27-436a-afc3-bae9f331dcf0.png)

## For my Milestone Project 3 I have created a Python program to help input and automate data management.

This is for a real world scenario of inputting team data into a spreadsheet, having the option to gain insights and retain/calculate key data. Visit the deployed Heroku page here: https://python-portfolio-project3.herokuapp.com/ 

## Purpose & Features

The purpose of the program is to help automate the process of inputting and interacting with data created by 5 teams, into a spreadsheet. I have taken this from personal experiences where this program would have been useful. 
- It speeds up the process of updating a spreadsheet with data.
- The program calculates and displays the percentage increase or decrease of the teams activity. 
- The program calculates and offers the option to view next months projected data - this is done to create more engagement between the user and the program. 

This is interaction with Python and Google Sheets is done via creating an API to allow the code to interact with a google sheet via a gspread import.

To follow a plan of creating this program I created a flow chart through diagrams.net: 
![image](https://user-images.githubusercontent.com/93741957/158696173-02e54fd0-48f7-4783-910f-59221fdf4098.png)


## Testing

![image](https://user-images.githubusercontent.com/93741957/158692261-47858492-5c08-4e4b-8848-b85d3f7afa0c.png)
 
- Code passed through PEP8 validator, via http://pep8online.com/ with 2 issues, which were rectified and the code now passes without issue. The 2 issues were a line length being too long on line 101, and a trailing blank space on line 40. 
- Tried passing program invalid data, e.g. csv length longer than 5. 
- Tested in GitHub terminal.
- Tested in Heroku terminal.
 
 ### Known bugs:
 The commit messages display errors, such as misplaced letters and spelling mistakes. This is due to computer glitches when typing in the commit messages in the terminal. 
 Chose to leave the errors in place, rather than risk losing work by editing the commits. 
 
 ## Using Git

I created a respository and opened in gitpod to create my code. To move my code from gitpod to repository ready for deployment I followed these steps (which I did often to show a journey of creating my site): 
 - git add .
 - git commit -m "message"
 - git push
 - git pull --rebase
