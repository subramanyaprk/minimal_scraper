<!-- MINIMAL SCRAPER for Product Analysis

Asyncio

TASK:
1. Use async libraries to get all the links on a given webpage
2. Get the parsed links
3. Minimal scraper project



Input takes the depth parameter
That level of depth should be traversed to get the links
 -->
 
 SETUP:
 
 Pip install the dependencies - 
 
**pip install aiohttp
 pip install asyncio
 pip intsall requests
 
 Run the Python file fetch_url.py:
 
**python3 fetch_url.py
 
 Working:
 
 The fetch_async sets up the event loops and uses the run_until_complete to wait till all the URL fetches are completed to pass the control back so we can print the total time taken.
