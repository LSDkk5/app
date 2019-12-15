from flask_restful import Resource

class GetAllOffers(Resource):
    def get(self, tags): #Pobranie wszystkich ofert według tagów
        pass

class Offers(Resource):
    def get(self, offer_oid): #Pobranie detali o ofercie
        pass
    
    def put(self, offer_id): #Aktualizacja
        pass

    def delete(self, offer_id): #Usunięcie oferty
        pass

class FollowedOffers(Resource):
    def get(self):  #Pobranie obserwowanych ofert użytkownika
        pass

class FollowOffersController(Resource):
    def post(self, offer_id): #Obserwowanie oferty
        pass

    def delete(self, offer_oid): #Usunięcie oferty z obserwowanych
        pass
