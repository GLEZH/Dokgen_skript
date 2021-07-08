import xlrd
import xlwt
from docxtpl import DocxTemplate

NumberZ = 100
AktNumber = 1000

#---------------------------------------------------------------------------

book = xlwt.Workbook('utf8')
font = xlwt.easyxf('font: height 240,name Arial,colour_index black, bold off,\
    italic off; align: wrap on, vert top, horiz left;\
    pattern: pattern solid, fore_colour green;')
sheet = book.add_sheet('sheet')
sheet.write(0, 0, "ФИО", font)
sheet.write(0, 1, "Рамочный", font)
sheet.write(0, 2, "Заявка-заказ", font)
sheet.write(0, 3, "Акт", font)
#---------------------------------------------------------------------------

x = 1
y = 1
o = 1
r = 1

#---------------------------------------------------------------------------

xldata = []
wb=xlrd.open_workbook("тинькоф новые 1.xls")
sh = wb.sheet_by_index(0)
for rownum in range(sh.nrows):
    xldata.append(sh.row_values(rownum))

#---------------------------------------------------------------------------

for u in range(len(xldata)):
    # ---------------------------------------------------------------------------
    doc = DocxTemplate("Templates/Ramochnyi_dogovor.docx")
    doc1 = DocxTemplate("Templates/Zadanye.docx")
    doc2 = DocxTemplate("Templates/Akt_vypolnennyh_rabot.docx")
    # ---------------------------------------------------------------------------

    data = xldata[u]
    Num = int(data[3])
    WorkerName = str(data[0]) + ' ' + str(data[1]) + ' ' + str(data[2])
    MailofWorker = 'Miketyson707@yandex.ru'
    inn = str(int(data[10]))
    Date_of_Birth = str(data[11])
    Adres_Worker = data[12]
    Passport = str(data[13]) + ' ' + 'Выдан:' + str(data[14]) + ' ' + str(data[15])
    TelephoneOfWorker = str(data[16])
    DescriptionOfWork = data[6]
    EvaragCoast = str(round(float(data[4]), 2)) + ' ' + 'руб.'
    DataStart = str(data[7])
    DataStop = str(data[8])
    NumberZ += 1
    AktNumber += 1
    TotalCoast = str(round(float(data[5]), 2)) + ' ' + 'руб.'








    # ---------------------------------------------------------------------------

    context = { 'DataST' : DataStart, 'Num' : Num,'WorkerName' : WorkerName,'InnNunber' : inn,'Date_of_Birth' : Date_of_Birth,'Adres_Worker' : Adres_Worker, 'MailOfWorker' : MailofWorker, 'Passport' : Passport, 'TelephoneOfWorker' : TelephoneOfWorker}
    doc.render(context)
    doc.save(f'{inn}' + '_' + "Договор" + '_' + WorkerName + '.docx')
    #convert("Договор" + WorkerName + f'{inn}' +'.docx')

    # ---------------------------------------------------------------------------
    context1 = { 'DataST' : DataStart, 'NumberZ' : NumberZ, 'RamochniyDataNum' : Num, 'WorkerName' : WorkerName, 'InnNunber' : inn, 'DescriptionOfWork' : DescriptionOfWork, 'EvaragCoast': EvaragCoast, 'DataStart' : DataStart, 'DataStop' : DataStop, 'Date_of_Birth' : Date_of_Birth,'Adres_Worker' : Adres_Worker, 'MailOfWorker' : MailofWorker, 'Passport' : Passport, 'TelephoneOfWorker' : TelephoneOfWorker}
    doc1.render(context1)
    doc1.save(f'{inn}' + '_' + "Заявка-заказ" + '_' + WorkerName + '.docx')
    #convert("Заявка-заказ" + WorkerName + f'{inn}' + '.docx')

    # ---------------------------------------------------------------------------
    context2 = {'WorkerName' : WorkerName, 'InnNunber' : inn, 'AktNumber' : AktNumber, 'NumberZ' : NumberZ, 'RamochniyDataNum' : Num, 'DataStart' : DataStart, 'DataStop' : DataStop, 'DescriptionOfWork' : DescriptionOfWork, 'TotalCoast' : TotalCoast, 'TotalCostText' : TotalCoast, 'Date_of_Birth' : Date_of_Birth,'Adres_Worker' : Adres_Worker, 'MailOfWorker' : MailofWorker, 'Passport' : Passport, 'TelephoneOfWorker' : TelephoneOfWorker}
    doc2.render(context2)
    doc2.save(f'{inn}' + '_' + "Акт выполненных работ" + '_' + WorkerName + '.docx')
    #convert("Акт выполненных работ" + WorkerName + f"{inn}" + '.docx')



