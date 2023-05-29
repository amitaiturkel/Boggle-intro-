import datetime
import tkinter as tk
import tkinter.font as tkFont
from helper_functions import *
from boggle_board_randomizer import randomize_board
from ex11_utils import init_game


class App:
    def __init__(self, root,board,legal_paths):
        #setting title
        self.root = root
        self.board = board
        root.title("Boogle game")
        #setting window size
        width=504
        height=493
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        self.time_started = False
        self.legal_paths = legal_paths #get from big program
        self.current_path =[] #update every press
        self.pause = True
        self.path_already_chosen = []
        self.is_step_legal = True
        self.play_again = False
        root['bg'] = "#FCEED9"

        
# ======================= TIMER =======================

        self.end_time = None
        self.countdown_label = tk.Label(root, text="", font=("Courier", 20))
        self.countdown_label.place(x=width - 200, y=10)
        self.countdown_label["bg"] = "#FCEED9"

# ===================== START BUTTON ===================

        start_button = tk.Button(root, text="Start", command=self.start_game)
        start_button.place(x=10,y=80,width=100,height=60)
        start_button["activeforeground"] = "#ebe6ca"
        start_button["bg"] = "#E7DDCF"
        ft = tkFont.Font(family='Courier', size=10)
        start_button["font"] = ft
        start_button["fg"] = "#000000"
        start_button["justify"] = "center"
        self.start_button = start_button

