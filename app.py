# import libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# load dataframes
vehicles = pd.read_csv('processed_vehicles.csv')
sales = pd.read_csv('vehicle_sales.csv')

# display both dataframes
st.image("sombrero.png")
st.header('Used car sales data')
st.markdown("""
This app examines used car sales data and was built using
**Python libraries:** Pandas, Streamlit, plotly.express

The data can be viewed below:""")
st.markdown('vehicles.csv')
st.dataframe(vehicles)

st.markdown("sales.csv")
st.dataframe(sales)

# LINE GRAPH
# plot total sales per day

# every vehicle sold value total
sum_sales = sales.sales_dollars.sum()

# header
st.subheader('Sales')
st.markdown(
    f"The data is from May 2018 - April 2019. The total vehicle sales amounted to: ${sum_sales:,}")

# select box to choose y variable
feature = st.selectbox('Feature', ['sales_dollars', 'sales_in_units',
                                   'inventory_in_dollars', 'inventory_in_units'])

# line plot of sales over time
line_fig = px.line(sales,
                   x='index',
                   y=feature)

line_fig.update_layout(xaxis_title="Time in day intervals",
                       yaxis_title=f"Sum of {feature}",
                       width=800,
                       height=600,
                       )

# retrieve last listing date for feature addition
last_listing = vehicles['date_posted'].max()

# Add a vertical line for average price
line_fig.add_shape(type="line",
                   x0=last_listing, x1=last_listing,
                   y0=0, y1=sales[feature].max()+50,
                   line=dict(color='red', dash='dash'))

# add text annotation for the line
line_fig.add_annotation(
    x=last_listing,
    y=(sales[feature].max() + 10),
    text=f"Last listing date: {last_listing}",
    showarrow=True,
    arrowhead=1,
    ax=40,
    ay=-40,
    bordercolor="black",
    borderwidth=1,
    borderpad=4,
    opacity=1,
)

st.plotly_chart(line_fig)

# BAR PLOT
# average listing duration of vehicle make (how fast vehicle makes sell)

# header
st.subheader('Average listing duration for vehicle manufacturers')
st.markdown('How fast vehicles sell (brand / type / color)')

# create a select box for car colors
sorted_color = sorted(vehicles['paint_color'].unique())
selected_color = st.multiselect(
    'Vehicle color', sorted_color, sorted_color[:1])

# create a select box for car type
sorted_type = sorted(vehicles['type'].unique())
selected_type = st.multiselect(
    'Vehicle type', sorted_type, sorted_type[9:10])

# calculate the average listing duration by vehicle make and or type
average_make = vehicles[
    (vehicles['paint_color'].isin(selected_color)) &
    (vehicles['type'].isin(selected_type))].groupby(
    'make')['days_listed'].mean().reset_index()

# bar plot
bar_fig = px.bar(average_make,
                 x='make',
                 y='days_listed')

# order the bars by ascending height
bar_fig.update_layout(xaxis={'categoryorder': 'total ascending'})

# add titles/ labels
bar_fig.update_layout(
    xaxis_title="Vehicle make",
    yaxis_title="Average listing duration (days)",
    width=800,
    height=575,
)

# add a horizontal line
bar_fig.add_shape(
    type="line",
    x0=-1, x1=len(vehicles['make'].unique()) - 0.5,
    y0=vehicles['days_listed'].mean(), y1=vehicles['days_listed'].mean(),
    line=dict(color='Red', width=2, dash='dash'),
)

# Add an annotation if desired
bar_fig.add_annotation(
    x=5,  # horizontal position within the plot area
    y=45,
    text="Average duration of all vehicles: 39.55 days",
    showarrow=False,
    yshift=10,  # vertical shift
    bordercolor="black",
    borderwidth=1,
    opacity=0.8
)

# automatically adjust text size, format, and position
bar_fig.update_traces(texttemplate='%{y:.2f}', textposition='inside')

# Show the plot
st.write(bar_fig)

# BAR2
# average price of vehicle type

st.subheader("Vehicle average listing price ($)")
st.markdown('Select which features to few')

# create a select box for car colors
sort_color = sorted(vehicles['paint_color'].unique())
select_color = st.multiselect(
    'Vehicle color', sort_color, sort_color, key='1')

# create a select box for car type
sort_type = sorted(vehicles['type'].unique())
select_type = st.multiselect(
    'Vehicle type', sort_type, sort_type, key='2')

