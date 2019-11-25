import re
from utils import is_number
from formats import ALPHABETIC, ALPHANUMERIC, NUMERIC

class Record:

    def __init__(self, record_length):
        self.fields = dict()

        if not is_number(record_length):
            raise ValueError("Record length #{record_length} is not a number.".format(record_length=str(record_length)))
        else:
            self.record_length = record_length

    #Create a field in the record. 
    def field(self, name, size, rng, typ, justify=None, fill=None):
        #Check if name is an 'identifier'.
        if not name.isidentifier():
            raise ValueError("Name #{name} is not a valid identifier.".format(name=name))

        #Check if size is numeric. 
        if not is_number(size):
            raise ValueError("Size #{size} is not a number.".format(size=size))

        #Check if range is valid. 
        if not bool(re.match(r"^(\d+)(?:-(\d+))?$", rng)):
            raise ValueError("Range '#{range}' is invalid".format(range=rng))

        #Get to, from, and check with size. 
        range_from = int(rng.split("-")[0])
        range_to = int(rng.split("-")[1])
        valid_range = (int(range_from) + (size - 1) == int(range_to))

        #Raise erorr if doesn't match up. 
        if not valid_range:
            raise ValueError("Invalid Range (size: #{size}, range: #{range})".format(size=size, range=rng))

        #Make sure range doesn't overlap with anything else.
        if not all([self.fields.get(pos) == None for pos in range(range_to, size)]):
            raise ValueError("Range #{range} conflicts with another range.")

        #Check if range_to is greater than record_length.
        if range_to > self.record_length:
            raise ValueError("Range #{range} ends after the record length.".format(range=rng))

        #If no errors, add field to record.
        self.fields[range_from] = {
            "name" : name, 
            "from" : int(range_from), 
            "to" : int(range_to), 
            "size" : size,
            "type" : typ, 
            "justify" : justify, 
            "fill" : fill
        }

    #Parse an existing record. 
    def parse(self, record):
        #Check that record is a string.
        if type(record) != str:
            raise ValueError('Record must be a string, not {record_type}'.format(record_type=str(type(record))))

        #Check field
        if self.fields == {}:
            raise ValueError("You must set fields before parsing a string.")

        #Check record length.
        if len(record) > self.record_length:
            raise ValueError("Parsed record length #{len} > defined record length {def_len}.".format(len=len(record), def_len=str(self.record_length)))

        #Output for storing. 
        output = dict()

        #If all clear, parse string into dictionary.
        pos = sorted(self.fields.keys())
        for i in range(0, len(pos)):
            #Get key vars
            name  =  self.fields[pos[i]].get("name")
            from_ = self.fields[pos[i]].get("from") - 1
            to_ = self.fields[pos[i]].get("to")

            #Add parsed value to output
            output[name] = str(record[from_:to_]).strip()
        
        return output

    def generate(self, data):
        output = ""

        #Check that there are field.
        if self.fields == {}:
            raise ValueError("Fields must be set to generate record.")
        
        #Acceptable data types: dictionary. 
        if isinstance(data, dict):
            #Loop through each of the items in fields and get value.
            for values in self.fields.values():

                #Get name, size, justify, and fill
                name = values.get("name")
                size = values.get("size")
                typ = values.get("type")

                #Get data value. 
                data_value = data.get(name)

                #Check if name is in data. 
                if data_value == None:
                    raise ValueError("Field name #{key} not in data dict.")

                #Make data_value string.
                data_value = str(data_value)

                #Compare length of value to size. 
                if len(str(data_value)) > size:
                    raise ValueError("Size of data value #{data_value} > size #{size}.".format(data_value=data_value, size=size))

                #Check if value matches regex format. 
                if not bool(re.match(typ["regex"], data_value)):
                    raise ValueError("Data value #{data_value} is not {form}".format(data_value=data_value, form=typ["name"]))
                    
                #Filler - Check for override. 
                if values.get("fill") == None:
                    filler = str(typ["fill"]) * (size - len(data_value))
                else:
                    filler = str(values.get("fill") * (size - len(data_value)))
                
                #Justify - Check for override. 
                if values.get("justify") == None:
                    justify = typ["justify"]
                else:
                    justify = values.get("justify")

                #Check that it's valid. 
                if justify == "left":
                    data_value = data_value + filler
                elif justify == "right":
                    data_value = filler + data_value
                else:
                    raise ValueError("Justification #{justify} is not right or left.".format(justify=typ["justify"]))

                #Add value to output. 
                output += data_value
        else:
            raise ValueError("Data of type #{type} is not supported. Dictionary required.".format(type=str(type(data))))

        return output






        
