import argparse
import pandas as pd
from pubmed import fetch_papers, identify_non_academic
from typing import Optional

def save_to_csv(papers, filename: Optional[str]):
    """Save the papers data to a CSV file or print to console."""
    if not papers:
        print("No papers to save.")
        return

    data = []
    for paper in papers:
        authors, affiliations = identify_non_academic(paper['Authors'])
        data.append({
            "PubmedID": paper['PubmedID'],
            "Title": paper['Title'],
            "Publication Date": paper['Publication Date'],
            "Non-academic Author(s)": ", ".join(authors),
            "Company Affiliation(s)": ", ".join(affiliations),
            "Corresponding Author Email": paper['Authors'][0].get('email', '')  # Get email from first author
        })
    
    df = pd.DataFrame(data)
    try:
        if filename:
            df.to_csv(filename, index=False)
            print(f"Results saved to {filename}")
        else:
            print(df)
    except Exception as e:
        print(f"Error saving CSV: {e}")


def main():
    """Main function to handle command-line execution."""
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed")
    parser.add_argument("query", help="Query to search PubMed")
    parser.add_argument("-f", "--file", help="File to save results", default=None)
    parser.add_argument("-d", "--debug", help="Enable debug mode", action="store_true")

    args = parser.parse_args()
    
    if args.debug:
        print(f"Fetching papers with query: {args.query}")
    
    papers = fetch_papers(args.query)
    save_to_csv(papers, args.file)

if __name__ == "__main__":
    main()
