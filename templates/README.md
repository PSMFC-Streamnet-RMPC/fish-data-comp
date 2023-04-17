# fish-data-comp Template Instructions
For using `fish-data-comp-TEMPLATE-fields.xlsx` and `fish-data-comp-TEMPLATE-codes.xlsx`

## fish-data-comp-TEMPLATE-fields
Before filling anything in, create a copy of the `fish-data-comp-TEMPLATE-fields.xlsx` file and insert the relevant topic (abbreviated if helpful) where TEMPLATE is. 

Example: save species as `fish-data-comp-species-fields.xlsx`, save locations as `fish-data-comps-locs-fields.xlsx`

### Filling in columns:
From data system documentation in _/data-sys-docs/_, fill in the following columns for all data systems. This will involve a lot of reading docs, copy and pasting info from docs, pdfs or websites, and possibly some transcribing information. For the species example, I went through document by document, program by program, in order: CAP HLI, FMD, PTAGIS, RMIS.

| sourceDataSystem | containingTable | fieldName | fieldDataType | fieldDefinition | fieldCodes | referenceDoc | hasCodes | comments |
|------------| ----------| --------------- | ------------ | -------------|-------------|-----|------|------|
|Enter the name of the data system. This will be either CAP HLI, FMD, PTAGIS, or RMIS.|Enter the name of the table in which the field is contained.|Enter the name of the field from the documentation.|Enter the data type listed in the documentation. This is not always provided verbatim but can sometimes be inferred from the fieldDefinition. If unsure or can't find it, use Unknown or Not provided.|Enter the definition for the field as provided in documentation here.|If given, enter the definition for the various field codes from the relevant document here. If not listed, then enter where you would find the code definitions in another document or URL.|What data-sys-doc file did you use to fill in the definitions and information? Use what makes sense to you. I tried to stick to file names and added Appendix labels if relevant.|Does the field contain codes or categories? Use Yes, No, or Unknown|any comments related to the field, such as missing or incorrect information, broken links, additional info, questions or anything needing clarification.|

If a field appears in one or more tables, enter the information in all columns under all tables. This way, later, we know which tables each field appears in and how information connects. An example of this is the CAP HLI field CommonName which appears in the NOSA, SAR, RperS, JuvenileOutmigrants, PNI, and Populations tables.

## fish-data-comp-TEMPLATE-codes
Before filling anything in, create a copy of the `fish-data-comp-TEMPLATE-codes.xlsx` file and insert the relevant topic (abbreviated if helpful) where TEMPLATE is. Example: save species as `fish-data-comp-species-codes.xlsx`, save locations as `fish-data-comps-locs-codes.xlsx`

### Filling in columns:
From data system documentation in _/data-sys-docs/_, fill in the following columns for all data systems. This will involve a lot of reading docs, copy and pasting info from docs, pdfs or websites, and possibly some transcribing of information. For the species example, I went through document by document, program by program, in order: CAP HLI, FMD, PTAGIS, RMIS.
roken links, additional info, questions or anything needing clarification.

| sourceDataSystem | fieldName | codeName | codeDefinition | definitionSource | comments |
|------------|----------|---------------|------------|-------------|-------------|
|Enter the name of the data system. This will be either CAP HLI, FMD, PTAGIS, or RMIS.|Enter the name of the field from the documentation here.|Enter the name of the code from the documentation here.|Enter the definition of the code from documentation here.|Enter the document you used to populate the definition. Stick to filenames (and the table in which the code is defined in) or URLs where possible.|any comments related to the code, such as missing or incorrect information, broken links, additional info, questions or anything needing clarification.|


Unlike for the fish-data-comp-fields table, if codes appear in more than one table, don't duplicate them. Codes only need to be defined and included once because their parent table is already recorded in the `fish-data-comp-fields.xlsx` table.

Once all of this information is compiled for a certain topic (such as species or location), then each data systems' fields and codes for that topic can be compared with the others. Files created by topic could eventually be combined into one giant file of all data system fields and codes but for now, I would leave species, location, etc. separate.
