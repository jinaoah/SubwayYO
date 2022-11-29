from tkinter import *
from PIL import Image, ImageTk
import time as t
import threading

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
        # 1. 게임 시작 버튼
        startBtn = Button(
                    self.startCnvs, 
                    text="Game Start", 
                    bg="white",
                    font=("빙그레 싸만코체", 20, "bold"),
                    command=self.startBtnClick)
        startBtn.place(x=246,y=520)
        
        ruleBtn = Button(self.startCnvs, text="게임 설명", bg="brown",fg="white",font=('Hack',20, "bold"), command=self.ruleWindow)
        ruleBtn.place(x=560, y=520)
        
        self.window.bind('<KeyPress>',self.key)
        self.window.mainloop() # window 종료할 때까지 계속 실행

    def set(self): #이미지, 게임 기본 세팅
        self.topBacon = ImageTk.PhotoImage(file = "img\베이컨.png")
        self.topPickle = ImageTk.PhotoImage(file = "img\피클.png")
        self.topLettuce = ImageTk.PhotoImage(file = "img\양상추.png")
        self.topUpBread = ImageTk.PhotoImage(file = "img\위빵.png")
        self.topDownBread = ImageTk.PhotoImage(file = "img\아래빵.png")
        self.topTomato = ImageTk.PhotoImage(file = "img\토마토.png")
        self.topDish = ImageTk.PhotoImage(file="img\접시.png")

        # 메이킹 라벨 이미지

        # self.backgroundImg = ImageTk.PhotoImage(file = "img\gameBackground.png")
        # self.gameCnvs.create_image(700,400, image = self.backgroundImg) #상단 라벨 프레임
        self.selectCnvs = Canvas(self.gameCnvs, bd =1 , bg = "yellow")
        self.selectCnvs.place(x=130,y=60)
        
        self.makeCnvs = Canvas(self.gameCnvs, bd=0, width=390, height=280, bg="orange")
        self.makeCnvs.place(x=130, y=350)
        self.makeY = 0 #메이킹 라벨 재료들의 그려지는 위치
        self.make(self.topDish, "") #make 함수 
        self.seleftF = self.selectCnvs.create_rectangle(sx,sy,ex,ey, fill="blue")

        # 버튼
        self.upBreadBtn = Button(self.selectCnvs, bg="white", image=self.topUpBread, width=100, height=100,
        highlightcolor="black", bd=5, command=lambda:self.click("UpB"))
        self.upBreadBtn.grid(row=0, column=0, padx=10,pady=10)

        self.pickleBtn = Button(self.selectCnvs, bg="green", image=self.topPickle, width=100, height=100,
        highlightcolor="black", bd=5, command=lambda:self.click("pickle"))
        self.pickleBtn.grid(row=0, column=1, padx=5, pady=5)

        self.baconBtn = Button(self.selectCnvs, bg="blue", image=self.topBacon, width=100, height=100, 
        bd=5, command=lambda:self.click("bacon"))
        self.baconBtn.grid(row=0, column=2, padx=10, pady=10)

        self.lettuceBtn = Button(self.selectCnvs, bg="green", image=self.topLettuce, width=100, height=100, bd=5,
        command=lambda:self.click("lettuce"))
        self.lettuceBtn.grid(row=1,column=2,padx=5,pady=5)

        self.tomatoBtn = Button(self.selectCnvs, bg="red", image=self.topTomato, width=100, height=100, bd=5, 
        command=lambda:self.click("tomato"))
        self.tomatoBtn.grid(row=1, column=1, padx=10, pady=10)

        self.downBreadBtn = Button(self.selectCnvs, bg="white", image=self.topDownBread, width=100, height=100, bd=5, 
        command=lambda:self.click("downB"))
        self.downBreadBtn.grid(row=1, column=0, padx=5, pady=5)

        # 버튼 포커스 및 락
        self.upBreadBtn.focus_set()
        # self.buttonLock()

        # 샌드위치 사진 가져오기
        self.goalImg1 = ImageTk.PhotoImage(file="img\sandwich1.png")
        self.goalImg2 = ImageTk.PhotoImage(file="img\sandwich2.png")
        self.goalImg3 = ImageTk.PhotoImage(file="img\sandwich3.png")
        self.goalImg4 = ImageTk.PhotoImage(file="img\sandwich4.png")
        self.goalImg5 = ImageTk.PhotoImage(file="img\sandwich5.png")

        # 샌드위치 주문서 캔버스
        self.orderSheet = Canvas(self.gameCnvs, bg="white", width=280, height=280)
        self.orderSheet.place(x=620, y=60)
        self.orderSheet.create_text(150, 10, text="주문서", fill="black")

    def make(self, img, code):
        global makeCode
        self.makeCnvs.create_image(200,250-self.makeY, image=img)
        self.makeY += 15 # 재료 높이 올리기
        if img == self.topLettuce:
            self.makeY -= 6
        makeCode += code
        print("makeCode: ", makeCode)
        if not goalCode.startswith(makeCode):
            self.endM()
        if makeCode == goalCode:
            self.endM()

    def click(self, str):
        if str == "upB" : self.make(self.topUpBread, "ub")
        elif str == "bacon" : self.make(self.topBacon, "p")

    def ruleWindow(self):
        global new
        new = Toplevel()

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