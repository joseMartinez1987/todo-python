import FreeSimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text('Selecte file to compress, can be multiple files')
input1 = sg.Input()
choose_button1 = sg.FilesBrowse('Choose', key='files')

label2 = sg.Text('Select the directory to save the compressed file')
input2 = sg.Input()
choose_button2 = sg.FolderBrowse('Choose', key='folder')

compress_button = sg.Button('Compress')

output = sg.Text(key='output', text_color='green', size=(40, 1))


window = sg.Window('Files Compressor',
          layout=[[label1, input1, choose_button1], [label2, input2, choose_button2], [compress_button, output]],
          font=('Helvetica', 18))


while True:
  event, value = window.read()
  print('event:', event)
  print('value:', value)
  match event:
    case 'Compress':
      files_path = value['files'].split(';')
      folder = value['folder']
      make_archive(files_path, folder)
      window['output'].update(value='Files compressed')

    case sg.WIN_CLOSED:
      break

window.close()