from jinja2 import Environment, FileSystemLoader
import pdfkit

path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)


class PdfFromTemplate:

    def __init__(self, name, AktNumber, NumberZ, RamochniyDataNum, DataST, WorkerName,
                 InnNumber, DataStart, DataStop, DescriptionOfWork, TotalCoast, TotalCostText, Date_of_Birth):
        # self.name = str(name)
        self.AktNumber = int(AktNumber)
        self.NumberZ = str(NumberZ)
        self.RamochniyDataNum = str(RamochniyDataNum)
        self.DataST = str(DataST)
        self.WorkerName = str(WorkerName)
        self.InnNumber = int(InnNumber)
        self.DataStatr = str(DataStart)
        self.DataStop = str(DataStop)
        self.DescriptionOfWork = DescriptionOfWork
        self.TotalCoast = TotalCoast
        self.TotalCostText = TotalCostText
        self.Date_of_Birth = Date_of_Birth

    def FromHtml(self):
        env = Environment(loader=FileSystemLoader('.'))
        template = env.get_template("Akt_rabot.html")
        pdf_template = template.render(
            dict(AktNumber=self.AktNumber, NumberZ=self.NumberZ, RamochniyDataNum=self.RamochniyDataNum,
                 DataST=self.DataST, WorkerName=self.WorkerName, InnNumber=self.InnNumber, DataStatr=self.DataStatr,
                 DataStop=self.DataStop, DescriptionOfWork=self.DescriptionOfWork, TotalCoast=self.TotalCoast,
                 TotalCostText=self.TotalCostText, Date_of_Birth=self.Date_of_Birth))
        pdfkit.from_string(pdf_template, 'out.pdf', configuration=config)

    pass


Alex = PdfFromTemplate('1', '1', '1', '3', '4', 1, '2', '4', '5', '5', '5', '5', '5')

Alex.FromHtml()
