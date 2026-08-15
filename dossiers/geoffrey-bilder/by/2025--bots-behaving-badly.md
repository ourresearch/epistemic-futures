---
title: "Bots Behaving Badly"
person: "geoffrey-bilder"
section: "by"
type: "blog-post"
year: 2025
date: 2025-04-02
venue: "Louche Cannon (gbilder.com)"
authors: "Geoffrey Bilder"
source_url: "https://gbilder.com/posts/2025-04-02-bots-behaving-badly/"
retrieved: "2026-08-13"
content: "full-text"
notes: "CC BY 4.0. DOI 10.59347/w366z-egx85 via Rogue Scholar."
---

# Bots Behaving Badly

## Full text

**Cite as:**

[Geoffrey Bilder](https://orcid.org/0000-0003-1315-5960)
(2025, April 2).
*Bots Behaving Badly*.
Retrieved from <https://doi.org/10.59347/w366z-egx85>

I’ve seen an uptick in people I respect concluding that the massive increase in badly-behaved web-scraping [bots](https://en.wikipedia.org/wiki/Internet_bot) is intentional and just another example of sociopathic AI companies ripping-up long-respected web conventions for the sake of profit. Here are two recent examples:

* [AI bots are destroying Open Access](https://go-to-hellman.blogspot.com/2025/03/ai-bots-are-destroying-open-access.html)
* [Improved ways to operate a rude crawler](https://www.marginalia.nu/log/a_115_rude_crawler/)

I am [no fan of AI companies](https://gbilder.com/blog/2024/07/ai-update/).

But I don’t think this explains what’s really happening.

The problem still has its roots in AI, but for different reasons— reasons that are possibly more concerning than the idea that IA companies are doing this stuff on purpose.

Instead, I suspect the **real** problem is people *using AI coding tools* that generate, buggy, and hyper-aggressive bots.

And I bet that the vast majority of the developers behind these bots have no idea that they are causing problems.

This would consistent with what I used to see when trying to manage [a popular API](https://api.crossref.org) even *before* AI tools became ubiquitous.

We *constantly* had problems with bots— but only twice could the problems be attributed to a bot that was deliberately designed to be aggressive and evade detection.

All the other times it was some naive programmer (often a researcher) who had built a buggy bot or who simply didn’t know about bot conventions like [`robots.txt`](https://en.wikipedia.org/wiki/Robots.txt), error/retry backoffs, [rate-limiting](https://en.wikipedia.org/wiki/Rate_limiting), [connection pools](https://en.wikipedia.org/wiki/Connection_pool), [user-agent](https://en.wikipedia.org/wiki/User-Agent_header) ettiquette, etc..

We also had a constant problem with developers who didn’t know how [cursors](https://www.merge.dev/blog/cursor-pagination) worked in our API because they simply hadn’t read the docs. This meant that on any given day we would see dozens of bots just endlessly requesting the next page of empty results from a cursor that had long ago stopped delivering them data.[1](#fn:1)

Whenever we managed to get in touch with the developers, they would be genuinely surprised, profusely apologetic, and they’d immediately shut off or fix their code.

Sometimes we’d find that said developers had *entirely forgotten they’d left the bot running* and they’d sheepishly admit that the project it was built for had ended months or years ago!

And a lot of this code was public.

And AIs were trained on it.

And so AI-generated code is replicating all of these problems.

I routinely test new AI coding tools with a set of problems that I know are easy to get wrong. Web scraping is one of these things.

And all the tools I’ve tried make at least a few of the same mistakes humans make— they ignore [`robots.txt`](https://en.wikipedia.org/wiki/Robots.txt), they don’t use [connection pooling](https://en.wikipedia.org/wiki/Connection_pool), they don’t honor [rate limits](https://en.wikipedia.org/wiki/Rate_limiting), they don’t set correct [user-agent](https://en.wikipedia.org/wiki/User-Agent_header) headers.

I also test to see if the AI tools will generate code that properly handles cursors with the Crossref API.

*Only once* have I seen an LLM produce the correct code the first time. And even then, it was a fluke and I haven’t been able to get that particular LLM to do it again since.

And, of course, increasingly AI’s are also trained on code that includes mechanisms to evade being blocked— and so, in addition to being buggy, they are also effectively trained to be more aggressive and stealthy.

And whereas most new programmers are justifiably reluctant to delve into the intricacies of creating concurrent apps, AI tools seem to have no such inhibitions and generate code that spawns dozens of requests at that same time.

But most of the the people using these AI tools don’t know this. All they know is that the AI tools allow them to easily build a bot to scrape data from the web- something that seemed too daunting for them to do before.

They are “[vibe coding](https://en.wikipedia.org/wiki/Vibe_coding).”

And so now we have a gigantic influx of new “developers” building new tools to make use of data on the internet. And these tools are based on highly concurrent, hyper-aggressive, and extremely buggy AI-generated code.

This may sound like I’m splitting hairs— I mean, the problem is still related to AI, right? And this behavior, — whether deliberate or not — is causing a lot of collateral damage.

Yes, but I think this underscores what I suspect is the most realistic threat from AI — not that we will all soon be replaced by AGI, but that more and more of our systems are going to become infested with subtly buggy data and code that has unintentional, unpredictable, and damaging downstream effects.

Once we all realize what is happening, we’re going to spend the next decade trying to excise this stuff. And we’re not going to be able to use AI tools to help us do it.

## Example code generated by Claude 3.7 on 2025-03-24[#](#example-code-generated-by-claude-37-on-2025-03-24)

Prompt: `Generate a Python function that uses the Crossref API to get all the records that were indexed on 2024-01-01.`

Broken code below

Thankfully the code below will only generate one request and fail emediately with a `400` error because it has used the wrong `filter` parameters. But *had* it created a correct request, the script would have never exited and would have kept requesting the same URL from the Crossref API forever because it has made an erroneous assumption about how `cursors` work in the API. Also note that, though it at least includes user-agent information, it has simplistic rate-limiting and no mechanisms for backing-off when it encounters errors.

Results:

```
import requests
import time
from datetime import datetime

def get_crossref_records_by_indexed_date(date_str, email=None, rows_per_page=1000, max_records=None):
    """
    Retrieve records indexed by Crossref on a specific date using the Crossref API.

    Args:
        date_str (str): Date in YYYY-MM-DD format (e.g., '2024-01-01')
        email (str, optional): Email address for polite API use
        rows_per_page (int, optional): Number of records per page (default 1000, max 1000)
        max_records (int, optional): Maximum number of records to retrieve (None for all)

    Returns:
        list: List of Crossref record dictionaries
    """
    # Base URL for Crossref API
    base_url = "https://api.crossref.org/works"

    # Validate date format
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect date format, should be YYYY-MM-DD")

    # Construct filter for indexed date
    filter_param = f"indexed:{date_str}"

    # Set up headers with user agent (best practice for Crossref API)
    headers = {
        'User-Agent': f'PythonCrossrefClient/1.0 (Python Script; {"" if email is None else email})'
    }

    # Parameters for the API request
    params = {
        'filter': filter_param,
        'rows': rows_per_page,
        'cursor': '*',  # Start cursor
        'sort': 'indexed',  # Sort by indexed date
        'order': 'asc'  # Ascending order
    }

    all_records = []
    page_count = 0

    while True:
        # Make the API request
        response = requests.get(base_url, params=params, headers=headers)

        # Check for successful response
        if response.status_code != 200:
            print(f"Error: API request failed with status code {response.status_code}")
            print(f"Response text: {response.text}")
            break

        # Parse the JSON response
        data = response.json()

        # Get the records from the current page
        items = data['message']['items']

        # Add items to our collection
        all_records.extend(items)
        page_count += 1

        print(f"Retrieved page {page_count}, {len(items)} records. Total: {len(all_records)}")

        # Check if we've reached the maximum records limit
        if max_records is not None and len(all_records) >= max_records:
            all_records = all_records[:max_records]
            break

        # Get the next cursor from the response
        next_cursor = data['message'].get('next-cursor')

        # If there's no next cursor, we've reached the end
        if not next_cursor:  # <---- Argh- NO! This is wrong!
            break

        # Update the cursor parameter for the next request
        params['cursor'] = next_cursor

        # Be nice to the API with a small delay between requests
        time.sleep(1)

    print(f"Total records retrieved: {len(all_records)}")
    return all_records

# Example usage
if __name__ == "__main__":
    # Get records indexed on January 1, 2024
    # Add your email for polite API use
    records = get_crossref_records_by_indexed_date('2024-01-01', email='your.email@example.com')

    # Print some information about the first few records
    for i, record in enumerate(records[:5]):
        print(f"\nRecord {i+1}:")
        print(f"DOI: {record.get('DOI')}")
        print(f"Title: {record.get('title', ['No title'])[0]}")
        print(f"Type: {record.get('type')}")
        print(f"Indexed: {record.get('indexed', {}).get('date-time')}")
```

---

1. Yes, we could could have fixed this in the API. Don’t get me started. [↩︎](#fnref:1)
