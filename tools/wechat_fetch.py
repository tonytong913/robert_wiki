#!/usr/bin/env python3
"""
微信公众号文章抓取工具
通过搜狗微信搜索间接获取文章内容
"""

import sys
import re
import urllib.request
import urllib.parse
from html.parser import HTMLParser

class WechatArticleFetcher:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
    
    def extract_title_from_url(self, url):
        """从微信文章URL中提取标题"""
        try:
            # 尝试直接获取
            req = urllib.request.Request(url, headers=self.headers)
            with urllib.request.urlopen(req, timeout=10) as response:
                html = response.read().decode('utf-8', errors='ignore')
                
                # 提取标题
                title_match = re.search(r'<h1[^>]*class="rich_media_title[^"]*"[^>]*>(.*?)</h1>', html, re.DOTALL)
                if title_match:
                    title = re.sub(r'<[^>]+>', '', title_match.group(1)).strip()
                    return title
                
                # 备用方案
                title_match = re.search(r'<title>(.*?)</title>', html)
                if title_match:
                    return title_match.group(1).strip()
                    
        except Exception as e:
            print(f"获取失败: {e}")
        
        return None
    
    def search_sogou(self, keyword):
        """通过搜狗搜索找文章"""
        try:
            encoded = urllib.parse.quote(keyword)
            url = f"https://weixin.sogou.com/weixin?type=2&query={encoded}"
            
            req = urllib.request.Request(url, headers=self.headers)
            with urllib.request.urlopen(req, timeout=10) as response:
                html = response.read().decode('utf-8', errors='ignore')
                return html
        except Exception as e:
            print(f"搜索失败: {e}")
            return None


def main():
    if len(sys.argv) < 2:
        print("用法: python wechat_fetch.py <微信文章URL>")
        print("示例: python wechat_fetch.py 'https://mp.weixin.qq.com/s/xxxxx'")
        sys.exit(1)
    
    url = sys.argv[1]
    fetcher = WechatArticleFetcher()
    
    print(f"正在获取: {url}")
    title = fetcher.extract_title_from_url(url)
    
    if title:
        print(f"\n文章标题: {title}")
        print("\n注意: 微信文章需要特殊处理才能获取完整内容")
        print("建议: 使用浏览器插件如 '简悦' 或 'Obsidian Web Clipper' 保存文章")
    else:
        print("\n无法获取文章，可能原因:")
        print("1. 文章需要登录/验证")
        print("2. 链接已过期")
        print("3. 反爬机制拦截")
        print("\n建议方案:")
        print("- 使用浏览器打开文章，复制内容")
        print("- 使用 Obsidian Web Clipper 插件")
        print("- 使用 '简悦' 等阅读模式插件")


if __name__ == "__main__":
    main()
