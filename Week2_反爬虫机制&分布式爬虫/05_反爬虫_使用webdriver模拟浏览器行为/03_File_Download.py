# 小文件下载
import requests
image_url = 'https://www.python.org/static/community_logos/python-logo-master-v3-TM.png'
r = requests.get(image_url)
with open("python_logo.png",'wb') as f:
    f.write(r.content)

# 大文件下载
# 如果文件比较大的话, 那么下载下来的文件先放在内存中, 内存还是比较有压力的
# 所以为了防止内存不够用的现象出现, 我们要想办法把下载的文件分块写到磁盘中

file_url = 'https://cdn.acwing.com/media/user/profile/photo/2675_lg_ee24c7ba78.jpg'
r = requests.get(file_url,stream=True)
with open('acwing_logo.jpg','wb') as logo:
    for chunk in r.iter_content(chunk_size=1024):
        if chunk:
            logo.write(chunk)

