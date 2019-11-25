NUMERIC = {
    "name" : "numeric",
    "description" : "0 through 9",
    "justify" : "right", 
    "fill" : "0", 
    "regex" : r"^\d+$|^$"
}

ALPHABETIC = {
    "alphabetic" : "alphabetic",
    "description" : "A through Z, a through z",
    "justify" : "left", 
    "fill" : " ", 
    "regex" : r"^[a-zA-Z]+$|^$"
}

ALPHANUMERIC = {
    "name" : "alphanumeric",
    "description" : """
    0 through 9, A through Z, a through z
    The following symbols and special characters are
    allowed: . / () & ' - and spaces
    Unless otherwise noted.""", 
    "justify" : "left", 
    "fill" : " ", 
    "regex" : r"^[a-zA-Z0-9 .()\/\&'\ -]+$|^$"
}
