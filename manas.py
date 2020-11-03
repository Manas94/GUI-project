from tkinter import *
import sports # a direct module for live score updates
from tkinter import messagebox #it is for warning symbol for invalid details

score = Tk()
score.geometry('750x500')
score.title(" IPL live score")
score.configure(bg='orange')

# Variable Classes in tkinter
date = StringVar()
time = StringVar()
league = StringVar()
team1 = StringVar()
team2 = StringVar()
team1_score = StringVar()
team2_score = StringVar()
link = StringVar()
season = StringVar()


def match_info():
    try:
        match = sports.get_match(sports.CRICKET, e1.get(), e2.get())
        date.set(match.match_date)
        time.set(match.match_time)
        league.set(match.league)
        team1.set(match.home_team)
        team2.set(match.away_team)
        team1_score.set(match.away_score)
        team2_score.set(match.home_score)
        link.set(match.match_link)
        season.set(match.away_score)
        season.set(match.home_score)


    except:
        messagebox.showerror("Error", "It was not a live match")


# Creating label for each information
# name using widget Label
Label(score, text="Team 1 :", bg="orange").grid(row=0, sticky=NE)
Label(score, text="Team 2 :", bg="orange").grid(row=1, sticky=NE)
Label(score, text="Date :", bg="orange").grid(row=2, sticky=NE)
Label(score, text="Time :", bg="orange").grid(row=3, sticky=NE)
Label(score, text="League :", bg="orange").grid(row=4, sticky=NE)
Label(score, text="Team A :", bg="orange").grid(row=5, sticky=NE)
Label(score, text="Team B :", bg="orange").grid(row=6, sticky=NE)
Label(score, text="Team A score :", bg="orange").grid(row=7, sticky=NE)
Label(score, text="Team B score :", bg="orange").grid(row=8, sticky=NE)
Label(score, text="Live updates from :", bg="orange").grid(row=9, sticky=NE)
Label(score, text="Total average score in season of team A :", bg="orange").grid(row=10, sticky=S)
Label(score, text="Total average score in season of team B:", bg="orange").grid(row=11, sticky=S)


# Creating label for class variable
# name using widget Entry
Label(score, text="", textvariable=date, bg="orange").grid(row=2, column=1, sticky=W)
Label(score, text="", textvariable=time, bg="orange").grid(row=3, column=1, sticky=W)
Label(score, text="", textvariable=league, bg="orange").grid(row=4, column=1, sticky=W)
Label(score, text="", textvariable=team1, bg="orange").grid(row=5, column=1, sticky=W)
Label(score, text="", textvariable=team2, bg="orange").grid(row=6, column=1, sticky=W)
Label(score, text="", textvariable=team1_score, bg="orange").grid(row=7, column=1, sticky=W)
Label(score, text="", textvariable=team2_score, bg="orange").grid(row=8, column=1, sticky=W)
Label(score, text="", textvariable=link, bg="orange").grid(row=9, column=1, sticky=W)
Label(score, text="", textvariable=season,  bg="orange").grid(row=10, column=1, sticky=W)
Label(score, text="", textvariable=season,  bg="orange").grid(row=11, column=1, sticky=W)

e1 = Entry(score)
e1.grid(row=0, column=1)

e2 = Entry(score)
e2.grid(row=1, column=1)

# creating a button using the widget
# Button that will call the submit function
b = Button(score, text="Show", command=match_info)
b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=1, pady=5)

score.mainloop()
