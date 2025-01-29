# Credit-Risk-Analysis

This project involves building a Credit Scoring Model for Bati Bank to assess customer risk, assign credit scores, and optimize loan amounts using eCommerce transaction data, while implementing MLOps practices for model deployment and management.

## Project Structure


```
├── notebooks
│   ├── 1.0-data-preprocessing.ipynb 
│   ├── 2.0-data-exploration.ipynb
│   ├── 3.0-feature-engineering.ipynb
│   ├── 5.0-Model-training.ipynb
│   ├── README.md                 
│   ├── __init__.py               
│
├── README.md                   
├── requirements.txt            
├── scripts
│   ├── README.md                 
│   ├── __init__.py               
│   ├── preprocess_data.py  
│   ├── feature_engineer.py  
│   ├── train_models.py  
│   ├── estimate_woe.py  
│   ├── eda
│   │   ├── bahavior_analysis.py
│   │   ├── correlation_analysis.py
│   │   ├── fraud_analysis.py
│   │   ├── provider_analysis.py
│   │   ├── transaction_analysis.py         
│
├── src            
│   ├── __init__.py         
├── app            
│   ├── main.py
│
├── tests
│   ├── __init__.py  
│

```

## Installation

1. Clone the repository:
   ```bash
   git clone <repo_url>
   cd <project_directory>
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv/Scripts/activate`
   pip install -r requirements.txt
   ```

## Contribution

Feel free to fork the repository, make improvements, and submit pull requests.