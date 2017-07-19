import re
import sys

# regular expression to parse the date entry
mdy = re.compile('(\d{2})-(\d{2})-(\d{4})')

# dictionary to convert event codes
codes = {
    '33': "Regular insulin dose", 
    '34': "NPH insulin dose", 
    '35': "UltraLente insulin dose", 
    '48': "Unspecified blood glucose measurement", 
    '57': "Unspecified blood glucose measurement", 
    '58': "Pre-breakfast blood glucose measurement", 
    '59': "Post-breakfast blood glucose measurement", 
    '60': "Pre-lunch blood glucose measurement", 
    '61': "Post-lunch blood glucose measurement", 
    '62': "Pre-supper blood glucose measurement", 
    '63': "Post-supper blood glucose measurement", 
    '64': "Pre-snack blood glucose measurement", 
    '65': "Hypoglycemic symptoms", 
    '66': "Typical meal ingestion", 
    '67': "More-than-usual meal ingestion", 
    '68': "Less-than-usual meal ingestion", 
    '69': "Typical exercise activity", 
    '70': "More-than-usual exercise activity", 
    '71': "Less-than-usual exercise activity", 
    '72': "Unspecified special event"
}

def standardize_date(dt):
    """ Convert MM-DD-YYYY format to ISO standard YYYY-MM-DD """
    matches = mdy.findall(dt)
    if not matches:
        print ("ERROR: Failed to parse date {}".format(dt))
        return dt  # missing date
    month, day, year = matches[0]
    isodate = '{}-{}-{}'.format(year, month, day)
    return isodate

def translate_code(code):
    """ Use dictionary to map code to a brief description """
    desc = codes.get(code, None)
    if not desc:
        print ("ERROR: Encountered unknown code {}".format(code))
        desc = ''  # blank for missing description
    return desc

def main(tsv):
    """ Main function for parsing TSV file """
    handle = open(tsv, 'rU')
    outfile = open(tsv+'.csv', 'w')
    
    for line in handle:
        try:
            date, time, code, value = line.strip('\n').split('\t')
        except:
            print (tsv)
            print (line)
            raise  # original behaviour (raises error)
        isodate = standardize_date(date)
        desc = translate_code(code)
        outfile.write(','.join([isodate, time, desc, value]) + '\n')
        
    outfile.close()
    handle.close()    

