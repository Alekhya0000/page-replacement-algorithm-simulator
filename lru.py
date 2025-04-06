# lru.py

def lru_algorithm(frames, pages):
    memory = []
    page_faults = 0
    output = []
    recent = []  # Tracks order of use
    
    for page in pages:
        if page not in memory:
            if len(memory) < frames:
                memory.append(page)
            else:
                lru_page = recent.pop(0)
                memory.remove(lru_page)
                memory.append(page)
            page_faults += 1
            output.append(f"Page {page}: Fault -> Memory: {memory}")
        else:
            recent.remove(page)
            output.append(f"Page {page}: Hit -> Memory: {memory}")
        recent.append(page)
    
    return output, page_faults
