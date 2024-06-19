import requests

ENDPOINT = 'https://api.gostatit.com/core'

class API:
    """A python API to interact with the api.gostatit.com web API"""
        
    def __init__(self, username: str, apikey: str):
        self.__username = username
        self.__apikey = apikey

    def __post(self, json):
        r = requests.post(ENDPOINT,auth=(self.__username, self.__apikey), json=json)
        if r.status_code != 200 : raise ValueError(r.text)
        return r.json()

    def getSerie(self, id: str) -> dict[str, any]:
        json = {
            'action': 'getSerie', 'input': {
                "id": id,
            },
        }
        return self.__post(json)

    def listSeries(self, parentid: str) -> list[dict[str, any]]:
        json = {
            'action': 'listSeries', 'input': {
                "id": parentid,
            },
        }
        return self.__post(json)

    def deleteSerie(self, id: str):
        json = {
            'action': 'deleteSerie', 'input': {
                "id": id,
            },
        }
        return self.__post(json)


    def getSerieJSON(self, input: dict[str, any]) -> dict[str, any]:
        json = {
            'action': 'getSerie', 'input': input,
        }
        return self.__post(json)

    def batchGetSerieJSON(self, input: list[dict[str, any]]):
        json = {
            'action': 'batchGetSerie', 'input': input,
        }
        return self.__post(json)

    def getAllSeriesJSON(self, input: list[dict[str, any]]):
        batch = []
        for serie in input:
            batch.append(serie)
            if len(batch) == 25:
                yield self.batchGetSerieJSON(batch)
                batch = []
        if batch != [] : yield self.batchGetSerieJSON(batch)

    def listSeriesJSON(self, input: dict[str, any]) -> list[dict[str, any]]:
        json = {
            'action': 'listSeries', 'input': input,
        }
        return self.__post(json)
        
    def putSerieJSON(self, input: dict[str, any]):
        json = {
            'action': 'putSerie', 'input': input,
        }
        return self.__post(json)

    def batchPutSerieJSON(self, input: list[dict[str, any]]):
        json = {
            'action': 'batchPutSerie', 'input': input,
        }
        return self.__post(json)

    def putAllSeriesJSON(self, input: list[dict[str, any]]):
        batch = []
        for serie in input:
            batch.append(serie)
            if len(batch) == 25:
                yield self.batchPutSerieJSON(batch)
                batch = []
        if batch != [] : yield self.batchPutSerieJSON(batch)
        
    def updateSerieJSON(self, input: dict[str, any]):
        json = {
            'action': 'updateSerie', 'input': input,
        }
        return self.__post(json)

    def deleteSerieJSON(self, input: dict[str, any]):
        json = {
            'action': 'deleteSerie', 'input': input,
        }
        return self.__post(json)

    def batchDeleteSerieJSON(self, input: list[dict[str, any]]):
        json = {
            'action': 'batchDeleteSerie', 'input': input,
        }
        return self.__post(json)

    def deleteAllSeriesJSON(self, input: list[dict[str, any]]):
        batch = []
        for serie in input:
            batch.append(serie)
            if len(batch) == 25:
                yield self.batchDeleteSerieJSON(batch)
                batch = []
        if batch != [] : yield self.batchDeleteSerieJSON(batch)
    



    