# =================== LETTER BUTTONS =================
        Button_0_3=tk.Button(root)
        Button_0_3["activeforeground"] = "#ebe6ca" 
        Button_0_3["bg"] = "#E7DDCF"
        ft = tkFont.Font(family='Courier',size=10)
        Button_0_3["font"] = ft
        Button_0_3["fg"] = "#000000"
        Button_0_3["justify"] = "center"
        Button_0_3["text"] = str(self.board[0][3])
        Button_0_3.place(x=250,y=170,width=70,height=70)
        Button_0_3["command"] = self.Button_0_3_command
        self.Button_0_3 = Button_0_3

        Button_1_3=tk.Button(root)
        Button_1_3["activeforeground"] = "#ebe6ca"
        Button_1_3["bg"] = "#E7DDCF"
        ft = tkFont.Font(family='Courier',size=10)
        Button_1_3["font"] = ft
        Button_1_3["fg"] = "#000000"
        Button_1_3["justify"] = "center"
        Button_1_3["text"] = str(self.board[1][3])
        Button_1_3.place(x=250,y=250,width=70,height=70)
        Button_1_3["command"] = self.Button_1_3_command
        self.Button_1_3 = Button_1_3

        Button_2_3=tk.Button(root)
        Button_2_3["activeforeground"] = "#ebe6ca"
        Button_2_3["bg"] = "#E7DDCF"
        ft = tkFont.Font(family='Courier',size=10)
        Button_2_3["font"] = ft
        Button_2_3["fg"] = "#000000"
        Button_2_3["justify"] = "center"
        Button_2_3["text"] = str(self.board[2][3])
        Button_2_3.place(x=250,y=330,width=70,height=70)
        Button_2_3["command"] = self.Button_2_3_command
        self.Button_2_3 = Button_2_3

        Button_3_3=tk.Button(root)
        Button_3_3["activeforeground"] = "#ebe6ca"
        Button_3_3["bg"] = "#E7DDCF"
        ft = tkFont.Font(family='Courier',size=10)
        Button_3_3["font"] = ft
        Button_3_3["fg"] = "#000000"
        Button_3_3["justify"] = "center"
        Button_3_3["text"] = str(self.board[3][3])
        Button_3_3.place(x=250,y=410,width=70,height=70)
        Button_3_3["command"] = self.Button_3_3_command
        self.Button_3_3 = Button_3_3

        Button_0_2=tk.Button(root)
        Button_0_2["activeforeground"] = "#ebe6ca"
        Button_0_2["bg"] = "#E7DDCF"
        ft = tkFont.Font(family='Courier',size=10)
        Button_0_2["font"] = ft
        Button_0_2["fg"] = "#000000"
        Button_0_2["justify"] = "center"
        Button_0_2["text"] = str(self.board[0][2])
        Button_0_2.place(x=170,y=170,width=70,height=70)
        Button_0_2["command"] = self.Button_0_2_command
        self.Button_0_2 = Button_0_2

        Button_1_2=tk.Button(root)
        Button_1_2["activeforeground"] = "#ebe6ca"
        Button_1_2["bg"] = "#E7DDCF"
        ft = tkFont.Font(family='Courier',size=10)
        Button_1_2["font"] = ft
        Button_1_2["fg"] = "#000000"
        Button_1_2["justify"] = "center"
        Button_1_2["text"] = str(self.board[1][2])
        Button_1_2.place(x=170,y=250,width=70,height=70)
        Button_1_2["command"] = self.Button_1_2_command
        self.Button_1_2 = Button_1_2

        Button_2_2=tk.Button(root)
        Button_2_2["activeforeground"] = "#ebe6ca"
        Button_2_2["bg"] = "#E7DDCF"
        ft = tkFont.Font(family='Courier',size=10)
        Button_2_2["font"] = ft
        Button_2_2["fg"] = "#000000"
        Button_2_2["justify"] = "center"
        Button_2_2["text"] = str(self.board[2][2])
        Button_2_2.place(x=170,y=330,width=70,height=70)
        Button_2_2["command"] = self.Button_2_2_command
        self.Button_2_2 = Button_2_2

        Button_3_2=tk.Button(root)
        Button_3_2["activeforeground"] = "#ebe6ca"
        Button_3_2["bg"] = "#E7DDCF"
        ft = tkFont.Font(family='Courier',size=10)
        Button_3_2["font"] = ft
        Button_3_2["fg"] = "#000000"
        Button_3_2["justify"] = "center"
        Button_3_2["text"] = str(self.board[3][2])
        Button_3_2.place(x=170,y=410,width=70,height=70)
        Button_3_2["command"] = self.Button_3_2_command
        self.Button_3_2 = Button_3_2

        Button_0_1=tk.Button(root)
        Button_0_1["activeforeground"] = "#ebe6ca"
        Button_0_1["bg"] = "#E7DDCF"
        ft = tkFont.Font(family='Courier',size=10)
        Button_0_1["font"] = ft
        Button_0_1["fg"] = "#000000"
        Button_0_1["justify"] = "center"
        Button_0_1["text"] = str(self.board[0][1])
        Button_0_1.place(x=90,y=170,width=70,height=70)
        Button_0_1["command"] = self.Button_0_1_command
        self.Button_0_1 = Button_0_1

        Button_2_1=tk.Button(root)
        Button_2_1["activeforeground"] = "#ebe6ca"
        Button_2_1["bg"] = "#E7DDCF"
        ft = tkFont.Font(family='Courier',size=10)
        Button_2_1["font"] = ft
        Button_2_1["fg"] = "#000000"
        Button_2_1["justify"] = "center"
        Button_2_1["text"] = str(self.board[2][1])
        Button_2_1.place(x=90,y=330,width=70,height=70)
        Button_2_1["command"] = self.Button_2_1_command
        self.Button_2_1 = Button_2_1

        Button_3_1=tk.Button(root)
        Button_3_1["activeforeground"] = "#ebe6ca"
        Button_3_1["bg"] = "#E7DDCF"
        ft = tkFont.Font(family='Courier',size=10)
        Button_3_1["font"] = ft
        Button_3_1["fg"] = "#000000"
        Button_3_1["justify"] = "center"
        Button_3_1["text"] = str(self.board[3][1])
        Button_3_1.place(x=90,y=410,width=70,height=70)
        Button_3_1["command"] = self.Button_3_1_command
        self.Button_3_1 = Button_3_1

        Button_1_1=tk.Button(root)
        Button_1_1["activeforeground"] = "#ebe6ca"
        Button_1_1["bg"] = "#E7DDCF"
        ft = tkFont.Font(family='Courier',size=10)
        Button_1_1["font"] = ft
        Button_1_1["fg"] = "#000000"
        Button_1_1["justify"] = "center"
        Button_1_1["text"] = str(self.board[1][1])
        Button_1_1.place(x=90,y=250,width=70,height=70)
        Button_1_1["command"] = self.Button_1_1_command
        self.Button_1_1 = Button_1_1

        Button_0_0=tk.Button(root)
        Button_0_0["activeforeground"] = "#ebe6ca"
        Button_0_0["bg"] = "#E7DDCF"
        ft = tkFont.Font(family='Courier',size=10)
        Button_0_0["font"] = ft
        Button_0_0["fg"] = "#000000"
        Button_0_0["justify"] = "center"
        Button_0_0["text"] = str(self.board[0][0])
        Button_0_0.place(x=10,y=170,width=70,height=70)
        Button_0_0["command"] = self.Button_0_0_command
        self.Button_0_0 = Button_0_0

        Button_1_0=tk.Button(root)
        Button_1_0["activeforeground"] = "#ebe6ca"
        Button_1_0["bg"] = "#E7DDCF"
        ft = tkFont.Font(family='Courier',size=10)
        Button_1_0["font"] = ft
        Button_1_0["fg"] = "#000000"
        Button_1_0["justify"] = "center"
        Button_1_0["text"] = str(self.board[1][0])
        Button_1_0.place(x=10,y=250,width=70,height=70)
        Button_1_0["command"] = self.Button_1_0_command
        self.Button_1_0 = Button_1_0

        Button_2_0=tk.Button(root)
        Button_2_0["activeforeground"] = "#ebe6ca"
        Button_2_0["bg"] = "#E7DDCF"
        ft = tkFont.Font(family='Courier',size=10)
        Button_2_0["font"] = ft
        Button_2_0["fg"] = "#000000"
        Button_2_0["justify"] = "center"
        Button_2_0["text"] = str(self.board[2][0])
        Button_2_0.place(x=10,y=330,width=70,height=70)
        Button_2_0["command"] = self.Button_2_0_command
        self.Button_2_0 = Button_2_0

        Button_3_0=tk.Button(root)
        Button_3_0["activeforeground"] = "#ebe6ca"
        Button_3_0["bg"] = "#E7DDCF"
        ft = tkFont.Font(family='Courier',size=10)
        Button_3_0["font"] = ft
        Button_3_0["fg"] = "#000000"
        Button_3_0["justify"] = "center"
        Button_3_0["text"] = str(self.board[3][0])
        Button_3_0.place(x=10,y=410,width=70,height=70)
        Button_3_0["command"] = self.Button_3_0_command
        self.Button_3_0 = Button_3_0

        Score=tk.Label(root)
        ft = tkFont.Font(family='Courier',size=28)
        Score["font"] = ft
        Score["fg"] = "#333333"
        Score["justify"] = "center"
        Score["text"] = "Score"
        Score["bg"] = "#FCEED9"
        Score.place(x=0,y=10,width=115,height=33)
        self.Score = Score
        #Score.wm_attributes('-transparentcolor', '#ab23ff')


        num_score = tk.Label(root)
        ft = tkFont.Font(family='Courier', size=28)
        num_score["font"] = ft
        num_score["fg"] = "#333333"
        num_score["justify"] = "center"
        num_score["text"] = 0
        num_score["bg"] = "#FCEED9"
        num_score.place(x=110,y=15,width=70,height=30)
        self.num_score = num_score

        current_word=tk.Label(root)
        current_word["bg"] = "#FCEED9"
        ft = tkFont.Font(family='Courier',size=28)
        current_word["font"] = ft
        current_word["fg"] = "#01040b"
        current_word["justify"] = "center"
        current_word["text"] = ""
        current_word.place(x=130,y=70,width=216,height=30)
        self.current_word = current_word

        submit=tk.Button(root)
        submit["bg"] = "#E7DDCF"
        ft = tkFont.Font(family='Courier',size=10)
        submit["font"] = ft
        submit["fg"] = "#000000"
        submit["justify"] = "center"
        submit["text"] = "Submit"
        submit.place(x=340,y=170,width=142,height=100)
        submit["command"] = self.submit_command

        word_already_chosen = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        word_already_chosen["font"] = ft
        word_already_chosen["fg"] = "#333333"
        word_already_chosen["justify"] = "center"
        word_already_chosen["text"] = ""
        word_already_chosen["bg"] = "#FCEED9"
        word_already_chosen.place(x=370, y=290, width=87, height=190)
        self.word_already_chosen = word_already_chosen
        self.all_button = [self.Button_3_0, self.Button_3_1, self.Button_3_2, self.Button_3_3,
                           self.Button_2_0, self.Button_2_1, self.Button_2_2, self.Button_2_3,
                           self.Button_1_0, self.Button_1_1, self.Button_1_2, self.Button_1_3,
                           self.Button_0_0, self.Button_0_1, self.Button_0_2, self.Button_0_3]

        self.all_button_info = [self.Button_3_0.place_info(), self.Button_3_1.place_info(),
                                self.Button_3_2.place_info(), self.Button_3_3.place_info(),
                                self.Button_2_0.place_info(), self.Button_2_1.place_info(),
                                self.Button_2_2.place_info(), self.Button_2_3.place_info(),
                                self.Button_1_0.place_info(), self.Button_1_1.place_info(),
                                self.Button_1_2.place_info(), self.Button_1_3.place_info(),
                                self.Button_0_0.place_info(), self.Button_0_1.place_info(),
                                self.Button_0_2.place_info(), self.Button_0_3.place_info()]

        for button in self.all_button:
            button.place_forget()


    def choose_letter(self,corr):
        self.current_word["text"] = self.current_word["text"] + self.board[corr[0]][corr[1]]

    def Button_0_3_command(self):
        if not self.pause:
            self.update_current_word((0,3))



    def Button_1_3_command(self):
        if not self.pause:
            self.update_current_word((1,3))

    def Button_2_3_command(self):
        if not self.pause:
            self.update_current_word((2,3))

    def Button_3_3_command(self):
        if not self.pause:
            self.update_current_word((3,3))

    def Button_0_2_command(self     ):
        if not self.pause:
            self.update_current_word((0,2))

    def Button_1_2_command(self):
        if not self.pause:
            self.update_current_word((1,2))

    def Button_2_2_command(self):
        if not self.pause:
            self.update_current_word((2,2))

    def Button_3_2_command(self):
        if not self.pause:
            self.update_current_word((3,2))

    def Button_0_1_command(self):
        if not self.pause:
            self.update_current_word((0,1))


    def Button_2_1_command(self):
        if not self.pause:
            self.update_current_word((2,1))

    def Button_3_1_command(self):
        if not self.pause:
            self.update_current_word((3,1))

    def Button_1_1_command(self):
        if not self.pause:
            self.update_current_word((1,1))

    def Button_0_0_command(self):
        if not self.pause:
            self.update_current_word((0,0))

    def Button_1_0_command(self):
        if not self.pause:
            self.update_current_word((1,0))

    def Button_2_0_command(self):
        if not self.pause:
            self.update_current_word((2,0))

    def Button_3_0_command(self):
        if not self.pause:
            self.update_current_word((3,0))

    def submit_command(self):
        if self.current_path in self.legal_paths and self.current_path not in self.path_already_chosen:
            self.set_score(len(self.current_path) ** 2)
            self.path_already_chosen.append(self.current_path)
            for letter in self.current_path:
                self.word_already_chosen.config(text=self.word_already_chosen.cget("text") + self.board[letter[0]][letter[1]])
            self.word_already_chosen.config(text=self.word_already_chosen.cget("text") + "\n")
        self.current_path = []
        self.current_word["text"]= ""


    def play_again_button_command(self):
        self.play_again = True
        self.root.destroy()


    def start_game(self):
        if not self.time_started:
            for but in range(len(self.all_button)):
                self.all_button[but].place(**self.all_button_info[but])
            self.end_time = datetime.datetime.now() + datetime.timedelta(minutes=3)
            self.root.after(1000, self.update_countdown)
            self.time_started = True
            self.pause = False

    def update_countdown(self):
        if datetime.datetime.now() > self.end_time:
            self.countdown_label.config(text="Time's up!")
            self.pause = True
            play_again_button = tk.Button(root)
            play_again_button["bg"] = "#E7DDCF"
            ft = tkFont.Font(family='Times', size=10)
            play_again_button["font"] = ft
            play_again_button["fg"] = "#000000"
            play_again_button["justify"] = "center"
            play_again_button["text"] = "play again?"
            play_again_button.place(x=390, y=70, width=79, height=57)
            play_again_button["command"] = self.play_again_button_command
            self.play_again_button = play_again_button

        else:
            time_left = self.end_time - datetime.datetime.now()
            minutes, seconds = divmod(time_left.seconds, 60)
            hours, minutes = divmod(minutes, 60)
            self.countdown_label.config(text='{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds))
            self.root.after(1000, self.update_countdown)

    def set_score(self,score):
        self.num_score["text"] += score

    def update_current_word(self, word_corr):
        if self.current_path == []:
            self.current_word.config(text=self.current_word.cget("text") + self.board[word_corr[0]][word_corr[1]])
            self.current_path.append(word_corr)
            pass
        else:
            last_path = self.current_path[-1]
            if word_corr in all_possible_moves(last_path) and word_corr not in self.current_path:
                self.current_word.config(text=self.current_word.cget("text") + self.board[word_corr[0]][word_corr[1]])
                self.current_path.append(word_corr)


if __name__ == "__main__":
    #opening the file in read mode
    my_file = open("boggle_dict.txt", "r")
    words = my_file.read().split("\n")
    my_file.close()
    play_again = True
    while play_again:
        board = randomize_board()
        root = tk.Tk()
        app = App(root,board, init_game(board, words))
        play_again = app.play_again
        root.mainloop()
        play_again = app.play_again

