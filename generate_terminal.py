import urllib.request, json, datetime, os

username = "Tokyo-00"
api_url = f"https://api.github.com/users/{username}/events/public"
latest_commit = "Classified Operation"
repo_name = "Unknown System"

try:
    req = urllib.request.Request(api_url, headers={'User-Agent': 'Mozilla/5.0'})
    data = json.loads(urllib.request.urlopen(req).read().decode())
    for event in data:
        if event['type'] == 'PushEvent':
            latest_commit = event['payload']['commits'][0]['message']
            repo_name = event['repo']['name']
            break
except Exception:
    pass

now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

svg = f"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 250" width="800" height="250">
    <style>
        .bg {{ fill: #0d1117; }}
        .header {{ fill: #161b22; }}
        .text {{ font-family: 'Courier New', monospace; font-size: 15px; fill: #00ff00; }}
        .cmd {{ fill: #39d353; font-weight: bold; }}
        .warn {{ fill: #ff7b72; font-weight: bold; }}
        .cursor {{ animation: blink 1s step-end infinite; fill: #00ff00; }}
        @keyframes blink {{ 50% {{ opacity: 0; }} }}
    </style>
    <rect width="100%" height="100%" rx="10" class="bg" />
    <rect width="100%" height="30" class="header" rx="10" />
    <circle cx="20" cy="15" r="5" fill="#ff5f56" />
    <circle cx="40" cy="15" r="5" fill="#ffbd2e" />
    <circle cx="60" cy="15" r="5" fill="#27c93f" />
    <text x="400" y="20" font-family="monospace" font-size="12" fill="#8b949e" text-anchor="middle">root@cyber_space:~</text>
    <g class="text" transform="translate(20, 60)">
        <text y="0"><tspan class="cmd">root@tokyo-00:~#</tspan> ./init_telemetry.sh</text>
        <text y="25">[+] Secure Connection established at {now}</text>
        <text y="50">[+] Target identity: {username}</text>
        <text y="75">[+] Scanning for recent operations...</text>
        <text y="100">[+] Target System: {repo_name}</text>
        <text y="125" class="warn">[!] LATEST INJECTED PAYLOAD: "{latest_commit}"</text>
        <text y="150">[+] Status: UNDETECTED</text>
        <text y="175"><tspan class="cmd">root@tokyo-00:~#</tspan> _<tspan class="cursor" dy="0" dx="-10">█</tspan></text>
    </g>
</svg>
"""
os.makedirs("dist", exist_ok=True)
with open("dist/live_terminal.svg", "w", encoding="utf-8") as f:
    f.write(svg)
