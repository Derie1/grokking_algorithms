from breadth_first_search import bf_search


def test_bf_search():
    graph = {}
    graph['me'] = ['Alex', 'Tom_designer', 'Elena_IT']
    graph['Alex'] = ['John', 'Jane']
    graph['Tom_designer'] = ['Colin', 'Max', 'Rupert_dude']
    graph['Elena_IT'] = ['Susanne', 'Tom_car_seller']
    graph['John'] = []
    graph['Jane'] = []
    graph['Colin'] = []
    graph['Max'] = []
    graph['Rupert_dude'] = []
    graph['Susanne'] = []
    graph['Tom_car_seller'] = []

    assert bf_search('me', graph) == True
    assert bf_search('Alex', graph) == False
    assert bf_search('Elena_IT', graph) == True