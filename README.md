# Lost-Found
A web lost and found system,which face to university.


#软件开发计划书

[TOC]

**项目名称:跨平台失物招领系统**
**日期:2018-5-10**
###技术栈
- Web端采用Django1.8+mysql,对不同设备进行适配
- 使用Nginx负载均衡,方便将请求分发至个服务器,并进行单个服务器调试
- 后期开发小程序版
###预期实现功能清单:
- 主页面(简洁至上)
  - 最新动态
    - 在主页根据发布时间陈列信息，并运用ajax以及浏览器定位功能动态刷新添加信息，并可以通过筛选功能筛选陈列的信息(如信息类型，地点，物品类型等)
  - 动态展示发布的失物招领(按时间排序,按回复量排序,按照悬赏金额排序,按照离我现在的位置排序)
  - 添加搜索,使用模糊查询|分类查询|按时间查询等功能
  - 发布物品按钮
  - 展示已成功处理失物招领数
- 发布物品页面
  - 包括标题，类型，可能遗失地点，上传图片功能，可选联系方式
  - 模式1:寻找物品主人
  - 模式2:寻找丢失物品(可设置悬赏,接入支付宝API)
  - 坐标信息录入(接入地图API)
- 消息推送页面
  - 匹配推送符合条件的信息(如发布寻物信息后，根据可能遗失地点、意识物品类型、证件信息等模糊匹配数据库中的招领信息，然后推送给失主，此后每当有招领信息发布，后台程序匹配符合此信息条件的失主然后推送
- 物品详情页面
  - 展示|描述物品
  - 留言功能(多级评论系统)
  - 分享链接功能
  - 私信(待定,技术难度较高)
- 登录|注册页面
  - 接入QQ|微信快捷登录(后期考虑接入学号数据库)
  - 找回密码(通过邮箱绑定等)
  - 用户密码采用非对称加密,一次登录后便将公钥加密后的密码存在用户的cookie中，免去每次登录的繁琐
- 荣誉墙
  - 根据用户的经验值来生成排行榜
- 用户个人页面
  - 修改个人信息|密码等
  	 查看|删除|修改|发布物品,处理申领(	我的发布|申领管理|我的申领);
- 后台管理页面
  - 用户管理
  - 发布管理

###数据库设计
- 绘制ER图
- 建表
###任务分工
- 暂时未定
###时间安排
- 2017-2018学年后八周
