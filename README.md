# Colorado historic weather visualization
This project attempts to provide a visual way to analyze weather trends here in Colorado.

It does so via data gathered from CSU's climate center, found [here](https://climate.colostate.edu/data_access_new.html)

## Preview

![image](https://github.com/Kaden-Patton/Fort-Collins-weather/assets/39076173/74c9c718-9c4d-4b61-833e-6db156cccd79)


![image](https://github.com/Kaden-Patton/Fort-Collins-weather/assets/39076173/814721f8-a8f9-44c5-b310-6a692732aea7)

## How to use

Download this repository onto your machine, insure that all dependencies are installed on your system.

Execute Main.py, from there select the weather station within Colorado you'd like to see, as well as the date range you're interested in and click submit.

## Dependencies

This project makes use of several libraries that come natively installed in Python distributions.

However, it also uses a few libraries that you must manually install.

* Requests to talk to the internet
* BeautifulSoup (bs4) for parsing data from webpages
* Numpy for working with data gathered
* Plotly for generating performant graphing using large datasets

You can install each of these packages using the following commands
```
pip install requests
pip install bs4
pip install numpy
pip install plotly
```
