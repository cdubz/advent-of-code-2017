def get_weight(program, responses):
    weight = responses[program]['weight']
    for child in responses[program]['children']:
        weight += get_weight(child, responses)
    return weight
