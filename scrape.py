import json, requests, re, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

EPIC_URL = "https://store.epicgames.com/en-US"
EPIC_API = "https://www.cheapshark.com/api/1.0/deals?storeID=25"
PS_PLUS_URL = "https://store.playstation.com/en-us/view/25d9b52a-7dcf-11ea-acb6-06293b18fe04/bc428b4a-f1b7-11ea-aadc-062143ad1e8d"
AMZ_PRI_URL = "https://gaming.amazon.com/home"
STEAM_API = "https://www.cheapshark.com/api/1.0/deals?storeID=1"
GOG_API = "https://www.cheapshark.com/api/1.0/deals?storeID=7"
# 1: Steam, 7: GoG, and 25: Epic Games

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")



data = []

#driver = webdriver.Chrome()
driver = webdriver.Chrome(options=options)
#time.sleep(3)
#
#try:
#    print("[SYSTEM]: Selenium running on Epic Games.")
#    driver.get(EPIC_URL)
#    driver.implicitly_wait(5)
#    epic_games_section = driver.find_element(By.CLASS_NAME, "css-1myhtyb")
#    epic_games = epic_games_section.find_elements(By.CLASS_NAME, "css-g3jcms")
#    for epic_game in epic_games:
#        epic_game_link = epic_game.get_attribute("href")
#        epic_game_title = epic_game.find_element(By.CSS_SELECTOR, ".eds_1ypbntd0.eds_1ypbntd7.eds_1ypbntdq").text
#        #epic_game_title = re.sub(r'[^a-zA-Z0-9\s]', '', epic_game_title)
#        #epic_game_title = epic_game_title.replace("  ", " ")
#        #epic_game_title = re.sub(r'\s+', " ", epic_game_title)
#        epic_game_id = epic_game_link.replace("https://store.epicgames.com/en-US/p/", "").strip().lower()
#        epic_game_img = epic_game.find_element(By.TAG_NAME, "img").get_attribute("data-image")
#        epic_game_status = epic_game.find_element(By.CSS_SELECTOR, ".css-82y1uz, .css-gyjcm9").text.strip().replace(" ", "_").lower()
#    
#        if epic_game_status == "free_now":
#            data.append({"title": epic_game_title, "id": epic_game_id, "img": epic_game_img, "link": epic_game_link, "market": "epic_games"})
#
#except Exception:
#    print("[SYSTEM]: Selenium has FAILED on Epic Games.")


time.sleep(3)
offset = 1


try:
    print("[SYSTEM]: Selenium running on PlayStation.")
    driver.get(PS_PLUS_URL)
    driver.implicitly_wait(5)
    ps_plus_games_section = driver.find_element(By.CSS_SELECTOR, ".psw-strand.psw-l-anchor.psw-clip.psw-with-medium-items")
    ps_plus_games = ps_plus_games_section.find_elements(By.CSS_SELECTOR, ".psw-link.psw-content-link");
    for ps_plus_game in ps_plus_games:
        ps_plus_game_link = ps_plus_game.get_attribute("href")
        ps_plus_game_id = ps_plus_game_link.replace("https://store.playstation.com/en-us/product/", "").strip().lower()
        ps_plus_game_img = ps_plus_game.find_element(By.XPATH, "/html/body/div[3]/main/div/div/div[2]/section/div/div[1]/ul/li[" + str(offset) + "]/div/a/div/div/div[1]/span[2]/img[2]").get_attribute("src")
        ps_plus_game_title = ps_plus_game.find_element(By.XPATH, "/html/body/div[3]/main/div/div/div[2]/section/div/div[1]/ul/li[" + str(offset) + "]/div/a/div/section/span").text
        #ps_plus_game_title = re.sub(r'[^a-zA-Z0-9\s]', "", ps_plus_game_title)
        #ps_plus_game_title = ps_plus_game_title.replace("  ", " ")
        #ps_plus_game_title = re.sub(r'\s+', " ", ps_plus_game_title)
        data.append({"title": ps_plus_game_title, "id": ps_plus_game_id, "img": ps_plus_game_img, "link": ps_plus_game_link, "market": "playstation"})
        offset+=1
    
