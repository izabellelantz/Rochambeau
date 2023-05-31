"""
Name: Izabelle Lantz
Program: Rochambeau
This program allows a user to play a game of rock, paper, scissors (or Rochambeau) either in 5 rounds or in 3.
This is done through a GUI that takes user's first name in entry and uses this to display winner and choices.
"""


from tkinter import *
from Player import Player as Pl
import datetime as dt
import random


w = Tk()
w.title("Rochambeau")
w.geometry("700x700")

p_score = 0
c_score = 0
draw = 0
rounds_played = 0

comp_values = {"0": "Rock",
              "1": "Paper",
              "2": "Scissors"}

rps_scores = {
   "Rock": {
       "Rock": 0,
       "Paper": -1,
       "Scissors": 1
   },
   "Paper": {
       "Rock": 1,
       "Paper": 0,
       "Scissors": -1
   },
   "Scissors": {
       "Rock": -1,
       "Paper": 1,
       "Scissors": 0
   }
}


def make_comp_choice():
   # choosing random value for computer
   return comp_values[str(random.randint(0, 2))]


def challenge(user_choice, comp_choice):
   # getting winner between player and computer
   return rps_scores[user_choice][comp_choice]


def play_rps_3r(player_choice, player_info):
   # play 3 round version
   global p_score, c_score, draw, rounds_played
   comp_choice = make_comp_choice()
   score = challenge(player_choice, comp_choice)
   rock5r["state"] = "disable"
   paper5r["state"] = "disable"
   scissors5r["state"] = "disable"

   match score:
       case 1:
           p_score += 1
       case -1:
           c_score += 1
       case 0:
           draw += 1

   rounds_played += 1

   if rounds_played == 3:
       p_score_label.config(text=f"{player_info}'s Score: {p_score}")
       c_score_label.config(text=f"Computer Score: {c_score}")
       p_result_lab.config(text=f"{player_info} -> {player_choice}")
       c_result_lab.config(text=f"Computer -> {comp_choice}")
       if p_score > c_score:
           winner_label.config(text=f"{player_info} won the game!")
       elif c_score > p_score:
           winner_label.config(text=f"Sorry {player_info}, computer won this time.")
       elif c_score == p_score:
           winner_label.config(text="Draw!")
       replay_button.pack(side=TOP, pady=10)
       rock3r.config(state="disabled")
       paper3r.config(state="disabled")
       scissors3r.config(state="disabled")
   else:
       p_score_label.config(text=f"{player_info}'s Score: {p_score}")
       c_score_label.config(text=f"Computer Score: {c_score}")
       p_result_lab.config(text=f"{player_info} -> {player_choice}")
       c_result_lab.config(text=f"Computer -> {comp_choice}")
       rounds_label.config(text=f"Round {rounds_played+1}")


def play_rps_5r(player_choice, player_info):
   # play 5 round version
   global p_score, c_score, draw, rounds_played
   comp_choice = make_comp_choice()
   score = challenge(player_choice, comp_choice)
   rock3r["state"] = "disable"
   paper3r["state"] = "disable"
   scissors3r["state"] = "disable"

   match score:
       case 1:
           p_score += 1
       case -1:
           c_score += 1
       case 0:
           draw += 1

   rounds_played += 1

   if rounds_played == 5:
       p_score_label.config(text=f"{player_info}'s Score: {p_score}")
       c_score_label.config(text=f"Computer Score: {c_score}")
       p_result_lab.config(text=f"{player_info} -> {player_choice}")
       c_result_lab.config(text=f"Computer -> {comp_choice}")
       if p_score > c_score:
           winner_label.config(text=f"{player_info} won the game!")
       elif c_score > p_score:
           winner_label.config(text=f"Sorry {player_info}, computer won this time.")
       elif c_score == p_score:
           winner_label.config(text="Draw!")
       replay_button.pack(side=TOP, pady=10)
       rock5r.config(state="disabled")
       paper5r.config(state="disabled")
       scissors5r.config(state="disabled")
   else:
       p_score_label.config(text=f"{player_info}'s Score: {p_score}")
       c_score_label.config(text=f"Computer Score: {c_score}")
       p_result_lab.config(text=f"{player_info} -> {player_choice}")
       c_result_lab.config(text=f"Computer -> {comp_choice}")
       rounds_label.config(text=f"Round {rounds_played+1}")


