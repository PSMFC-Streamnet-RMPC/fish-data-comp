# fish-data comp Template Instructions
For fish-data-comp-TEMPLATE-fields.xlsx and fish-data-comp-TEMPLATE-codes.xlsx

## fish-data-comp-TEMPLATE-fields
Before filling anything in, create a copy of the fish-data-comp-TEMPLATE-fields file and insert the relevant topic (abbreviated if helpful) where TEMPLATE is. Example: save species as fish-data-comp-species-fields, save locations as fish-data-comps-locs-fields

### Filling in columns:
Column headers:
- sourceDataSystem: Enter the name of the data system. This will be either CAP HLI, FMD, PTAGIS, or RMIS.
- containingTable: Enter the name of the table in which the field is contained.
- fieldName: Enter the name of the field from the documentation.
- fieldDataType: Enter the data type listed in the documentation. This is not always provided verbatim but can sometimes be inferred from the fieldDefinition. If unsure or can't find it, use Unknown or Not provided.
- fieldDefinition: Enter the definition for the field here.
- fieldCodes: If given, enter the definition for the various field codes from the relevant document here. If not listed, then enter where you would find the code definitions in another document or URL.
- referenceDoc: What data-sys-doc file did you use to fill in the definitions and information? Use what makes sense to you. I tried to stick to file names and added Appendix labels if relevant.
- hasCodes: Does the field contain codes or categories? Use Yes, No, or Unknown
Y = yes, the field has codes/categories
N = no, the field does not have codes/categories
Unknown = documentation is not clear if there are codes/categories or not
- comments: any comments related to the field, such as missing or incorrect information, broken links, additional info, questions or anything needing clarification.

If a field appears in one or more tables, enter the information in all columns under all tables. This way, later, we know which tables each field appears in and how information connects. An example of this is the CAP HLI field CommonName which appears in the NOSA, SAR, RperS, JuvenileOutmigrants, PNI, and Populations tables.

## fish-data-comp-TEMPLATE-codes
Before filling anything in, create a copy of the fish-data-comp-TEMPLATE-codes file and insert the relevant topic (abbreviated if helpful) where TEMPLATE is. Example: save species as fish-data-comp-species-codes, save locations as fish-data-comps-locs-codes

### Filling in columns:
- sourceDataSystem: Enter the name of the data system. This will be either CAP HLI, FMD, PTAGIS, or RMIS.
- fieldName: Enter the name of the field from the documentation.
- codeName: Enter the name of the code from the documentation.
- codeDefinition: Enter the definition of the code rfom documentation.
- definitionSource: Enter the document you used to populate the definition. Stick to filenames (and the table in which the code is defined in) or URLs where possible.
- comments: any comments related to the code, such as missing or incorrect information, broken links, additional info, questions or anything needing clarification.

Unlike for the fish-data-comp-fields table, if codes appear in more than one table, don't duplicate them. Codes only need to be defined and included once because their parent table is already recorded in the fish-data-comp-fields table.
