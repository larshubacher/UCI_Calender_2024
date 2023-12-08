from PySide6.QtWidgets import QWidget, QScrollArea, QCheckBox, QCalendarWidget, QTableWidgetItem, QTableWidget, QGridLayout, QPushButton, QGroupBox, QDateEdit, QLabel, QHBoxLayout, QVBoxLayout, QFileDialog
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import Qt
import folium
import pandas as pd
import sys
import csv


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

        ## Title
        self.setWindowTitle("UCI XCO Calender 2024")

        ## load csv
        path = "data/uci_calender_2024.csv"
        df = pd.read_csv(path)

        ## Map placeholder
        self.groupBox_map = QGroupBox("Map", self)
        self.map_group_layout = QVBoxLayout(self.groupBox_map)
        #self.map_group_layout.addWidget(self.groupBox_map)


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

        groupBox_locations = QGroupBox("Locations")
        ## list of countriess
        countries = [x for x in df["Counter_Code"]]
        countries = set(countries)

        location_layout = QVBoxLayout(groupBox_locations)
        for country in countries:
            checkbox = QCheckBox(country,self)
            location_layout.addWidget(checkbox)

        groupBox_race_cat = QGroupBox("Race Category")
        race_categories = [y for y in df["Category"]]
        race_categories = set(race_categories)

        race_cat_layout = QVBoxLayout(groupBox_race_cat)
        for race_cat in race_categories:
            checkbox = QCheckBox(race_cat, self)
            race_cat_layout.addWidget(checkbox)

    
        groupBox_races = QGroupBox("Race details")
        self.races_table = QTableWidget(self)
        groupBox_races_layout = QVBoxLayout(groupBox_races)
        groupBox_races_layout.addWidget(self.races_table)


        ## Grid overview and structure
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.groupBox_map,0,0,2,1) #Take up 2 rows and 1 column
        grid_layout.addWidget(groupBox_timespan,0,1) 

        scroll_area_locations = QScrollArea()
        scroll_area_locations.setWidget(groupBox_locations)
        grid_layout.addWidget(scroll_area_locations,0,2) 

        scroll_area_race_cat = QScrollArea()
        scroll_area_race_cat.setWidget(groupBox_race_cat)
        grid_layout.addWidget(scroll_area_race_cat,1,1)


        grid_layout.addWidget(groupBox_races, 3,0,1,3)
        self.display_csv_in_table(path)

        self.setLayout(grid_layout)

    def display_csv_in_table(self, csv_filename):
        with open(csv_filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)
            self.races_table.setColumnCount(len(header))
            self.races_table.setHorizontalHeaderLabels(header)

            for row_index, row in enumerate(reader):
                self.races_table.insertRow(row_index)
                for col_index, value in enumerate(row):
                    item = QTableWidgetItem(value)
                    self.races_table.setItem(row_index, col_index, item)



        
