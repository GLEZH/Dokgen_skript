from jinja2 import Environment, FileSystemLoader
import pdfkit


class PdfFromTemplate:

    def __init__(self, name="no name"):
        self.name = name

    def FromHtml(self):
        env = Environment(loader=FileSystemLoader('.'))
        template = env.get_template("pdf_template.html")
        pdf_template = template.render({'name': self.name})
        pdfkit.from_string(pdf_template, 'out.pdf')

    pass


Alex = PdfFromTemplate("Александр")

Alex.FromHtml()
