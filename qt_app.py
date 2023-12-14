from PySide6.QtWidgets import QWidget, QApplication, QMainWindow, QTableWidget,QTableWidgetItem, QCheckBox, QScrollArea, QGridLayout, QGroupBox, QDateEdit, QLabel, QHBoxLayout, QVBoxLayout
from PySide6.QtWebEngineWidgets import QWebEngineView
import folium
import pandas as pd
import numpy as np
import sys

class main_window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("UCI Calender 2024")

        container = QWidget()
        containerLayout = QVBoxLayout()
        container.setLayout(containerLayout)

        layout_widget = layout()
        containerLayout.addWidget(layout_widget)

        #time_filter = time_filter_widget()
        #containerLayout.addWidget(time_filter)

        self.setCentralWidget(container)


class layout(QWidget):
    def __init__(self):
        super().__init__()

        ## Title
        self.setWindowTitle("UCI XCO Calender 2024")

        ## load csv
        path = "data/uci_calender_2024.csv"
        self.df = pd.read_csv(path)


        ## Map placeholder
        self.groupBox_map = QGroupBox("Map", self)
        self.map_group_layout = QVBoxLayout(self.groupBox_map)
        self.map_view = self.create_folium_map(self.df, [], [])  # Pass empty lists for initial display
        self.map_group_layout.addWidget(self.map_view)

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


        groupBox_locations = QGroupBox("Locations", self)
        location_layout = QVBoxLayout(groupBox_locations)
        ## list of countriess
        countries = [x for x in self.df["Counter_Code"]]
        countries = sorted(set(countries))


        self.location_checkboxes = [] ## store checkboxes
        for country in countries:
            checkbox = QCheckBox(country,self)
            checkbox.toggled.connect(self.update_table_and_map)
            location_layout.addWidget(checkbox)
            self.location_checkboxes.append(checkbox)

        groupBox_race_cat = QGroupBox("Race Category")
        ## List of race categories
        race_categories = [y for y in self.df["Category"]]
        race_categories = sorted(set(race_categories))

        race_cat_layout = QVBoxLayout(groupBox_race_cat)
        self.race_cat_checkboxes = [] ## store checkboxes
        for race_cat in race_categories:
            checkbox = QCheckBox(race_cat, self)
            checkbox.toggled.connect(self.update_table_and_map)
            race_cat_layout.addWidget(checkbox)
            self.race_cat_checkboxes.append(checkbox)

    
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

        ## Connect dataChanged signal to update table
        self.date_edit1.dateChanged.connect(self.update_table_and_map)
        self.date_edit2.dateChanged.connect(self.update_table_and_map)

        self.display_dataframe_in_table(self.df)

        self.setLayout(grid_layout)

    def display_dataframe_in_table(self, df):
        self.races_table.setRowCount(0)  # Clear existing rows

        header = df.columns.tolist()
        self.races_table.setColumnCount(len(header))
        self.races_table.setHorizontalHeaderLabels(header)

        for row_index in range(len(df)):
            self.races_table.insertRow(row_index)
            for col_index, value in enumerate(df.iloc[row_index]):
                item = QTableWidgetItem(str(value))
                self.races_table.setItem(row_index, col_index, item)


    def create_folium_map(self, df, selected_categories, selected_nations, start_date=None, end_date=None):
        # Create a Folium map centered around the first data point
        #map_view = folium.Map(location=[self.df['Latitude'].iloc[0], self.df['Longitude'].iloc[0]], zoom_start=12)
        map_view = folium.Map(zoom_start=12)

        # Add markers for each data point, handling NaN values
        for index, row in self.df.iterrows():
            latitude = row['Latitude']
            longitude = row['Longitude']
            category = row['Category']
            nation = row['Counter_Code']
            start_date_point = row['StartDate']
            end_date_point = row['EndDate']

            # Check for NaN values and if the category and nation are selected within the date range
            if (
                not np.isnan(latitude) 
                and not np.isnan(longitude) 
                and (not selected_categories or category in selected_categories)
                and (not selected_nations or nation in selected_nations)
                and (not start_date or start_date_point >= start_date)
                and (not end_date or end_date_point <= end_date)
            ):
                folium.Marker([latitude, longitude], popup=row['Location']).add_to(map_view)

        # Save the map to an HTML file
        map_view.save("map.html")

        # Display the map in a QWebEngineView
        web_view = QWebEngineView()
        web_view.setHtml(open("map.html").read())

        return web_view




    def update_table_and_map(self):
        selected_race_categories = [checkbox.text() for checkbox in self.race_cat_checkboxes if checkbox.isChecked()]
        selected_locations = [checkbox.text() for checkbox in self.location_checkboxes if checkbox.isChecked()]
        selected_start_date = self.date_edit1.date().toPython()
        selected_end_date = self.date_edit2.date().toPython()

        # Convert "StartDate" and "EndDate" columns to datetime.date
        self.df["StartDate"] = pd.to_datetime(self.df["StartDate"]).dt.date
        self.df["EndDate"] = pd.to_datetime(self.df["EndDate"]).dt.date
        
        filtered_df = self.df[(self.df["Category"].isin(selected_race_categories)) &
                               (self.df["Counter_Code"].isin(selected_locations)) &
                               ((self.df["StartDate"] >= selected_start_date)&
                                (self.df["EndDate"] <= selected_end_date)
                                )]
        
        # Update the map with the selected filters and date range
        map_view = self.create_folium_map(filtered_df, selected_race_categories, selected_locations, selected_start_date, selected_end_date)

        # Clear the existing map view and add the updated map view
        self.map_group_layout.removeWidget(self.map_view)
        self.map_view.deleteLater()
        self.map_view = map_view
        self.map_group_layout.addWidget(self.map_view)


        self.display_dataframe_in_table(filtered_df)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = main_window()
    main_window.show()
    app.exec()