
'''
    This class will process the evaluation of the story based on the method
    proposed in the paper. Here where we will utilize all neccessary tools such
    as BertProcessor and other utills
'''
from bert.BertProcessor import BertProcessor
from utills.EntityRemoverUtill import EntityRemoverUtill
from utills.SentenceUtill import SentenceUtill
from utills.StopWordUtill import StopWordsUtill
from utills.VectorUtill import VectorUtill
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.spatial import distance

class StoryQualityEvaluator:

    def __init__(self):
        # bert processor
        self.bert = BertProcessor()
        # stopwords utils to remove stop words on each sentence
        # will do the sentence processing prior to utilizing this util
        self._STOP_WORD_UTILL = StopWordsUtill()
        # sentence utils for extracting the sentences from the paragraph
        self._SENTENCE_UTIL = SentenceUtill()
        # entity remover utill
        self._ENTITY_REMOVER_UTILL = EntityRemoverUtill()
        # vector utils
        self._VECTOR_UTILL = VectorUtill();
        # batch
        self._bertComputedSentences = []

    def initiateBertProcess(self, story):

        if len(story) == 0:
            return

        ## perform sentence breaking
        sentenceList = self._SENTENCE_UTIL.extractSentencesFromParagraph(story)
        ## clear the bertComputedSentences
        self._bertComputedSentences = []

        ## we need to process three sentences at a time
        index = 0
        sentenceIndex = 0

        while index < len(sentenceList):
            rawBatchList = sentenceList[index:index+3]
            nonEntityBatchList = self._ENTITY_REMOVER_UTILL.removeEntities(rawBatchList)
            nonStopWordBatchList = self._removeStopWordsForBatch(nonEntityBatchList)
            self.bert.process(nonStopWordBatchList)
            wordVectorList = self.bert.getWordVectorListByBatch()
            self._appendComputedBatches(rawBatchList, nonStopWordBatchList, nonEntityBatchList, wordVectorList)
            index = index + 3

    def computeMovingCosineSimilarity(self):

        ## start from second sentence
        sentenceIndex = 1

        ## add all vectors in the first sentence
        sumVector = []
        # wordVectorList = self._bertComputedSentences[1]["vector_values"]
        meanDivider = 1
        meanVector = []
        # for wordVector in wordVectorList:
        #     ## get the vector
        #     keys = wordVector.keys()
        #     for key in keys:
        #         sumVector = self._VECTOR_UTILL.performVectorArthimetic(sumVector, wordVector[key], "ADD")
        #         meanDivider = meanDivider + 1
        # sumVector = list(list(wordVectorList["vector_values"][0].keys())[0])

        while sentenceIndex < len(self._bertComputedSentences):
            ## in the current sentence traverse the vector
            wordVectorList = self._bertComputedSentences[sentenceIndex]["vector_values"]
            cosineSimilarityList = []
            for wordVector in wordVectorList:
                ## get the vector
                keys = wordVector.keys()
                for key in keys:
                    ## compute moving cosine
                    cosineSimilarity = self._VECTOR_UTILL.computeCosineSimilarity(self._VECTOR_UTILL.meanVector(sumVector, meanDivider), wordVector[key])
                    ## add the current vector into the word vector for next computation
                    sumVector = self._VECTOR_UTILL.performVectorArthimetic(sumVector, wordVector[key], "ADD")

                    ##testing code
                    if len(meanVector) == 0:
                        ## push the current vector into the meanvector
                        meanVector.append(wordVector[key])
                    meanVectorValue = np.mean(meanVector ,axis=0,dtype=np.float64).tolist()
                    ## cosineSimilarityTest = self._VECTOR_UTILL.computeCosineSimilarity(meanVectorValue, wordVector[key])
                    cosineSimilarityTest = distance.cosine(meanVectorValue, wordVector[key])
                    ## append the current key for next processing
                    meanVector.append(wordVector[key])

                    ## add the similarity to the list
                    ##cosineSimilarityList.append(key+"_"+str(cosineSimilarity))
                    cosineSimilarityList.append(float(cosineSimilarityTest))
                    ## increament mean divider
                    meanDivider = meanDivider + 1

            ## add the cosine list to the bert sentence list
            self._bertComputedSentences[sentenceIndex]["moving_cosine_similarity"] = cosineSimilarityList
            ## append next index
            sentenceIndex = sentenceIndex + 1
        print(self._bertComputedSentences)

    def plotCosineSimilaritiesBySentenceWord(self):
        x_axis = []
        y_axis = []
        for index, sentenceData in enumerate(self._bertComputedSentences):
            cosineSimList = sentenceData['moving_cosine_similarity']
            wordList = sentenceData["vector_values"]
            for wordIndex,cosineData in enumerate(cosineSimList):
                x_axis.append(str(index + 1) + "_" + list(wordList[wordIndex].keys())[0])
                y_axis.append(float(cosineData))
        ## sort
        ## plot the graph
        # data
        copyList = y_axis.copy()
        copyList.sort()
        plt.plot(range(len(x_axis)), y_axis, color='green')
        plt.title("Moving cosine similarity")
        plt.ylabel("Cosine Similarity")
        plt.xlabel("Words by sentence")
        plt.xticks(ticks=range(len(x_axis)), labels=x_axis, rotation = 90)
        plt.show()


    def _removeStopWordsForBatch(self, rawBatchList):
        nonStopWordBatchList = []
        for batch in rawBatchList:
            nonStopWordBatchList.append(self._STOP_WORD_UTILL.removeStopWords(batch))
        return nonStopWordBatchList

    def _appendComputedBatches(self, rawBatchList, nonStopWordBatchList, nonEntityBatchList, wordVectorList):
        index = 0
        while index < len(rawBatchList):
            computedSentences = {}
            computedSentences["raw_batch"] = rawBatchList[index]
            computedSentences["non_entity_batch"] = nonEntityBatchList[index]
            computedSentences["non_stop_word_batch"] = nonStopWordBatchList[index]
            computedSentences["vector_values"] = wordVectorList[index]
            computedSentences["moving_cosine_similarity"] = []
            self._bertComputedSentences.append(computedSentences)
            index = index + 1

