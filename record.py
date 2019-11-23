import re
from utils import is_number

class Record:

    def __init__(self, record_length):
        self.fields = dict()

        if not is_number(record_length):
            raise ValueError("Record length #{record_length} is not a number.".format(record_length=str(record_length)))
        else:
            self.record_length = record_length

    @property
    def record_length(self):
        return self._record_length

    @record_length.setter
    def record_length(self, value):

        self._record_length = value

    #Create a field in the record. 
    def field(self, name, size, rng, typ):
        #Check if name is an 'identifier'.
        if not name.isidentifier():
            raise ValueError("Name #{name} is not a valid identifier.".format(name=name))

        #Check if size is numeric. 
        if not is_number(size):
            raise ValueError("Size #{size} is not a number.".format(size=size))

        #Check if range is valid. 
        if not bool(re.match("^(\d+)(?:-(\d+))?$", rng)):
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
            "type" : typ
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
            typ = self.fields[pos[i]].get("type")

            #Add parsed value to output
            output[name] = record[from_:to_]
        
        return output

    def generate(self):
        #Check that there are field.
        pass

test = "101 234567890 1234567891310081642C094101ImmDestName            ImmOriginName                  "

#Initialize record. 
file_header = Record(94)

#name, size, rng, typ
file_header.field("record_type_code", 1, "1-1", "numeric")
file_header.field("priority_code", 2, "2-3", "numeric")
file_header.field("immediate_destination", 10, "4-13", "numeric")
file_header.field("immediate_origin", 10, "14-23", "numeric")
file_header.field("file_creation_date", 6, "24-29", "numeric")
file_header.field("file_creation_time", 4, "30-33", "numeric")
file_header.field("file_id_modifier", 1, "34-34", "numeric")
file_header.field("record_size", 3, "35-37", "numeric")
file_header.field("blocking_factor", 2, "38-39", "numeric")
file_header.field("format_code", 1, "40-40", "numeric")
file_header.field("immediate_destination_name", 23, "41-63", "numeric")
file_header.field("immediate_origin_name", 23, "64-86", "numeric")
file_header.field("reference_code", 8, "87-94", "numeric")

print(file_header.parse(test))







        
