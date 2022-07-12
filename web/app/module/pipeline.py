'''Backend API
'''

from flask_restful import Resource

from .sbert import SBERT
from .utils import get_input

class Pipeline(Resource):
    '''Backend API resource for the demo
    '''

    def __init__(self) -> None:
        '''Initialise SBERT instance
        '''
        self.__sbert_instance = SBERT('sentence-transformers/all-MiniLM-L6-v2')

    @staticmethod
    def preprocess(input_str : str) -> list:
        '''Splitting a string to list of strings with endline as determiner.
        '''

        # input_str.splitlines returns a list with '\n' converted as blank string,
        # using filter to remove them.
        splitted_input = list(filter(lambda x : len(x) > 0, input_str.splitlines()))
        return splitted_input

    def post(self):
        '''Handling POST method.
        '''
        try:
            target_sentence = get_input('target_sentence')
            sentences_list = Pipeline.preprocess(get_input('sentences_list'))
            threshold_max = float(get_input('threshold_max'))

        except AssertionError as error_field:
            return {
                'error' : True,
                'error_field' : str(error_field)
            }, 400

        # Convert target sentence to vector
        target_embedding = self.__sbert_instance.sentence_embedding(target_sentence)

        # Convert sentences list to vector
        sentences_list_embedding = self.__sbert_instance.list_embedding(sentences_list)

        # Get predictions from vector list.
        predictions = self.__sbert_instance.sentence_list_similarity(
            target_embedding, sentences_list_embedding
        )

        response_dict = {}
        for index, value in enumerate(sentences_list):
            response_dict[index] = {
                "sentence" : value,
                "score" : str(predictions[index]),
                "similar" : bool(predictions[index] >= threshold_max),
            }

        return {
            'error' : False,
            'response_dict' : response_dict,
        }, 200
