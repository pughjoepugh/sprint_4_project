# sprint_4_project
_________
### Introduction:<br>
The purpose of this exercise is to analyze used car sales data from the United States and produce a web app to share findings. First, the data will be loaded, then opened and inspected in order to understand the structure and potential issues. Next is processing the data. By making necessary or useful updates, the data will be prepared for further data exploration.

Preprocessing the data will consist of two parts. The first part is cleaning the data. This will ensure the data is accurate and consistent. Techniques involved are:

Filling Missing Values: Data points that are missing will be filled in to avoid errors. For quantitative data, an average from similiar data will be utilized; for qualitative data points, the most common entry among similiar data.

Standardizing Values: Data entries may have different spelling or formats from eachother while meaning to express the same value. An example that comes up is (f-150, f150, f_150 superduty)

Correcting Data Types: Ensure each column of data is in the correct format, such that numbers are numbers, and dates are dates.

Feature Engineering: Creation of new data columns that might be useful, like extracting the manufacturer from a model column.

Most of the preprocessing will be done in the preprocessing notebook ('PreProcessing.ipynb'). Converting dates to datetime format as well as the creation of a second dataframe storing sales data, will be conducted in the EDA notebook ('EDA.ipynb')

At the end of preprocessing, the state of the data has been saved as: processed_vehicles.csv
After the creation of the sales dataframe, it was stored in the root directory as: vehicle_sales.csv
The original data file is located in the root directory and is titled 'vehicles_us.csv'

### EDA
___
Most of the preprocessing was be done in the preprocessing notebook ('PreProcessing.ipynb'). Converting dates to datetime format as well as the creation of a second dataframe storing sales data, will be conducted in the EDA notebook ('EDA.ipynb')

A second dataframe will be constructed with data from the pre-processed dataframe. The second dataframe will focus on sales. columns will be date, sales_in_units, sales_in_dollars, inventory_in_units, inventory_in_dollars (based on sale price). The original dataframe had listing dates and how many days the vehicle was for sale. I used this information to create a sale date. And anytime time between listing and sold would refer to a time when the vehicle was in the inventory.

Analyzing the Data: <br.>
In this notebook will be several plots created in order to further investigate the data.  Plotly.express is the visualization library utilized. 

Statistical Analysis: <br>
Various statistical calculations will be made in order to interpret data and draw conclusions, identifying trends or correlations.

### Insights & conclusions
___
The primary take away I got from exploring the data was inventory size. Over the course of the dataset, vehicles are listed and sold. The inventory starts at zero and climbs all the way to 6000 vehicles. The inventory will hover around 6000 until they the last day of listing. From then vehicles are only sold off.

Assumptions being made: 
each vehicle takes up the same space/ parking spot.
vehicles are being sold on a percent markup. Purchase price of vehicles was not provided, only the listing price. (not technically the sale price)
Inventory was a limiting factor, maybe it wasn't

Inventory size is important because certain vehicles traits have different listing durations. Example: hatchback vehicles have a below average sale price, and an above average listing duration. Hatchbacks generate less revenue per vehicle. 

Over the datasets timeframe they sold $625,125,255 in vehicles. I do not work in car sales. But that sounds like a congratulations!

### Tools
___
Tools being used during the analysis are:

Pandas: <br>
Library with tools used for data manipulation and analysis. All tables being displayed are in the pandas dataframe format. This is the primary tool used for cleaning, transforming, and aggregating the dataset.

NumPy: <br>
A library designed to handles numerical support across larger datasets.

Streamlit:<br>
A library used to build web applications with an emphasis on data science. Streamlit allows for creation of interactive applications to share data insights

Plotly Express:<br>
A data visualization library used to create interactive plots and visualizations.

Datetime:<br>
Datetime is a module used to interupt, handle, and change date or time data.

Render:<br>
A web application hosting site. Render will be linked to a gitHub account hosting this project/ repository.

GitHub:<br>
A web-based platform that allows users to store, share, and manage code. Github is also a service that facilitates version control, allowing multiple contributers to make changes, while offering the means to correct potential mistakes.

VScode:<br>
IDE or coding platform used to in creation of this project.
