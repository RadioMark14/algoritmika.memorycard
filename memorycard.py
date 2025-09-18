from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QTextEdit, QListWidget, QLineEdit, QInputDialog, QMessageBox
notes = []
app = QApplication([])
main = QWidget()
main.resize(900, 600)
main.setWindowTitle('Умные Заметки')

note_tab = QTextEdit()

listt = QLabel('Список заметок')
listt_notes = QListWidget()
create_note = QPushButton('Создать заметку')
delete_note = QPushButton('Удалить заметку')
save_note = QPushButton('Сохранить заметку')
tag_list = QLabel('Список тегов')
listt_tags = QListWidget()
type_tag = QLineEdit()
type_tag.setPlaceholderText('Введите тег...')
add_to_notes = QPushButton('Добавить к заметке')
unpin_from_note = QPushButton('Открепить от заметки')
search_by_tag = QPushButton('Искать заметки по тегу')

main_line = QHBoxLayout()
linev1 = QVBoxLayout()
linev1.addWidget(note_tab)
linev2 = QVBoxLayout()
linev2.addWidget(listt)
linev2.addWidget(listt_notes)
lineh1 = QHBoxLayout()
lineh1.addWidget(create_note)
lineh1.addWidget(delete_note)
linev2.addLayout(lineh1)
lineh2 = QHBoxLayout()
lineh2.addWidget(save_note)
linev2.addLayout(lineh2)
linev2.addWidget(tag_list)
linev2.addWidget(listt_tags)
linev2.addWidget(type_tag)
lineh3 = QHBoxLayout()
lineh3.addWidget(add_to_notes)
lineh3.addWidget(unpin_from_note)
linev2.addLayout(lineh3)
lineh4 = QHBoxLayout()
lineh4.addWidget(search_by_tag)
linev2.addLayout(lineh4)
main_line.addLayout(linev1)
main_line.addLayout(linev2)
main.setLayout(main_line)

def show_note():
    name = listt_notes.selectedItems()[0].text()
    for note in notes:
        if note[0] == name:
            note_tab.setText(note[1])
            listt_tags.clear()
            listt_tags.addItems(note[2])
            
def add_note():
    note_name, ok = QInputDialog.getText(main, 'добавить заметку', "Название заметки")
    if ok and note_name != '':
        note = list()
        note = [note_name, '', []]
        notes.append(note)
        listt_notes.addItem(note[0])
        filename = str(len(notes)-1)+'.txt'
        with open (filename, 'w', encoding='utf-8') as file:
            file.write(note[0]+'\n')
    else:
        warning = QMessageBox()
        warning.setText('Заметка не создана!')
        warning.setInformativeText('Для создания заметки следует написать её имя и нажать ок.')
        warning.setWindowTitle('Ошибка!')
        warning.exec_()

def save_notee():
    if listt_notes.selectedItems():
        name = listt_notes.selectedItems()[0].text()
        i = 0
        for note in notes:
            if note[0] == name:
                note[1] = note_tab.toPlainText()
                filename = str(i)+'.txt'
                with open (filename, 'w', encoding='utf-8') as file:
                    file.write(note[0]+'\n')
                    file.write(note[1]+'\n')
                    for tag in note[2]:
                        file.write(tag+' ')
                    file.write('\n')
            i += 1

    else:
        warning = QMessageBox()
        warning.setText('Заметка не сохранена!')
        warning.setInformativeText('Для сохранения заметки следует выбрать её.')
        warning.setWindowTitle('Ошибка!')
        warning.exec_()
               
listt_notes.itemClicked.connect(show_note)
create_note.clicked.connect(add_note)
save_note.clicked.connect(save_notee)

name = 0
note = list()
while True:
    filename = str(name)+'.txt'
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.replace('\n', '')
                note.append(line)
        tags = note[2].split(' ')
        note[2] = tags
        notes.append(note)
        note = []
        name += 1
    except IOError:
        break

for note in notes:
    listt_notes.addItem(note[0])

main.show()
app.exec_()
