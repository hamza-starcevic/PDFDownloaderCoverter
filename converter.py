import os
import re
import PyPDF2

# Path to the directory containing the PDF files
pdf_dir = './pdfs'

# Loop over all PDF files in the directory
for pdf_file_name in os.listdir(pdf_dir):
    # Print progress
    print('Processing ' + pdf_file_name)
    if pdf_file_name.endswith('.pdf'):
        # Open the PDF file
        try:
            pdf_file_path = os.path.join(pdf_dir, pdf_file_name)
            pdf_file = open(pdf_file_path, 'rb')

            # Create a PDF reader object and extract text from each page 
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            #Put a newline between each document's text
            with open('text.txt', 'a') as text_file:
                text_file.write('\n')

            #Put the title and author of the document into the text file
            with open('text.txt', 'a') as text_file:
                text_file.write('Title: ')
                #Check if the title is not None
                if pdf_reader.metadata.title is not None:
                    text_file.write(pdf_reader.metadata.title)
                else:
                    text_file.write('Not specified')
                text_file.write('\n')

                text_file.write('Author: ')
                #Check if the author is not None or empty
                if pdf_reader.metadata.author is not None:
                    text_file.write(pdf_reader.metadata.author)
                elif pdf_reader.metadata.author == '':
                    text_file.write('Not specified')
                else:
                    text_file.write('Not specified')
                text_file.write('\n')

                
            for page_num in range(len(pdf_reader.pages)):
                page_obj = pdf_reader.pages[page_num]
                text = page_obj.extract_text()
                # Write the text to a text file
                with open('text.txt', 'a') as text_file:
                    text_file.write(text)

            # Extract metadata from the PDF file and into info.txt
            doc_info = pdf_reader.metadata
            
            with open('info.txt', 'a') as info_file:
                info_file.write(str(doc_info))

            # Close the PDF file
            pdf_file.close()
        except:
            print('Error processing ' + pdf_file_name)
            continue

# Go through info.txt and put a newline betwen each document's metadata
with open('info.txt', 'r') as info_file:
    info = info_file.read()
    info = info.replace('}{', '}\n{')
    with open('info.txt', 'w') as info_file:
        info_file.write(info)

# Remove all non alphanumeric characters from text.txt
with open('text.txt', 'r') as text_file:
    text = text_file.read()
    text = ''.join(e for e in text if e.isalnum() or e == ' ')
    with open('text.txt', 'w') as text_file:
        text_file.write(text)


# remove all non english characters from text.txt
with open('text.txt', 'r') as text_file:
    text = text_file.read()
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)
    with open('text.txt', 'w') as text_file:
        text_file.write(text)


