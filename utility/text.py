import cv2
import pytesseract

def get_text(pic):
    
    tessdata_dir_config  =  r' -  tessdata-dir“<replace_with_your_tessdata_dir_path>”'
    img = cv2.imread(pic)
    text=pytesseract.image_to_string(img, lang='chi_sim', config=tessdata_dir_config)
    print(text)

get_text(r'D:\Work\GitHub\Dnfpy\utility\test.png')