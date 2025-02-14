import turtle
import datetime
import pytz  # 引入 pytz 模組以支持時區功能

# 設置畫布 (Screen)
screen = turtle.Screen()
screen.title("Analog Clock with Timezone Support")  # 設置窗口標題
screen.bgcolor("white")  # 設置背景顏色為白色
screen.setup(width=800, height=800)  # 設置畫布大小為 800x800

# 創建畫筆 (Turtle) 用來繪製時鐘表盤
tur = turtle.Turtle()
tur.speed(0)  # 設置繪圖速度為最快
tur.hideturtle()  # 隱藏畫筆箭頭形狀，保持畫面整潔

# 繪製時鐘表盤
def draw_clock_face():
    tur.penup()
    tur.goto(0, -300)  # 移動到圓心下方，用來繪製圓形表盤
    tur.pendown()
    tur.circle(300)  # 繪製半徑為 300 的圓形
    tur.penup()
    tur.goto(0, 0)  # 回到畫布中心
    tur.seth(90)  # 設置方向朝北

    # 繪製數字刻度
    for i in range(0, 12):
        tur.penup()
        tur.forward(260)  # 向前移動到數字刻度位置
        if i == 0:
            tur.write(12, align="center", font=("Arial", 16, "normal"))  # 寫下數字
        else:
            tur.write(i, align="center", font=("Arial", 16, "normal"))  # 寫下數字
        tur.back(260)  # 返回圓心
        tur.right(30)  # 每次旋轉 30 度以繪製下一個數字

# 繪製表盤
draw_clock_face()

# 創建時針、分針和秒針的畫筆
hour_hand = turtle.Turtle()
minute_hand = turtle.Turtle()
second_hand = turtle.Turtle()

# 配置指針的屬性
for hand in (hour_hand, minute_hand, second_hand):
    hand.shape("arrow")  # 設置指針形狀為箭頭
    hand.shapesize(stretch_wid=0.2, stretch_len=10)  # 設置指針的寬度和長度
    hand.speed(0)  # 設置指針繪圖速度為最快
    hand.penup()  # 確保指針移動時不繪製軌跡
    hand.goto(0, 0)  # 指針起點設置在圓心
    hand.seth(90)  # 設置指針初始方向為北

# 調整不同指針的長度
second_hand.shapesize(stretch_wid=0.1, stretch_len=12) # 秒針較長且較細
minute_hand.shapesize(stretch_wid=0.2, stretch_len=14) # 分針稍長
hour_hand.shapesize(stretch_wid=0.3, stretch_len=8) # 時針較短且較粗

# 更新指針位置的函數
def update_clock(target_timezone):
    # 獲取指定時區的當前時間
    now = datetime.datetime.now(pytz.timezone(target_timezone))
    h = now.hour % 12 # 小時數（12 小時制）
    m = now.minute  # 分鐘數
    s = now.second  # 秒數

    # 計算每個指針的旋轉角度
    hour_angle = h * 30 + m / 60 * 30
    minute_angle = m * 6
    second_angle = s * 6

    # 更新指針角度
    hour_hand.setheading(90 - hour_angle)
    minute_hand.setheading(90 - minute_angle)
    second_hand.setheading(90 - second_angle)

    # 每秒重新調用一次更新函數
    screen.ontimer(lambda: update_clock(target_timezone), 1000)

# 設置目標時區 
# Examples: 'Asia/Tokyo', 'America/New_York', 'Europe/London'
target_timezone = 'Asia/Taipei'

# 啟動時鐘並開始更新
update_clock(target_timezone)

# 保持窗口開啟
screen.mainloop()
