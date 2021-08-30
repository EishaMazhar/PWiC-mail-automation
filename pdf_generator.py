import csv
from fdfgen import forge_fdf
import os
import sys

sys.path.insert(0, os.getcwd())
filename_prefix = "MLH"
csv_file = "data.csv"
pdf_file = "lhd-2020-certificate.pdf"
tmp_file = "tmp.fdf"
output_folder = './filled/'

def process_csv(file):
    data =  []
    csv_data = csv.reader(open(file))
    for i, row in enumerate(csv_data):
      field = []
      name = str(row[0]).strip()
      field.append(('attendee_name', name))
      field.append((('email'), row[1]))
      field.append(('start_date', '18th April 2020'))
      field.append(('venue_name', 'Digital Broadcast by Pakistani Women in Computing, Karachi'))
      field.append(('file_name', name.replace(" ", "_").lower()))
      data.append(field)
    return data

def form_fill(fields):
  fdf = forge_fdf("",fields,[],[],[])
  fdf_file = open(tmp_file,"wb")
  fdf_file.write(fdf)
  fdf_file.close()
  output_file = '{0}{1}_{2}.pdf'.format(output_folder, filename_prefix, fields[4][1])
  cmd = 'pdftk "{0}" fill_form "{1}" output "{2}" dont_ask'.format(pdf_file, tmp_file, output_file)
  os.system(cmd)
  os.remove(tmp_file)

def write_processed_data(data):
  processed = []
  for row in data:
    field = []
    field.append(row[0][1])
    field.append(row[1][1])
    field.append('MLH_{0}.pdf'.format(row[4][1]))
    processed.append(field)
  with open('processed.csv', 'w') as result_file:
    wr = csv.writer(result_file, dialect='excel')
    wr.writerows(processed)


data = process_csv(csv_file)
print('Generating Forms:')
print('-----------------------')
for i in data:
  print('{0} {1} created...'.format(filename_prefix, i[4][1]))
  form_fill(i)

write_processed_data(data)