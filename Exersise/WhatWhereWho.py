from graphlib import TopologicalSorter, CycleError

class _MROError(Exception):
    pass

def _merge(seqs):
    out = []
    seqs = [list(s) for s in seqs if s]
    while seqs:
        for s in seqs:
            head = s[0]
            if not any(head in tail[1:] for tail in seqs):
                break
        else:
            raise _MROError
        out.append(head)
        ns = []
        for t in seqs:
            if t and t[0] == head:
                t.pop(0)
            if t:
                ns.append(t)
        seqs = ns
    return out

def _lin(name, plans, cache, visiting):
    if name in cache:
        return cache[name]
    if name in visiting:
        raise _MROError
    visiting.add(name)
    bases = plans[name]
    lin_bases = [_lin(b, plans, cache, visiting) for b in bases]
    visiting.remove(name)
    res = [name] + _merge(lin_bases + [bases[:]])
    cache[name] = res
    return res

def solve():
    import sys
    lines = []
    for line in sys.stdin:
        line = line.rstrip("\n")
        if line == "":
            break
        lines.append(line)

    plans = {}
    order = []
    for line in lines:
        if ":" not in line:
            print("UNKNOWN")
            return
        who, rest = line.split(":", 1)
        who = who.strip()
        order.append(who)
        asks = [x.strip() for x in rest.split(",") if x.strip()] if rest.strip() else []
        plans[who] = asks

    known = set(plans)
    for asks in plans.values():
        for a in asks:
            if a not in known:
                print("UNKNOWN")
                return

    ts = TopologicalSorter()
    for who, asks in plans.items():
        ts.add(who, *asks)
    try:
        _ = list(ts.static_order())
    except CycleError:
        print("CYCLE")
        return

    cache = {}
    try:
        for who in order:
            _ = _lin(who, plans, cache, set())
    except _MROError:
        print("INEFFECTIVE")
        return

    out = []
    for who in order:
        seq = cache[who][1:]
        out.append(f"{who}: {', '.join(seq)}" if seq else f"{who}: ")
    print("\n".join(out))

solve()
