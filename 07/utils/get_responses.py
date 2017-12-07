import re


def get_responses():
    responses = {}
    with open('input.txt') as f:
        for line in f:
            result = re.search('(?P<program>[a-z]+) \((?P<weight>\d+)\)( -> )?'
                               '(?P<children>[a-z, ]+)?', line.strip())

            program = result.group('program')
            responses[program] = {
                'weight': int(result.group('weight')),
                'children': []
            }
            if result.group('children'):
                responses[program].update({
                    'children': result.group('children').split(', ')
                })
    return responses
