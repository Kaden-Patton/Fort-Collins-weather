import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

class Station:
    def __init__(self, data=None):
        if data:
            self._name = data["name"]
            self._id = data["ID"]
        else:
            self._name = ""
            self._id = ""
        self._data = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
    
    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, value):
        self._data = value

    def add_data(self, date, max_temp, min_temp, precipitation, snowfall):
        self.data.append({
            "date": date,
            "max_temp": max_temp,
            "min_temp": min_temp,
            "precipitation": precipitation,
            "snowfall": snowfall
        })
        return self.data
    
    def get_date_range(self):
        return [self.data[0]["date"], self.data[-1]["date"]]

    def get_max_temps(self):
        return [entry["max_temp"] for entry in self.data]

    def get_min_temps(self):
        return [entry["min_temp"] for entry in self.data]

    def get_precipitations(self):
        return [entry["precipitation"] for entry in self.data]

    def get_snowfalls(self):
        return [entry["snowfall"] for entry in self.data]
        
    def clean_data(self):
        cleaned_data = []
        for entry in self.data:
            cleaned_entry = {}
            for key, value in entry.items():
                if key == 'date':
                    cleaned_entry[key] = value
                elif value == 'M' or value == 'T':
                    cleaned_entry[key] = np.nan
                else:
                    cleaned_entry[key] = float(value)
            cleaned_data.append(cleaned_entry)
        self.data = cleaned_data
    
    def plot_data_plotly(self):
        dates = [entry["date"] for entry in self.data]
        max_temps = [entry["max_temp"] for entry in self.data]
        min_temps = [entry["min_temp"] for entry in self.data]
        precipitations = [entry["precipitation"] for entry in self.data]
        snowfalls = [entry["snowfall"] for entry in self.data]

        fig = make_subplots(rows=3, cols=1, row_heights=[0.4, 0.3, 0.3],
                            subplot_titles=("Temperature", "Precipitation", "Snowfall"))

        fig.add_trace(go.Scatter(x=dates, y=max_temps, name="Max Temperature"), row=1, col=1)
        fig.add_trace(go.Scatter(x=dates, y=min_temps, name="Min Temperature"), row=1, col=1)

        fig.add_trace(go.Bar(x=dates, y=precipitations, name="Precipitation"), row=2, col=1)

        fig.add_trace(go.Bar(x=dates, y=snowfalls, name="Snowfall"), row=3, col=1)

        fig.update_xaxes(title_text="Date", row=1, col=1)
        fig.update_xaxes(title_text="Date", row=2, col=1)
        fig.update_xaxes(title_text="Date", row=3, col=1)

        fig.update_yaxes(title_text="Fahrenheit", row=1, col=1)
        fig.update_yaxes(title_text="Inches", row=2, col=1)
        fig.update_yaxes(title_text="Inches", row=3, col=1)

        fig.update_layout(title_text=f"Weather Data for Station: {self.name} ({self.id}) from ({self.get_date_range()[0]}) to ({self.get_date_range()[-1]})",
                          height=800, width=1600, title_x=0.5)

        fig.show()