def restart_game():
   # reset game and restart
   global p_score, c_score, rounds_played
   p_score = 0
   c_score = 0
   rounds_played = 0
   p_score_label.config(text=f"{player_info}'s Score: {p_score}")
   c_score_label.config(text=f"Computer Score: {c_score}")
   p_result_lab.config(text="")
   c_result_lab.config(text="")
   winner_label.config(text="")
   replay_button.pack_forget()
   rock3r.config(state="normal")
   paper3r.config(state="normal")
   scissors3r.config(state="normal")
   rock5r.config(state="normal")
   paper5r.config(state="normal")
   scissors5r.config(state="normal")
   rounds_label.config(text=f"Round {rounds_played+1}")


def get_player_info():
   # get players name through entry
   global player_info_var
   player_info_var = StringVar()
   name_window = Toplevel(w)
   name_window.title("Player Name")
   name_window.geometry("300x300")
   name_window.configure(bg="pink")
   name_label = Label(name_window, text="Please enter your first name:", fg="red", bg="pink")
   name_label.pack(side=TOP, pady=10)
   name_ent = Entry(name_window, textvariable=player_info_var, font="20", fg="red", bg="white")
   name_ent.pack(side=TOP, pady=10)


   def submit_info():
       # store and display information
       global player_info
       player_info = player_info_var.get()
       player = Pl(player_info)
       name_window.destroy()
       p_score_label.config(text=f"{player}'s Score: {p_score}")
       c_score_label.config(text=f"Computer Score: {c_score}")
       rounds_label.config(text=f"Round {rounds_played+1}")


   info_button = Button(name_window, text="Submit", command=submit_info, font="15", fg="red")
   info_button.pack(side=TOP, pady=10)


date = dt.datetime.now()
date_label = Label(w, text=f"{date:%A, %B %d, %Y", fg="red")
date_label.pack(side=TOP)


rps_title = Label(text="Rochambeau", font="Arial 40 bold", fg="pink")
rps_title.pack()


p_score_label = Label(w, text="", font="20", fg="pink")
p_score_label.pack(side=TOP, pady=10)


c_score_label = Label(w, text="", font="20", fg="blue")
c_score_label.pack(side=TOP, pady=10)


p_result_lab = Label(w, text="", font="20", fg="pink")
p_result_lab.pack(side=TOP, pady=10)


c_result_lab = Label(w, text="", font="20", fg="blue")
c_result_lab.pack(side=TOP, pady=10)


winner_label = Label(w, text="", font="25")
winner_label.pack(side=TOP, pady=10)


choices_label = Label(w, text="Three or Five Rounds:")
choices_label.pack(side=BOTTOM, padx=10)


rock3r = Button(w, text="Rock", fg="red", bg="pink", command=lambda: play_rps_3r("Rock", player_info_var.get()))
rock3r.pack(side=LEFT, padx=10)


paper3r = Button(w, text="Paper", fg="red",bg="pink", command=lambda: play_rps_3r("Paper", player_info_var.get()))
paper3r.pack(side=LEFT, padx=10)


scissors3r = Button(w, text="Scissors", fg="red", bg="pink", command=lambda: play_rps_3r("Scissors", player_info_var.get()))
scissors3r.pack(side=LEFT, padx=10)


rock5r = Button(w, text="Rock", fg="pink", bg="red", command=lambda: play_rps_5r("Rock", player_info_var.get()))
rock5r.pack(side=RIGHT, padx=10)


paper5r = Button(w, text="Paper", fg="pink", bg="red", command=lambda: play_rps_5r("Paper", player_info_var.get()))
paper5r.pack(side=RIGHT, padx=10)


scissors5r = Button(w, text="Scissors", fg="pink", bg="red", command=lambda: play_rps_5r("Scissors", player_info_var.get()))
scissors5r.pack(side=RIGHT, padx=10)


replay_button = Button(w, text="Play Again", command=restart_game, font="Arial 20", fg="red")
replay_button.pack(side=TOP, pady=10)


rounds_label = Label(w, text="", font="Arial 20", fg="blue")
rounds_label.pack(side=TOP, pady=10)


get_player_info()
w.mainloop()
