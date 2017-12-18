from random import randint

END_INDEX = 100

allOptions = {
    0: {
        'values': [('Did you know that', 1)],
        'punctuation': ''
    },
    1: {
        'values': [
            ('the', 2),
            ('the', 3),
            ('the', 4),
            ('daylight', 5),
            ('leap', 6),
            ('easter', 20),
            ('the', 8),
            ('toyota truck month', 20),
            ('shark week', 20)
        ]
    },
    2: {
        'values': [
            ('fall', 11),
            ('spring', 11)
        ]
    },
    3: {
        'values': [
            ('winter', 12),
            ('summer', 12)
        ]
    },
    4: {
        'values': [
            ('earliest', 13),
            ('latest', 13)
        ]
    },
    5: {
        'values': [
            ('saving', 14),
            ('savings', 14)
        ]
    },
    6: {
        'values': [
            ('day', 20),
            ('year', 20)
        ]
    },
    8: {
        'values': [('the', 15)]
    },

    11: {
        'values': [('equinox', 20)]
    },
    12: {
        'values': [
            ('solstice', 20),
            ('olympics', 20)
        ]
    },
    13: {
        'values': [
            ('sunrise', 20),
            ('sunset', 20)
        ]
    },
    14: {
        'values': [('time', 20)]
    },
    15: {
        'values': [
            ('harvest', 16),
            ('super', 16),
            ('blood', 16)
        ]
    },
    16: {
        'values': [('moon', 20)]
    },
    20: {
        'values':[('')],
        'end': True,
        'punctuation': '.'
    }
}


def main():
    print(recurseValues(allOptions[0]))

def recurseValues(obj):
    if 'end' in obj:
        return obj['punctuation'];
    index = randint(0, len(obj['values']) - 1)
    string, next = obj['values'][index];
    return getPunctuation(obj) + string + recurseValues(allOptions[next])

def getPunctuation(obj):
    if 'punctuation' in obj:
        return obj['punctuation']
    return ' '

if __name__ == "__main__":
    main()
