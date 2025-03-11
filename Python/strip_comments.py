def strip_comments(text, markers):
    lines = text.split('\n')
    cleaned_lines = []
    
    for line in lines:
        for marker in markers:
            line = line.split(marker)[0]  # Keep only text before the marker
        cleaned_lines.append(line.rstrip())  # Remove trailing spaces
    
    return '\n'.join(cleaned_lines)
