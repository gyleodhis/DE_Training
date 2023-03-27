import pandas as pd
import plotly.express as px

cls=['#006400','#98FB98','#7FFF00','#00FF00','#32CD32','#00FF7F','#3CB371','#2E8B57','#228B22','#008000']
# cls=['#a70000','#a70000','#ff0000','#ff0000','#ff5252','#ff5252','#ff7b7b','#ff7b7b','#ffbaba','#ffbaba']
data_url = './static/DEMOOilData1.csv'
"""This function loads the data and returns a sorted dataframe"""
def get_data(a='data_url')->pd.DataFrame:
    df_oil = pd.read_csv(data_url)
    df_oil['Date'] = pd.to_datetime(df_oil['Date'])  # converting date column to type date
    df_oil = df_oil.sort_values('Oil_production',ascending=False).reset_index(drop=True)
    df_oil['Oil_production'] = df_oil['Oil_production'].fillna(0)
#     df_oil= df_oil.iloc[1:] #filter out the first data which looks weird
#     df_oil['Oil_production'] = pd.to_numeric(df_oil["Oil_production"],downcast="float")
    return df_oil

df_oil=get_data()

def oil_by_field():
    df_field = df_oil[['Field','Oil_production']]
    df_field=df_field.groupby('Field').sum().reset_index()
    return df_field

def fig_bar():
    return px.bar(oil_by_field().head(10), x='Field',y='Oil_production',color_discrete_sequence=cls,template="simple_white",
                  labels={'Oil_production': 'Oil Production in Barrels','Field':'Field'})

def fig_funnel():
    return px.funnel(oil_by_field().tail(10), x='Field', y='Oil_production',
                       labels={"Oil_production": "Oil Production in Barels", "Field": "Field"},
                    color_discrete_sequence=cls)