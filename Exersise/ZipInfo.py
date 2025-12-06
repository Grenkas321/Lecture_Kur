import sys, io, re, zipfile

hex_dump = sys.stdin.read()
hex_bytes = bytes.fromhex(re.sub(r'[^0-9A-Fa-f]', '', hex_dump))

with zipfile.ZipFile(io.BytesIO(hex_bytes)) as zf:
    count_f = 0
    total = 0
    for info in zf.infolist():
        is_dir = info.is_dir() if hasattr(info, "is_dir") else info.filenameendswith("/")
        if not is_dir:
            count_f += 1
            total += info.file_size

print(f"{count_f} {total}")