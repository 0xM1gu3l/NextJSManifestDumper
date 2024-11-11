import requests

def test_source_maps(url, jsfile):
    r = requests.get(f"https://{url}/_next/{jsfile}.map")
    if (r.status_code == 200 and r.text[0] == "{"):
        return True
    else:
        return False