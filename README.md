# British Airways Data Science Simulation – Forage ✈

This repository contains both Task 1 and Task 2 completed as part of the **British Airways Data Science Virtual Experience Program** hosted on [Forage](https://www.theforage.com/).  
The project demonstrates how data-driven decision-making can support strategic operations at British Airways, focusing on lounge planning and customer behavior analysis.

---

##  Tasks Overview

###  Task 1: Lounge Eligibility Analysis
Analyzed British Airways’ summer schedule data to evaluate passenger lounge eligibility across various flight segments.

####  Key Highlights:
- Created a `GROUP` feature combining haul type, time of day, and arrival region
- Aggregated Tier 1–3 eligible passengers and calculated their percentages
- Added business insights and mapped example destinations
- Exported a stakeholder-friendly lookup table in Excel

 Files:
- `code/analyze_lounge.py`  
- `outputs/lounge_lookup_table.xlsx`  
- `data/British Airways Summer Schedule Dataset.xlsx` *(not included if proprietary)*

---

###  Task 2: Predicting Customer Buying Behaviour
Scraped and analyzed customer review and booking data to identify patterns and build a predictive model for purchase behavior.

####  Key Highlights:
- Performed EDA on structured customer booking data
- Built classification models (e.g., Logistic Regression, Random Forest)
- Evaluated model using Accuracy, F1 Score, Precision, and Recall
- Identified key predictors like `purchase_lead` that impact buying decisions

 Files:
- `code/Getting Started.ipynb`  
- `data/customer_booking.csv`  
- `report/summary.key` *(summary of findings)*

---

##  Tools & Techniques

- Python: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`
- NLTK for text processing
- TensorFlow (used in validation comparison)
- GridSearchCV for hyperparameter tuning
- Confusion matrix, learning/validation curves, and F1 Score for evaluation

---

##  Project Structure

british-airways-data-science-simulation/
├── README.md
├── code/
│ ├── analyze_lounge.py
│ └── Getting Started.ipynb
├── data/
│ ├── British Airways Summer Schedule Dataset.xlsx
│ └── customer_booking.csv
├── outputs/
│ └── lounge_lookup_table.xlsx
├── report/
│ └── summary.key



---

##  Sample Insights

### Lounge Eligibility:
- **LONG Afternoon – Asia:** High Tier 1 and Tier 2 percentages → potential for more premium service offerings
- **SHORT Evening – Europe:** Low Tier 1 traffic → fewer premium passengers

### Customer Behavior:
- `purchase_lead` was the strongest predictor of buying behavior
- Model achieved ~85% accuracy, but recall for minority buyers was low, suggesting a class imbalance issue

---

##  Disclaimer
This project was developed as part of a **virtual job simulation** for educational purposes. It does not represent real consulting work for British Airways.

---

##  Author

**Komala Belur Srinivas**  
 [komalsrinivas20@gmail.com](mailto:komalsrinivas20@gmail.com)  
 [LinkedIn](https://www.linkedin.com/in/yourprofile)

