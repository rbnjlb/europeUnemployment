The project:

Pulled population data from the World Bank API with a json get request.
Built a clean Pandas DataFrame.
Visualized the data with Matplotlib.
Improved the plot for readability and correct interpretation.



Issues faced:

Data types problems (strings vs integers).
Missing values (None / <NA>) in real-world data.
Errors when converting data types with NaN.
Misleading plots due to scale choice (linear vs log).
Mixing log-transformed data with incorrect axis labels.
Trying to handle missing data too early (inside loops).


What we were trying to solve :

Build a robust data pipeline:
raw API → structured data → analysis-ready data
Handle missing values correctly without bias.
Decide when to interpolate and when not to.



What we learned:

APIs return messy data that need to be checked.
NaN is information, not an error.
Interpolation must be methodologically justified.
Clean analysis = clear structure + explicit choices.
