import os
import re

# 设置电影文件夹路径
folder_path = 'F:\mov\movie'

# 正则表达式，用于匹配并删除方括号及其中的内容
pattern = re.compile(r'\[.*?\]')

# 自定义需要替换为空的字符串
strings_to_remove = [
    '阳光电影www.ygdy8.com.',
    '阳光电影dygod.org.',
    '1080P.中英双字',
    'BD.1080P',
    '中英双字',
    'H265',
    '1080P.',
    '1080p.',
    '720p',
    'WEB.h264-QUiNTESSENCE',
    '.HD1080P.X264.AAC.Korean.CHS.BDYS',
    'HDX264.AAC.Korean.CHS.BDYS.',
    '.Chi_Jap.HDTVrip.1280X720-ZhuixinFan',
    '.1080p.NF.WEB-DL.DDP5.1.H.264-MagicStar',
    '.NF.WEB-DL.DDP5.1.H.264-MagicStar',
    '.HD1080p',
    'BD韩语中字',
    '.BD',
    '.中文字幕',
    '.日语中字',
    '中英双字',
    '.国日双语中字',
    '.国语中字'
]

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    # 新文件名：去掉方括号及其中内容
    new_filename = re.sub(pattern, '', filename).strip()
    
    # 替换指定的字符串为空
    for string in strings_to_remove:
        new_filename = new_filename.replace(string, '')
    
    # 去除多余空格
    new_filename = new_filename.strip()
    
    # 获取文件的完整路径
    old_file = os.path.join(folder_path, filename)
    new_file = os.path.join(folder_path, new_filename)
    
    # 重命名文件
    os.rename(old_file, new_file)
    print(f'Renamed: {filename} -> {new_filename}')

print("所有文件已重命名完毕！")
