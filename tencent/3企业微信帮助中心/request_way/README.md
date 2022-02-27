## 使用方式

测试url和下载分开实现的原因是因为下载时候如果存在js渲染 可以使用 selenium 而selenium 速度太慢

### 寻找url

多线程速度会更快 但是 因为目前没有编写代理部分 也没有编写 进程记录部分 一段时间请求失败 需要根据爬取url重新定义起始点等参数 
单线程和多线程抓取到的结果理论上是完全一样的 

```bash
python a.py // 单线程抓取 存放到 ./requests_url.txt
python m.py // 多线程抓取 存放到 ./requests_url_thread.txt
```

### 清洗URL 下载网页

清洗数据 
```bash
python w_a.py // 清洗单线程数据
python w_m.py // 清洗多线程数据
```
抓取网页
```bash
python d.py
```
