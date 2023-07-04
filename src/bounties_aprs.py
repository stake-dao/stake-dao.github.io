import json
import requests
from utils.write_file import write_file

API_URL = "https://votemarket.stakedao.org/api/bribes/aprs"
OUTPUT_FILE_PATH = "out/bounties/aprs/index.json"

r = requests.get(API_URL)
write_file(OUTPUT_FILE_PATH, "w", json.dumps(r.json()))
