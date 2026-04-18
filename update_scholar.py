from scholarly import scholarly
import os

SCHOLAR_ID = "MhlvmB4AAAAJ"
PUBLICATIONS_DIR = "_publications"

os.makedirs(PUBLICATIONS_DIR, exist_ok=True)

def create_permalink_title(title):
    return "".join(c for c in title if c.isalnum() or c.isspace()).lower().replace(' ', '_')[:30]

print(f"Fetching publications for scholar ID: {SCHOLAR_ID}")

try:
    author = scholarly.search_author_id(SCHOLAR_ID)
    author = scholarly.fill(author)
except Exception as e:
    print(f"Error fetching scholar data: {e}")
    exit()

print(f"Found {len(author['publications'])} publications.")

for pub in author['publications']:
    print(f"Processing: {pub['bib']['title']}")
    try:
        scholarly.fill(pub) # Fetch full details
        bib = pub['bib']
        
        title = bib.get('title', 'No Title').replace('"', '\\"')
        year = bib.get('pub_year', 'YYYY')
        venue = bib.get('venue', '')
        paperurl = pub.get('pub_url', '')
        
        file_title = create_permalink_title(title)
        filename = os.path.join(PUBLICATIONS_DIR, f"{year}_{file_title}.md")
        permalink_suffix = f"{year}_{file_title}"
        
        content = f"""---
title: "{title}"
collection: publications
category: papers
permalink: /publication/{permalink_suffix}
venue: '{venue}'
paperurl: '{paperurl}'
---
"""
        
        if not os.path.exists(filename):
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Generated file: {filename}")
        else:
            print(f"File already exists: {filename}")
            
    except Exception as e:
        print(f"Error processing publication {pub['bib']['title']}: {e}")

print("Scholar update complete.")
