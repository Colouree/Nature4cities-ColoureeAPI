

import requests
import json
import argparse

parser = argparse.ArgumentParser(description='Call API test _python2_ script.')

parser.add_argument('-t', '--token', help='Your quite secret token', required=True)

args = parser.parse_args()

project = json.dumps({"type":"FeatureCollection","features":[{"type":"Feature","properties":{"landuse":"green_area"},"geometry":{"type":"Polygon","coordinates":[[[-3.372867,40.482438],[-3.373039,40.481981],[-3.372685,40.481899],[-3.372492,40.482234],[-3.372867,40.482438]]]}},{"type":"Feature","properties":{"building":"yes","height":3},"geometry":{"type":"Polygon","coordinates":[[[-3.37203,40.483046],[-3.372256,40.482573],[-3.371821,40.482413],[-3.371365,40.482826],[-3.37203,40.483046]]]}}]})

lon, lat = -3.372264335328447, 40.48248638141262

pilot_city = 'alcala_de_henares'

kpi = 'accessibility'

response = requests.post('https://app.colouree.com/n4c/api/kpi.json/{kpi}/{pilot_city}'.format(**vars()), data=dict(
    lon=lon, lat=lat, project=project,
    assessment='both', percentages='[]',
        token = args.token
))

print response.text
