def get_trunk(responses):
    for program, response in dict(responses).items():
        for child in response.get('children'):
            if child in responses:
                del responses[child]
    return list(responses)[0]
