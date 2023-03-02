import arxiv



search = arxiv.Search(
  query = "ti:biology",
  max_results = 900,
  sort_by = arxiv.SortCriterion.SubmittedDate
)

# Add the pdf_url to the links array
links = []
for result in search.results():
    try:
      links.append(result.pdf_url)
      #Check if the pdf_url None or empty
      if result.pdf_url is None or result.pdf_url == '':
          print("No pdf_url for " + result.title)
          continue
      result.download_pdf(dirpath='pdfs', filename=result.title + '.pdf')
      #Show how many have been downloaded out of the max_results
      print("Downloaded " + str(len(links)) + " out of " + str(search.max_results))
    except:
      print("Error downloading " + result.title)
      continue