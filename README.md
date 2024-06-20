# Data Scientist Job Descriptions Analysis

## Overview
This project aims to analyze web-scraped data containing job descriptions for data scientists and engineers. The analysis includes data cleaning, exploration, and visualization using Python libraries such as pandas, numpy, and matplotlib.

## Objectives
- Perform basic cleaning operations on the dataset.
- Generate plots for the following:
  - Distribution of salaries
  - Top 10 most frequently used words in the job descriptions
  - Top 10 Most Frequently Used Words in Job Descriptions (Excluding Common Words)
  - Correlation between ratings and salaries
  - Correlation between employee number and salaries
  - Count of easy apply jobs
  - Average salary by company size
- Expand analysis using interactive visualizations with Plotly or Bokeh.
- Build predictive models to forecast salaries based on various features.
  - Try different machine learning algorithms: linear regression, decision trees, and random forests.
  - Showcase model performance using recommended metrics for each selected approach.
  - Additional Visualizations for Predictive Modeling:
      - Scatter Plot with Regression Line: Visualize how the model fits the data.
      - Residual Plot: Check for homoscedasticity and identify patterns in residuals.
      - Actual vs. Predicted Values Plot: Visualize the accuracy of predictions.
      - Learning Curves: Diagnose if the model is overfitting or underfitting.
      - Feature Importance: Understand which variables have the most impact on salary.
- Use NLP techniques to cluster job descriptions into different categories.
  - Analyze clusters/groups and assign meaningful categories
  - Additional Visualizations for NLP Clustering:
      - Scatter Plot with Centroids: Visualize clusters and centroids.
      - Elbow Method Plot: Determine the optimal number of clusters (K).
      - Silhouette Plot: Evaluate the quality of clusters.

## Materials
- **Dataset:** [Data Scientist Jobs on Kaggle](https://www.kaggle.com/datasets/andrewmvd/data-scientist-jobs)
- **IDE:** Jupyter Notebook/Lab
- **Visualization Libraries:** Matplotlib, Plotly, Bokeh

## Repository Structure
- `data/`: Contains the raw and processed data files.
- `notebooks/`: Jupyter notebooks with the analysis and visualizations.
  - `01_data_cleaning.ipynb`: Data cleaning operations.
  - `02_visualization_drop_na.ipynb`: Data visualization with drop NA.
  - `03_visualization_fill_nan.ipynb`: Data visualization with fill NA.
  - `04_interactive_visualizations.ipynb`: Interactive visualizations.
  - `05_predictive_modeling.ipynb`: Predictive modeling with machine learning algorithms.
  - `06_nlp_clustering.ipynb`: NLP clustering of job descriptions.
- `scripts/`: Python scripts for data cleaning and manipulation.
  - `dash_app.py`: Script for the interactive dashboard using Plotly Dash.
- `README.md`: Project overview and documentation.


## Getting Started
1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/kristinacovic/mentorship.git
    ```
2. Navigate to the project directory:
    ```bash
    cd mentorship
    ```
3. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```
4. Open the Jupyter Notebook:
    ```bash
    jupyter notebook
    ```
5. Explore the notebooks in the `notebooks/` directory.


## Requirements
The required Python libraries are listed in `requirements.txt`. To create a `requirements.txt` file, you can use the following command:
```bash
pip freeze > requirements.txt
