from timeit import default_timer as timer
import requests
import json


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
    else:
        break

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
print() # i needs space
name = content[1]
base = content[2]
for element in content:
    if "Sockets" in element:
        linked = element.count('-')
        if linked != 0:
            linked += 1
            data['link_min'] = linked - 1
            data['link_max'] = linked + 1
print(name)
print(base)
print(linked, "links +/- 1")
data['name'] = name
data['base'] = base

response = requests.post('https://poe.trade/search',  data=data)

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
print() # i needs space
print(response.url)
