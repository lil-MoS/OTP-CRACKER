OTP Code Cracker - کرکر کد یکبار مصرف
English Version
🔥 OTP Code Cracker
A powerful Python automation tool for testing all possible 6-digit OTP (One-Time Password) combinations with intelligent speed optimization.

🚀 Features
Brute-force Automation: Tests all 6-digit combinations (000000-999999)

Smart Speed Control: Optimized timing for maximum efficiency

Hotkey Controls: Start/Stop with simple keyboard shortcuts

Resume Capability: Continues from last tested code if interrupted

Real-time Progress: Live display of current code being tested

🛠️ Installation & Setup
Prerequisites:

pip install pyautogui keyboard
Usage:

Run the script: python code_cracker.py

Click on the first input field of the 6-digit OTP form

Press Shift + T to start cracking

Press Shift + Y to stop at any time

⚡ Technical Details
Input Method: High-speed typing with 0.02s interval

Processing Delay: 0.3s between attempts (adjustable)

Auto-clear: Automatic field clearing between attempts

Progress Tracking: Saves last tested code

⚠️ Important Notes
Use only on systems you own or have explicit permission to test

Intended for educational and authorized security testing

Adjust sleep timings based on target system response

نسخه فارسی - کرکر کد یکبار مصرف
🚀 کرکر کد یکبار مصرف
یک ابزار اتوماسیون پایتون قدرتمند برای تست تمام ترکیبات ممکن کدهای شش رقمی یکبار مصرف با بهینه‌سازی هوشمند سرعت

✨ ویژگی‌ها
اتوماسیون کامل: تست تمام ترکیبات شش رقمی (000000-999999)

کنترل سرعت هوشمند: زمان‌بندی بهینه برای حداکثر کارایی

کنترل با کلیدهای میانبر: شروع و توقف با کلیدهای ساده

قابلیت ادامه: از آخرین کد تست شده ادامه می‌دهد

نمایش پیشرفت زنده: نمایش لحظه‌ای کد در حال تست

🛠️ نصب و راه‌اندازی
پیش‌نیازها:


pip install pyautogui keyboard
طریقه استفاده:

اجرای اسکریپت: python code_cracker.py

کلیک روی اولین فیلد ورودی از فرم کد شش رقمی

فشردن Shift + T برای شروع عملیات

فشردن Shift + Y برای توقف در هر زمان

⚡ جزئیات فنی
روش ورود: تایپ پرسرعت با فاصله 0.02 ثانیه

تأخیر پردازش: 0.3 ثانیه بین هر تلاش (قابل تنظیم)

پاک‌سازی خودکار: پاک کردن فیلدها بین هر تلاش

ردیابی پیشرفت: ذخیره آخرین کد تست شده

⚠️ نکات مهم
فقط روی سیستم‌هایی استفاده شود که مالک آن هستید یا مجوز تست دارید

برای تست امنیت و اهداف آموزشی طراحی شده

زمان‌های تأخیر را بر اساس پاسخ سیستم هدف تنظیم کنید

📁 File Structure

OTP-CRACKER/
│
├── code_cracker.py      # Main script
├── README.md           # This file
└── requirements.txt    # Dependencies
🎯 Quick Start

# Run and follow instructions
python code_cracker.py
🔧 Customization
Adjust these values in the code for different speeds:


pyautogui.write(code, interval=0.02)  # Typing speed
time.sleep(0.3)                       # Processing delay
pyautogui.press('backspace', presses=6, interval=0.01)  # Clear speed
⚠️ مسئولیت استفاده بر عهده کاربر است. تنها برای اهداف آموزشی و تست امنیتی مجاز استفاده شود.

