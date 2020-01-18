#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests

def Obtenir_prix_essence():
    send_url = "http://public.opendatasoft.com/api/records/1.0/search//?dataset=prix_des_carburants_j_7&lang=fr&rows=1&sort=price_sp98&facet=price_sp98&refine.cp=49120&timezone=Europe%2FParis"
    r = requests.get(send_url)
    j = json.loads(r.text)

    prix_sp_98 = j["records"][0]["fields"]["price_sp98"]
    print(prix_sp_98)


if __name__ == "__main__":
    Obtenir_prix_essence()
#>>1.559
