4W - Web 101 日记本

- 任务目标：在CLI基础上完成极简交互笔记的Web版本(万维网)
- 需求如下：
    - 通过网页访问系统：
        - 每次运行时合理打印出过往的所有笔记
        - 一次接受输入一行笔记
        - 在服务器端保存为文件
    - 同时兼容3W的Net版本的命令行界面进行交互
- 发布到各自仓库`_src/0m2py4w/4wex0/`目录中
- 关键技术
    - [Bottle框架](http://bottlepy.org/)（快速完成原型)
    - C/S 服务器/客户端架构系统

- 推荐使用 Bottle 框架来快速完成原型:
  - 发布一个网站
  - 可以接收用户输入
  - 可以动态将用户输入打印回网页


Bottle 内置的模板非常简单,简单到什么都要自个儿撸
那么使用现成的模板系统来美化网站吧!

Jinja2 (The Python Template Engine)
什么是模板?
为什么有模板?
Python 世界中有哪些模板?
为什么大妈推荐 Jinja2?

网站的美化是没有极限的!
但是,我们有什么方法可以用最小成本美化到足够拿出手?!

Bootstrap · The world's most popular mobile-first and responsive front-end framework.
Bootstrap 的生态包含了什么?
为什么 Bootstrap 如此受欢迎?
有更加简洁的同类 样式 框架嘛?

网站能看了,但是,数据还在用文件就不够看了...
嗯哼?! 为什么!?
必须用数据库了,但是,还不会 SQL 怎么办?
给我们的网站配置上一种 NoSQL 数据库吧!

什么是 NoSQL ?
NoSQL 分哪些种类?
哪种最简单?
如何策略数据库结构?
如何迁移数据?
如何备份?
11.13. sqlite3 — DB-API 2.0 interface for SQLite databases — Python 2.7.10 documentation
11.11. bsddb — Interface to Berkeley DB librayr — Python 2.7.10 documentation
kvdb
bottle-simple-todo / wiki / Home — Bitbucket