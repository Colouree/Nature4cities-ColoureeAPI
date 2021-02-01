import requests
import json
import argparse

parser = argparse.ArgumentParser(description='Call API test _python2_ script.')

parser.add_argument('-t', '--token', help='Your quite secret token', required=True)

args = parser.parse_args()

project = json.dumps({"type":"FeatureCollection","features":[{"id":"b45d83d4dc1021f5ae336411a0b99338","type":"Feature","properties":{"landuse":"green_land"},"geometry":{"coordinates":[[[20.155196014211725,46.25157926225671],[20.15740566288136,46.25043724508555],[20.163130396887766,46.25373932879842],[20.162103974398775,46.25471590356162],[20.155196014211725,46.25157926225671]]],"type":"Polygon"}}]})

# WARNING! You must specify a coordinates inside the pilot city area you ask for!
lon, lat = -3.372264335328447, 40.48248638141262   # Alcala De Henares
# lon, lat = 20.156300838546542, 46.25100825367113 # Szeged

pilot_city = 'alcala_de_henares'

kpi = 'areal_sprawl'

response = requests.post('https://app.colouree.com/n4c/api/kpi.json/{kpi}/{pilot_city}'.format(**vars()), data=dict(
    lon=lon, lat=lat, project=project,
    assessment='both', percentages='[]',
        token = args.token
))

print response.text
