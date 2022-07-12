'''Some validation tests
'''

SENTENCES_WITH_ENDLINES = '''
HELLO WORLD, MY NAME IS QUAN\n\n
CHEEKY BREEKY V DONKE\n\n\n
'''

CRAZY_SENTENCE = '\n\n\n\n\n'

def test_sending_blank_target(client):
    '''Test sending blank target sentence
    '''
    response = client.post('/score', data = {
        'target_sentence' : '',
        'sentences_list' : SENTENCES_WITH_ENDLINES,
        'threshold' : .5
    })

    assert response.status_code == 400


def test_sending_blank_sentences_list(client):
    '''Test sending blank sentences list
    '''
    response = client.post('/score', data = {
        'target_sentence' : SENTENCES_WITH_ENDLINES,
        'sentences_list' : '',
        'threshold' : .5
    })

    assert response.status_code == 400

def test_sending_with_crazy_input(client):
    '''Test sending crazy input sentences list
    aka sending endlines only.
    '''
    response = client.post('/score', data = {
        'target_sentence' : SENTENCES_WITH_ENDLINES,
        'sentences_list' : CRAZY_SENTENCE,
        'threshold' : .5
    })

    assert response.status_code == 400
