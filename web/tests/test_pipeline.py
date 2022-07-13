'''Some validation tests
'''

EXAMPLE_TARGET_SENTENCE = 'Hello, my name is Quan'

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
        'threshold_max' : .5
    })

    assert response.status_code == 400

    assert response.json["error"] is True

    assert response.json["error_field"] == 'target_sentence'


def test_sending_blank_sentences_list(client):
    '''Test sending blank sentences list
    '''
    response = client.post('/score', data = {
        'target_sentence' : EXAMPLE_TARGET_SENTENCE,
        'sentences_list' : '',
        'threshold_max' : .5
    })

    assert response.status_code == 400

    assert response.json["error"] is True

    assert response.json["error_field"] == 'sentences_list'

def test_sending_with_crazy_input(client):
    '''Test sending crazy input sentences list
    aka sending endlines only.
    '''
    response = client.post('/score', data = {
        'target_sentence' : EXAMPLE_TARGET_SENTENCE,
        'sentences_list' : CRAZY_SENTENCE,
        'threshold_max' : .5
    })

    assert response.status_code == 400

    assert response.json["error"] is True

    assert response.json["error_field"] == 'sentences_list'

def test_sending_with_crazy_but_valid_input(client):
    '''Sending crazy but valid input
    aka sentences separated with minimum 1 endline.
    '''
    response = client.post('/score', data = {
        'target_sentence' : EXAMPLE_TARGET_SENTENCE,
        'sentences_list' : SENTENCES_WITH_ENDLINES,
        'threshold_max' : .5
    })

    # Ensure nothing wrong happened.
    assert response.status_code == 200

    # Only 2 records should be available in response.
    assert len(response.json["response_dict"]) == 2
