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
        'values':[
            ('happens', 21),
            ('drifts out of sync with the', 22),
            ('might', 23)
        ]
    },
    21: {
        'values':[
            ('earlier', 24),
            ('later', 24),
            ('at the wrong time', 24)
        ]
    },
    22: {
        'values': [
            ('sun', 40),
            ('moon', 40),
            ('Zodiac', 40),
            ('Gregorian', 25),
            ('Mayan', 25),
            ('Lunar', 25),
            ('iPhone', 25),
            ('atomic clock in Colorado', 40),
        ]
    },
    23: {
        'values': [
            ('not happen', 26),
            ('happen twice', 26),
        ]
    },
    24: {
        'values': [('every year', 40)]
    },
    25: {
        'values': [('calendar', 40)]
    },
    26: {
        'values': [('this year', 40)]
    },

    40: {
        'values': [('because of', 41)]
    },
    41: {
        'values': [
            ('time zone legislation in', 42),
            ('a decree by the pope in the 1500s', 60),
            ('precession', 43),
            ('libration', 43),
            ('nutation', 43),
            ('libation', 43),
            ('ecentricity', 43),
            ('obliquity', 43),
            ('magnetic field reversal', 60),
            ('an arbitrary decision by', 44)

        ]
    },
    42: {
        'values': [
            ('Indiana', 60),
            ('Arizona', 60),
            ('Russia', 60)
        ]
    },
    43: {
        'values': [('of the', 45)]
    },
    44: {
        'values': [
            ('Benjamin Franklin', 60),
            ('Isaac Newton', 60),
            ('FDR', 60)
        ]
    },
    45: {
        'values': [
            ('Moon', 60),
            ('Sun', 60),
            ('Earth\'s axis', 60),
            ('equator', 60),
            ('prime meridian', 60),
            ('international date', 46),
            ('Mason-Dixon', 46)
        ]
    },
    46: {
        'values': [('line', 60)]
    },

    60: {
        'values': [('', 61)],
        'punctuation': '?'
    },
    61: {
        'values': [('Apparently', 62)]
    },
    62: {
        'values': [
            ('it causes a predicatble increase in car accidents', 80),
            ('that\'s why we have leap seconds', 80),
            ('scientists are really worried', 80),
            ('it was even more extreme during the', 63),
            ('there\'s a proposal to fix it, but it', 64),
            ('it\'s getting worse and no one knows why', 80)
        ]
    },
    63: {
        'values': [
            ('Bronze Age', 80),
            ('Ice Age', 80),
            ('Cretaceous', 80),
            ('1990s', 80)
        ]
    },
    64: {
        'values': [
            ('will never happen', 80),
            ('actually makes things worse', 80),
            ('is stalled in congress', 80),
            ('might be unconstitutional', 80)
        ]
    },

    80: {
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