# calculate the average listing duration by vehicle make and or type
average_price = vehicles[
    (vehicles['paint_color'].isin(select_color)) &
    (vehicles['type'].isin(select_type))].groupby(
    'make')['price'].mean().reset_index()

# bar plot
fig3 = px.bar(average_price,
              x='make',
              y='price',
              text='price')

# automatically adjust text size, format, and position
fig3.update_traces(texttemplate='%{y:,.2f}', textposition='inside')

# order the bars by descending height
fig3.update_layout(xaxis={'categoryorder': 'total descending'})

# add titles/ labels
fig3.update_layout(
    xaxis_title="Vehicle type",
    yaxis_title="Average listing price ($)",
    width=800,
    height=575,
)

# add a horizontal line
fig3.add_shape(
    type="line",
    # extend line horizontally across the plot
    x0=-0.5, x1=len(vehicles['make'].unique()) - 0.5,
    # set at average_value
    y0=vehicles['price'].mean(), y1=vehicles['price'].mean(),
    line=dict(color='Red', width=2, dash='dash'),  # Style of the line
)

# add an annotation if desired
fig3.add_annotation(
    x='van',  # horizontal position within the plot area
    y=vehicles['price'].mean()+100,
    text=f'Average price: ${vehicles['price'].mean():,.2f}',
    showarrow=False,
    yshift=10,  # vertical shift
    bordercolor="black",
    borderwidth=1,
    opacity=0.8
)
# Show the plot
st.plotly_chart(fig3)


# SCATTER
st.subheader('Comparing price with release year of used cars')

# slider to select years
years = st.slider("Select a range of years", 1929, 2019, (2000, 2010))
st.write("Model years:", years)
st.markdown(
    'Once year range has been selected, please auto-scale the plot (6th icon to the right)')

# unpack the tuple
early, later = years

# filter range selection
time_zone = vehicles[(vehicles['model_year'] >= early) &
                     (vehicles['model_year'] <= later)]

# explore data
fig4 = px.scatter(time_zone,
                  x='model_year',
                  y='price',
                  color='condition',
                  category_orders={'condition': [
                      'salvage', 'fair', 'good', 'excellent', 'like new', 'new']}
                  )
fig4.update_layout(
    xaxis_title="Vehicle production year",
    yaxis_title="Price of vehicle ($)",
    width=800,
    height=575,
)
fig4.update_traces(opacity=0.5)
# Set x and y axis limits
fig4.update_xaxes(range=[vehicles['model_year'].min() -
                         1, vehicles['model_year'].max()+1])
fig4.update_yaxes(range=[0, 100000])

st.write(fig4)

# HISTO
st.subheader('Used car prices')

# create a select box for car conditions
sort_condition = sorted(vehicles['condition'].unique())
select_condition = st.multiselect(
    'Vehicle condition', sort_condition, sort_condition, key='99')

# create grouping
# calculate the average price by condition
average_condition = vehicles.groupby('condition')['price'].mean().reset_index()

# calculate the average price by condition
conditions = vehicles[(vehicles['condition'].isin(select_condition))]

# histogram plot
fig5 = px.histogram(conditions,
                    x='price',
                    nbins=230,
                    color='condition',
                    barmode='overlay',
                    )

# add an annotation
fig5.add_annotation(x=80000,
                    y=3250,
                    text=f"""Average prices:<br>
                    {average_condition.iloc[0, 0]}: ${average_condition.iloc[0, 1]:,.2f}<br>
                    {average_condition.iloc[1, 0]}: ${average_condition.iloc[1, 1]:,.2f}<br>
                    {average_condition.iloc[2, 0]}: ${average_condition.iloc[2, 1]:,.2f}<br>
                    {average_condition.iloc[3, 0]}: ${average_condition.iloc[3, 1]:,.2f}<br>
                    {average_condition.iloc[4, 0]}: ${average_condition.iloc[4, 1]:,.2f}<br>
                    {average_condition.iloc[5, 0]}: ${average_condition.iloc[5, 1]:,.2f}""",
                    showarrow=False,
                    bordercolor="black",
                    borderwidth=1,
                    opacity=0.8,
                    align="left"
                    )

fig5.update_layout(xaxis_title="Price ($)",
                   yaxis_title="Number of vehicles",
                   width=800,
                   height=575,
                   )

# Change transparency/visibility with 'opacity' parameter
fig5.update_traces(opacity=0.6)

# set x and y axis limits
fig5.update_xaxes(range=[0, 100000])
fig5.update_yaxes(range=[0, len(conditions['condition'])/10])

st.write(fig5)
