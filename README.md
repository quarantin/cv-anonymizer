# cv-anonymizer
A simple script to anonymize your resume and generate PDF (only works for .odt files).

# Use Case
I need at minimum 2 resumes, one in english and one in french. I also need anonymized versions of all my resumes, with personal and contact information stripped from the document. Sometimes I write new variants of my resumes to reply to specific job offers. In the end it can become really time consuming to maintain. For example when you want to make a small edit, you have to edit all the .odt files, then create the corresponding anonymized versions, then generate PDF for each resume. Using this tool I can simply edit my english and french resumes and it will generate an anonymized version for each of them. Then it will generate a PDF for each resume.

# How Does it Work?
In my resumes all my personal and contact information are contained in a table at the top of the document. This tool will simply strip the first table it can find in the document.

# Usage
```
git clone https://github.com/quarantin/cv-anonymizer.git
cd cv-anonymizer
cp /path/to/your/resumes/*.odt .
make
```

# Example
```
~/cv-anonymizer$ ls -1
anonymize.py
cv_en_2023.odt
cv_fr_2023.odt
LICENSE
Makefile
README.md
```
```
~/cv-anonymizer$ make
rm -f *.pdf *_anon.odt
./anonymize.py *.odt
Anonymzing cv_en_2023.odt
Anonymzing cv_fr_2023.odt
libreoffice --headless --convert-to pdf *.odt
convert /home/co/cv/cv_en_2023.odt -> /home/co/cv/cv_en_2023.pdf using filter : writer_pdf_Export
convert /home/co/cv/cv_en_2023_anon.odt -> /home/co/cv/cv_en_2023_anon.pdf using filter : writer_pdf_Export
convert /home/co/cv/cv_fr_2023.odt -> /home/co/cv/cv_fr_2023.pdf using filter : writer_pdf_Export
convert /home/co/cv/cv_fr_2023_anon.odt -> /home/co/cv/cv_fr_2023_anon.pdf using filter : writer_pdf_Export
```
```
~/cv-anonymizer$ ls -1
anonymize.py
cv_en_2023_anon.odt
cv_en_2023_anon.pdf
cv_en_2023.odt
cv_en_2023.pdf
cv_fr_2023_anon.odt
cv_fr_2023_anon.pdf
cv_fr_2023.odt
cv_fr_2023.pdf
LICENSE
Makefile
README.md
```
