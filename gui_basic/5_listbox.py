from tkinter import *
root = Tk()
root.title("GUI basic")         # window 제목
root.geometry("640x480")

# 텍스트 (여러 줄을 입력할 때)

listbox = Listbox(root, selectmode="extended", height=0)        # extended는 여러 개 선택 가능, single은 하나만 선택가능, height는 0이면 list 전체 출력, 특정 숫자로 하면 그 숫자만큼만 출력
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
    #listbox.delete(END)     # 맨 뒤 항목 삭제
    # listbox.delete(0)     # 맨 앞 항목 삭제

    # 갯수 확인
    # print("리스트에는", listbox.size(), "개가 있어요")

    # 항목 확인
    # print("1번째부터 3번째까지의 항목 : ", listbox.get(0, 2))

    # 선택된 항목 확인
    print("선택된 항목 : ", listbox.curselection())     # 항목의 위치값 반환


btn =Button(root, text="클릭", command=btncmd)
btn.pack()


root.mainloop()