# OTP CRACKER - 6 Digit Code Brute Forcer ⚡

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![PyAutoGUI](https://img.shields.io/badge/PyAutoGUI-automate-green)
![Status](https://img.shields.io/badge/status-active-brightgreen)
![License](https://img.shields.io/badge/license-MIT-yellow)

A fast and efficient **6-digit OTP brute force tool** using keyboard & mouse automation.  
Perfect for testing websites or apps that use 6 separate input boxes for one-time passwords (common in Iranian banks, 2FA pages, etc.).

**Warning**: Use only on systems or websites you own or have explicit permission to test. Unauthorized brute-force attacks are illegal.

---

### Features
- Super fast code testing (~3 codes per second)
- Resume from last tested code
- Start/Stop with hotkeys (`Shift+T` / `Shift+Y`)
- Auto-clear fields using Backspace
- Live counter in console
- Simple & lightweight (only 2 dependencies)

---

### Requirements
```bash
pip install pyautogui keyboard

How to Use

Open the target website/app with 6 separate digit input boxes
Run the script
Click on the first input box with your mouse
Press Shift + T to start cracking
Press Shift + Y to stop anytime

The script will automatically:

Type the 6-digit code
Press Enter
Wait a moment
Clear all 6 fields with Backspace
Continue with next code...

From 000000 → 999999

Hotkeys

time.sleep(0.3)  # ← change this value (0.5, 1.0, etc.)
If there is no requirements.txt, add only the libraries you need for simulation.

Responsible Disclosure & Ethics

Do not use this code to access accounts or systems you don't own or don't have permission to test.

If you discover a real vulnerability, follow an established responsible disclosure process for the affected vendor or service.

Keep logs and evidence of authorization for any security testing.

Contributing (ethical contributions only)

Contributions are welcome only if they promote defensive research, education, or otherwise improve security posture. Suggested contributions:

Example safe lab (HTML + server) that demonstrates concepts without threatening real services.

Documentation on mitigation strategies (rate-limiting, MFA best-practices).

Unit tests and example simulation scripts.

License

This repository is distributed under the MIT license. See LICENSE for details.

Contact / Questions

If you are a legitimate security researcher and want to collaborate on defensive research or an authorized test, open an issue or contact the repository owner with written authorization details.



██████╗ ████████╗██████╗      ██████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
██╔═══██╗╚══██╔══╝██╔══██╗    ██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██║   ██║   ██║   ██████╔╝    ██║     ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
██║   ██║   ██║   ██╔═══╝     ██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
╚██████╔╝   ██║   ██║         ╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
 ╚═════╝    ╚═╝   ╚═╝          ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
ابزار حرفه‌ای و فوق سریع برای تست خودکار کدهای ۶ رقمی (مثل رمز دوم پویا بانک‌ها، سامانه‌های ثنا، صیاد و...)
ویژگی‌های خفن 🔥

سرعت بالا (حدود ۳ کد در ثانیه)
ادامه از آخرین کد تست‌شده
شروع و توقف با کلید میانبر
پاک‌سازی خودکار فیلدها
نمایش زنده کد فعلی
فقط ۲ تا کتابخونه نیاز داره!


نصب پیش‌نیازها

<code>pip install pyautogui keyboard<code/>

نحوه استفاده 📝

سایت یا برنامه‌ای که ۶ تا کادر جدا داره رو باز کن
اسکریپت رو اجرا کن
با موس روی اولین کادر کلیک کن
کلیدهای Shift + T رو بزن → شروع میشه!
هر وقت خواستی Shift + Y بزن → می‌ایسته

همه‌چیز خودکار انجام میشه:

تایپ کد → اینتر → صبر کوتاه → پاک کردن ۶ تا فیلد → کد بعدی...

از 000000 تا 999999
کلیدهای میانبر 🎮

هشدار مهم ⚠️
این ابزار فقط برای تست قانونی و مجاز (مثل تست سیستم خودتون) ساخته شده.
استفاده غیرمجاز = غیرقانونی و پیگرد قانونی داره.
توسعه‌دهنده هیچ مسئولیتی در قبال سوءاستفاده نداره.

ساخته شده با ❤️ توسط lil-MoS




















کلیدکارShift + Tشروع کرکShift + Yتوقف کرکCtrl + Cخروج کامل از برنامه
تنظیم سرعت ⏱️
اگه سایت کند بود یا بلاکت کرد، این خط رو تغییر بده:


















HotkeyActionShift + TStart crackingShift + YStop crackingCtrl + CExit program

Speed Adjustment
If the website is slow or blocks you, increase the delay here:

