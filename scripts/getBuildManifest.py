from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
# import time

def get_build_manifest(url):
    print(url)
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(f"{url}")
    # time.sleep(3)
    build_manifest = driver.execute_script("return __BUILD_MANIFEST")
    driver.close()
    return json.loads(str(build_manifest).replace("'", '"'))