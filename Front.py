import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import sys
from crawl_stoixima import execute

class Mywindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.height = 200
        self.width = 400
        self.left = 10
        self.top = 20
    
    def title(self):    

        # Add title
        self.setWindowTitle('Settings')

        # Geometry
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        # Set layout
        self.setLayout(qtw.QVBoxLayout())

    
    def create_label(self,label_text,font_size):

        # Create a label
        my_label = qtw.QLabel(label_text)

        # Change font size
        my_label.setFont(qtg.QFont('Helvetica',font_size)) #'Configutre Settings'

        self.layout().addWidget(my_label)


    def textbox(self,label_text,field):

        # Create label for box
        self.create_label(label_text,10)

        # Create a box 
        my_entry = qtw.QLineEdit()
        my_entry.move(20, 20)
        my_entry.resize(280,40)


        my_entry.setObjectName(field)
        my_entry.setText('False')
        

        self.layout().addWidget(my_entry)

        return my_entry
    
    def create_button(self):

        # Create button
        my_button = qtw.QPushButton("Run")

        self.layout().addWidget(my_button)

        # adding action to a button
        my_button.clicked.connect(self.on_click)
       
    
    def save_path(self):

        if self.path.text()=='False':
            return 'C:\\Users\\User\\OneDrive\\Desktop\\Apiron\\Crawler\\infobeto_'
        else:
            return self.path.text()

    
    def on_click(self):

        # Find path to save file
        path = self.save_path()
        
        
        # Crawling settings
        settings = {

            'URL': 'https://www.infobeto.com/kouponi-opap',
            
            'choose_date': str(self.date.text()), # Date in form 2022-01-05 # if executed on previous date assign 'False'

            'save_path': str(path),
            
            'element_xpath':"//div[@class='table-responsive']//tbody/tr[@class='lineHeight']",


            'crawling_settings':
            {
                'Δ':".//td[@class='flag']",
                'ΩΕ': ".//td[@class='gameHour']",
                'Α': ".//td[3]",
                '1' : ".//td[3]",
                'ΓΗΠΕΔΟΥΧΟΣ' : ".//td[@class='team1']",
                'Χ' : ".//td[8]",
                'ΦΙΛΟ/ΝΟΥΜΕΝΗ' : ".//td[@class='team2']",
                '2' : ".//td[10]",
                '1Χ':".//td[11]",
                '12' : ".//td[12]",
                'Χ2': ".//td[13]",
                'Under' : ".//td[14]",
                'Over' : ".//td[15]",
                'Goal' : ".//td[16]",
                'No Goal': ".//td[17]",
                'Ημ/νο': ".//td[18]",
                'Τελικο':".//td[19]",
                'Σημ.' : ".//td[20]",
                'Αποδ' : ".//td[21]"
            }

        }


        
        exec = execute(settings)
        exec.crawler()
    
    def create_window(self):
        self.title()
        
        self.create_label('Configutre Settings',16)

        self.date = self.textbox('Choose date','Date')
        self.path = self.textbox('Choose path to save files','Path for saving files')

        self.create_button()    

        self.show()




        


