from PySide6.QtWidgets import QWidget, QCalendarWidget, QGridLayout, QPushButton, QSizePolicy, QGroupBox, QDateEdit, QLabel, QFrame, QHBoxLayout, QVBoxLayout, QRadioButton, QButtonGroup, QApplication
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import Qt
import folium
import pandas as pd
import numpy as np

class time_filter_widget(QWidget):
    def __init__(self):
        super().__init__()

        calendar = QCalendarWidget()
        calendar.setGridVisible(True)
        grid_layout = QGridLayout()
        grid_layout.addWidget(calendar, 0, 0)
        self.setLayout(grid_layout)

class layout(QWidget):
    def __init__(self):
        super().__init__()

        ## Map
        groupBox_map = QGroupBox("Map", self)
        map_group_layout = QVBoxLayout(groupBox_map)
        # Read data from CSV file (latitude and longitude columns are assumed)
        df = pd.read_csv('data/uci_calender_2024.csv')
        self.map_view = self.create_folium_map(df, [], [])  # Pass empty lists for initial display
        map_group_layout.addWidget(self.map_view)

        ## Timespan (from and to)
        groupBox_timespan = QGroupBox("Timespan", self)
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

        group_layout_timespan = QVBoxLayout(groupBox_timespan)
        group_layout_timespan.addLayout(date_layout1)
        group_layout_timespan.addLayout(date_layout2)

        ## Locations
        groupBox_locations = QGroupBox("Locations", self)
        group_layout_locations = QVBoxLayout(groupBox_locations)

        # Race Category radio buttons
        race_category_group = QButtonGroup(self)
        race_category_group.setExclusive(False)  # Allow multiple selections

        for category in df['Category'].unique():
            radio_button = QRadioButton(category, self)
            race_category_group.addButton(radio_button)
            group_layout_locations.addWidget(radio_button)

        race_category_group.buttonClicked.connect(self.on_race_category_button_clicked)

        groupBox_locations.setLayout(group_layout_locations)

        ## Nations
        groupBox_nations = QGroupBox("Nations", self)
        group_layout_nations = QVBoxLayout(groupBox_nations)

        # Nation radio buttons
        nation_group = QButtonGroup(self)
        nation_group.setExclusive(False)  # Allow multiple selections

        for nation in df['Counter_Code'].unique():
            radio_button = QRadioButton(nation, self)
            nation_group.addButton(radio_button)
            group_layout_nations.addWidget(radio_button)

        all_nations_button = QRadioButton("All", self)
        nation_group.addButton(all_nations_button)
        group_layout_nations.addWidget(all_nations_button)

        nation_group.buttonClicked.connect(self.on_nation_button_clicked)

        groupBox_nations.setLayout(group_layout_nations)

        ## Race details
        groupBox_races = QGroupBox("Race details", self)

        ## Set the grid position
        grid_layout = QGridLayout()
        grid_layout.addWidget(groupBox_map, 0, 0, 2, 1)  # Take up 2 rows and 1 column
        grid_layout.addWidget(groupBox_timespan, 0, 1)
        grid_layout.addWidget(groupBox_locations, 0, 2)
        grid_layout.addWidget(groupBox_nations, 0, 3)
        grid_layout.addWidget(groupBox_races, 3, 0, 1, 4)

        self.setLayout(grid_layout)

    def create_folium_map(self, df, selected_categories, selected_nations):
        # Create a Folium map centered around the first data point
        map_view = folium.Map(location=[df['latitude'].iloc[0], df['longitude'].iloc[0]], zoom_start=12)

        # Add markers for each data point, handling NaN values
        for index, row in df.iterrows():
            latitude = row['latitude']
            longitude = row['longitude']
            category = row['Category']
            nation = row['Counter_Code']

            # Check for NaN values and if the category and nation are selected
            if (
                not np.isnan(latitude) 
                and not np.isnan(longitude) 
                and (not selected_categories or category in selected_categories)
                and (not selected_nations or nation in selected_nations)
            ):
                folium.Marker([latitude, longitude], popup=row['Location']).add_to(map_view)

        # Save the map to an HTML file
        map_view.save("map.html")

        # Display the map in a QWebEngineView
        web_view = QWebEngineView()
        web_view.setHtml(open("map.html").read())

        return web_view

    def on_race_category_button_clicked(self):
        # Update the map based on the selected categories and nations
        selected_categories = [button.text() for button in self.findChildren(QRadioButton) if button.isChecked()]
        selected_nations = [button.text() for button in self.findChildren(QRadioButton) if button.isChecked()]

        # Read data from CSV file
        df = pd.read_csv('data/uci_calender_2024.csv')

        # Update the map
        self.map_view.setHtml(self.create_folium_map(df, selected_categories, selected_nations).page().toHtml())

    def on_nation_button_clicked(self):
        # Update the map based on the selected categories and nations
        selected_categories = [button.text() for button in self.findChildren(QRadioButton) if button.isChecked()]
        selected_nations = [button.text() for button in self.findChildren(QRadioButton) if button.isChecked()]

        # Read data from CSV file
        df = pd.read_csv('data/uci_calender_2024.csv')

        # Update the map
        self.map_view.setHtml(self.create_folium_map(df, selected_categories, selected_nations).page().toHtml())

if __name__ == "__main__":
    app = QApplication([])
    window = layout()
    window.show()
    app.exec_()
