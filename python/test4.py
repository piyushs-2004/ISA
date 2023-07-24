import os
import io
import requests
from bs4 import BeautifulSoup
from PIL import Image
import shutil
from funtioning import check_obscene
#url = 'https://cheery-mermaid-32f0cb.netlify.app/'
# url='https://www.doubtnut.com/'
def download(url):
    folder_name = "downloaded_image"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    image = soup.find_all('img')
    image2=soup.find_all('a')
    c=0
    link={}
    for i in image:
        if c<50:
            chr=i['src']
            if chr[-5:].lower()=='.webp' and chr[:7]=='https://':
                img_data=requests.get(chr).content
                im=Image.open(io.BytesIO(img_data)).convert('RGB')
                name=chr.split('-')[0]
                img_path=os.path.join(folder_name,name[-5:]+'.png')
                im.save(img_path[:-5]+'.png','PNG')
                link[name]=i['src']
                with open(img_path,'wb') as f:
                    img_data=requests.get(chr).content
                    f.write(img_data)
                    print(f"Downloaded {name}")
                c+=1
            # elif chr[-5:].lower()=='.svg' and chr[:7]=='https://':
            #     convert = svg2rlg(chr[:-4])
            #     renderPM.drawToFile(convert,chr[:-4]+'.png',fmt='PNG')
            #     name=chr.split('/')[-1].split('?')[0]
            #     img_path=os.path.join(folder_name,name)
            #     with open(img_path,'wb') as f:
            #         img_data=requests.get(chr).content
            #         f.write(img_data)
            #         print(f"Downloaded {name}")
            #     count+=1  
        elif chr!='' and chr[-4:].lower()!='.gif' and chr[:7]=='https://':
                if chr[-4:].lower()=='.jpg' or chr[-4:].lower()=='.png' or chr[-5:].lower()=='.jpeg':
                    name=chr.split('/')[-1].split('?')[0]
                    img_path=os.path.join(folder_name,name)
                    link[name]=i['src']
                    with open(img_path,'wb') as f:
                        img_data=requests.get(chr).content
                        f.write(img_data)
                        print(f"Downloaded {name}")
                    c+=1
    for j in image2:
        if c<50:
            chr2=j['href'] 
            if chr2!='' and chr2[-4:]!='.gif':
                    if chr2[-4:].lower()=='.jpg' or chr2[-4:].lower()=='.png' or chr2[-5:].lower()=='.jpeg':
                        name=chr2.split('/')[-1].split('?')[0]
                        img_path=os.path.join(folder_name,name)
                        link[name]=j['href']
                        with open(img_path,'wb') as f:
                            img_data=requests.get(chr2).content
                            f.write(img_data)
                            print(f"Downloaded {name}")
                        c+=1
    obscene_links=check_obscene(folder_name,link)
    return obscene_links
    #shutil.rmtree(folder_name)