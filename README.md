# Credit-Risk-Analysis

This project focuses on extracting named entities from Telegram messages, tokenizing the data, and preparing it for further analysis. It utilizes various Python scripts, notebooks, and testing frameworks to facilitate efficient data processing.


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