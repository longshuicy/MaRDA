#!/usr/bin/env python

"""Example extractor based on the clowder code."""

import logging
import os
from pyclowder.extractors import Extractor
import pyclowder.files
import pandas as pd
import matplotlib.pyplot as plt


class TurnsIcExtractor(Extractor):
    """Count the number of characters, words and lines in a text file."""
    def __init__(self):
        Extractor.__init__(self)
        
        self.setup()

        # setup logging for the exctractor
        logging.getLogger('pyclowder').setLevel(logging.DEBUG)
        logging.getLogger('__main__').setLevel(logging.DEBUG)

    def process_message(self, connector, host, secret_key, resource, parameters):

        logger = logging.getLogger(__name__)
        inputfile = resource["local_paths"][0]
        file_id = resource['id']

        # These process messages will appear in the Clowder UI under Extractions.
        connector.message_process(resource, "Loading contents of file...")

        # 3. read data
        original_filename = resource["name"]
        data = pd.read_csv(inputfile)
        
        # scatter plot
        plt.scatter(data['Turns'],data['Ic(A)'])
        plt.xlabel('Turns')
        plt.ylabel('Ic(A)')
        
        # save figure
        figure = os.path.splitext(original_filename)[0] + ".png"
        plt.savefig(figure)
        pyclowder.files.upload_preview(connector, host, secret_key, file_id, figure)
        

if __name__ == "__main__":
    extractor = TurnsIcExtractor()
    extractor.start()
