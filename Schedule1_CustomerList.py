import pandas as pd
import plotly.express as px

df = pd.read_csv('/home/vmichel/Downloads/Schedule1_CustomerList.csv')

df_melted = df.melt(id_vars=['Name','Location','Quality'],
                    value_vars= ['Like#1','Like#2','Like#3'],
                    var_name = 'Like_Type', value_name='Like')

like_counts = df_melted.groupby(['Location','Like']).size().reset_index(name='like_counts')

fig = px.treemap(like_counts,
                 path=['Location','Like'],
                 values='like_counts',
                 color='Location',
                 title='Customer Preferences by Location'
                 )
fig.show()
