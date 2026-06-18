import math

def haversine(lat1, lon1, lat2, lon2):
    R = 3958.7613  # miles
    p1, p2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlam = math.radians(lon2 - lon1)
    a = math.sin(dphi/2)**2 + math.cos(p1)*math.cos(p2)*math.sin(dlam/2)**2
    return 2*R*math.asin(math.sqrt(a))

# Part A extracted profile
current = ("Dallas, TX", 32.7767, -96.7970)   # "I'm in Dallas"
home    = ("San Antonio, TX", 29.4241, -98.4936)  # "based out in San Antonio"
min_rpm = 2.00   # "As long as it's above $2 per mile"
equip   = {"Hotshot", "Gooseneck"}  # "I run a hotshot gooseneck trailer"
weight_cap = 14200  # heaviest he discusses comfortably; gooseneck hotshot class

loads = [
    ("L01","Fort Worth",32.7555,-97.3308,"Oklahoma City",35.4676,-97.5164,"Van",42000.0,620.0),
    ("L02","Houston",29.7604,-95.3698,"Laredo",27.5306,-99.4803,"Hotshot",11500.0,1600.0),
    ("L03","Austin",30.2672,-97.7431,"Corpus Christi",27.8006,-97.3964,"Gooseneck",14200.0,1500.0),
    ("L04","Plano",33.0198,-96.6989,"Memphis",35.1495,-90.0490,"Van",38000.0,1500.0),
    ("L05","Waco",31.5493,-97.1467,"San Antonio",29.4241,-98.4936,"Flatbed",9800.0,640.0),
    ("L06","Shreveport",32.5252,-93.7502,"Atlanta",33.7490,-84.3880,"Van",46500.0,None),
    ("L07","Tulsa",36.1540,-95.9928,None,None,None,"Hotshot",13400.0,1100.0),
    ("L08","Dallas",32.7767,-96.7970,"McAllen",26.2034,-98.2300,"Hotshot",12600.0,1700.0),
]

print(f"{'ID':4}{'eff_rpm':>9}  {'reason'}")
results = []
for (lid,o,olat,olon,d,dlat,dlon,tr,wt,pr) in loads:
    reasons = []
    if pr is None: reasons.append("missing price")
    if dlat is None: reasons.append("missing destination")
    if tr not in equip: reasons.append(f"trailer {tr} not run")
    if wt > weight_cap: reasons.append(f"weight {wt:.0f}>cap")
    if reasons:
        print(f"{lid:4}{'--':>9}  REJECT: {', '.join(reasons)}")
        continue
    dh_o = haversine(current[1],current[2],olat,olon)
    loaded = haversine(olat,olon,dlat,dlon)
    dh_h = haversine(dlat,dlon,home[1],home[2])
    total = dh_o+loaded+dh_h
    eff = pr/total
    elig = eff >= min_rpm
    tag = "OK" if elig else f"eff {eff:.3f}<min"
    print(f"{lid:4}{eff:9.3f}  {tag}  (dh_o {dh_o:.0f}+loaded {loaded:.0f}+dh_h {dh_h:.0f}={total:.0f})")
    if elig:
        results.append((lid,round(eff,3)))

print("\nTOP 3:")
for r,(lid,eff) in enumerate(sorted(results,key=lambda x:-x[1])[:3],1):
    print(f"{r}. {lid}  {eff:.3f}")
