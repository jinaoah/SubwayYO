from tkinter import *
from PIL import ImageTk, Image
import time as t

# 윈도우 크기
w = 980
h = 700
# 상단 버튼 선택프레임 좌표
sx = 0
sy = 0
ex = 130
ey = 130

makeCode = "" #정답 입력 str
goalCode = "goal"

class GameManger:
    def __init__(self):
        self.window = Tk()
        self.window.title("Subway YO")

        # 윈도우 크기 설정
        screenWidth = self.window.winfo_screenwidth()
        screenHeight = self.window.winfo_screenheight()
        x = (screenWidth - w)/2
        y = (screenHeight - h)/2
        self.window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.window.resizable(False, False) #윈도우 크기 고정시키기
        
        # 게임화면
        self.gameCnvs = Canvas(self.window, bd=2, bg="white")
        self.gameCnvs.pack(fill="both", expand=True) #공간을 채워넣어 배치
        # 게임 세팅
        self.set()

        # 프로그램 시작화면
        self.sTi = ImageTk.PhotoImage(Image.open("img/subwayShop.png"))
        self.startCnvs = Canvas(self.gameCnvs,width=980,height=700,bd=0,bg="brown")
        self.gameCnvs.create_window(w/2, h/2, window=self.startCnvs, tags="startCnvs")
        self.startCnvs.create_image(450,350,image=self.sTi)
        startBtn = Button(
                    self.startCnvs, 
                    text="Game Start", 
                    bg="white",
                    font=("빙그레 싸만코체", 20, "bold"),
                    command=self.startBtnClick)
        startBtn.place(x=246,y=520)
 
        self.window.bind('<KeyPress>',self.key)
        self.window.mainloop() # window 종료할 때까지 계속 실행

    def set(self): #이미지, 게임 기본 세팅
        pass

    def startBtnClick(self):
        for x in range(10) :
            self.gameCnvs.move("startCnvs",0,5)
            t.sleep(0.01)
            self.window.update()
        for x in range(35) :
            self.gameCnvs.move("startCnvs",0,-30-x*20)
            t.sleep(0.01)
            self.window.update()
        self.startCnvs.destroy()

    def key(self, event):
        #버튼 셀렉프라임 의 위치에 따라 버튼 포커스 이동 
        select = [sx,sy]

if __name__ == "__main__":
    GameManger()