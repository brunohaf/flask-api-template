from flask_restful import Resource

class artefact_service(Resource):

    def getName(self):
        return self.name

    def getType(self):
        return self.type

    def getDescription(self):
        return self.description

    def setName(self, name):
        self.name = name

    def setType(self, type):
        self.type = type

    def setDescription(self, description):
        self.description = description

    def get(self):
        try:
            self.setName('Batata')
            self.setType("Teste")
            self.setDescription('teeste')
            response = {"name": self.name,
                    "type": self.type,
                    "description" : self.description}
            return response, 200
        except:
            return "error", 400
