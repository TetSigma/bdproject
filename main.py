import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QFont
import pyodbc
from PyQt5.QtCore import Qt
# Connect to the MSSQL database
conn = pyodbc.connect(
    'DRIVER={SQL Server};'
    'SERVER=DESKTOP-678OMMV;'
    'DATABASE=SpaceX;'
)

# Create a cursor
cursor = conn.cursor()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Space Company App")
        self.setStyleSheet("background-color: white; color: white;")
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setAlignment(Qt.AlignTop)
        self.current_widget = None

        self.create_widgets()
        self.list_spacemans()

    def create_widgets(self):
        self.list_spacemans_button = QPushButton("List Professional Spacemans")
        self.list_spacemans_button.setStyleSheet("background-color: black; font-weight: bold; border-radius: 4px; height: 50px; ")
        self.list_spacemans_button.clicked.connect(self.list_spacemans)
        self.layout.addWidget(self.list_spacemans_button)

        self.list_newbies_button = QPushButton("List Newbie Spacemans")
        self.list_newbies_button.setStyleSheet("background-color: black; font-weight: bold; border-radius: 4px; height: 50px;")
        self.list_newbies_button.clicked.connect(self.list_newbies)
        self.layout.addWidget(self.list_newbies_button)

        self.list_missions_button = QPushButton("List Missions")
        self.list_missions_button.setStyleSheet("background-color: black; font-weight: bold; border-radius: 4px; height: 50px;")
        self.list_missions_button.clicked.connect(self.list_missions)
        self.layout.addWidget(self.list_missions_button)

        self.add_spaceman_button = QPushButton("Add Spaceman")
        self.add_spaceman_button.setStyleSheet("background-color: black; font-weight: bold; border-radius: 4px; height: 50px;")
        self.add_spaceman_button.clicked.connect(self.add_spaceman)
        self.layout.addWidget(self.add_spaceman_button)

        self.add_newbie_button = QPushButton("Add Newbie")
        self.add_newbie_button.setStyleSheet("background-color: black; font-weight: bold; border-radius: 4px; height: 50px;")
        self.add_newbie_button.clicked.connect(self.add_newbie)
        self.layout.addWidget(self.add_newbie_button)

        self.add_mission_button = QPushButton("Add Mission")
        self.add_mission_button.setStyleSheet("background-color: black; font-weight: bold; border-radius: 4px; height: 50px;")
        self.add_mission_button.clicked.connect(self.add_mission)
        self.layout.addWidget(self.add_mission_button)

        self.assign_spaceman_button = QPushButton("Assign Spaceman")
        self.assign_spaceman_button.setStyleSheet("background-color: black; font-weight: bold; border-radius: 4px; height: 50px;")
        self.assign_spaceman_button.clicked.connect(self.assign_spaceman)
        self.layout.addWidget(self.assign_spaceman_button)

    def list_spacemans(self):
        if self.current_widget:
            self.layout.removeWidget(self.current_widget)
            self.current_widget.deleteLater()

        self.current_widget = QWidget(self)
        self.current_widget.setStyleSheet("background-color: black; color: white; border-radius:6px; font-weight: bold;")
        layout = QVBoxLayout(self.current_widget)
        layout.addWidget(QLabel("List of Professional Spacemans", self.current_widget))

        cursor.execute("SELECT * FROM ProfessionalSpacemans")
        rows = cursor.fetchall()

        for row in rows:
            spaceman_label = QLabel(f"{row.name} " f"{row.surname}" f" \n\nStatus: {row.status}\nMission name: {row.MissionName}",self.current_widget)
            spaceman_label.setStyleSheet("background-color: white; color: black; padding: 10px; border-radius:4px; height:50px; text-align: center; font-weight: bold; border-radius:6px;")
            layout.addWidget(spaceman_label)

        self.layout.addWidget(self.current_widget)

    def list_newbies(self):
        if self.current_widget:
            self.layout.removeWidget(self.current_widget)
            self.current_widget.deleteLater()

        self.current_widget = QWidget(self)
        self.current_widget.setStyleSheet("background-color: black; color: white; border-radius:6px; font-weight: bold;")
        layout = QVBoxLayout(self.current_widget)
        layout.addWidget(QLabel("List of Newbie Spacemans", self.current_widget))

        cursor.execute("SELECT * FROM NewbieSpacemans")
        rows = cursor.fetchall()

        for row in rows:
            newbie_label = QLabel(f"{row.name} {row.surname} \n\nTime: {row.start_date} - {row.end_date}\n\nOverall Training Cost: {row.overall_training_cost}", self.current_widget)
            newbie_label.setStyleSheet("background-color: white; color: black; padding: 10px; border-radius:4px; height:50px; text-align: center; font-weight: bold; border-radius:6px;")
            layout.addWidget(newbie_label)

        self.layout.addWidget(self.current_widget)

    def list_missions(self):
        if self.current_widget:
            self.layout.removeWidget(self.current_widget)
            self.current_widget.deleteLater()

        self.current_widget = QWidget(self)
        self.current_widget.setStyleSheet("background-color: black; color: white; border-radius:6px; font-weight: bold;")
        layout = QVBoxLayout(self.current_widget)
        layout.addWidget(QLabel("List of Missions", self.current_widget))

        cursor.execute("SELECT * FROM Missions")
        rows = cursor.fetchall()

        for row in rows:
            mission_label = QLabel(f"Mission Name: {row.mission_name}\nStart Date: {row.start_date}\nApproximate Cost: {row.approximate_cost}", self.current_widget)
            mission_label.setStyleSheet("background-color: white; color: black; padding: 10px; border-radius:4px; height:50px; text-align: center; font-weight: bold; border-radius:6px;")
            layout.addWidget(mission_label)

        self.layout.addWidget(self.current_widget)

    def add_spaceman(self):
        if self.current_widget:
            self.layout.removeWidget(self.current_widget)
            self.current_widget.deleteLater()

        self.current_widget = QWidget(self)
        self.current_widget.setStyleSheet("background-color: black; color: white; border-radius:6px; font-weight:bold;")
        layout = QVBoxLayout(self.current_widget)
        layout.addWidget(QLabel("Add Spaceman", self.current_widget))

        name_label = QLabel("Name:", self.current_widget)
        name_entry = QLineEdit(self.current_widget)
        name_entry.setStyleSheet(
            "background-color: white; color: black; border-radius:6px; font-weight:bold; height:50px;")
        layout.addWidget(name_label)
        layout.addWidget(name_entry)

        surname_label = QLabel("Surname:", self.current_widget)
        surname_entry = QLineEdit(self.current_widget)
        surname_entry.setStyleSheet("background-color: white; color: black; border-radius:6px; font-weight:bold; height:50px;")
        layout.addWidget(surname_label)
        layout.addWidget(surname_entry)

        status_label = QLabel("Status (on mission or on earth):", self.current_widget)
        status_entry = QLineEdit(self.current_widget)
        status_entry.setStyleSheet(
            "background-color: white; color: black; border-radius:6px; font-weight:bold; height:50px; margin-bottom:15px;")
        layout.addWidget(status_label)
        layout.addWidget(status_entry)

        add_button = QPushButton("Add", self.current_widget)
        add_button.setStyleSheet("background-color: white; color:black; border-radius:6px; font-weight: bold; height:50px;")
        add_button.clicked.connect(lambda: self.add_spaceman_to_db(name_entry.text(), surname_entry.text(),
                                                                  status_entry.text()))
        layout.addWidget(add_button)

        self.layout.addWidget(self.current_widget)

    def add_spaceman_to_db(self, name, surname, status):
        cursor.execute("INSERT INTO ProfessionalSpacemans (name, surname, status) VALUES (?, ?, ?)",
                       name, surname, status)
        conn.commit()
        self.list_spacemans()

    def add_newbie(self):
        if self.current_widget:
            self.layout.removeWidget(self.current_widget)
            self.current_widget.deleteLater()

        self.current_widget = QWidget(self)
        self.current_widget.setStyleSheet("background-color: black; color: white; border-radius:6px; font-weight:bold;")
        layout = QVBoxLayout(self.current_widget)
        layout.addWidget(QLabel("Add Newbie", self.current_widget))

        name_label = QLabel("Name:", self.current_widget)
        name_entry = QLineEdit(self.current_widget)
        name_entry.setStyleSheet(
            "background-color: white; color: black; border-radius:6px; font-weight:bold; height:50px;")
        layout.addWidget(name_label)
        layout.addWidget(name_entry)

        surname_label = QLabel("Surname:", self.current_widget)
        surname_entry = QLineEdit(self.current_widget)
        surname_entry.setStyleSheet(
            "background-color: white; color: black; border-radius:6px; font-weight:bold; height:50px;")
        layout.addWidget(surname_label)
        layout.addWidget(surname_entry)

        start_date_label = QLabel("Start Date (YYYY-MM-DD):", self.current_widget)
        start_date_entry = QLineEdit(self.current_widget)
        start_date_entry.setStyleSheet(
            "background-color: white; color: black; border-radius:6px; font-weight:bold; height:50px;")
        layout.addWidget(start_date_label)
        layout.addWidget(start_date_entry)

        end_date_label = QLabel("End Date (YYYY-MM-DD):", self.current_widget)
        end_date_entry = QLineEdit(self.current_widget)
        end_date_entry.setStyleSheet(
            "background-color: white; color: black; border-radius:6px; font-weight:bold; height:50px;")
        layout.addWidget(end_date_label)
        layout.addWidget(end_date_entry)

        overall_cost_label = QLabel("Overall Training Cost:", self.current_widget)
        overall_cost_entry = QLineEdit(self.current_widget)
        overall_cost_entry.setStyleSheet(
            "background-color: white; color: black; border-radius:6px; font-weight:bold; height:50px;margin-bottom:15px")
        layout.addWidget(overall_cost_label)
        layout.addWidget(overall_cost_entry)

        add_button = QPushButton("Add", self.current_widget)
        add_button.setStyleSheet("background-color: white; color:black; border-radius:6px; font-weight: bold; height:50px;")
        add_button.clicked.connect(lambda: self.add_newbie_to_db(name_entry.text(), surname_entry.text(),
                                                                start_date_entry.text(), end_date_entry.text(),
                                                                overall_cost_entry.text()))
        layout.addWidget(add_button)

        self.layout.addWidget(self.current_widget)

    def assign_spaceman(self):
        if self.current_widget:
            self.layout.removeWidget(self.current_widget)
            self.current_widget.deleteLater()

        self.current_widget = QWidget(self)
        self.current_widget.setStyleSheet(
            "background-color: black; color: white; border-radius:6px; font-weight:bold;")
        layout = QVBoxLayout(self.current_widget)
        layout.addWidget(QLabel("Assign Spaceman", self.current_widget))

        name_label = QLabel("Spaceman Name:", self.current_widget)
        name_entry = QLineEdit(self.current_widget)
        name_entry.setStyleSheet(
            "background-color: white; color: black; border-radius:6px; font-weight:bold; height:50px;")
        layout.addWidget(name_label)
        layout.addWidget(name_entry)

        surname_label = QLabel("Spaceman Surname:", self.current_widget)
        surname_entry = QLineEdit(self.current_widget)
        surname_entry.setStyleSheet(
            "background-color: white; color: black; border-radius:6px; font-weight:bold; height:50px;")
        layout.addWidget(surname_label)
        layout.addWidget(surname_entry)

        mission_label = QLabel("Mission Name", self.current_widget)
        mission_entry = QLineEdit(self.current_widget)
        mission_entry.setStyleSheet(
            "background-color: white; color: black; border-radius:6px; font-weight:bold; height:50px;")
        layout.addWidget(mission_label)
        layout.addWidget(mission_entry)

        add_button = QPushButton("Assign", self.current_widget)
        add_button.setStyleSheet(
            "background-color: white; color:black; border-radius:6px; font-weight: bold; height:50px;")
        add_button.clicked.connect(lambda: self.assign_to_mission(name_entry.text(), surname_entry.text(), mission_entry.text()))
        layout.addWidget(add_button)

        self.layout.addWidget(self.current_widget)

    def add_newbie_to_db(self, name, surname, start_date, end_date, overall_cost):
        cursor.execute("INSERT INTO NewbieSpacemans (name, surname, start_date, end_date, overall_training_cost) "
                       "VALUES (?, ?, ?, ?, ?)", name, surname, start_date, end_date, overall_cost)
        conn.commit()
        self.list_newbies()

    def assign_to_mission(self, name, surname, mission_name):
        cursor.execute("UPDATE ProfessionalSpacemans SET MissionName = ? WHERE name = ? and surname = ?", mission_name, name, surname)
        conn.commit()
        self.list_spacemans()

    def add_mission(self):
        if self.current_widget:
            self.layout.removeWidget(self.current_widget)
            self.current_widget.deleteLater()

        self.current_widget = QWidget(self)
        self.current_widget.setStyleSheet("background-color: black; color: white; border-radius:6px; font-weight:bold;")
        layout = QVBoxLayout(self.current_widget)
        layout.addWidget(QLabel("Add Mission", self.current_widget))

        start_date_label = QLabel("Start Date (YYYY-MM-DD):", self.current_widget)
        start_date_entry = QLineEdit(self.current_widget)
        start_date_entry.setStyleSheet(
            "background-color: white; color: black; border-radius:6px; font-weight:bold; height:50px;")
        layout.addWidget(start_date_label)
        layout.addWidget(start_date_entry)

        mission_name_label = QLabel("Mission Name:", self.current_widget)
        mission_name_entry = QLineEdit(self.current_widget)
        mission_name_entry.setStyleSheet(
            "background-color: white; color: black; border-radius:6px; font-weight:bold; height:50px;")
        layout.addWidget(mission_name_label)
        layout.addWidget(mission_name_entry)

        approximate_cost_label = QLabel("Approximate Cost:", self.current_widget)
        approximate_cost_entry = QLineEdit(self.current_widget)
        approximate_cost_entry.setStyleSheet(
            "background-color: white; color: black; border-radius:6px; font-weight:bold; height:50px; margin-bottom:15px;")
        layout.addWidget(approximate_cost_label)
        layout.addWidget(approximate_cost_entry)

        add_button = QPushButton("Add", self.current_widget)
        add_button.setStyleSheet("background-color: white; color:black; border-radius:6px; font-weight: bold; height:50px;")
        add_button.clicked.connect(lambda: self.add_mission_to_db(start_date_entry.text(), mission_name_entry.text(),
                                                                  approximate_cost_entry.text()))
        layout.addWidget(add_button)

        self.layout.addWidget(self.current_widget)

    def add_mission_to_db(self, start_date, mission_name, approximate_cost):
        cursor.execute("INSERT INTO Missions (start_date, mission_name, approximate_cost) VALUES (?, ?, ?)",
                       start_date, mission_name, approximate_cost)
        conn.commit()
        self.list_missions()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    font = QFont("Arial", 12)
    app.setFont(font)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())
