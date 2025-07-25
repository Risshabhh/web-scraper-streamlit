Web Scraper and Report Generator

This is a simple tool built with Python and Streamlit that can scrape a website along with its internal pages, then generate a text report containing all the scraped content.

Features

Crawl a website up to a chosen depth
Follow internal links automatically
Collect and save page text into a single report.txt file
Clean and simple Streamlit interface for input and download
Ready to deploy on Streamlit Cloud
How it works

Enter a website URL in the app.
Select how deep you want the scraper to follow links (depth 1, 2, or 3).
The scraper visits the site and its subpages, extracts the page text, and combines everything.
A downloadable report is generated.
Project Structure

mini_task_streamlit.py            # Streamlit interface
mini_task_class4.py        # Core scraping logic
requirements.txt  # Required Python packages
README.md         # Project documentation
Running locally

Make sure you have Python 3 installed, then:

git clone https://github.com/<your-username>/web-scraper-streamlit.git
cd web-scraper-streamlit
pip install -r requirements.txt
streamlit run app.py
Streamlit will launch in your browser, usually at http://localhost:8501.

Deploying

Push this project to a GitHub repository.
Go to Streamlit Cloud, sign in, and create a new app.
Choose your repository and app.py as the entry point.
Deploy and share your Streamlit link.
Notes

Please make sure you scrape only websites you are allowed to.
Respect the site’s robots.txt and usage policies.
For large or deep crawls, consider adding rate limits to avoid overloading a server.
GitHub Repository: https://github.com/Risshabhh/web-scraper-streamlit/tree/e0ea932fb423a50d941b1cff21e5df4766ebf731
Live App on Streamlit: https://web-scraper-app-ca8vczgymqvglbpmmzh4xd.streamlit.app
