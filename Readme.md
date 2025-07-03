# 🏙️ Real Estate Web Scraper

A Python-based web scraper that extracts property listings from Redfin in New York City using Playwright. This project demonstrates scalable scraping of dynamic websites, modular architecture, and data export for analysis.

---

## 🚀 Features

- ✅ Scrapes real estate listings from Redfin (New York City)
- ✅ Handles dynamic content with Playwright
- ✅ Automatic scrolling and pagination support
- ✅ Modular, production-grade code
- ✅ Exports listings to CSV for analysis

---

## 📁 Project Structure


```
real-estate-scraper/
├── main.py                  
├── requirements.txt        
├── .env.example              
├── scraper/                 
│   ├── config.py
│   ├── fetcher.py
│   ├── parser.py
│   ├── exporter.py
│   └── utils.py
├── data/
    └── listings.csv            

```
---

## 📦 Installation

### 1. Clone the Repository
```
git clone https://github.com/yourusername/real-estate-scraper-nyc.git
cd real-estate-scraper-nyc
```

### 2. Install Python Dependencies

```
python -m venv venv
source venv/bin/activate  # or venv\\Scripts\\activate on Windows
pip install -r requirements.txt
```

### 3. Install Playwright Browsers

```
playwright install
```

### 4. Create `.env` File

```
cp .env.example .env
```

---

## ⚙️ Usage

```
python main.py
```

The scraper will visit multiple pages of Redfin listings, auto-scroll to load all items, extract data such as:

* Address
* Price
* Bedrooms / Bathrooms
* Square Footage
* Agent Info
* Listing URL

Output is saved as `data/listings.csv`.

---

## 📊 Sample CSV Output

| Address                   | Price     | Beds | Baths | Sqft  | Agent      | URL                                           |
| ------------------------- | --------- | ---- | ----- | ----- | ---------- | --------------------------------------------- |
| 123 Main St, New York, NY | \$950,000 | 2    | 2     | 1,200 | Compass RE | [https://redfin.com/](https://redfin.com/)... |

---

## 🛡️ Ethical Disclaimer

This project is intended for educational and portfolio use only. Ensure you follow Redfin's [robots.txt](https://www.redfin.com/robots.txt) and **terms of service** when scraping any data.

---

## 🧠 What I Learned

* Working with asynchronous scraping and browser automation
* Handling dynamic pages using scrolling
* Structuring a clean Python scraping project
* Data cleaning and CSV exporting

---

## 📬 Contact

**Natnael Yohannes** – [LinkedIn](https://www.linkedin.com/in/natnael-yohannes-gesiab/) • [Upwork Profile](https://www.upwork.com/freelancers/~01cfd1e9bf46f6a96c)
📧 Email: [yohannesnatnael9@gmail.com](mailto:yohannesnatnael9@gmail.com)

---