# bundestag_protocols

## Bundestagsprotokolle

The collection of scripts works with the protocols of the different callings of the German Bundestag. The protocols are presented in two types of the XML-format. The protocols of the 19th calling are presented in a better format with more meta data, therefore parsing of these protocols was done with the use of two separate scripts. 

## Usage

1. Extraction of the protocols of the callings 1-18. 

The first code ``Bundestag_XML_Parsing.py`` iterates over the directory with XML-files (callings 1-18), extracts the information and saves the output of each file in a singe TXT-file. If the files already exist, they will be overwritten. Run the code as follows:
```
python3 Bundestag_XML_Parsing.py path_to_a_directory_with_protocols
```
The second script ``Concatenating_sents.py`` iterates over the directory with the extracted protocolos in the TXT-format and concatenates sentences, if there are any line breaks made with the use of hyphen. Different variations of line breaks are taken into account. The output for each file is saved in a new single TXT-file. If the files already exist, they will be overwritten. Run this script as follows: 
```
python3 Concatenating_sents.py path_to_a_directory_with_protocols
```
The last code for this collection of protocols is ``Tokenizing_into_sents.py``, which uses the NLTK library to tokenize sentences, got as a result of the second script ``Concatenating_sents.py``, and saves an output as a single TXT-file in the format 'One sentence per line'. If the files already exist, they will be overwritten. Run this file as follows:
```
python3 Tokenizing_into_sents.py path_to_a_directory_with_protocols
```
2. Extraction of the protocols of the 19th calling. 

The proctols of the 19th calling have more metadata, therefore they should be parsed in a different way. 

The first script ``19_Periode.py`` iterates over the directory with the files in the XML-format and extracts the information. The output is saved in a single TXT-file, which corresponds with the initial XML-file. If the files already exist, they will be overwritten. Run it as follows:
```
python3 Bundestag_XML_Parsing.py path_to_a_directory_with_protocols
```
The second script ``19_Periode_Sents.py`` uses the NLTK library to tokenize the input into sentences and save the output in the format 'One sentence per line'. The code iterates over the directory with the TXT-files which were got as the output of the code ``9_Periode.py`` and saves the information as single TXT-files. If the files already exist, they will be overwritten. Run the script as follows:
```
python3 19_Periode_Sents.py path_to_a_directory_with_protocols
```
