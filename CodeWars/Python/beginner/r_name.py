
# Create a function which answers the question "Are you playing banjo?". 

def are_you_playing_banjo(name):
    # Implement me!
    analize_name = name.lower()
    
    if analize_name[0] == 'r':
        analize_name = f'{name} plays banjo'
    
    else:
        analize_name = f'{name} does not play banjo'
    
    return analize_name