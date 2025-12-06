import sys

BOX = {
    ("LIGHT", "LIGHT"): {
        "horiz": "─",
        "vert": "│",
        "tl": "┌",
        "tr": "┐",
        "bl": "└",
        "br": "┘",
        "top_cross": "┬",
        "bot_cross": "┴",
        "mid_left": "├",
        "mid_right": "┤",
        "mid_cross": "┼",
        "up_horiz": "┴",
        "down_horiz": "┬",
    },
    ("LIGHT", "HEAVY"): {
        "horiz": "━",
        "vert": "│",
        "tl": "┍",
        "tr": "┑",
        "bl": "┕",
        "br": "┙",
        "top_cross": "┯",
        "bot_cross": "┷",
        "mid_left": "┝",
        "mid_right": "┥",
        "mid_cross": "┿",
        "up_horiz": "┷",
        "down_horiz": "┯",
    },
    ("HEAVY", "LIGHT"): {
        "horiz": "─",
        "vert": "┃",
        "tl": "┎",
        "tr": "┒",
        "bl": "┖",
        "br": "┚",
        "top_cross": "┰",
        "bot_cross": "┸",
        "mid_left": "┠",
        "mid_right": "┨",
        "mid_cross": "╂",
        "up_horiz": "┸",
        "down_horiz": "┰",
    },
    ("HEAVY", "HEAVY"): {
        "horiz": "━",
        "vert": "┃",
        "tl": "┏",
        "tr": "┓",
        "bl": "┗",
        "br": "┛",
        "top_cross": "┳",
        "bot_cross": "┻",
        "mid_left": "┣",
        "mid_right": "┫",
        "mid_cross": "╋",
        "up_horiz": "┻",
        "down_horiz": "┳",
    },
}

def wrap_words(words, width):
    rows = []
    cur = []
    cur_len = 0
    for w in words:
        if not cur:
            cur = [w]
            cur_len = len(w)
            continue
        k = len(cur)
        area_new = width - (k + 2)
        if cur_len + len(w) <= area_new:
            cur.append(w)
            cur_len += len(w)
        else:
            rows.append(cur)
            cur = [w]
            cur_len = len(w)
    if cur:
        rows.append(cur)
    return rows


def prepare_rows(words, width):
    rows_w = wrap_words(words, width)
    rows = []
    for ws in rows_w:
        k = len(ws)
        area = width - (k + 1) 
        lens = list(map(len, ws))
        pad = area - sum(lens)
        lens[-1] += pad
        bounds = [0]
        for wlen in lens:
            bounds.append(bounds[-1] + wlen + 1)
        rows.append((ws, lens, bounds))
    return rows



text_line = sys.stdin.readline().rstrip("\n")
params = sys.stdin.readline().split()
width = int(params[0])
v_thick = params[1].upper()
h_thick = params[2].upper()

style = BOX[(v_thick, h_thick)]
horiz = style["horiz"]
vert = style["vert"]

words = text_line.split()
rows = prepare_rows(words, width)

out_lines = []

top_bounds = rows[0][2]
bset = set(top_bounds)
line = []
for i in range(width):
    if i in bset:
        if i == 0:
            ch = style["tl"]
        elif i == width - 1:
            ch = style["tr"]
        else:
            ch = style["top_cross"]
    else:
        ch = horiz
    line.append(ch)
out_lines.append("".join(line))

for idx, (ws, lens, bounds) in enumerate(rows):
    line = [" "] * width
    for b in bounds:
        line[b] = vert
    for j, w in enumerate(ws):
        start = bounds[j] + 1
        width_cell = lens[j]
        txt = w.ljust(width_cell)
        line[start:start + width_cell] = txt
    out_lines.append("".join(line))

    if idx < len(rows) - 1:
        next_bounds = rows[idx + 1][2]
        set_up = set(bounds)
        set_dn = set(next_bounds)
        line = []
        for i in range(width):
            up = i in set_up
            down = i in set_dn
            if i == 0:
                if up and down:
                    ch = style["mid_left"]
                elif up:
                    ch = style["bl"]
                elif down:
                    ch = style["tl"]
                else:
                    ch = horiz
            elif i == width - 1:
                if up and down:
                    ch = style["mid_right"]
                elif up:
                    ch = style["br"]
                elif down:
                    ch = style["tr"]
                else:
                    ch = horiz
            else:
                if up and down:
                    ch = style["mid_cross"]
                elif up:
                    ch = style["up_horiz"]
                elif down:
                    ch = style["down_horiz"]
                else:
                    ch = horiz
            line.append(ch)
        out_lines.append("".join(line))

last_bounds = rows[-1][2]
bset = set(last_bounds)
line = []
for i in range(width):
    if i in bset:
        if i == 0:
            ch = style["bl"]
        elif i == width - 1:
            ch = style["br"]
        else:
            ch = style["bot_cross"]
    else:
        ch = horiz
    line.append(ch)
out_lines.append("".join(line))

print("\n".join(out_lines))