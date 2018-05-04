# Assignment 5 - Scraping a website

Please submit your completed Markdown file to me by June 20, 2017.

1. Use Python's `urllib` module to submit an HTTP request to the URL provided below.  This website is hosted by the US CDC and provides a table breaking down the prevalence of arthritis in different categories of adults living in the State of New York.  Use BeautifulSoup to extract the table element.  Provide your Python source below and run the command provided at the end of the code block:
   ```python
   url = 'https://www.cdc.gov/arthritis/data_statistics/state-data/newyork.html'
   
   # provide your source code here
   
   # run this command and paste the result below
   tables[0].text.split('\n\n\n')  # assumes you're using the variable name `tables`
   
   ```


2. Modify `examples/scraper.py` to output the contents of the `results` list in a CSV format without a header row, where each cell of the CSV is the cause of death (string), *i.e.*, the first element of the tuple.  
   ```python
   # insert your code that replaces this lines of the script:
   # print (results)
   ```

3. Obviously `scraper.py` does not parse the header row of the table, which is identified by `<th>` tags.  Write a new function that takes the `tables[0]` variable as its argument, extracts the header row, and returns a list of its `<td>` entries as strings (as in `soup2table`):
    ```python
    # insert your code here
    ```

4. (**Optional, no grade**)  Suggest a website where scraping might be useful for your research:
    ```html
    
    ```
