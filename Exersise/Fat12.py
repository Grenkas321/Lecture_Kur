import sys

data = sys.stdin.buffer.read()

bytes_per_sector = int.from_bytes(data[11:13], "little")
sectors_per_cluster = data[13]
reserved_sectors = int.from_bytes(data[14:16], "little")
num_fats = data[16]
max_root_entries = int.from_bytes(data[17:19], "little")
sectors_per_fat = int.from_bytes(data[22:24], "little")

root_dir_sectors = (max_root_entries * 32 + bytes_per_sector - 1) // bytes_per_sector
root_dir_start_sector = reserved_sectors + num_fats * sectors_per_fat
root_dir_offset = root_dir_start_sector * bytes_per_sector
root_dir_size = root_dir_sectors * bytes_per_sector

root = data[root_dir_offset: root_dir_offset + root_dir_size]

entries = []

for i in range(0, max_root_entries * 32, 32):
    entry = root[i:i+32]
    if len(entry) < 32:
        break

    first_byte = entry[0]
    if first_byte == 0x00:
        break
    if first_byte == 0xE5:
        continue

    attr = entry[11]

    if (attr & 0x0F) == 0x0F:
        continue

    if (attr & 0x08) and not (attr & 0x10):
        continue

    is_dir = (attr & 0x10) != 0

    name_raw = entry[0:8]
    ext_raw = entry[8:11]

    name = name_raw.decode("cp866", "replace").rstrip()
    ext = ext_raw.decode("cp866", "replace").rstrip()

    if not name:
        continue

    if ext:
        full_name = f"{name}.{ext}"
    else:
        full_name = name

    size = int.from_bytes(entry[28:32], "little")

    entries.append((full_name, is_dir, size))

entries.sort(key=lambda x: x[0])

for full_name, is_dir, size in entries:
    left = f"{full_name:12}"
    right = "dir" if is_dir else str(size)
    print(f"{left} {right}")
