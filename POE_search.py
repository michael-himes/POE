from timeit import default_timer as timer
import requests
import json
import sys
import os

def search():
    content = []
    iteration = 0
    input_interval = 0
    last_input = 0
    Input_Not_Finshed = True
    while Input_Not_Finshed: 
        if iteration < 4 or input_interval < 0.1:
            line = input()
            if len(content) > 4 and line == '': #Break loop
                Input_Not_Finshed = False
                os.system('cls')
            elif line == 'qq': #Exit condition
                sys.exit() 
            elif line != '':
                input_interval = timer() - last_input
                last_input = timer()
                iteration += 1
                content.append(line)

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
    base = content[2]
    linked = 0
    for element in content:
        if "Sockets" in element:
            linked = element.count('-')
            if linked != 0:
                linked += 1
                data['link_min'] = linked - 1
                data['link_max'] = linked + 1
    print('\n'+name)
    print(base)
    if linked != 0:
        print(linked, "links +/- 1")
    data['name'] = name
    data['base'] = base
    print('\t'+'Searching!')
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
        print('\t'+str(curency[item])+'\t'+item)
    print('\n'+'\t'+response.url+'\n') # i needs space

while True:
    search()
