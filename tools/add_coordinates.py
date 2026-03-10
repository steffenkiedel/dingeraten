#!/usr/bin/env python3
"""Add lat/lng to existing Länder and Hauptstädte items."""
import json, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(BASE, 'data')

# Country centroids (approximate)
LAENDER_COORDS = {
    'deutschland':    (51.2, 10.5),
    'frankreich':     (46.2,  2.2),
    'spanien':        (40.4, -3.7),
    'italien':        (42.8, 12.6),
    'grossbritannien':(54.0, -2.0),
    'usa':            (38.0,-97.0),
    'china':          (35.9,104.2),
    'indien':         (20.6, 79.0),
    'brasilien':      (-10.0,-51.9),
    'australien':     (-25.3,133.8),
    'russland':       (61.5, 90.0),
    'kanada':         (56.1,-106.3),
    'japan':          (36.2,138.3),
    'mexiko':         (23.6,-102.5),
    'suedafrika':     (-29.0, 25.0),
    'argentinien':    (-38.4,-63.6),
    'nigeria':        (10.0,  8.0),
    'aegypten':       (26.8, 30.8),
    'saudioarabien':  (23.9, 45.1),
    'tuerkei':        (38.9, 35.2),
    'indonesia':      (-0.8,113.9),
    'pakistan':       (30.4, 69.3),
    'thailand':       (15.9,100.9),
    'schweiz':        (46.8,  8.2),
    'oesterreich':    (47.5, 14.5),
    'niederlande':    (52.1,  5.3),
    'portugal':       (39.4, -8.2),
    'griechenland':   (39.1, 21.8),
}

# Capital city coordinates
HAUPTSTAEDTE_COORDS = {
    'berlin':       (52.5, 13.4),
    'paris':        (48.9,  2.3),
    'london':       (51.5, -0.1),
    'rom':          (41.9, 12.5),
    'madrid':       (40.4, -3.7),
    'tokio':        (35.7,139.7),
    'washington':   (38.9,-77.0),
    'ottawa':       (45.4,-75.7),
    'canberra':     (-35.3,149.1),
    'nairobi':      (-1.3, 36.8),
    'wien':         (48.2, 16.4),
    'amsterdam':    (52.4,  4.9),
    'stockholm':    (59.3, 18.1),
    'bern':         (46.9,  7.4),
    'athen':        (38.0, 23.7),
    'peking':       (39.9,116.4),
    'moskau':       (55.8, 37.6),
    'kairo':        (30.1, 31.2),
    'brasilia':     (-15.8,-47.9),
    'buenos_aires': (-34.6,-58.4),
    'seoul':        (37.6,126.9),
    'reykjavik':    (64.1,-21.9),
}

def add_coords(filepath, coords_map):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    updated = 0
    for item in data:
        if item['id'] in coords_map and 'lat' not in item:
            lat, lng = coords_map[item['id']]
            item['lat'] = lat
            item['lng'] = lng
            updated += 1
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return updated

n = add_coords(os.path.join(DATA, 'laender.json'), LAENDER_COORDS)
print(f"laender.json: {n} items updated with coordinates")

n = add_coords(os.path.join(DATA, 'hauptstaedte.json'), HAUPTSTAEDTE_COORDS)
print(f"hauptstaedte.json: {n} items updated with coordinates")
print("Done!")
