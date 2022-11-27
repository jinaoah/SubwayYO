import tkinter as tk

class Game:
    print('게임')
    
    def __init__(self): #게임화면 셋팅
        self.window = tk.Tk() #가장 상위 레벨의 윈도우 창을 생성
        self.window.title("서브웨이yo ~ 🥪🌯")
        # self.window.geometry("1080x780")
        self.window.state("zoomed")

        label = tk.Label(self.window, text='Subway Yo 🥪 ~', font=('Arial',36),
                background='yellow',highlightthickness=8,
                highlightbackground='green')
        # label.place(x=400, y=0)
        label.pack()
        
        #게임시작 버튼 클릭 시 start() 함수 호출
        start_btn = tk.Button(self.window, text='게임 시작', command=self.start)
        start_btn.place(x=300, y=90)

        self.window.mainloop() #윈도우 창을 윈도우가 종료될 때까지 실행
    
    def start(self): 
        print('게임시작')
    
    def rule():
        print('게임 설명')

    def set():
        print('게임 초기 설정')
    
    def timeOn():
        print('게임 중 타이머 설정 함수')
    
    def correct():
        print('샌드위치 재료를 모두 맞췄을 경우')
    
    def fail():
        print('샌드위치 재료를 못 맞춘 경우')
    
    def finish():
        print('게임 통과')
        # 0이면 게임 종료 1이면 게임 재시작

# 함수 호출
if __name__ == "__main__":
    Game()