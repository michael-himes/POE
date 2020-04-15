from timeit import default_timer as timer
import requests
import json


start =  timer()
content = []
iteration = 0
interval = 0
last = 0
while True:
    if iteration < 4 or interval < 0.1 :
        line = input()
        interval = timer() - last
        last = timer()
        iteration += 1
        content.append(line)
    #if line == 'qq':
    #    break
    else:
        break

cookies = {
    '_ga': 'GA1.2.1454003851.1584649422',
    '__qca': 'P0-1838013029-1584649422698',
    '__gads': 'ID=cddbdb8d500fcb86:T=1584649426:S=ALNI_MY2_uIdaxoqOeNrip3jgAR9xyA7Qw',
    'league': 'Delirium',
    'CRISPSUBNO': '3c6f0bc0d631048ac3b3a4e2ffa2be34',
    '_gid': 'GA1.2.151124699.1586906311',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Origin': 'https://poe.trade',
    'Upgrade-Insecure-Requests': '1',
    'Content-Type': 'application/x-www-form-urlencoded',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    'Sec-Fetch-Dest': 'document',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Referer': 'https://poe.trade/search/ehamewaritanoh',
    'Accept-Language': 'en-US,en;q=0.9',
}

data = {
  'league': 'Delirium',
  'type': '',
  'base': '',
  'name': 'Carrion Spiker',
  'dmg_min': '',
  'dmg_max': '',
  'aps_min': '',
  'aps_max': '',
  'crit_min': '',
  'crit_max': '',
  'dps_min': '',
  'dps_max': '',
  'edps_min': '',
  'edps_max': '',
  'pdps_min': '',
  'pdps_max': '',
  'armour_min': '',
  'armour_max': '',
  'evasion_min': '',
  'evasion_max': '',
  'shield_min': '',
  'shield_max': '',
  'block_min': '',
  'block_max': '',
  'sockets_min': '',
  'sockets_max': '',
  'link_min': '',
  'link_max': '',
  'sockets_r': '',
  'sockets_g': '',
  'sockets_b': '',
  'sockets_w': '',
  'linked_r': '',
  'linked_g': '',
  'linked_b': '',
  'linked_w': '',
  'rlevel_min': '',
  'rlevel_max': '',
  'rstr_min': '',
  'rstr_max': '',
  'rdex_min': '',
  'rdex_max': '',
  'rint_min': '',
  'rint_max': '',
  'mod_name': '',
  'mod_min': '',
  'mod_max': '',
  'mod_weight': '',
  'group_type': 'And',
  'group_min': '',
  'group_max': '',
  'group_count': '1',
  'q_min': '',
  'q_max': '',
  'level_min': '',
  'level_max': '',
  'ilvl_min': '',
  'ilvl_max': '',
  'rarity': '',
  'progress_min': '',
  'progress_max': '',
  'sockets_a_min': '',
  'sockets_a_max': '',
  'map_series': '',
  'altart': '',
  'identified': '',
  'corrupted': '',
  'crafted': '',
  'enchanted': '',
  'fractured': '',
  'synthesised': '',
  'mirrored': '',
  'veiled': '',
  'shaper': '',
  'elder': '',
  'crusader': '',
  'redeemer': '',
  'hunter': '',
  'warlord': '',
  'seller': '',
  'thread': '',
  'online': 'x',
  'capquality': 'x',
  'buyout_min': '',
  'buyout_max': '',
  'buyout_currency': '',
  'has_buyout': '',
  'exact_currency': ''
}
name = content[1]
print(name)
data['name'] = name

response = requests.post('https://poe.trade/search', headers=headers, cookies=cookies, data=data)

curency = {}
for line in response.text.split('\n'):
    if "data-buyout" in line:
        value = line.split('=')[1]
        if value not in curency:
            curency[value] = 1
        else:
            curency[value] += 1
for item in curency:
    print('\t',curency[item],'\t',item)
