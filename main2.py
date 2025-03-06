# coding:utf-8
import configparser
from pygtrans import Translate
import os
import hashlib
import datetime
import time
from rfeed import *
import feedparser
from urllib import parse

# 计算字符串的 MD5 值
def get_md5_value(src):
    return hashlib.md5(src.encode('utf-8')).hexdigest()

# 获取 RSS 条目的发布时间
def get_time(entry):
    try:
        return datetime.datetime(*entry.published_parsed[:6])
    except (AttributeError, TypeError):
        return datetime.datetime.now()

# 获取 RSS 源的副标题
def get_subtitle(feed):
    return getattr(feed, 'subtitle', '')

class GoogleTran:
    def __init__(self, url, source='auto', target='zh-CN'):
        self.url = url
        self.source = source
        self.target = target
        self.client = Translate()
        try:
            self.feed = feedparser.parse(url)
        except Exception as e:
            print(f"Error parsing RSS feed {url}: {e}")
            self.feed = None

    def translate(self, content):
        if not content or self.source == 'proxy':
            return content
        try:
            result = self.client.translate(content, target=self.target, source=self.source)
            return result.translatedText if result else ""
        except Exception as e:
            print(f"Translation error: {e}")
            return ""

    def get_new_content(self, max_items=2):
        if not self.feed or not self.feed.entries:
            return None
        item_list = []
        max_items = min(max_items, len(self.feed.entries))
        for entry in self.feed.entries[:max_items]:
            item = Item(
                title=self.translate(entry.title),
                link=entry.link,
                description=self.translate(entry.summary),
                guid=Guid(entry.link),
                pubDate=get_time(entry)
            )
            item_list.append(item)
        feed = self.feed.feed
        new_feed = Feed(
            title=self.translate(feed.title),
            link=feed.link,
            description=self.translate(get_subtitle(feed)),
            lastBuildDate=get_time(feed),
            items=item_list
        )
        return new_feed.rss()

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
    return ('proxy', 'proxy') if action == 'proxy' else action.split('->') if '->' in action else ('auto', 'zh-CN')

# 创建输出目录
BASE = get_cfg('cfg', 'base')
os.makedirs(BASE, exist_ok=True)

links = []
def process_section(section):
    name = get_cfg(section, 'name')
    out_dir = os.path.join(BASE, name)
    url = get_cfg(section, 'url')
    max_items = int(get_cfg(section, 'max'))
    source, target = get_translation_config(section)
    
    global links
    links.append(f" - {section} [{url}]({url}) -> [{name}]({parse.quote(out_dir)})\n")
    
    translator = GoogleTran(url, source=source, target=target)
    content = translator.get_new_content(max_items)
    if content:
        with open(out_dir, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Translated: {url} > {out_dir}")
    else:
        print(f"Skipped {url} due to fetch or translation failure")

# 处理每个 RSS 源
for section in sections[1:]:
    process_section(section)
    print(config.items(section))

# 保存更新后的配置
with open('test.ini', 'w', encoding='utf-8') as configfile:
    config.write(configfile)

# 更新 README.md
def update_readme(file_path="README.md"):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for idx, line in enumerate(lines):
        if "## rss translate links" in line:
            break
    else:
        idx = len(lines)
    new_lines = lines[:idx + 2] + links
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

update_readme()
