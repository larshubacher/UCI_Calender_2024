from PySide6.QtWidgets import QWidget, QCalendarWidget, QGridLayout, QPushButton, QSizePolicy, QGroupBox, QDateEdit, QLabel, QFrame, QHBoxLayout, QVBoxLayout
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import Qt
import folium
import pandas as pd


class time_filter_widget(QWidget):
    def __init__(self):
        super().__init__()

        calendar = QCalendarWidget()
        calendar.setGridVisible(True)
        grid_layout = QGridLayout()
        grid_layout.addWidget(calendar,0,0)
        self.setLayout(grid_layout)

class layout(QWidget):
    def __init__(self):
        super().__init__()
        ## Map
        groupBox_map = QGroupBox("Map", self)
        map_group_layout = QVBoxLayout(groupBox_map)
        # Read data from CSV file (latitude and longitude columns are assumed)
        df = pd.read_csv('data/uci_calender_2024.csv')
        map_view = self.create_folium_map(df)
        map_group_layout.addWidget(map_view)

        map_group_layout.addWidget(groupBox_map)

        ## Timespan (from and to)
        groupBox_timespan = QGroupBox("Timespan", self)
        group_layout = QHBoxLayout(groupBox_timespan)
        date_layout1 = QHBoxLayout()
        label_from = QLabel("From:", self)
        self.date_edit1 = QDateEdit(self)
        date_layout1.addWidget(label_from)
        date_layout1.addWidget(self.date_edit1)

        date_layout2 = QHBoxLayout()
        label_to = QLabel("To:", self)
        self.date_edit2 = QDateEdit(self)
        date_layout2.addWidget(label_to)
        date_layout2.addWidget(self.date_edit2)

        group_layout.addLayout(date_layout1)
        group_layout.addLayout(date_layout2)

        ## Locations
        groupBox_locations = QGroupBox(str("Locations"))

        ## Race Category
        groupBox_race_cat = QGroupBox(str("Race Category"))

        ## Race details
        groupBox_races = QGroupBox(str("Race details"))
 
        




        ## Set the grid position
        grid_layout = QGridLayout()
        grid_layout.addWidget(groupBox_map,0,0,2,1) #Take up 2 rows and 1 column
        grid_layout.addWidget(groupBox_timespan,0,1) 
        grid_layout.addWidget(groupBox_locations,0,2) 
        grid_layout.addWidget(groupBox_race_cat,1,1)
        grid_layout.addWidget(groupBox_races, 3,0,1,3)


        self.setLayout(grid_layout)

    def create_folium_map(self, df):
        # Create a Folium map centered around the first data point
        map_view = folium.Map(location=[df['latitude'].iloc[0], df['longitude'].iloc[0]], zoom_start=12)

        # Add markers for each data point
        for index, row in df.iterrows():
            folium.Marker([row['latitude'], row['longitude']], popup=row['Location']).add_to(map_view)

        # Save the map to an HTML file
        map_view.save("map.html")

        # Display the map in a QWebEngineView
        web_view = QWebEngineView()
        web_view.setHtml(open("map.html").read())

        return web_view
