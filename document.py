from record import Record
from formats import NUMERIC, ALPHANUMERIC, ALPHABETIC
from utils import is_number

class Document:

    def __init__(self):
        self.records = dict()
        self.line_ending = "\n"
    
    def record(self, name, record_object, identifier=None):
        #Add to document. 
        self.records[name] = {
            "record" : record_object, 
            "identifier" : identifier 
        }

    def generate(self, data):
        #Data must be a list of dictionaries: each object is a line. 
        if not isinstance(data, list):
            raise ValueError("Data must be a list of dictionaries, not #{data}".format(type(data)))

        #Loop through the data and add to string. 
        output = ""

        for line in data:
            #Check if name is in records. 
            if line.get("name") not in list(self.records.keys()):
                raise ValueError("#Record name {line} is not in document records.".format(line=line.get("name")))

            #Get record object. 
            record = self.records[line.get("name")].get("record")

            #Generate line. 
            output += record.generate(line.get("values")) + self.line_ending

        #Return output.
        return output

    def parse(self, document):
        pass











