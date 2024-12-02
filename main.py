import time
import pyautogui

# 准备时间
#time.sleep(6)

def play_game():
    # 买英雄
    champions = ['kennen.png', 'evelynn.png', 'gnar.png', 'katarina.png', 'lillia.png', 'neeko.png', 'qiyana.png',
                 'yone.png', 'zed.png']
    for champion in champions:
        buy_champion = pyautogui.locateCenterOnScreen(champion, confidence=0.7)
        if buy_champion:
            pyautogui.click(buy_champion)



#while True:

#    x, y = pyautogui.position()
#    time.sleep(1)
    # 打印坐标
#    print(f"Current mouse position - X: {x}, Y: {y}")



while True:

    # 找到开始游戏按钮并点击
    start_button = pyautogui.locateCenterOnScreen('start_button.png', confidence=0.7)
    if start_button:
        pyautogui.click(start_button)

    # 找到接受游戏按钮并点击
    accept_button = pyautogui.locateCenterOnScreen('accept_button.png', confidence=0.7)
    if accept_button:
        pyautogui.click(accept_button)


    buy_champion = pyautogui.locateCenterOnScreen('katarina.png', confidence=0.7)
    if buy_champion:
        #pyautogui.click(buy_champion)
        pyautogui.click(buy_champion, button='left')
        time.sleep(0.2)
        pyautogui.mouseUp(x=818, y=800)
    buy_champion = pyautogui.locateCenterOnScreen('evelynn.png', confidence=0.7)
    if buy_champion:
        pyautogui.click(buy_champion, button='left')
        time.sleep(0.2)
        pyautogui.mouseUp(x=818, y=800)

    center_button = pyautogui.locateCenterOnScreen('center.png', confidence=0.5)
    if center_button:
        pyautogui.rightClick(center_button)
        pyautogui.mouseUp(center_button)

    # 找到结束游戏按钮并点击
    end_game = pyautogui.locateCenterOnScreen('end_game.png', confidence=0.7)
    if end_game:
        pyautogui.click(end_game)

    # 找到再玩一次按钮并点击
    again_button = pyautogui.locateCenterOnScreen('again_button.png', confidence=0.7)
    if again_button:
        pyautogui.click(again_button)