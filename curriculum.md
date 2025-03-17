
# **INTERMEDIATE PYTHON**

---

## **DAY 1 – Foundations and Control**

| Time | Topic | Step-by-Step Plan |
|------|-------|-------------------|
| **09:00 – 09:15** | Welcome & Intro | - Welcome and goals<br>- Salesforce context: "Why intermediate Python is critical in automation, integrations, and backend processing." |
| **09:15 – 10:45** | **Advanced Data Types** <br> (`namedtuple`, `defaultdict`, `deque`, `OrderedDict`) | 1. Explain problem: handling CRM-like customer data.<br>2. Live code: customer records with `namedtuple`.<br>3. `defaultdict` for grouping related data (like accounts, contacts).<br>4. Exercise: Build a simple contact management structure.<br>5. Q&A. |
| **10:45 – 11:00** | Break | |
| **11:00 – 12:30** | **Functional Programming** <br> (`map`, `filter`, `reduce`, `lambda`, `operator`) | 1. Why FP? Data transformations.<br>2. Live code: filter inactive leads, map emails, reduce revenue totals.<br>3. Exercise: Process a list of opportunities (filter closed, sum totals).<br>4. Demo: Decorators – add logging to functions.<br>5. Exercise: Decorator that tracks execution time. |
| **12:30 – 13:30** | Lunch | |
| **13:30 – 15:00** | **Generators and Iterators** | 1. Show large datasets (Salesforce reports, logs).<br>2. Live code: generator to stream records.<br>3. `itertools` demo: chaining daily reports.<br>4. Exercise: Build a generator that processes pages of API results.<br>5. Connect to next: use generator inside a context manager. |
| **15:00 – 15:15** | Break | |
| **15:15 – 16:30** | **Context Managers** | 1. Why? Resource handling (APIs, files).<br>2. Live code: mock API session with `with` statement.<br>3. Exercise: Context manager to simulate opening/closing Salesforce session.<br>4. Use context manager wrapping generator from previous session. |
| **16:30 – 17:00** | **Intro to Testing** | 1. Why tests matter in Salesforce ecosystem (deployments, releases).<br>2. Demo: basic test for data processing function.<br>3. Small exercise: write a test for the generator from earlier. |
| **17:00** | Wrap-up | Recap building blocks and link to Day 2: "We'll fully test and log this!" |

---

## **DAY 2 – Testing, Observability, and Data**

| Time | Topic | Step-by-Step Plan |
|------|-------|-------------------|
| **09:00 – 09:15** | Recap Day 1 | Q&A, recap how components connect. |
| **09:15 – 10:30** | **Testing (continued)** | 1. Test suites and coverage.<br>2. Live code: refactor yesterday's tests.<br>3. Exercise: Build full test coverage around data processing functions.<br>4. Tie-in: logging failures. |
| **10:30 – 10:45** | Break | |
| **10:45 – 11:45** | **Logging** | 1. Why logs matter (SF integrations, error tracking).<br>2. Live code: logging in processing pipeline.<br>3. Exercise: add logs to existing decorators, generators.<br>4. Use different log levels (INFO, ERROR). |
| **11:45 – 12:30** | **NumPy** | 1. Why math? Stats on Salesforce reports (revenue, lead scoring).<br>2. Demo: array of monthly revenue.<br>3. Exercise: calculate average deal size, growth rates. |
| **12:30 – 13:30** | Lunch | |
| **13:30 – 14:30** | **Pandas** | 1. Load CSV of mock Salesforce leads.<br>2. Group by industry, sum revenues.<br>3. Exercise: clean dataset (missing values), aggregate by region. |
| **14:30 – 15:45** | **Scraping (Full Session)** | 1. Show Salesforce Help API / public data pages (mock).<br>2. Live code: scrape table from HTML.<br>3. Exercise: scrape JSON from public API and push into Pandas.<br>4. Build pipeline: Scrape → Clean (Pandas) → Log steps. |
| **15:45 – 16:00** | Break | |
| **16:00 – 17:00** | Day task | Build a mini ETL pipeline:<br>Scrape -> Clean -> Log -> Test. |
| **17:00** | Wrap-up | Tease Day 3: "Now we'll scale and serve this data!" |

---

## **DAY 3 – Concurrency, Networking, and Web**

| Time | Topic | Step-by-Step Plan |
|------|-------|-------------------|
| **09:00 – 09:15** | Recap Day 2 | Quick demo of best ETL solution from yesterday. |
| **09:15 – 10:30** | **Multiprocessing and Threading** | 1. Why? Salesforce batch jobs, parallel API calls.<br>2. Live code: threaded scraper.<br>3. Exercise: scrape multiple pages concurrently.<br>4. Discuss shared state (rate limits, etc.). |
| **10:30 – 10:45** | Break | |
| **10:45 – 12:00** | **Networking** | 1. Socket basics.<br>2. Live code: simple server to accept data (simulate Salesforce data hook).<br>3. Exercise: build a client to push data.<br>4. Optional: JSON-REST API calls to public data. |
| **12:00 – 13:00** | Lunch | |
| **13:00 – 14:30** | **Django Intro** | 1. Why web? Internal dashboards for Salesforce data.<br>2. Live demo: Django project scaffold.<br>3. Show how to build a view to display cleaned Pandas data.<br>4. Exercise: add a route and view to render dummy data. |
| **14:30 – 15:45** | **Final Project** | Group exercise:<br>1. Scrape some data.<br>2. Clean and process.<br>3. Store in Pandas.<br>4. Serve via Django.<br>5. Log all steps and write minimal tests. |
| **15:45 – 16:00** | Break | |
| **16:00 – 17:00** | Presentations + Wrap-up | - Groups show final project.<br>- Final Q&A.<br>- Feedback and next steps. |

---
