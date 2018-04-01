import random
from nGramModel import *


class BigramModel(NGramModel):
    
    def trainModel(self, text):
        """
            Requires: text is a list of lists of strings
            Modifies: self.nGramCounts, a two-dimensional dictionary. For examples
            and pictures of the BigramModel's version of
            self.nGramCounts, see the spec.
            Effects:  this function populates the self.nGramCounts dictionary,
            which has strings as keys and dictionaries of
            {string: integer} pairs as values.
            """
        for sentence in text:
            for i in range(len(sentence)-1):
                if sentence[i] not in self.nGramCounts:
                    self.nGramCounts[sentence[i]] = {}
                if sentence[i+1] not in self.nGramCounts[sentence[i]]:
                    self.nGramCounts[sentence[i]][sentence[i+1]] = 0
                self.nGramCounts[sentence[i]][sentence[i+1]] += 1
        return self.nGramCounts
        pass
    
    def trainingDataHasNGram(self, sentence):
        """
            Requires: sentence is a list of strings, and len(sentence) >= 1
            Modifies: nothing
            Effects:  returns True if this n-gram model can be used to choose
            the next token for the sentence. For explanations of how this
            is determined for the BigramModel, see the spec.
            """
        if sentence[-1] in self.nGramCounts:
            return True
        else:
            return False
        
        
        
        pass
    
    def getCandidateDictionary(self, sentence):
        """
            Requires: sentence is a list of strings, and trainingDataHasNGram
            has returned True for this particular language model
            Modifies: nothing
            Effects:  returns the dictionary of candidate next words to be added
            to the current sentence. For details on which words the
            BigramModel sees as candidates, see the spec.
            """
        return self.nGramCounts[sentence[-1]]
        pass

###############################################################################
# Main
###############################################################################

if __name__ == '__main__':
    # Add your test cases here
    text = [['I', 'AM', 'LSA', 'STUDENT'],['LET','US', 'GO', 'I', 'BLUE']]
    print text
    sentence = ['GO', 'LSA', 'I', 'GO']
    bigramModel = BigramModel()
    print bigramModel.trainModel(text)
    print bigramModel.trainingDataHasNGram(sentence)
    print bigramModel.getCandidateDictionary(sentence)

    
