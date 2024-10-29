import PySide2
from PySide2 import QtWidgets, QtCore
import SandboxBridge


class ToDoApp(QtWidgets.QWidget):
    def __init__(self):
        super(ToDoApp, self).__init__()
        self.setLayout(QtWidgets.QVBoxLayout())
        self.layout().setAlignment(QtCore.Qt.AlignTop)

        # Set a fixed size for the widget to prevent uncontrolled growth
        self.setFixedHeight(600)

        # Add Task Button
        self.add_task_button = QtWidgets.QPushButton("Add Task")
        self.add_task_button.clicked.connect(self.add_task)
        self.layout().addWidget(self.add_task_button)

        # Scroll Area to contain tasks
        self.scroll_area = QtWidgets.QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_content = QtWidgets.QWidget()
        self.scroll_layout = QtWidgets.QVBoxLayout(self.scroll_content)
        self.scroll_layout.setAlignment(QtCore.Qt.AlignTop)
        self.scroll_area.setWidget(self.scroll_content)
        self.layout().addWidget(self.scroll_area)

    def add_task(self):
        # Add a new QLineEdit for task, a Checkbox, and a Delete Button when the button is clicked
        h_layout = QtWidgets.QHBoxLayout()
        h_layout.setAlignment(QtCore.Qt.AlignLeft)

        task_line_edit = QtWidgets.QLineEdit("New Task")
        task_line_edit.setMinimumWidth(150)

        task_checkbox = QtWidgets.QCheckBox("Done")
        task_checkbox.setMinimumWidth(80)

        delete_button = QtWidgets.QPushButton("Delete Task")
        delete_button.clicked.connect(lambda: self.delete_task(h_layout))

        h_layout.addWidget(task_line_edit)
        h_layout.addWidget(task_checkbox)
        h_layout.addWidget(delete_button)
        self.scroll_layout.addLayout(h_layout)

    def delete_task(self, layout):
        # Delete all widgets in the provided layout
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        layout.deleteLater()


SandboxBridge.register_window(ToDoApp, "To-Do List", category="Productivity", needs_menu_item=True, menu_path="To-Do", unique=False)
