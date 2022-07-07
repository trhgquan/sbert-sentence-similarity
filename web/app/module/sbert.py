'''SBERT module
'''

from transformers import AutoTokenizer, AutoModel
import torch
import torch.nn.functional as F

class SBERT:
    '''SBERT, but impemented as an OOP class.
    '''

    def __init__(self, model_name):
        '''Load tokenizer and model from available pre-trained
        '''
        self.__tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.__model = AutoModel.from_pretrained(model_name)

    @staticmethod
    def mean_pooling(model_output, attention_mask):
        '''Mean pooling: take attention mask into account for correct averaging
        '''
        token_embeddings = model_output[0]
        input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()

        torch_sum = torch.sum(token_embeddings * input_mask_expanded, 1)
        torch_clamp = torch.clamp(input_mask_expanded.sum(1), min = 1e-9)

        return torch_sum / torch_clamp

    @staticmethod
    def sentence_similarity(first_sentence_vector, second_sentence_vector):
        '''Calculate similarity between two sentence representations
        '''
        cos_similarity = F.cosine_similarity(first_sentence_vector, second_sentence_vector).numpy()
        return cos_similarity[0]

    @staticmethod
    def sentence_list_similarity(source_sentence_vector, sentence_vector_list):
        '''Calculate similarity between a source sentence and a list of sentences,
        Then return the similarity scores as a list.
        '''
        similarity_list = []

        for vector in sentence_vector_list:
            similarity_list.append(SBERT.sentence_similarity(source_sentence_vector, vector))

        return similarity_list

    def list_embedding(self, sentence_list) -> list:
        '''Using SBERT to encode a list of sentences.
        '''
        embedded_sentences = []

        for sentence in sentence_list:
            embedded_sentences.append(self.sentence_embedding(sentence))

        return embedded_sentences

    def sentence_embedding(self, sentence):
        '''Using SBERT to encode a sentence.
        '''
        encoded_input = self.__tokenizer(
            sentence,
            padding = True,
            truncation = True,
            return_tensors = 'pt'
        )

        with torch.no_grad():
            model_output = self.__model(**encoded_input)

        sentence_embeddings = SBERT.mean_pooling(model_output, encoded_input['attention_mask'])
        sentence_embeddings = F.normalize(sentence_embeddings, p = 2, dim = 1)

        return sentence_embeddings
