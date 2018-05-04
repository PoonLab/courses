
def main(csv):
  handle = open(csv, 'rU')
  outfile = open(csv.replace('.csv', '.csv2'), 'w')
  for line in handle:
    items = line.strip('\n').split(',')
    outfile.write(','.join(items[:-2]) + '\n')
  outfile.close()
  handle.close()

