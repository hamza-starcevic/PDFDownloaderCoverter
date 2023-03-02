from Bio import Entrez, Medline
import urllib.request
from http.client import IncompleteRead

# Set the email necessary for the Entrez API
Entrez.email = 'hstarcevic@capeannenterprises.com'

# Set the search term
try:
    search_term = 'genetics'
    handle = Entrez.esearch(db='pubmed', retmax=900, term=search_term)
    record = Entrez.read(handle)
    handle.close()

    # Fetch the data
    id_list = record['IdList']
    handle = Entrez.efetch(db='pubmed', id=id_list,
                        rettype='medline', retmode='text')
    records = Medline.parse(handle)

    counter = 0
except:
    print('An error occurred during setup')

try:
    # Save the data
    for rec in records:
        # Print progress and number of records processed
        print('Downloaded ')
        print(counter)
        print(' out of ' + str(len(id_list)))
        counter += 1
        pmid = rec.get('PMID')
        title = rec.get('TI')
        url = 'https://www.ncbi.nlm.nih.gov/pubmed/' + pmid
        filename = title + '.pdf'
        try:
            # Download the pdfs to the pdfs folder
            urllib.request.urlretrieve(url, './pdfs/' + filename)
        except IncompleteRead:
            continue
        except:
            print("Error downloading " + filename)
            continue

        print("Downloaded " + filename)
except IncompleteRead:
    print('An error occurred during download')