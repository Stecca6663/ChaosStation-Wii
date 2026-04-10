import urllib.request
import json

url = 'https://api.github.com/repos/libertyernie/LoopingAudioConverter/releases'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response:
    data = json.loads(response.read().decode('utf-8'))
for release in data[:5]:
    print(f"Release: {release['tag_name']}")
    for asset in release['assets']:
        print(f"  - {asset['name']}: {asset['browser_download_url']}")
