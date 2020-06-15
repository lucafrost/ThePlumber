from typing import List
from auko.components.clients.stanford import StanfordClient
from auko.components.extractors.base import StanfordBasedExtractor
from auko.components.format import Triple


class OpenIEExtractor(StanfordBasedExtractor):

    def __init__(self, **kwargs):
        kwargs['key'] = 'openie'
        super().__init__(name='Open IE extractor', **kwargs)

    def get_triples(self, text) -> List[Triple]:
        response = self.client.openie(text, simple_format=False)
        return self.transform_triples(response['sentences'], text)
