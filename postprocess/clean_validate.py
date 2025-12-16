def clean_data(data):
    cleaned = {}
    for k, v in data.items():
        cleaned[k] = v.strip().replace("\n", " ")
    return cleaned
