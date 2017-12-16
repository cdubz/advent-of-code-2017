def move(positions, movements):
    for movement in movements:
        move, partners = movement[0], movement[1:]
        if move == 's':
            positions = list(positions[-int(partners):]) + \
                        list(positions[0:-int(partners)])
        elif move == 'x':
            key1, key2 = partners.split('/')
            partner1 = positions[int(key1)]
            positions[int(key1)] = positions[int(key2)]
            positions[int(key2)] = partner1
        elif move == 'p':
            partner1, partner2 = partners.split('/')
            key1, key2 = positions.index(partner1), positions.index(partner2)
            positions[key1] = partner2
            positions[key2] = partner1
    return positions
