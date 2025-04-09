# Research Paper Fetcher from PubMed

This Python program fetches research papers from PubMed based on a user-defined query and identifies non-academic authors and companies. It processes the retrieved papers and saves them to a CSV file, including details like the title, authors, publication date, and affiliations.

## How the Code is Organized

The code is organized into several functions to perform distinct tasks:

### `fetch_papers(query: str, max_results: int = 100)`
Fetches paper metadata from PubMed based on a query.

### `parse_pubmed_ids(xml_data: str)`
Parses PubMed IDs from the XML response.

### `fetch_paper_details(pubmed_ids: List[str])`
Fetches detailed paper information from PubMed using the provided PubMed IDs.

### `parse_paper_details(xml_data: str)`
Extracts paper details (e.g., title, authors) from the XML response.

### `identify_non_academic(authors: List[Dict])`
Identifies non-academic authors and their company affiliations.

### `save_to_csv(papers, filename: Optional[str])`
Saves the fetched papers to a CSV file or prints the data to the console.

### `main()`
Handles command-line execution, parsing arguments, and calling necessary functions to fetch papers and save the results.

## Tools and Libraries Used

### `argparse`
For command-line argument parsing.  
[Documentation](https://docs.python.org/3/library/argparse.html)

### `pandas`
For data handling and saving results to CSV.  
[Documentation](https://pandas.pydata.org/pandas-docs/stable/)

### `requests`
For making HTTP requests to the PubMed API.  
[Documentation](https://docs.python-requests.org/en/master/)

### PubMed API
For fetching research papers from PubMed.  
[Documentation](https://pubmed.ncbi.nlm.nih.gov/)

## Installation Instructions

### Prerequisites
Ensure that you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

### Dependencies
To install the required dependencies, you can use pip:

```bash
pip install pandas requests
