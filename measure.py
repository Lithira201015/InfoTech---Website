from PIL import Image

files = [
    r'C:\Users\INFOTECH ADMIN\.gemini\antigravity\brain\ce9a5681-afbc-4334-96cf-e54cd79724bd\media__1774848676306.png',
    r'C:\Users\INFOTECH ADMIN\.gemini\antigravity\brain\ce9a5681-afbc-4334-96cf-e54cd79724bd\media__1774848689059.png',
    r'C:\Users\INFOTECH ADMIN\.gemini\antigravity\brain\ce9a5681-afbc-4334-96cf-e54cd79724bd\media__1774848698936.png'
]
for f in files:
    img = Image.open(f)
    print(f, img.size)
