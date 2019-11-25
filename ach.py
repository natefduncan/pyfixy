from record import Record
from formats import NUMERIC, ALPHANUMERIC, ALPHABETIC
from document import Document

#### FILE HEADER ####
#Initialize record. 
file_header = Record(94)

#Add fields
file_header.field("record_type_code", 1, "1-1", NUMERIC)
file_header.field("priority_code", 2, "2-3", NUMERIC)
file_header.field("immediate_destination", 10, "4-13", NUMERIC, justify="right", fill=" ")
file_header.field("immediate_origin", 10, "14-23", NUMERIC, justify="right", fill=" ")
file_header.field("file_creation_date", 6, "24-29", NUMERIC)
file_header.field("file_creation_time", 4, "30-33", NUMERIC)
file_header.field("file_id_modifier", 1, "34-34", ALPHANUMERIC)
file_header.field("record_size", 3, "35-37", NUMERIC)
file_header.field("blocking_factor", 2, "38-39", NUMERIC)
file_header.field("format_code", 1, "40-40", NUMERIC)
file_header.field("immediate_destination_name", 23, "41-63", ALPHANUMERIC)
file_header.field("immediate_origin_name", 23, "64-86", ALPHANUMERIC)
file_header.field("reference_code", 8, "87-94", ALPHANUMERIC)

#### BATCH HEADER ####
batch_header = Record(94)

#Add fields
batch_header.field("record_type_code", 1, "1-1", NUMERIC)
batch_header.field("service_class_code", 3, "2-4", NUMERIC)
batch_header.field("company_name", 16, "5-20", ALPHANUMERIC)
batch_header.field("company_discretionary_data", 20, "21-40", NUMERIC)
batch_header.field("company_identification", 10, "41-50", NUMERIC)
batch_header.field("standard_entity_class_code", 3, "51-53", ALPHABETIC)
batch_header.field("company_entry_description", 10, "54-63", ALPHANUMERIC)
batch_header.field("company_descriptive_date", 6, "64-69", ALPHANUMERIC)
batch_header.field("effective_entry_date", 6, "70-75", ALPHANUMERIC)
batch_header.field("settlement_date", 3, "76-78", ALPHANUMERIC)
batch_header.field("originator_status_code", 1, "79-79", NUMERIC)
batch_header.field("originator_dfi_identification", 8, "80-87", NUMERIC)
batch_header.field("batch_number", 7, "88-94", NUMERIC)

#### Initialize Document ####
AchDocument = Document()
AchDocument.record("file_header", file_header)
AchDocument.record("batch_header", batch_header)



