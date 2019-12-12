from flask_restful import Resource

class GetAllOffers(Resource):
    def get(self):
        pass

class GetOfferDetails(Resource):
    def get(self, offer_oid):
        pass

class DeleteOffer(Resource):
    def delete(self, offer_oid):
        pass
    
class UpdateOffer(Resource):
    def put(self, offer_oid):
        pass

class FollowOffer(Resource):
    def get(self, offer_oid):
        pass

class UnfollowOffer(Resource):
    def delete(self, offer_oid):
        pass