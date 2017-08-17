#Script to find the number of regex matches from sheet A with Urls in sheet B
import xlrd
import xlwt
from regexcomp import Regexcomp

rtester = Regexcomp()
input_pattern_sheet = xlrd.open_workbook("pattern.xlsx")
input_urls_sheet = xlrd.open_workbook("urls.xlsx")
input_pattern_sheet.sheet_names()
input_urls_sheet.sheet_names()
#Choose the first sheet
sh_pattern = input_pattern_sheet.sheet_by_index(0)
sh_urls = input_urls_sheet.sheet_by_index(0)
#Choose the encoding format for output Excel Sheet and Name for the sheet
output = xlwt.Workbook(encoding="utf-8")
sw = output.add_sheet("sheet 1")
styleb=xlwt.easyxf('font:color-index black, bold on')
output_row = 1
output_col = 0
url_row = 0
url_col = 0
pattern_row = 0
pattern_col = 0
regex_count=0
sw.write( 0, 0, 'URL' , styleb)
sw.write( 0, 1, 'Number Of Regex Matches', styleb )
sw.write( 0, 2, 'Matching Regex', styleb )
INT_NUMBER_OF_PATTERNS = sh_pattern.nrows
print INT_NUMBER_OF_PATTERNS
INT_NUMBER_OF_URLS = sh_urls.nrows
print INT_NUMBER_OF_URLS
for url_row in range(0,INT_NUMBER_OF_URLS):
    sw.write( output_row, 0, sh_urls.cell(url_row,url_col).value )
    output_col = 2
    regex_count = 0
    for pattern_row in range(0,INT_NUMBER_OF_PATTERNS):
        regex_count = regex_count + 1
        try:
            temp = rtester.comp( sh_pattern.cell(pattern_row,pattern_col).value, sh_urls.cell(url_row,url_col).value )
            sw.write( output_row, output_col, sh_pattern.cell(pattern_row,pattern_col).value )
            output_col = output_col + 1
        except Exception:
            regex_count = regex_count - 1
            pass
        pattern_row = pattern_row +1
    url_row = url_row + 1
    sw.write( output_row, 1, regex_count )
    output_row = output_row + 1
output.save("results.xls")