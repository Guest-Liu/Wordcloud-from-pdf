import io
from pdfminer.converter import PDFConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage

def pdf_to_file(file_path):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = PDFConverter(resource_manager,fake_file_handle)
    page_interpreter = PDFPageInterpreter(converter,resource_manager)

    with open(filename,'rb') as fp:
        fp.seek(0,0) 
        for page in PDFPage.get_pages(fp,
                                      caching=True,
                                      check_extractable=True):
            page_interpreter.process_page(int(0))

        text = fake_file_handle.getvalue()

    converter.close()
    fake_file_handle.close()

    if text:
        return text

if __name__ =='__main__':
    filename = 'CV.pdf'
    print(pdf_to_file('fp'))

        
