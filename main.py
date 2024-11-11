import requests as r
import os
from scripts.getBuildManifest import get_build_manifest
from scripts.testSourceMaps import test_source_maps
from colorama import Fore

sourcemap = False
page_url = input("Enter the NextJS page URL (with https://): ").split("/")[2]
base_url = f"https://{page_url}/_next"
manifest = get_build_manifest(f"https://{page_url}")
file_qty = 0
i = 1

ans = input("Wanna test if the website has source maps exposed? [y/n]: ")
if (ans == 'Y' or ans == 'y'):
    has_sourcemap = test_source_maps(page_url, manifest["/"][0])
    if (has_sourcemap):
        print("Website HAS exposed Source Maps!")
        sourcemap = True
        print(sourcemap)
    else: 
        print("Website does not contain exposed source maps... Continuing with js file only...")
    input("Press ENTER to continue...")
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
            if sourcemap:
                f = r.get(f"{base_url}/{file}.map")
            else:
                f = r.get(f"{base_url}/{file}")
            if f.status_code == 200:
                print(f"{Fore.GREEN}Success!{Fore.WHITE}")
            else:
                print(f"{Fore.GREEN}Error!{Fore.WHITE}")
                input("Press ENTER to continue...")
            if sourcemap:
                with open(f"out/{page_url}/{file.split('/')[-1]}.map", "w+") as wf:
                    wf.write(f.text)
                    wf.close()
            else:
                with open(f"out/{page_url}/main_slash/{file.split('/')[-1]}", "w+") as wf:
                    wf.write(f.text)
                    wf.close()
        else:
            if not os.path.exists(f"out/{page_url}{page}"):
                os.makedirs(f"out/{page_url}{page}")
            print(f"{base_url}/{file}")
            if sourcemap:
                f = r.get(f"{base_url}/{file}.map")
            else:
                f = r.get(f"{base_url}/{file}")
            if f.status_code == 200:
                print(f"{Fore.GREEN}Success!{Fore.WHITE}")
            else:
                print(f"{Fore.GREEN}Error!{Fore.WHITE}")
                input("Press ENTER to continue...")
            if sourcemap:
                with open(f"out/{page_url}/{file.split('/')[-1]}.map", "w+") as wf:
                    wf.write(f.text)
                    wf.close()
            else:
                with open(f"out/{page_url}{page}/{file.split('/')[-1]}", "w+") as wf:
                    wf.write(f.text)
                    wf.close()
        i += 1