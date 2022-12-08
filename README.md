# Empirical Retraction Lit bibliography 
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5498474.svg)](https://doi.org/10.5281/zenodo.5498474) 
Includes bibliography data and web maintenance instructions.

# Description
Bibliography of empirical literature related to retraction from the "Reducing the Inadvertent Spread of Retracted Science: Shaping a Research and Implementation Agenda" (RISRS) project, Alfred P. Sloan Foundation G-2020-12623.

This contains content (bibliographic data), website materials (for an Exhibit-based website), and web maintenance materials.
Formats EPPI-Reviewer JSON export for use as Exhibit JSON

Code that takes a JSON-formatted file exported from EPPI-Reviewer and formats it for use as Exhibit JSON to enable online sharing of review bibliographies. The page also includes archived versions of the Info Quality Lab’s RISRS bibliography. The current official version can be found here: https://infoqualitylab.org/projects/risrs2020/bibliography/ 

# Included Files

README.md - This file

The latest bibliography data in 3 common file formats.
    
    o	Zotero-v2-385.bib
    o	Zotero-v2-385.csv
    o	Zotero-v2-385.ris
 
    
FOLDER: web-maintenance   

Describes how to maintain the bibliography website https://infoqualitylab.org/projects/risrs2020/bibliography/ (assuming a structure of Exhibit files).

  
The instructions for retrieving the input file from EPPI-Reviewer and running the code
    
    o	web-maintenance_instructions.docx
    
The code for metadata editing and formatting. Formats EPPI-Reviewer JSON export for use as Exhibit JSON on the bibliography website
    
    o	 json_pipeline.py
    
A sample export from EPPI-Reviewer PRIOR to formatting via the code. Running json_pipeline.py on this input results in key output (publications.json) in the website directory
    
    o	eppi_export--2021-09-09.json
    

FOLDER: website
Provides the Exhibit data for the bibliography website https://infoqualitylab.org/projects/risrs2020/bibliography/ . 

Underlying data for the latest version of the Empirical Retraction Lit bibliography
    
    o	index.html
    o	publications.json
    
# Version History

Pre-versioned
## Description
This page includes code that takes a JSON-formatted file exported from EPPI-Reviewer and formats it for use as Exhibit JSON to enable online sharing of review bibliographies. The page also includes archived versions of the Info Quality Lab’s RISRS bibliography. The current official version can be found here: https://infoqualitylab.org/projects/risrs2020/bibliography/ 



v.1.0.0

o	Initial Release--Bibliography of 162 items

## Description
First release of the bibliography of 162 items, with the materials for retrieving them.

## Included Files
The instructions for retrieving the input file from EPPI-Reviewer and running the code
    
    o	instructions_github.docx
    
The code for metadata editing and formatting
    
    o	 json_pipeline.py
    
Underlying data for v.1 of RISRS bibliography
    
    o	index--2021-05-18.html
    o	publications--2021-05-18.json
    
A sample export from EPPI-Reviewer PRIOR to formatting via the code
    
    o	eppi_export_162.json
    
Alternative formats for v. 1 of RISRS bibliography
    
    o	Zotero-v1-162.bib
    o	Zotero-v1-162.csv
    o	Zotero-v1-162.ris
    

v.2.0.0

o	Bibliography of 385 items

v.2.1.0

o	Bibliography of 386 items

v.2.15.0

o	Bibliography of 386 items

o	Refined categorization for web filters

v.2.20.0 (aka v2.2.0)

o	Bibliography of 385 items

o   Replaced 3 preprints with published versions

o	Excluded 1 research project (now published)

o	Updated metadata for online first items now in a formally published journal issue

o	Refined categorization for web filters

o	Renamed from RISRS Bibliography to Empirical Retraction Lit


v.2.20.5

o	Maintenance release:
 o	Renamed repository to Empirical Retraction Lit from EPPI-Reviewer_to_Exhibit_JSON_

 o   Fixed versioning consistency between GitHub, Zenodo, archive

 o   Updated folder structure to distinguish bibliography files from web maintenance files

 o   Renamed instructions DOCX to explicate that it's for web maintenance/bibliography updates
 o   Updated README.md and added to release

o	Bibliography of 385 items (unchanged from v.2.2 typo release and v2.20.0)


v.2.20.6

o	Maintenance release:

 o   Updated folder structure to distinguish website files from web maintenance files

 o   Updated README.md and added to release

o	Bibliography of 385 items (unchanged since v.2.20.0 (aka v2.2.0))
