from typing import List
from plumber.components.resolvers.base import BaseResolver
from plumber.components.format import Chain
import requests


HMTL_URL = 'http://localhost:11111/jmd/'


class HMTLResolver(BaseResolver):
    def __init__(self, name: str = 'Dummy Resolver', **kwargs):
        super().__init__(name, **kwargs)

    def get_coreference_chains(self, text: str) -> List[Chain]:
        payload = "{\"text\": \""+text+"\"}"
        headers = {
            'accept': 'application/json',
            'content-type': 'application/json'
        }

        response = requests.request("POST", HMTL_URL, headers=headers, data=payload)

        content = response.json()
        chains = []
        for coref_arc in content['coref_arcs']:
            chain = Chain(coref_arc['text1'])
            chain.add_alias(coref_arc['text2'],
                            coref_arc['mention2_begin_char'],
                            coref_arc['mention2_end_char'],
                            text)
            chains.append(chain)
        return chains


if __name__ == '__main__':
    resolver = HMTLResolver()
    x = resolver.get_coreference_chains('Rembrandt painted The Storm on the Sea of Galilee. It was painted in 1633.')
