

# 生成 requirements
'''
pip install pipreqs
pipreqs ./ --force
'''

```

    def Search(self, keyword):
        '''
        查找微信好友或关键词
        keywords: 要查找的关键词，str   * 最好完整匹配，不完全匹配只会选取搜索框第一个
        '''
        self.UiaAPI.SetFocus()
        time.sleep(0.2)
        self.UiaAPI.SendKeys('{Ctrl}f', waitTime=1)
        self.UiaAPI.SendKeys('{Ctrl}a', waitTime=0.5)  # 全选文本
        self.UiaAPI.SendKeys('{Delete}', waitTime=0.5)  # 删除选中的文本
        time.sleep(0.2)
        self.UiaAPI.SendKeys('{Ctrl}f', waitTime=1)
        self.SearchBox.SendKeys(keyword, waitTime=1.5)
        self.SearchBox.SendKeys('{Enter}')
```


'''
	python -m pip install --upgrade pip
	pip install --ignore-installed -r requirements.txt
'''


```
curl -X POST -F "file=@/Users/panda/Desktop/github.nosync/ticketing-website/backend/data/16211702261434_.pic.jpg" http://14.103.200.99:8001/test/upload_file
```


```
图片字体安装
sudo apt-get install fonts-arphic-ukai


生成图片需要清理字体缓存
rm -rf ~/.cache/matplotlib

```


```
#清华源
pip install markdown -i https://pypi.tuna.tsinghua.edu.cn/simple

# 阿里源
pip install markdown -i https://mirrors.aliyun.com/pypi/simple/

# 腾讯源
pip install markdown -i http://mirrors.cloud.tencent.com/pypi/simple

# 豆瓣源
pip install markdown -i http://pypi.douban.com/simple/

作者：waws520
链接：https://juejin.cn/post/7141566114412101662
来源：稀土掘金
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。





# 清华源
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

# 阿里源
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/

# 腾讯源
pip config set global.index-url http://mirrors.cloud.tencent.com/pypi/simple

# 豆瓣源
pip config set global.index-url http://pypi.douban.com/simple/# 换回默认源pip config unset global.index-url



作者：waws520
链接：https://juejin.cn/post/7141566114412101662
来源：稀土掘金
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


```