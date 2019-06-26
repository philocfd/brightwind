
<div style='margin-top: 3em; margin-bottom: 3em;'>
</div>

Welcome to the brightwind python library tutorial page. The brightwind library makes analysing wind data easy, fast and repeatable. Here you will learn how to [install the Brightwind library](https://brightwind-dev.github.io/brightwind-docs/tutorials/getting_started_on_windows.html), get started with using the Jupyter notebook environment and carry out a range of useful functions. 

***

<div style='margin-top: 3em; margin-bottom: 3em;'>
</div>


## Prerequisites 

Before starting these tutorials, ideally the user should have a background in wind data analysis or wind resource assessment. No prior knowledge of the python programming language is necessary, but is preferable. EdX have a nice [introductory course to python and pandas dataframes](https://www.edx.org/course/python-for-data-science-2) which will give you a good grounding of some basic python concepts for data science aswell as pandas dataframes which are used extensively by the library.

***

<div style='margin-top: 3em; margin-bottom: 3em;'>
</div>

### Tutorial 1: [Getting started on windows 10](https://brightwind-dev.github.io/brightwind-docs/tutorials/getting_started_on_windows.html)
This tutorial shows you how to download and install the Anaconda python distribution, install the brightwind library and how to get started with the brightwind library in Jupyter notebooks.

<div style='margin-top: 3em; margin-bottom: 3em;'>
</div>

### Tutorial 2: [Introduction to the brightwind library](https://brightwind-dev.github.io/brightwind-docs/tutorials/Basic_Analysis_Stable_Development.html)
This tutorial shows you how get started with the brightwind library, load some csv data using the `load_csv()` from the brightwind demo datasets and use the `monthly_means()` function to plot the monthly means.

<div style='margin-top: 3em; margin-bottom: 3em;'>
</div>

### Tutorial 3: [How to load data into brightwind](https://brightwind-dev.github.io/brightwind-docs/tutorials/how_to_load_data_into_brightwind.html)
This tutorial shows you how to use the library to load in files in different formats. The user will get familiar with loading csv files using the `load_csv()` function, Campbell Scientific data using the `load_campbell_scientific()`function, data in excel using the `load_excel()` function and data exported from windographer using the `load_windographer_txt()`.

<div style='margin-top: 3em; margin-bottom: 3em;'>
</div>

### Tutorial 4: [How to get some useful stats](https://brightwind-dev.github.io/brightwind-docs/tutorials/how_to_get_some_useful_stats.html)
This tutorial shows you how to get some useful statistics from your wind data. Here we use the `time_continuity_gaps()` function to find any time gaps in the data, the `basic_stats()` function to get some useful stats, the `coverage()` function to get the monthly or annual coverage of specific instruments and finally the `momm()` function to get the mean of monthly means.

<div style='margin-top: 3em; margin-bottom: 3em;'>
</div>

### Tutorial 5: [How to apply a cleaning file](https://brightwind-dev.github.io/brightwind-docs/tutorials/how_to_apply_a_cleaning_file.html)
In this tutorial, you will learn how to apply cleaning to a raw dataset by reading in a structured cleaning file and using the `apply_cleaning()` function. You will also learn how to apply cleaning from an windographer flag file exported from windographer using the `apply_cleaning_windographer()` function.

<div style='margin-top: 3em; margin-bottom: 3em;'>
</div>

### Tutorial 6: [How to get some useful plots](https://brightwind-dev.github.io/brightwind-docs/tutorials/how_to_get_some_useful_plots.html)
This tutorial shows you how to get useful plots for your data. The `plot_timeseries()` allows you to plot a time series of your data for any specific period. The `plot_scatter()` function allows you to plot a scatter plot of any two variables. The `plot_scatter_wspd()` and `plot_scatter_wdir()` functions plot a scatter plot of two anemometers or two wind vanes respectively and includes a reference line. The `sector_ratio()` plot shows the ratio of two anemometers versus wind direction in a polar plot.

<div style='margin-top: 3em; margin-bottom: 3em;'>
</div>

### Tutorial 7: [How to transform your data](https://brightwind-dev.github.io/brightwind-docs/tutorials/how_to_transform_your_data.html)
In this tutorial you will learn how to transform your data in some useful ways. You will learn:
- how the `scale_wind_speed()` function is used to scale a wind speed timeseries dataset
- how the `average_data_by_period()` function can be used to average the data for a specific period 
- how to adjust the slope and offset of a timeseries using the `adjust_slope_offset()` 
- how to apply a direction offset to a wind vane using the `offset_wind_direction()` 
- how the `offset_timestamps()` function can be used to correct a timestamp offset
- how to selectively average two anemometers to remove mast shadow using the `selective_avg()` function.

<div style='margin-top: 3em; margin-bottom: 3em;'>
</div>

### Tutorial 8: [How to plot a wind speed frequency distribution and a distribution of anything!](https://github.com/brightwind-dev/brightwind/tree/master/docs/source/tutorials/how_dist_function_works.ipynb)
This tutorial will introduce you to plotting the wind speed frequency distribution and how to plot the distribution of any two variables using the `dist()`, `dist_of_wind_speed()` and `freq_distribution()` functions.

<div style='margin-top: 3em; margin-bottom: 3em;'>
</div>

### Tutorial 9: [How to calculate air density](https://brightwind-dev.github.io/brightwind-docs/tutorials/how_to_calculate_air_density.html)
This tutorial shows you how to use the `calc_air_density()` function to calculate the air density from your site data, and how to scale it to a specific height based on a defined lapse rate.

<div style='margin-top: 3em; margin-bottom: 3em;'>
</div>

### Tutorial 10: [Plotting and understanding turbulence](https://brightwind-dev.github.io/brightwind-docs/tutorials/plotting_and_understanding_turbulence.html)
This tutorial shows you how to get insights into your site data by plotting a variety of turbulence plots. The `TI.by_sector()` function shows the turbulence intensity by sector on a polar plot to examine both mast and local affects on instrumentation. The `TI.by_speed()` function plots the turbulence intensity by windspeed and shows the data versus the IEC class standards. The `TI.by_12x24()` shows a 12 month by 24 hour matrix of turbulence to see how turbulence varies diurnally throughout the year.

<div style='margin-top: 3em; margin-bottom: 3em;'>
</div>

### Tutorial 11: [How to calculate shear](https://brightwind-dev.github.io/brightwind-docs/tutorials/how_to_calculate_shear.html)
In this tutorial, you will learn how to calculate the shear in a variety of different ways and then scale it to hub height. The `Shear.power_law()` function is used to calculate the shear using the power law method. The `Shear.by_sector()` calculates the shear using the power law method by direction sector. The `Shear.apply()` function shows you how to apply your preferred shear method to the data. The `Shear.by_12x24()` function plots a nice heat map showing the 12 month by 24 hour matrix of shear to see how shear varies diurnally throughout the year.

<div style='margin-top: 3em; margin-bottom: 3em;'>
</div>

### Tutorial 12: [Becoming a correlation wizard!](https://brightwind-dev.github.io/brightwind-docs/tutorials/becoming_a_correlation_wizard.html)
This tutorial shows you the true power of the brightwind library by allowing you to run multiple correlations for different time periods and reference datasets. We will use the `OrdinaryLeastSquares()` function to carry out a ordinary least squares linear regression correlation. We will then show how this can be run in a loop for various reference datasets and time periods. We will also touch on other correlation methods in the library such as `OrthogonalLeastSquares()`, `MultipleLinearRegression()`, `Speedsort()`, `SVR()` and the `SimpleSpeedRatio()`. 

<div style='margin-top: 3em; margin-bottom: 3em;'>
</div>

### Tutorial 13: [Exporting a tab file and saving your data](https://brightwind-dev.github.io/brightwind-docs/tutorials/exporting_a_tab_file_and_saving_your_data.html)
This tutorial shows you how to generate a frequency table and export a tab file using the `export_tab_file()` function for use in other packages such as WASP or Openwind. Additionally you will learn how to use the `export_csv()` function to export your time series data.


***

<div style='margin-top: 3em; margin-bottom: 3em;'>
</div>
