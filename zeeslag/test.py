boten_info = {
    "vliegdekschip": {"lengte": 6, "aantal": 1},
    "slagschip": {"lengte": 4, "aantal": 2},
    "onderzeeër": {"lengte": 3, "aantal": 1},
    "patrouilleschip": {"lengte": 2, "aantal": 4}
}

for naam in boten_info:
    lengte = boten_info[naam]["lengte"]
    aantal = boten_info[naam]["aantal"]
    print(lengte, aantal)
    