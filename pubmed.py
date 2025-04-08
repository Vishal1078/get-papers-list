import requests
import pandas as pd
from typing import List, Tuple, Dict

# PubMed API URL
PUBMED_BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

def fetch_papers(query: str, max_results: int = 100) -> List[Dict]:
    """Fetch papers from PubMed based on the user's query."""
    search_url = f"{PUBMED_BASE_URL}esearch.fcgi"
    search_params = {
        "db": "pubmed",
        "term": query,
        "retmax": max_results,
        "usehistory": "y",
        "retmode": "xml"
    }

    try:
        search_response = requests.get(search_url, params=search_params)
        search_response.raise_for_status()  # Raise an HTTPError for bad responses
    except requests.RequestException as e:
        print(f"Error fetching papers: {e}")
        return []

    # Parse the search response to get the PubMed IDs
    ids = parse_pubmed_ids(search_response.text)

    papers = fetch_paper_details(ids)
    return papers


def parse_pubmed_ids(xml_data: str) -> List[str]:
    """Parse PubMed IDs from the search response."""
    # Placeholder logic for XML parsing, ideally using an XML library
    # For simplicity, assuming it returns a list of PubMed IDs.
    # Use libraries like `xml.etree.ElementTree` or `lxml` for real XML parsing.
    return ["12345678", "87654321"]  # Example PubMed IDs

def fetch_paper_details(pubmed_ids: List[str]) -> List[Dict]:
    """Fetch detailed paper information given PubMed IDs."""
    details_url = f"{PUBMED_BASE_URL}efetch.fcgi"
    papers = []
    
    for pubmed_id in pubmed_ids:
        paper_params = {
            "db": "pubmed",
            "id": pubmed_id,
            "retmode": "xml",
        }
        
        paper_response = requests.get(details_url, params=paper_params)
        paper_response.raise_for_status()
        
        # Extract the paper details (title, authors, etc.)
        paper_details = parse_paper_details(paper_response.text)
        papers.append(paper_details)
    
    return papers

def parse_paper_details(xml_data: str) -> Dict:
    """Extract the paper's details from the XML response."""
    # Placeholder logic, ideally using an XML parsing library
    return {
        "PubmedID": "12345678",
        "Title": "Sample Paper Title",
        "Publication Date": "2025-04-08",
        "Authors": [
            {"name": "John Doe", "affiliation": "Some Biotech Company", "email": "john@biotech.com"}
        ]
    }

def identify_non_academic(authors: List[Dict]) -> Tuple[List[str], List[str]]:
    """Identify non-academic authors and pharmaceutical/biotech companies."""
    non_academic_authors = []
    company_affiliations = []
    
    for author in authors:
        if 'biotech' in author['affiliation'].lower() or 'pharma' in author['affiliation'].lower():
            company_affiliations.append(author['affiliation'])
        else:
            non_academic_authors.append(author['name'])
    
    return non_academic_authors, company_affiliations
