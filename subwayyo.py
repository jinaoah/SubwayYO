from tkinter import *
from PIL import Image, ImageTk
import time as t
import random
import threading

# 윈도우 크기
w = 980
h = 700
# 상단 버튼 선택프레임 좌표
sx = 0
sy = 0
ex = 130
ey = 130
time = 10
score = 0
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
    def start(self):
        global goalCode
        self.goalImg = random.choice(list(self.goal.keys()))
        self.orderSheet.create_image(110,120,image=self.goalImg,tags="img")
        goalCode = self.goal(self.goalImg)
        self.th1 = threading.Thread(target=self.get_Goal)
        # self.timerOn()
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
        self.countStart()

    def countStart(self):
        global makeCode
        self.scoreStr="현재점수:{0}🍟".format(str(score))
        self.scoreLabel.config(text=self.scoreStr)
        for i in range(3): #카운트 다운
            self.orderSheet.delete("all")
            tagStr="count"
            for x in range(20):
                self.orderSheet.move(tagStr,7,0)
                t.sleep(0.02)
                self.window.update()
            for o in range(60):
                self.window.update()
                t.sleep(0.01)
            self.orderSheet.delete("all")
        for o in range(100):#start!! 이후 1초 쉬고 시작
                self.window.update()
                t.sleep(0.01)
        self.orderSheet.delete("all")
        self.buttonUnlock()
        self.start()

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
        highlightcolor="black", bd=5, command=lambda:self.click("upBread"))
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
        command=lambda:self.click("downBread"))
        self.downBreadBtn.grid(row=1, column=0, padx=5, pady=5)

        # 버튼 포커스 및 락
        self.upBreadBtn.focus_set()
        self.buttonLock()

        # 점수
        global score
        # global highScore
        self.currentScore = f'🎮 현재점수 : {str(score)}🥪'
        self.scoreLabel = Label(self.gameCnvs, text=self.currentScore, bg="white", font=("빙그레 싸만코체", 20, ""))
        self.scoreLabel.place(x=640, y=580)
        # 샌드위치 사진 가져오기
        self.goalImg1 = ImageTk.PhotoImage(file="img\sandwich1.png")
        self.goalImg2 = ImageTk.PhotoImage(file="img\sandwich2.png")
        self.goalImg3 = ImageTk.PhotoImage(file="img\sandwich3.png")
        self.goalImg4 = ImageTk.PhotoImage(file="img\sandwich4.png")
        self.goalImg5 = ImageTk.PhotoImage(file="img\sandwich5.png")

        # 샌드위치 정답코드
        # 윗빵 ub 양상추 le 토마토 to 피클 pi 베이컨 ba 아래빵 db
        self.goal = {
            self.goalImg1:"dbletopibaub",self.goalImg2:"dblebaub",
            self.goalImg3:"dblebalebaub",self.goalImg4:"dblepitoub",
            self.goalImg5:"dbletobaub"
        }

        # 샌드위치 주문서 캔버스
        self.orderSheet = Canvas(self.gameCnvs, bg="black", width=280, height=280)
        self.orderSheet.place(x=620, y=60)

        # 타이머
        self.timeCnvs = Canvas(self.gameCnvs, bg="black", width=220, height=60)
        self.timeCnvs.place(x=650, y=270)

    def get_Goal(self):
        global goalCode
        self.orderSheet.move("img",30,0)
        self.goalImg = random.choice(list(self.goal.keys()))
        self.orderSheet.create_image(-92,120,image=self.goalImg,tags="img2")
        goalCode = self.goal.get(self.goalImg)
        print("goalcode: ", goalCode)
        for x in range(20):
            self.orderSheet.move("img",15,0)
            self.orderSheet.move("img2",10,0)
            t.sleep(0.02)

    def make(self, img, code):
        global makeCode
        self.makeCnvs.create_image(200,250-self.makeY, image=img)
        self.makeY += 40 # 재료 높이 올리기
        # if img == self.topLettuce:
        #     self.makeY -= 6
        makeCode += code
        print("makeCode: ", makeCode)
        if not goalCode.startswith(makeCode):
            self.endM()
        if makeCode == goalCode:
            self.endM()

    def endM(self):
        global makeCode
        global goalCode
        if makeCode==goalCode:
             self.correct()
        else: self.wrong()
        timer = threading.Timer(2, self.endM2)
        timer.start()
        #todo 정답과 비교
        #todo 클릭 잠그기
        self.buttonLock()
    def endM2(self):           
        if self.runT-self.startT<60: #게임 종료 전
            self.th1.start()
            self.th1 = threading.Thread(target=self.get_Goal)
            self.buttonUnlock()
            self.makeInit()

    def correct(self):
        global score
        self.correctImg = ImageTk.PhotoImage("img\정답.png") 
        self.makeCnvs.create_image(190,140,image=self.correctImg)
        score+=1
        self.scoreLabel.config(text=self.currentScore)
    def wrong(self):
        self.wrongImg = ImageTk.PhotoImage("img\\오답.png")
        self.makeCnvs.create_image(185,150, image=self.wrongImg)

    def buttonLock(self):
        self.baconBtn['command']=""
        self.upBreadBtn['command']=""
        self.downBreadBtn['command']=""
        self.tomatoBtn['command']=""
        self.lettuceBtn['command']=""
        self.pickleBtn['command']=""
     #버튼 커맨드 
    def buttonUnlock(self):
        self.baconBtn['command']=lambda:self.click("bacon")
        self.upBreadBtn['command']=lambda:self.click("upBread")
        self.lettuceBtn['command']=lambda:self.click("lettuce")
        self.downBreadBtn['command']=lambda:self.click("downBread")
        self.tomatoBtn['command']=lambda:self.click("tomato")
        self.pickleBtn['command']=lambda:self.click("pickle")

    # 샌드위치 한 개당 타이머 10초
    # 10초가 지나면 게임 종료
    # 10초가 되기 전에 샌드위치 완성 -> 다음 사진으로 이동
    # def timeSet(self, i): 
    #     self.start = time.time()
    #     self.end = time.time()

    def click(self, str):
        if str == "upBread" : self.make(self.topUpBread, "ub")
        elif str == "bacon" : self.make(self.topBacon, "ba")
        elif str == "lettuce" : self.make(self.topLettuce, "le")
        elif str == "tomato" : self.make(self.topTomato, "to")
        elif str == "pickle" : self.make(self.topPickle, "pi")
        elif str == "downBread" : self.make(self.topDownBread, "db")
    
    # 키세팅
    def r(self):
        global sx
        global ex
        self.selectCnvs.delete("all")
        sx += 132
        if sx >= 396: sx = 0
        ex += 132
        if ex>=526:ex=132
        self.seleftF = self.selectCnvs.create_rectangle(sx,sy,ex,ey, fill="blue")
    def u(self):
        global ey
        self.selectCnvs.delete("all")
        sy-=132
        ey-=132
        if sy<=-132:sy=132
        if ey<=-2:ey=262
        self.seleftF = self.selectCnvs.create_rectangle(sx,sy,ex,ey, fill="blue")
    def l(self):
        global sx
        global ex
        self.selectCnvs.delete("all")
        sx-=132
        if sx<0:sx=264
        ex-=132
        if ex<130:ex=394
        self.seleftF = self.selectCnvs.create_rectangle(sx,sy,ex,ey, fill="blue")
    def d(self):
        global sy
        global ey
        self.selectCnvs.delete("all")
        sy+=132
        ey+=132
        if sy>=264:sy=0
        if ey>=394:ey=130
        self.seleftF = self.selectCnvs.create_rectangle(sx,sy,ex,ey, fill="blue")
    def key(self,event):
        if event.keycode==37:self.l()
        elif event.keycode==38:self.u()
        elif event.keycode==39:self.r()
        elif event.keycode==40:self.d()

        #버튼 셀렉프라임 의 위치에 따라 버튼 포커스 이동    
        sel = [sx,sy]
        if [0,0] == sel : self.upBreadBtn.focus_set()
        elif [132,0] == sel : self.pickleBtn.focus_set()
        elif [264,0] == sel : self.baconBtn.focus_set()
        if [0,132] == sel : self.downBreadBtn.focus_set()
        elif [132,132] == sel : self.tomatoBtn.focus_set()
        elif [264,132] == sel : self.lettuceBtn.focus_set()  

    def ruleWindow(self):
        global new
        new = Toplevel()

if __name__ == "__main__":
    GameManger()