import os
import urllib.request

domains = [
    "peoplesbank.lk", "masholdings.com", "muncheelk.com", "jatholdings.com", 
    "accessengsl.com", "gallefacehotel.com", "godrej.com", "softlogic.lk", 
    "lionbeer.com", "pizzahut.lk", "tacobell.lk", "aia.com", "malibanbiscuit.com",
    "bureauveritas.com", "watersedge.lk", "cic.lk"
]

output_dir = "assets/clients/downloaded"
os.makedirs(output_dir, exist_ok=True)

valid_logos = []

for domain in domains:
    url = f"https://logo.clearbit.com/{domain}"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                with open(f"{output_dir}/{domain}.png", "wb") as f:
                    f.write(response.read())
                valid_logos.append(f"{domain}.png")
                print(f"Downloaded: {domain}")
    except Exception as e:
        print(f"Failed: {domain} - {e}")

print(f"Total downloaded: {len(valid_logos)}")
with open("valid_logos.txt", "w") as f:
    f.write(",".join(valid_logos))
