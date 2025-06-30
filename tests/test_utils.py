import unittest
import os
from evidence_encoder.utils import *
import shutil 
from fpdf import FPDF
from tests.testing_helper import *
from dotenv import load_dotenv
load_dotenv()
FONT_PATH = os.getenv("FONT_PATH")
print(f"FONT_PATH: {FONT_PATH}")
class TestUtils(unittest.TestCase):
    
    def test_check_directory(self):
        self.assertEqual(check_directory(), None)
        try:
            shutil.rmtree('input')
        except FileNotFoundError:
            pass
    
    def test_non_default_directory(self):
        make_some_dummy_files()
        with self.assertRaises(ValueError):
            check_directory("non_default")
        try:
            shutil.rmtree('input')
        except FileNotFoundError:
            pass
    
    def test_check_pdf_files_pdf(self):
        make_some_dummy_files()
        self.assertRaises(SystemExit, check_pdf_files)
        try:
            shutil.rmtree('input')
        except FileNotFoundError:
            pass
    
    def test_check_pdf_files_empty_dir(self):
        os.makedirs('input', exist_ok=True)
        with self.assertRaises(ValueError):
            check_pdf_files()
        try:
            shutil.rmtree('input')
        except FileNotFoundError:
            pass
    
    def test_check_pdf_files_non_pdf(self):
        with self.assertRaises(SystemExit):
            make_some_dummy_files()
            check_pdf_files()
        try:
            shutil.rmtree('input')
        except FileNotFoundError:
            pass
        
    def test_get_all_file_path(self):
        make_some_dummy_files()
        file_paths = get_all_file_path()
        self.assertEqual(len(file_paths), 3)
        self.assertIn('input/test3.pdf', file_paths)
        try:
            shutil.rmtree('input')
        except FileNotFoundError:
            pass
    
    def test_get_file_info(self):
        make_some_dummy_files()
        create_fpdf("input", "test5.pdf")
        file_info = get_file_info("input/test5.pdf")
        self.assertTrue(file_info['file_size'] > 0)
        self.assertTrue(file_info['page_count'] > 0)
        self.assertIsInstance(file_info['metadata'], dict)
        self.assertEqual(file_info['first_page_orientation'], 'Portrait')
        try:
            shutil.rmtree('input')
        except FileNotFoundError:
            pass
        
    def test_add_text_to_pdf(self, FONT_PATH=FONT_PATH):
        testing_text = "扶她"  
        create_fpdf("input", "test6.pdf", orientation='P')
        self.assertTrue(add_text_to_pdf(
            "input/test6.pdf",
            "input/test6_with_text.pdf",
            page_num=0,text = testing_text,
            x=50, y=250,
            font_size=40,
            encoding = 'utf-8-sig',
            fontname = "TW-MOE-Std-Kai"
                        ))
        #find the text in the pdf
        doc = pymupdf.open("input/test6_with_text.pdf")
        page = doc[0]
        text_instances = page.search_for(testing_text)
        doc.close()
        self.assertTrue(len(text_instances) > 0, "Inserted text not found in PDF")
        print(f"Testing text: {testing_text} inserted and found successfully.")
        try:
            shutil.rmtree('input')
        except FileNotFoundError:
            pass
        
        
        
        

            
        
        
        
