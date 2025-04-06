# optimal.py

def optimal_algorithm(frames, pages):
    memory = []
    page_faults = 0
    output = []
    
    for i, page in enumerate(pages):
        if page not in memory:
            if len(memory) < frames:
                memory.append(page)
            else:
                future = pages[i+1:]
                replace = memory[0]
                max_dist = -1
                for m in memory:
                    try:
                        dist = future.index(m)
                    except ValueError:
                        dist = float('inf')
                    if dist > max_dist:
                        max_dist = dist
                        replace = m
                memory[memory.index(replace)] = page
                page_faults += 1
                output.append(f"Page {page}: Fault -> Memory: {memory}")
        else:
            output.append(f"Page {page}: Hit -> Memory: {memory}")
    
    return output, page_faults
