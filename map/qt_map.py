import sys
import io
import folium
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PySide6.QtWebEngineWidgets import QWebEngineView

class MyMap(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Folium im PySide6 Example")
        
        layout = QVBoxLayout()
        self.setLayout(layout)

        coordinate = (47.37662848207693, 8.644777188628023)

        m = folium.Map(
            tiles="cartodb positron",
            zoom_start=13,
            location=coordinate   
        )

        ## save map data to data object
        data = io.BytesIO()
        m.save(data, close_file=False)

        ## display the map
        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        layout.addWidget(webView)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet("""
        QWidget {
                      font-size: 35px:
        }""")
    MyMap = MyMap()
    MyMap.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print("Closing Window...")
