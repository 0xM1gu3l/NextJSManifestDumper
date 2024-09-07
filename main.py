import requests as r
import json
import os
from colorama import Fore

page_url = input("Enter the NextJS page URL: ").split("/")[2]
base_url = f"https://{page_url}/_next"
manifest = json.loads(open("buildManifest.json", "r").read())
file_qty = 0
i = 1

for page in manifest:
    if page == "sortedPages" or page == "__rewrites": continue
    file_qty += len(manifest[page])

for page in manifest:
    if page == "sortedPages" or page == "__rewrites": continue
    for file in manifest[page]:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Downloading {file.split('/')[-1]} {i}/{file_qty}")
        if (page == "/"):
            if not os.path.exists(f"out/{page_url}/main_slash"):
                os.makedirs(f"out/{page_url}/main_slash")
            f = r.get(f"{base_url}/{file}")
            if f.status_code == 200:
                print(f"{Fore.GREEN}Success!{Fore.WHITE}")
            else:
                print(f"{Fore.GREEN}Error!{Fore.WHITE}")
                input("Press ENTER to continue...")
            with open(f"out/{page_url}/main_slash/{file.split('/')[-1]}", "w+") as wf:
                wf.write(f.text)
                wf.close()
        else:
            if not os.path.exists(f"out/{page_url}{page}"):
                os.makedirs(f"out/{page_url}{page}")
            f = r.get(f"{base_url}/{file}")
            if f.status_code == 200:
                print(f"{Fore.GREEN}Success!{Fore.WHITE}")
            else:
                print(f"{Fore.GREEN}Error!{Fore.WHITE}")
                input("Press ENTER to continue...")
            with open(f"out/{page_url}{page}/{file.split('/')[-1]}", "w+") as wf:
                wf.write(f.text)
                wf.close()
        i += 1