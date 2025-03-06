# coding:utf-8
import configparser
from pygtrans import Translate
from bs4 import BeautifulSoup
import os
import hashlib
from urllib import request, parse

# 计算 MD5 值
def get_md5_value(src):
    return hashlib.md5(src.encode('utf-8')).hexdigest()

# 读取和解析 test.ini
with open('test.ini', 'r', encoding='utf-8') as f:
    ini_data = parse.unquote(f.read())
config = configparser.ConfigParser()
config.read_string(ini_data)
sections = config.sections()

def get_cfg(section, key):
    return config.get(section, key).strip('"')

def set_cfg(section, key, value):
    config[section][key] = f'"{value}"'

def get_translation_config(section):
    action = get_cfg(section, 'action')
    return ('auto', 'zh-CN') if action == 'auto' else action.split('->')

# 创建输出目录
BASE = get_cfg('cfg', 'base')
os.makedirs(BASE, exist_ok=True)

links = []
def translate_rss(section):
    name = get_cfg(section, 'name')
    out_dir = os.path.join(BASE, name)
    url = get_cfg(section, 'url')
    max_items = int(get_cfg(section, 'max'))
    old_md5 = get_cfg(section, 'md5')
    source, target = get_translation_config(section)

    global links
    links.append(f" - {section} [{url}]({url}) -> [{name}]({parse.quote(out_dir)})\n")

    # 获取 RSS 内容
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36'
    }
    try:
        req = request.Request(url, headers=headers)
        html_doc = request.urlopen(req).read().decode('utf-8')
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")
        return

    new_md5 = get_md5_value(html_doc)
    if old_md5 == new_md5:
        print(f"No changes in {url}, skipping.")
        return
    set_cfg(section, 'md5', new_md5)

    # 解析和处理 RSS
    html_doc = html_doc.replace('<?', '</s').replace('?>', '/>')
    soup = BeautifulSoup(html_doc, 'xml')  # 使用 xml 解析器更适合 RSS
    for idx, item in enumerate(soup.find_all('item')):
        if idx >= max_items:
            item.decompose()

    content = str(soup)
    content = content.replace('<title', '<stitle').replace('title>', 'stitle>')
    content = content.replace('<pubDate>', '<pubDate><span translate="no">')
    content = content.replace('</pubDate>', '</span></pubDate>')

    # 翻译内容
    translator = Translate()
    try:
        translated = translator.translate(content, target=target, source=source)
        if not translated or not translated.translatedText:
            raise ValueError("Translation returned empty result")
        content = translated.translatedText
    except Exception as e:
        print(f"Translation failed for {url}: {e}")
        return

    # 还原标签
    content = (content.replace('<stitle', '<title')
                     .replace('stitle>', 'title>')
                     .replace('<span translate="no">', '')
                     .replace('</span></pubDate>', '</pubDate>'))

    # 写入文件
    with open(out_dir, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Translated: {url} > {out_dir}")

# 处理每个 RSS 源
for section in sections[1:]:
    translate_rss(section)
    print(config.items(section))

# 保存更新后的配置
with open('test.ini', 'w', encoding='utf-8') as configfile:
    config.write(configfile)

# 更新 README.md
def update_readme(file_path="README.md"):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        for idx, line in enumerate(lines):
            if "## rss translate links" in line:  # 动态查找插入点
                insert_idx = idx + 2
                break
        else:
            insert_idx = len(lines)
        new_lines = lines[:insert_idx] + links
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
    except Exception as e:
        print(f"Failed to update README.md: {e}")

update_readme()
