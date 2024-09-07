import requests as r
import json
import os
from colorama import Fore

page_url = input("Enter the NextJS page URL: ").split("/")[2]
base_url = f"https://{page_url}/_next"
manifest = json.loads(open("buildManifest.json", "r").read())


for page in manifest:
    if page == "sortedPages" or page == "__rewrites": continue
    for file in manifest[page]:
        print(f"Downloading {file.split('/')[-1]}")
        if (page == "/"):
            if not os.path.exists(f"out/main_slash"):
                os.makedirs(f"out/main_slash")
            f = r.get(f"{base_url}/{file}")
            if f.status_code == 200:
                print(Fore.GREEN, "Success!", Fore.WHITE)
            else:
                print(Fore.RED, "Error!", Fore.WHITE)
            with open(f"out/main_slash/{file.split('/')[-1]}", "w+") as wf:
                wf.write(f.text)
                wf.close()
        else:
            if not os.path.exists(f"out{page}"):
                os.makedirs(f"out{page}")
            f = r.get(f"{base_url}/{file}")
            if f.status_code == 200:
                print(Fore.GREEN, "Success!", Fore.WHITE)
            else:
                print(Fore.RED, "Error!", Fore.WHITE)
            with open(f"out{page}/{file.split('/')[-1]}", "w+") as wf:
                wf.write(f.text)
                wf.close()