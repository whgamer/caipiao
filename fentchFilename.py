import os
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3NoHeaderError

import os
import re
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3NoHeaderError

# 过滤掉Windows不允许的文件名字符
def sanitize_filename(name):
    # 定义Windows文件名中不允许使用的字符
    illegal_chars = r'[\/:*?"<>|]'
    # 使用正则表达式去除这些非法字符
    return re.sub(illegal_chars, '', name)

def rename_file_with_metadata(file_path):
    try:
        # 打开音频文件，提取metadata
        audio = EasyID3(file_path)
        title = audio.get('title', [''])[0].encode('utf-8').decode('utf-8')
        album = audio.get('album', [''])[0].encode('utf-8').decode('utf-8')

        # 检查title和album是否为空
        if not title or not album:
            print(f"跳过文件（title或album为空）: {file_path}")
            return  # 跳过该文件，继续处理下一个

        # 过滤非法字符
        sanitized_title = sanitize_filename(title)
        sanitized_album = sanitize_filename(album)

        # 组合新的文件名
        new_file_name = f"{sanitized_title} + {sanitized_album}{os.path.splitext(file_path)[1]}"

        # 获取文件所在目录
        file_dir = os.path.dirname(file_path)

        # 生成新的完整路径
        new_file_path = os.path.join(file_dir, new_file_name)

        # 重命名文件
        os.rename(file_path, new_file_path)
        print(f"文件重命名为: {new_file_path}")

    except ID3NoHeaderError:
        print(f"文件没有ID3标签: {file_path}")

def rename_files_in_directory(directory):
    # 遍历目录中的所有文件
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            rename_file_with_metadata(file_path)


# 指定你想处理的文件夹路径
directory = r'F:\secret\mp3'
rename_files_in_directory(directory)
