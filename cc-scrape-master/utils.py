
def remove_bad_chars(string):
    return string.encode('ascii', 'ignore').decode('ascii')
    #return string.replace('℠', '').replace('+', '').replace('®', '').replace('*', '').replace('™', '').replace('†', '').replace('–', ' ')