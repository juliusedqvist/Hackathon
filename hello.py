from flask import Flask
app = Flask(__name__)


@app.route('/<5> <Vallentuna_station> <Kemistvägen_1A>')
def find_alt_travel(walk, startplats, slutdest):

    """ Finds the optimal path based on walktime, start and stop dest """

    vallentuna_teg1 = {'walk': "5", 'starttid': 751, 'sluttid': 823, 'startplats': 'Vallentuna_station',
                       'avdest': 'Galoppfältet', 'slutdest': 'Kemistvägen_1A'}
    vallentuna_teg2 = {'walk': "10", 'starttid': 751, 'sluttid': 825, 'startplats': 'Vallentuna_station',
                       'avdest': 'Stockholmsvägen', 'slutdest': 'Kemistvägen_1A'}
    vallentuna_teg3 = {'walk': "20", 'starttid': 751, 'sluttid': 825, 'startplats': 'Vallentuna_station',
                       'avdest': 'Tibble', 'slutdest': 'Kemistvägen_1A'}

    routes = [vallentuna_teg1, vallentuna_teg2, vallentuna_teg3]

    for items in range(len(routes)):
        if routes[items]['walk'] == walk and routes[items]['startplats'] == startplats and routes[items]['slutdest'] == slutdest:
            return routes[items]
