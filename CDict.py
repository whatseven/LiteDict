import pickle
import re
import sqlite3

from ext import LOCALDBPATH, REMOTEDBPATH, INDEXDBPATH


class CDict():

    def __init__(self):
        try:
            with open(LOCALDBPATH, 'rb') as f:
                self.ContentStaticsDictList = pickle.load(f)
        except BaseException:
            self.ContentStaticsDictList = list()
        try:
            with open(INDEXDBPATH, 'rb') as f:
                self.IndexList = pickle.load(f)
        except BaseException:
            self.IndexList = list()

    def update(self):
        DataChanged=False

        Cn = sqlite3.connect(REMOTEDBPATH)
        Cu = Cn.cursor()
        ResultCursor = Cu.execute('select id,title,text from article')
        Results = ResultCursor.fetchall()

        ContentStaticsDictList = []

        def noBlankAndDOwnToThree(vStr):
            return len(vStr) >= 3

        for Result in Results:
            if Result[1] in self.IndexList:
                continue
            DataChanged=True
            self.IndexList.append(Result[1])
            ContentStaticsDict = dict()
            ContentStaticsDict['myID'] = Result[0]
            ContentStaticsDict['myTitle'] = Result[1]
            ContentList = filter(noBlankAndDOwnToThree, re.split(r'\W+', Result[2]))
            for word in ContentList:
                if word not in ContentStaticsDict:
                    ContentStaticsDict[word] = 1
                else:
                    ContentStaticsDict[word] += 1
            ContentStaticsDictList.append(ContentStaticsDict)
        self.ContentStaticsDictList += ContentStaticsDictList

        if DataChanged:
            with open(LOCALDBPATH, 'wb') as f:
                pickle.dump(self.ContentStaticsDictList, f)
            with open(INDEXDBPATH, 'wb+') as f:
                pickle.dump(self.IndexList, f)

        Cn.close()

    def recommendArticle(self,vStudyWords):
        recommendDicts=dict()
        #for one article
        for itemDict in self.ContentStaticsDictList:
            WordDict=dict()
            WordDict['myRate']=0
            # for every words
            for studyWord in vStudyWords:
                if studyWord in itemDict:
                    WordDict['myRate']+=itemDict.get(studyWord)/100
                    WordDict[studyWord]=itemDict.get(studyWord)
            recommendDicts[itemDict.get('myID')]=WordDict
        return sorted(recommendDicts.items(),key=lambda item:item[1]['myRate'],reverse=True)