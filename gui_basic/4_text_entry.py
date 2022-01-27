from tkinter import *
root = Tk()
root.title("GUI basic")         # window 제목
root.geometry("640x480")

# 텍스트 (여러 줄을 입력할 때)
txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "글자를 입력하세요.")

# 엔트리 (한줄만 입력할 때)
e = Entry(root, width=30)
e.pack()
e.insert(0, "한 줄만 입력하세요")

def btncmd():
    # 내용 출력
    print(txt.get("1.0", END))      # txt에 있는 모든 내용 가져옴. 1은 줄을 뜻하고 0은 0번째 열, END는 끝까지
    print(e.get())

    # 화면에서 내용 삭제 
    txt.delete("1.0", END)
    e.delete(0, END)

btn =Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop()