from tkinter import *
root = Tk()
root.title("GUI basic")         # window 제목
root.geometry("640x480")
btn1 = Button(root, text="버튼1")
btn1.pack()     # 버튼 출력

btn2 = Button(root, padx=5, pady=10, text="버튼2")  # 버튼내의 공간을 띄워줌
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼4")       # 실제 버튼 크기를 고정함.
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼5")        # fg는 글자색, bg는 버튼 색
btn5.pack()

photo = PhotoImage(file="gui_basic/img.png")
btn6 = Button(root, image=photo)
btn6.pack()

# 버튼 동작
def btncmd():
    print("버튼이 클릭되었어요.")

btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop()