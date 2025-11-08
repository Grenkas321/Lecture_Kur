from collections import OrderedDict
from typing import Iterable, Iterator, List, Tuple

class Spiral:

    def __init__(self, s_or_groups: Iterable[str] | List[Tuple[str, int]]):
        if isinstance(s_or_groups, str):
            od = OrderedDict()
            for ch in s_or_groups:
                od[ch] = od.get(ch, 0) + 1
            self._groups: List[Tuple[str, int]] = list(od.items())
        else:
            self._groups = [(ch, int(cnt)) for ch, cnt in s_or_groups if int(cnt) > 0]

    def _expanded(self) -> str:
        return "".join(ch * cnt for ch, cnt in self._groups)

    @staticmethod
    def _render_increasing_segments(s: str) -> str:
        if not s:
            return ""
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        x = y = 0
        d = 0
        seg = 1
        pts: List[Tuple[int, int, str]] = []
        i, n = 0, len(s)
        while i < n:
            for _ in range(seg):
                if i >= n:
                    break
                pts.append((x, y, s[i]))
                dx, dy = dirs[d & 3]
                x += dx; y += dy
                i += 1
            d += 1
            seg += 1

        xs = [x for x, _, _ in pts]
        ys = [y for _, y, _ in pts]
        xmin, xmax = min(xs), max(xs)
        ymin, ymax = min(ys), max(ys)
        w, h = xmax - xmin + 1, ymax - ymin + 1
        grid = [[' '] * w for _ in range(h)]
        for x, y, ch in pts:
            grid[ymax - y][x - xmin] = ch
        return "\n".join("".join(row) for row in grid)

    def __str__(self) -> str:
        return self._render_increasing_segments(self._expanded())

    def __repr__(self) -> str:
        return f"Spiral({self._groups!r})"

    def __add__(self, other: "Spiral") -> "Spiral":
        if not isinstance(other, Spiral):
            return NotImplemented
        od = OrderedDict(self._groups)
        for ch, cnt in other._groups:
            od[ch] = od.get(ch, 0) + cnt
        return Spiral(list(od.items()))

    def __sub__(self, other: "Spiral") -> "Spiral":
        if not isinstance(other, Spiral):
            return NotImplemented
        od = OrderedDict(self._groups)
        for ch, cnt in other._groups:
            if ch in od:
                new_cnt = od[ch] - cnt
                if new_cnt > 0:
                    od[ch] = new_cnt
                else:
                    del od[ch]
        return Spiral(list(od.items()))

    def __mul__(self, n: int) -> "Spiral":
        if not isinstance(n, int) or n < 1:
            raise ValueError("Множитель должен быть натуральным числом (n >= 1).")
        return Spiral([(ch, cnt * n) for ch, cnt in self._groups])

    __rmul__ = __mul__

    def __iter__(self) -> Iterator[str]:
        for ch, cnt in self._groups:
            for _ in range(cnt):
                yield ch

    def groups(self) -> List[Tuple[str, int]]:
        return list(self._groups)

    def __len__(self) -> int:
        return sum(cnt for _, cnt in self._groups)
