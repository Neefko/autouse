from flask import Flask, request
import pyautogui
import subprocess
import webbrowser
import socket
import smtplib

app = Flask(__name__)


pyautogui.FAILSAFE = False

@app.route('/send', methods=['POST'])
def send_data():
    data = request.json
    action = data.get('zero')

    if action == 'chrome':
        subprocess.call(r'C:\Program Files\Google\Chrome\Application\chrome.exe')

    elif action == 'explorer':
        subprocess.call(r'C:\Windows\explorer.exe', shell=True)

    elif action == 'volpl':
        pyautogui.press('volumeup')

    elif action == 'volmn':
        pyautogui.press('volumedown')

    elif action == 'pycharm':
        subprocess.call(r'C:\Program Files\JetBrains\PyCharm Community Edition 2024.2.2\bin\pycharm64.exe')

    elif action == 'vpn':
        subprocess.call(
            r'C:\Program Files\WindowsApps\FreeVPNPlanet.PlanetVPN_2.9.1.0_x64__b2qrq2z57ppd2\PlanetVPN.exe')

    elif action == 'gmail':
        webbrowser.open('https://mail.google.com/mail/u/0/#inbox', new=2)

    elif action == 'calcul':
        subprocess.call(r'C:\Windows\System32\calc.exe')

    elif action == 'lkm':
        pyautogui.mouseDown(button='left')
        pyautogui.mouseUp(button='left')

    elif action == 'pkm':
        pyautogui.mouseDown(button='right')
        pyautogui.mouseUp(button='right')

    elif action == 'up':
        pyautogui.press('up')

    elif action == 'down':
        pyautogui.press('down')

    elif action == 'left':
        pyautogui.press('left')

    elif action == 'right':
        pyautogui.press('right')

    return {'status': 'success'}


@app.route('/update_mouse', methods=['POST'])
def update_mouse():
    data = request.json
    action = data.get('action')

    if action == 'move':
        x = data.get('x')
        y = data.get('y')
        pyautogui.move(x * 1.5, y * 1.5)

    elif action == 'click':
        pyautogui.click()

    elif action == 'scroll':
        delta = data.get('delta')
        if isinstance(delta, (int, float)):
            clicks = int(delta * 10)  # Приводим к целому числу
            if clicks == 0:
                return {'status': 'success'}
            else:
                pyautogui.scroll(clicks)

    return {'status': 'success'}
@app.route('/links', methods=['POST'])
def open_links():
    data = request.json
    link = data.get('link')
    webbrowser.open(link, new=2)
    return {'status': 'success'}

def my_local_ip():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.connect(("8.8.8.8", 80))  # Google DNS
        local_ip = sock.getsockname()[0]

        with open("email.txt", "r") as email:
            em = email.readline()
            passw = email.readlines()[-1]

        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.starttls()
        smtp_server.login(em, passw)
        smtp_server.sendmail(em, em, local_ip)
        smtp_server.quit()

        return local_ip



if __name__ == '__main__':
    app.run(host=my_local_ip(), port=5000)