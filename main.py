import requests
url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
resp = requests.get(url)
our_hero = {}
max = 0
def search(heroes):
    for hero in resp.json():
        if hero['name'] in heroes:
            powerstats = hero['powerstats']
            intel = powerstats['intelligence']
            our_hero[heroes] = int(intel)

search ('Hulk')
search ('Captain America')
search ('Thanos')
print(our_hero)
for key, value in our_hero.items():
    if value > max:
        max = value
    if value == max:
        best = key
print(best)


