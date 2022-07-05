from flask_restful import Resource

from .sbert import SBERT
from .utils import get_input

class Pipeline(Resource):
    def __init__(self) -> None:
        self.__sbert_instance = SBERT('sentence-transformers/all-MiniLM-L6-v2')
    
    @staticmethod
    def preprocess(input_str : str) -> list:
        splitted_input = input_str.split('\n')

        if len(splitted_input) == 1:
            return [].append(input_str)
        
        return splitted_input

    def post(self):
        try:
            target_sentence = get_input('target_sentence')
            sentences_list = Pipeline.preprocess(get_input('sentences_list'))
            threshold_max = float(get_input('threshold_max'))

        except AssertionError as e:
            return {
                'error' : True,
                'error_field' : str(e)
            }, 400
        
        target_embedding = self.__sbert_instance.sentence_embedding(target_sentence)
        sentences_list_embedding = self.__sbert_instance.list_embedding(sentences_list)
        predictions = self.__sbert_instance.sentence_list_similarity(target_embedding, sentences_list_embedding)

        response_dict = dict()
        for index in range(len(sentences_list)):
            response_dict[index] = {
                "sentence" : sentences_list[index],
                "score" : str(predictions[index]),
                "similar" : True if predictions[index] >= threshold_max else False,
            }

        return {
            'error' : False,
            'response_dict' : response_dict,
        }, 200