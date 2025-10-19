import sys

data = sys.stdin.read()
parts = data.split('\n\n', 1)

words_text = parts[0]
program_text = parts[1] if len(parts) > 1 else ""

words = words_text.split()
sets = {'ALL': set(words)}

lines = program_text.splitlines()
for line in lines:
    line = line.strip()
    if not line:
        continue
        
    parts = line.split()
    if parts[0] == 'print':
        set_names = parts[1].split(',')
        result_set = set()
        for name in set_names:
            if name in sets:
                result_set.update(sets[name])
        sorted_list = sorted(result_set)
        print(' '.join(sorted_list))
            
    elif parts[0] == 'search':
        if 'where' in parts:
            idx_where = parts.index('where')
            idx_to = parts.index('to')
            source_names = parts[1].split(',')
            search_string = parts[idx_where + 1]
            result_name = parts[idx_to + 1]
            
            source_set = set()
            for name in source_names:
                if name in sets:
                    source_set.update(sets[name])
            
            result_set = {word for word in source_set if search_string in word}
            sets[result_name] = result_set
            
        elif 'for' in parts:
            idx_for = parts.index('for')
            idx_to = parts.index('to')
            source_names = parts[1].split(',')
            search_names = parts[idx_for + 1].split(',')
            result_name = parts[idx_to + 1]
            
            source_set = set()
            for name in source_names:
                if name in sets:
                    source_set.update(sets[name])
            
            search_set = set()
            for name in search_names:
                if name in sets:
                    search_set.update(sets[name])
            
            result_set = source_set & search_set
            sets[result_name] = result_set