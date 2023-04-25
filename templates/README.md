# fish-data-comp Template Instructions
For using these files to collect/combine data and then crosswalk data between systems:
- `fish-data-comp-TEMPLATE-fields.xlsx`
- `fish-data-comp-TEMPLATE-codes.xlsx`
- `fish-data-xwalk-fields-TEMPLATE.csv`
- `fish-data-xwalk-codes-TEMPLATE.csv`

## For collating and combining data

### fish-data-comp-TEMPLATE-fields
Before filling anything in, create a copy of the `fish-data-comp-TEMPLATE-fields.xlsx` file and insert the relevant topic (abbreviated if helpful) where TEMPLATE is. 

Example: save species as `fish-data-comp-species-fields.xlsx`, save locations as `fish-data-comps-locs-fields.xlsx`

#### Filling in columns:
From data system documentation in _/data-sys-docs/_, fill in the following columns for all data systems. This will involve a lot of reading docs, copy and pasting info from docs, pdfs or websites, and possibly some transcribing information. For the species example, I went through document by document, program by program, in order: CAP HLI, FMD, PTAGIS, RMIS.

| sourceDataSystem | containingTable | fieldName | fieldDataType | fieldDefinition | fieldCodes | referenceDoc | hasCodes | comments |
|------------| ----------| --------------- | ------------ | -------------|-------------|-----|------|------|
| Enter the name of the data system. This will be either CAP HLI, FMD, PTAGIS, or RMIS.| Enter the name of the table in which the field is contained. | Enter the name of the field from the documentation.| Enter the data type listed in the documentation. This is not always provided verbatim but can sometimes be inferred from the fieldDefinition. If unsure or can't find it, use Unknown or Not provided. | Enter the definition for the field as provided in documentation here. | If given, enter the definition for the various field codes from the relevant document here. If not listed, then enter where you would find the code definitions in another document or URL. | What data-sys-doc file did you use to fill in the definitions and information? Use what makes sense to you. I tried to stick to file names and added Appendix labels if relevant. | Does the field contain codes or categories? Use Yes, No, or Unknown|any comments related to the field, such as missing or incorrect information, broken links, additional info, questions or anything needing clarification. |

If a field appears in one or more tables, enter the information in all columns under all tables. This way, later, we know which tables each field appears in and how information connects. An example of this is the CAP HLI field CommonName which appears in the NOSA, SAR, RperS, JuvenileOutmigrants, PNI, and Populations tables.

### fish-data-comp-TEMPLATE-codes
Before filling anything in, create a copy of the `fish-data-comp-TEMPLATE-codes.xlsx` file and insert the relevant topic (abbreviated if helpful) where TEMPLATE is. Example: save species as `fish-data-comp-species-codes.xlsx`, save locations as `fish-data-comps-locs-codes.xlsx`

#### Filling in columns:
From data system documentation in _/data-sys-docs/_, fill in the following columns for all data systems. This will involve a lot of reading docs, copy and pasting info from docs, pdfs or websites, and possibly some transcribing of information. For the species example, I went through document by document, program by program, in order: CAP HLI, FMD, PTAGIS, RMIS.

| sourceDataSystem | fieldName | codeName | codeDefinition | definitionSource | comments |
|------------|----------|---------------|------------|-------------|-------------|
|Enter the name of the data system. This will be either CAP HLI, FMD, PTAGIS, or RMIS.|Enter the name of the field from the documentation here.|Enter the name of the code from the documentation here.|Enter the definition of the code from documentation here.|Enter the document you used to populate the definition. Stick to filenames (and the table in which the code is defined in) or URLs where possible.|any comments related to the code, such as missing or incorrect information, broken links, additional info, questions or anything needing clarification.|


Unlike for the fish-data-comp-fields table, if codes appear in more than one table, don't duplicate them. Codes only need to be defined and included once because their parent table is already recorded in the `fish-data-comp-fields.xlsx` table.

Once all of this information is compiled for a certain topic (such as species or location), then each data systems' fields and codes for that topic can be compared and cross-walked with the others (see below).

## For crosswalking data

### fish-data-xwalk-fields-TEMPLATE
This file serves as a blank template for the `fish-data-xwalk-fields.csv` file. Use the template in the same way as described above (making a copy, saving the file with a name including the topic of relevance) or alternatively, make a copy of the `fish-data-xwalk-fields.csv` file and continue adding to it.

#### Filling in columns
Use information collected in the `fish-data-comp-species-fields.xlsx`, fill in the following:

| sourceDataSystem | sourceDataField | sourceDataFieldDef | sourceDataType | notes | 
|------------|----------|---------------|------------|-------------|
| Enter the name of the data system. This will be either CAP HLI, FMD, PTAGIS, or RMIS. | Enter the name of the field from the documentation here. If the field does not exist in that data system, enter none. | Enter the definition of the code from documentation here. If the field does not exist in that data system, enter none. | Enter the data type listed in the documentation. This is not always provided verbatim but can sometimes be inferred from the fieldDefinition. If unsure or can't find it, use Unknown or Not provided. | Enter any notes relevant to the field for cross-walking purposes, such as, if unsure whether a field is equivalent to other data systems or if a field only exists in one data system and not the others. If no notes, enter none. |

You will notice the information in this table is essentially copied/replicated from the `fish-data-comp-species-fields.xlsx` and may be redundant and not even be necessary to re-format in this second file. It's up to you what works best for you/if you find this second file useful or not. It is possible to create a script to read the `fish-data-comp-species-fields.xlsx` and automatically fill in this table rather than doing it manually but was not something I explored.

### fish-data-xwalk-codes-TEMPLATE
Before filling anything in, create a copy of the `fish-data-xwalk-codes-TEMPLATE.csv` file and insert the relevant topic before the 'codes' and remove TEMPLATE. Example: save species as `fish-data-xwalk-species-codes.csv`, save locations as `fish-data-xwalk-location-codes.csv`.

#### Filling in columns 
Using information from `fish-data-comp-species-codes.csv`, fill in the following:

| sourceDataSystem | code | sourceDataCode | sourceDataCodeDef | sourceDataField | notes |
|------------|----------|---------------|------------|-------------|---|
| Enter the name of the data system. This will be either CAP HLI, FMD, PTAGIS, or RMIS. | Enter the name of the code or category (generally) being compared between stystems. | Enter the code from the data system. If the code does not exist in that data system, enter none. | Enter the definition of the code from the data system. | Enter the data field under which the code falls. If the code does not exist in that data system, enter none.  | Enter any relevant notes, issues, or uncertainties, such as if note sure a code is equivalent to the codes in other data systems or if a code only appears in one data system and not the others. If no notes, enter none. |

It is possible to create a script to read the `fish-data-comp-species-fields.xlsx` and automatically fill in this table rather than doing it manually but was not something I explored.