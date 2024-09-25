from flask_restful import Resource
from flask import request
import json

Emps = [{"id": 1, "name": "ABC" ,"role": "sde-1","salary":78000},
         {"id": 2, "name": "XYZ","role": "MLe",'salary':91000}]


class EmpsGETResource(Resource):
    def get(self):
        return Emps

class EmpGETResource(Resource):
    def get(self, id):
        for Emp in Emps:
            if Emp["id"] == id:
                return Emp
        return None


class EmpPOSTResource(Resource):
    def post(self):
        Emp = json.loads(request.data)
        new_id = max(Emp["id"] for Emp in Emps) + 1
        Emp["id"] = new_id
        Emps.append(Emp)
        return Emp


class EmpPUTResource(Resource):
    def put(self, id):
        Emp = json.loads(request.data)
        for _Emp in Emps:
            if _Emp["id"] == id:
                _Emp.update(Emp)
                return _Emp


class EmpDELETEResource(Resource):
    def delete(self, id):
        global Emps
        Emps = [Emp for Emp in Emps if Emp["id"] != id]
        return "", 204
