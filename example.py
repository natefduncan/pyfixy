from ach import AchDocument

data = [
    {
        "name" : "file_header",
        "values" : {
            'record_type_code': '1', 
            'priority_code': '01', 
            'immediate_destination': '234567890', 
            'immediate_origin': '123456789', 
            'file_creation_date': '131008', 
            'file_creation_time': '1642', 
            'file_id_modifier': 'C', 
            'record_size': '094', 
            'blocking_factor': '10', 
            'format_code': '1', 
            'immediate_destination_name': 'ImmDestName', 
            'immediate_origin_name': 'ImmOriginName', 
            'reference_code': ''
        },
    },
    {
        "name" : "batch_header", 
        "values" : {
            'record_type_code': '5', 
            'service_class_code': '200', 
            'company_name': 'YOUR COMPANY', 
            'company_discretionary_data': '', 
            'company_identification': '1234567890', 
            'standard_entity_class_code': 'PPD', 
            'company_entry_description': 'PAYROLL', 
            'company_descriptive_date': '', 
            'effective_entry_date': '140903', 
            'settlement_date': '', 
            'originator_status_code': '1', 
            'originator_dfi_identification': '12345678', 
            'batch_number': '0000001'
        }
    }
]

#### EXAMPLE: ACH PRE-SET ####
print(AchDocument.generate(data))

