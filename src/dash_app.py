import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
from collections import Counter
import re

# Load the data
df = pd.read_csv('../data/processed/DataScientist_cleaned.csv')  # Ensure this path is correct

# Preprocess for common words without excluding connectors
all_descriptions = ' '.join(df['Job Description']).lower()
all_descriptions = re.sub(r'[^a-z\s]', '', all_descriptions)
words = all_descriptions.split()
word_counts_with_connectors = Counter(words).most_common(10)
common_words_with_connectors_df = pd.DataFrame(word_counts_with_connectors, columns=['word', 'count'])

# Preprocess for common words excluding connectors
stop_words = set(['and', 'the', 'to', 'in', 'a', 'with', 'an', 'for', 'of', 'on', 'at', 'by', 'from', 'about', 'as', 'into', 'like', 'through', 'after', 'over', 'between', 'out', 'against', 'during', 'without', 'before', 'under','other','this', 'around','are','be','that','or', 'is','you','we','will','our', 'among'])
words_excluding_connectors = [word for word in words if word not in stop_words]
word_counts_without_connectors = Counter(words_excluding_connectors).most_common(10)
common_words_without_connectors_df = pd.DataFrame(word_counts_without_connectors, columns=['word', 'count'])

# Initialize the app
app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='salary-distribution', figure=px.histogram(df, x='Salary Estimate', title='Distribution of Salaries')),
    dcc.Graph(id='top-words-with-connectors', figure=px.bar(common_words_with_connectors_df, x='word', y='count', title='Top 10 Most Frequently Used Words (Including Connectors)')),
    dcc.Graph(id='top-words-without-connectors', figure=px.bar(common_words_without_connectors_df, x='word', y='count', title='Top 10 Most Frequently Used Words (Excluding Connectors)')),
    dcc.Graph(id='ratings-salaries', figure=px.scatter(df, x='Rating', y='Salary Estimate', title='Correlation between Ratings and Salaries')),
    dcc.Graph(id='employees-salaries', figure=px.scatter(df, x='Size', y='Salary Estimate', title='Correlation between Employee Number and Salaries'))
])

if __name__ == '__main__':
    app.run_server(debug=True)