except Exception:
    print("[SYSTEM]: Selenium has FAILED on PlayStation.")


time.sleep(3)


try:
    print("[SYSTEM]: Selenium running on Prime Gaming.")
    driver.get(AMZ_PRI_URL)
    driver.implicitly_wait(5)
    #prime_games_section = driver.find_element(By.CLASS_NAME, "grid-carousel__content")
    #prime_games = prime_games_section.find_elements(By.CLASS_NAME, "grid-carousel__slide");
    prime_games_section = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/main/div/div/div/div[4]/div[1]/div/div[2]/div/div/div[1]/div[1]/div/div/ul")
    prime_games = prime_games_section.find_elements(By.TAG_NAME, "li");

    for prime_game in prime_games:
        prime_game_link = prime_game.find_element(By.TAG_NAME, "a").get_attribute("href")
        prime_game_id = prime_game_link.replace("https://gaming.amazon.com/", "").strip().lower()
        end_char = prime_game_id.index("/")
        prime_game_id = prime_game_id[:end_char]
        prime_game_img = "https://m.media-amazon.com/images/G/01/sm/shared/166979982420469/social_image._CB409110150_.jpg"
        prime_game_title = prime_game.find_element(By.TAG_NAME, "a").get_attribute("aria-label")
        data.append({"title": prime_game_title, "id": prime_game_id, "img": prime_game_img, "link": prime_game_link, "market": "amazon"})
    
except Exception:
    print("[SYSTEM]: Selenium has FAILED on Prime Gaming.")


time.sleep(1)
driver.close()


try:
    print("[SYSTEM]: Fetching Epic API...")
    response = requests.get(EPIC_API)
    epic_data = response.json()
    for game in epic_data:
        if float(game["salePrice"]) == 0 and float(game["savings"]) == 100:
        #if float(game["salePrice"]) > 0:
            epic_game_id = game["steamAppID"]
            epic_game_link = "http://store.steampowered.com/app/" + str(epic_game_id) + "/"
            data.append({"title": game["title"], "id": epic_game_id, "img": game["thumb"], "link": epic_game_link, "market": "epic_games"})

except Exception:
    print("[SYSTEM]: Failed to fetch Epic API...")


try:
    print("[SYSTEM]: Fetching Steam API...")
    response = requests.get(STEAM_API)
    steam_data = response.json()
    for game in steam_data:
        if float(game["salePrice"]) == 0 and float(game["savings"]) == 100:
        #if float(game["salePrice"]) > 0:
            steam_game_id = game["steamAppID"]
            steam_game_link = "http://store.steampowered.com/app/" + str(steam_game_id) + "/"
            data.append({"title": game["title"], "id": steam_game_id, "img": game["thumb"], "link": steam_game_link, "market": "steam"})

except Exception:
    print("[SYSTEM]: Failed to fetch Steam API...")
    

try:
    print("[SYSTEM]: Fetching GOG API...")
    response = requests.get(GOG_API)
    gog_data = response.json()
    for game in gog_data:
        if float(game["salePrice"]) == 0 and float(game["savings"]) == 100:
        #if float(game["salePrice"]) > 0:
            gog_game_id = re.sub(r'[^a-zA-Z0-9\s]', '', game["title"])
            #gog_game_id = gog_game_id.strip().replace("  ", " ").lower()
            #gog_game_id = gog_game_id.replace(" ", "_")
            ##gog_game_id = gog_game_id.strip().replace(" ", "_").lower()
            gog_game_id = re.sub(r'\s+', '_', gog_game_id)
            gog_game_link = "https://www.gog.com/en/game/" + str(gog_game_id) + "/"
            data.append({"title": game["title"], "id": gog_game_id, "img": game["thumb"], "link": gog_game_link, "market": "gog"})

except Exception:
    print("[SYSTEM]: Failed to fetch GOG API...")


print("[SYSTEM]: Scraping is complete.")
with open("./src/resources/data.json", "w") as file:
    json.dump(data, file, indent=4)
