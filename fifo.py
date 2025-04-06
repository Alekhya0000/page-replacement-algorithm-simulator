# fifo.py

def fifo_algorithm(frames, pages):
    memory = []
    page_faults = 0
    output = []
    
    for page in pages:
        if page not in memory:
            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
            page_faults += 1
            output.append(f"Page {page}: Fault -> Memory: {memory}")
        else:
            output.append(f"Page {page}: Hit -> Memory: {memory}")
    
    return output, page_faults
