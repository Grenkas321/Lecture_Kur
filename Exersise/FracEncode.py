import sys

data = sys.stdin.buffer.read()

try:
    sep = data.index(0)
except ValueError:
    sys.exit(0)

text_bytes = data[:sep]
text = text_bytes.decode("utf-8")

frags_bytes = data[sep + 1 :].split(b"\x00")

codecs = ["cp866", "cp1251", "koi8-r", "iso8859_5"]

for frag in frags_bytes:
    if not frag:
        continue

    ok = False
    for enc in codecs:
        try:
            s = frag.decode(enc)
        except UnicodeDecodeError:
            continue
        if s in text:
            ok = True
            break

    print("Yes" if ok else "No")
