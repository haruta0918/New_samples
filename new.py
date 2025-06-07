import json
json_open = open('samples/20250415_165815.jpg.supplemental-metadata.json', 'r')
json_load = json.load(json_open)
print(json_load['geoData']['latitude'])
print(json_load['geoData']['longitude'])