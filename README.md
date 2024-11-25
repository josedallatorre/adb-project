# Advanced Database Project: Relational vs. NoSQL Databases

This project focuses on comparing MySQL (Relational Database) and MongoDB (NoSQL Database) for data modeling, querying, and optimizations. The chosen dataset is [Finance Transaction Dataset](https://www.kaggle.com/datasets/computingvictor/transactions-fraud-datasets?select=transactions_data.csv) from Kaggle.

## Prerequisites

1. Install Python (version 3.8 or above).
2. Set up MySQL (recommended: local installation).
3. Set up MongoDB (local installation or Atlas).
4. Clone this repository to your local system.

### Environment Configuration

Create a `.env` file in the root directory with the following structure to define database connection details:

```plaintext
# MySQL configuration
mysql_username=root
mysql_password=
mysql_hostname=localhost

# MongoDB configuration
mongo_username=
mongo_password=
mongo_hostname=
mongo_port=
```

### Project Setup

* Navigate to the project folder.
* Create a virtual environment:
```plaintext
python -m venv venv
```
* Activate the environment:
```plaintext
venv\Scripts\activate
```
* Run the first cell in the exercise.ipynb file to install the packages and update the pip 
