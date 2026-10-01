import subprocess
import time
import pyautogui
import datetime

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1

# 1️⃣ Launch Chrome directly with a default profile
subprocess.Popen(
    r'"C:\Program Files\Google\Chrome\Application\chrome.exe" --profile-directory="Default"'
)

# 2️⃣ Wait for Chrome to open
time.sleep(3)

# 3️⃣ Open a new tab
pyautogui.hotkey('ctrl', 't')

# 4️⃣ Navigate to the news channel website
pyautogui.write('https://www.bbc.com/news')
pyautogui.press('enter')

# 5️⃣ Wait for the website to load fully
time.sleep(6)

# 6️⃣ Select all content on the page
pyautogui.hotkey('ctrl', 'a')
time.sleep(1)

# 7️⃣ Copy the selected content
pyautogui.hotkey('ctrl', 'c')
time.sleep(1)

# 8️⃣ Open Excel
pyautogui.press('win')
pyautogui.write('excel')
pyautogui.press('enter')

# 9️⃣ Wait for Excel to fully load
time.sleep(6)

# 🔟 Ensure Excel is in workbook mode (sometimes Excel opens in backstage mode)
# Press ESC twice to close any popups or backstage screens
pyautogui.press('esc')
time.sleep(1)
pyautogui.press('esc')
time.sleep(1)

# 1️⃣1️⃣ Create a new blank workbook (if Excel opened in Home screen)
pyautogui.hotkey('ctrl', 'n')
time.sleep(3)

# 1️⃣2️⃣ Ensure the first cell is selected
pyautogui.hotkey('ctrl', 'home')
time.sleep(1)

# 1️⃣3️⃣ Paste the copied news content into Excel
pyautogui.hotkey('ctrl', 'v')
time.sleep(3)

# 1️⃣4️⃣ Save the Excel file with today's date
today = datetime.datetime.now().strftime("%Y-%m-%d")
filename = f"today_news_dump_{today}"

pyautogui.hotkey('ctrl', 's')
time.sleep(2)

# 1️⃣5️⃣ Type the filename and save
pyautogui.write(filename)
pyautogui.press('enter')

print("News copied and saved to Excel successfully.")