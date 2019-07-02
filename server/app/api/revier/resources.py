from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.api.user.models import User
from app.api.revier.models import (
    Revier, 
    GrenzPunkt, 
    Einrichtung, 
    RevierSchema, 
    GrenzPunktSchema,
    EinrichtungSchema
)
from app.database import db


class RevierListApi(Resource):

    @jwt_required
    def get(self):
        response = {}
        reviere = Revier.get_all()
        schema = RevierSchema(many=True)

        response['status'] = "OK"
        response['reviere'] = schema.dump(reviere).data
        return response, 200
    
    @jwt_required
    def post(self):
        response = {}
        user = User.find_by_id(get_jwt_identity())
        if not user:
            response['status'] = "ERROR"
            response['message'] = "User konnte nicht gefunden werden."
            return response, 404
        
        schema = RevierSchema()
        result = schema.load(request.json)

        if not result.errors:
            data = request.get_json()

            revier = Revier(
                user_id=user.id,
                reviername = data['reviername'],
                ort = data['ort']
            )
            for each in data['revierGrenzen']:
                punkt = GrenzPunkt(
                    long=each.long,
                    lat=each.lat
                )
                revier.grenzen.append(punkt)
            
            revier.save()
            response['status'] = "OK"
            response['message'] = "Neues Revier wurde angelegt."
            return response, 201
            
        else:

            response['status'] = "ERROR"
            reponse['message'] = result.errors
            return response, 300

class RevierApi(Resource):

    @jwt_required
    def get(self, id):
        response = {}

        revier = Revier.find_by_id(id=id)
        if not revier:
            response['status'] = "ERROR"
            response['message' ] = "Revier kann nicht gefunden werden."
            return response, 404
        
        schema = RevierSchema()
        response['status'] = "OK"
        response['revier'] = schema.dump(revier).data
        return response, 200

    
    @jwt_required
    def put(self, id):
        response = {}
        schema = RevierSchema()
        result = schema.load(request.json)
        if not result.errors:
            revier = Revier.query.filter_by(id=id)
            revier.update(request.json)

            db.session.commit()
            response['status'] = "OK"
            reponse['message'] = "Revier wurde geändert."
            return response, 200
        else:
            response['status'] = "ERROR"
            reponse['message'] = result.errors
            return response, 300

    
    @jwt_required
    def delete(self, id):
        pass
