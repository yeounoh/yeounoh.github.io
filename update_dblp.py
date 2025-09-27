import requests
import xml.etree.ElementTree as ET
import os

DBLP_PID = "132/1869" # e.g., "11/399"
DBLP_URL = f"https://dblp.org/pid/{DBLP_PID}.xml"
PUBLICATIONS_DIR = "_publications"

# Ensure the publications directory exists
os.makedirs(PUBLICATIONS_DIR, exist_ok=True)

# 2. Function to sanitize title for permalink
def create_permalink_title(title):
    # Simplistic function: convert to lowercase, replace non-alphanumeric with hyphen
    return "".join(c for c in title if c.isalnum() or c.isspace()).lower().replace(' ', '_')[:30]

# 3. Fetch and Parse dblp Data
try:
    response = requests.get(DBLP_URL)
    response.raise_for_status() # Raise HTTPError for bad responses
    
    # DBLP XML is returned with a root tag 'dblp'
    root = ET.fromstring(response.content)
    
except Exception as e:
    print(f"Error fetching or parsing DBLP data: {e}")
    exit()

# 4. Process Each Publication
# Publications are usually nested under <dblp> -> <r> -> <article>, <inproceedings>, etc.
for rec in root.findall('r'): 
    # Find the single publication tag (e.g., <article>, <inproceedings>)
    pub = rec[0] 
    pub_type = pub.tag
    
    # Extract common metadata
    title_element = pub.find('title')
    title = title_element.text.strip().replace('"', '\\"') if title_element is not None and title_element.text else "No Title"

    year_element = pub.find('year')
    year = year_element.text if year_element is not None else 'YYYY'
    
    # Venue/Collection - often in 'journal' or 'booktitle'
    venue_element = pub.find('journal') or pub.find('booktitle') or pub.find('publisher')
    venue = venue_element.text if venue_element is not None else ''
    
    # Find the DOI or URL (usually the first 'ee' element)
    paperurl = next((ee.text for ee in pub.findall('ee') if ee.text and 'doi' in ee.text), '')
    if not paperurl:
        # Fallback to the first available URL if no DOI is found
        paperurl = next((ee.text for ee in pub.findall('ee') if ee.text), '')


    # Determine the output filename and permalink structure
    # You might customize this to fit your academicpages template logic
    file_title = create_permalink_title(title)
    filename = os.path.join(PUBLICATIONS_DIR, f"{year}_{file_title}.md")
    permalink_suffix = f"{year}_{file_title}"
    
    # Create the Jekyll Front Matter content
    content = f"""---
title: "{title}"
collection: publications
category: papers
permalink: /publication/{permalink_suffix}'
venue: '{venue}'
paperurl: '{paperurl}'
---
"""
    
    # Write the file
    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Generated file: {filename}")

print("DBLP update complete. Check the _publications directory.")