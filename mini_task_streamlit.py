  # app.py
import streamlit as st
from mini_task_class4 import scrape_website

st.title("Web Scraper and Report Generator")
st.write("Enter a URL and choose a crawl depth to scrape internal pages and download a report.")

url = st.text_input("Enter website URL:", "https://example.com")
depth = st.slider("Depth to crawl (0 = only main page)", 0, 3, 1)

if st.button("Scrape"):
    st.write("Scraping in progress...")
    report = scrape_website(url, depth=depth)
    # Save to file
    with open("report.txt", "w", encoding="utf-8") as f:
        f.write(report)
    st.success("Scraping completed! Download your report below.")
    st.download_button("📥 Download Report", report, file_name="report.txt")
 
