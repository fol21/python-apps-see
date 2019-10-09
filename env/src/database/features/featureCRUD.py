from ..base.baseCRUD import BaseCRUD

class FeatureCRUD(BaseCRUD):

    def __init__(self,url,dbname):
        super().__init__(url, dbname)
    
    def insertAnalysis(self, name, base64, analysis):
        super().createDocument('Analysis',
            {
                'name': name,
                'base64': base64,
                'categories': analysis['categories'],
                'tags': analysis['description']['tags'],
                'captions': analysis['description']['captions']
            })
        return self
    
    def updateAnalysis(self, name, analysis):
        super().updateDocument('Analysis',
            {'name': name},
            {
                '$set': {
                    'categories': analysis['categories'],
                    'tags': analysis['description']['tags'],""
                    'captions': analysis['description']['captions']
                }
            })
        return self

    
    def getAnalysis(self, name):
        return super().readDocument('Analysis', {'name': name})

    def deleteAnalysis(self, name):
        super().deleteDocument('Analysis', {'name': name})
        return self
        
