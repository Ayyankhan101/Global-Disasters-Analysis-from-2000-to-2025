# Global Disasters Analysis and Dashboard

This project analyzes global disaster data from the EM-DAT database and presents the findings in an interactive web-based dashboard.

## Project Overview

The project consists of two main parts:

1.  **Data Analysis:** A Jupyter Notebook (`Analysis.ipynb`) is used for in-depth analysis of the disaster data. This includes data cleaning, transformation, and exploratory data analysis to uncover trends and insights.
2.  **Interactive Dashboard:** A Streamlit application (`dashboard.py`) provides an interactive dashboard to visualize the disaster data. Users can filter the data by region, disaster type, and minimum number of deaths, and explore the data through various charts and maps.

## File Descriptions

*   `Analysis.ipynb`: Jupyter Notebook containing the detailed data analysis of the EM-DAT dataset.
*   `dashboard.py`: Streamlit application for the interactive disaster dashboard.
*   `public_emdat_custom_request.csv`: The raw disaster data in CSV format.
*   `public_emdat_custom_request.xlsx`: The raw disaster data in Excel format.
*   `emdat_summary_meta.csv`: Metadata for the EM-DAT dataset.
*   `requirements.txt`: A list of Python packages required to run the project.

## How to Run the Project

1.  **Install Dependencies:**
    Make sure you have Python installed. Then, install the required packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the Dashboard:**
    To start the interactive dashboard, run the following command in your terminal:

    ```bash
    streamlit run dashboard.py
    ```

    This will open a new tab in your web browser with the dashboard.

## Dependencies

The project uses the following Python libraries:

*   streamlit
*   pandas
*   plotly
*   pydeck
*   altair
*   folium
*   numpy
*   matplotlib
*   seaborn
*   openpyxl

These can be installed by running `pip install -r requirements.txt`.
