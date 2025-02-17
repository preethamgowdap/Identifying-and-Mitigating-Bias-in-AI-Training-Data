import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

# Sample data for visualization
data = {'Metric': ['Accuracy', 'Precision', 'Recall', 'F1-Score'], 'Value': [0.92, 0.88, 0.91, 0.89]}
df = pd.DataFrame(data)

# Create Dash app
app = dash.Dash(__name__)
app.layout = html.Div([
    dcc.Graph(figure=px.bar(df, x='Metric', y='Value', title='Model Performance Metrics'))
])

if __name__ == '__main__':
    app.run_server(debug=True)