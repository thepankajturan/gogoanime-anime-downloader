
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
import subprocess
from pathlib import Path
import json


# Loading data from data.json
data = json.loads(Path("data.json").read_text())


# INPUTS

# Credentials : retrieveing from data.json file
username = data["username"]
password = data["password"]

# Anime info input
anime_name = input("Enter Anime Name: ")
quality_of_ep = int(input(
    "Enter quality of episodes (choose 1, 2, 3, 4):\n 1. 360p \n 2. 480p \n 3. 720p \n 4. 1080p ")) + 1

number_of_episodes = int(input("Enter No. of episodes to download: "))


# Disabling Images for faster loading of webpage

firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference('permissions.default.image', 2)
firefox_profile.set_preference(
    'dom.ipc.plugins.enabled.libflashplayer.so', 'false')

browser = webdriver.Firefox(firefox_profile=firefox_profile)


# Installing Addon (Ad Blocker) for faster loading and less congestion on the webpage
# path_to_extensions retrieved from data.json
browser.install_addon(data["path_to_extensions"])


browser.get("https://gogoanime.lu/login.html")
browser.maximize_window()


# Logging In
email_box = browser.find_element_by_xpath(
    "/html/body/div[2]/div/div/section/section[1]/div/div[2]/div/form/input[2]")
email_box.send_keys(username)

password_box = browser.find_element_by_xpath(
    "/html/body/div[2]/div/div/section/section[1]/div/div[2]/div/form/input[3]")
password_box.send_keys(password)

sign_in_button = browser.find_element_by_xpath(
    "/html/body/div[2]/div/div/section/section[1]/div/div[2]/div/form/button")
sign_in_button.click()


# Searching for anime
search_box = browser.find_element_by_id("keyword")
search_box.send_keys(f"{anime_name}" + Keys.RETURN)

time.sleep(4)


# Selecting anime after search : select Dub or Sub
anime_link = browser.find_element_by_css_selector(
    f".name > a[title='{anime_name}']")
anime_link.click()

# Scrolling into view
browser.execute_script("window.scrollTo(0, 150)")


# Selecting Ep01 link from Episode index
episode_index = browser.find_element_by_css_selector(
    "ul#episode_related > li:last-child > a")
episode_index.click()

time.sleep(2)


# Looping for the required number of episodes

episode_link_list = []


def download_link_grabber():
    for i in range(number_of_episodes):

        # Scrolling into view
        browser.execute_script("window.scrollTo(0, 350)")

        # Selecting the quality
        episode_link = browser.find_element_by_css_selector(
            f"div.cf-download > a:nth-child({quality_of_ep})")
        # episode_link.click()

        # Appending to the link's list
        episode_link_list.append(episode_link.get_attribute("href"))

        time.sleep(2)

        next_episode_dl = browser.find_element_by_xpath(
            "/html/body/div[2]/div/div/section/section[1]/div[1]/div[2]/div[4]/div[2]/a")
        next_episode_dl.click()

        time.sleep(1)


download_link_grabber()

# Writing links to a txt file

with open(f"{anime_name}_links.txt", "w") as file:
    for link in episode_link_list:
        file.write(link + "\n")


# Printing links just to make sure

print(episode_link_list)
browser.quit()

#
for link in episode_link_list:
    i = 1
    subprocess.call(["wget", "-v", f"-O {anime_name}_ep{i}.mp4", f"{link}"])
    i += 1
