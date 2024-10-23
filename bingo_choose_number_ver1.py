import threading
import time as tm
import _thread
import tkinter

flag_stop = 0
app = int

def start_choose(event):
    global flag_stop
    flag_stop = 1

def choose():
    global flag_stop
    bingo_num = list(range(1,76))
    past_num = [0]*75
    list_num = 0
    choose_num = 0
    i = 74
    j = 0
    #n = -2
    while True:
        for j in range(i,-1,-1):
            #print(flag_stop)
            if flag_stop == 0:
                choose_num = bingo_num[j]

            elif flag_stop != 0:
                pop_num = bingo_num.pop(j)
                past_num[list_num] = pop_num
                list_num += 1
                i -= 1
                flag_stop = 0
                pop_num_label["text"] = '%d' %pop_num
                past1_num_label["text"] = '%ls' %past_num[list_num-2]
                past2_num_label["text"] = '%ls' %past_num[list_num-3]
                past3_num_label["text"] = '%ls' %past_num[list_num-4]
                break

def close_window():
    window.destroy()
    window.quit()

thread1 = threading.Thread(target=choose)
thread1.start()
 
# 画面作成
window = tkinter.Tk()
window.geometry("400x300")
window.title("ビンゴ司会システム")

#抽選した数字の表示
pop_num_label = tkinter.Label(window, text="抽選しよう", font=(16),bg='lightpink')
pop_num_label.place(x=125, y=150, width=150)

#履歴を表示
past_num_label = tkinter.Label(window, text="履歴", font=(10), bg='white')
past1_num_label = tkinter.Label(window, text="履歴", font=(10), bg='white')
past1_num_label.place(x=125, y=100, width=150)
past2_num_label = tkinter.Label(window, font=(10), bg='white')
past2_num_label.place(x=125, y=50, width=150)
past3_num_label = tkinter.Label(window, font=(10), bg='white')
past3_num_label.place(x=125, width=150)


# 抽選ボタンの作成
btn1 = tkinter.Button(window, text="抽選")
btn1.place(x=125, y=230, width=150, height=40)

#GUI終了ボタン
button_close = tkinter.Button(text="終了", command=close_window)
button_close.place(x=50,y=240)
 
# ボタンに関数をbind
btn1.bind("<Button-1>", start_choose)
 
# 画面表示（常駐）
window.mainloop()