# unbind 词表

在 Obsidian 里改这个文件，然后在项目目录跑 `python3 tools/build_pairs.py` 重建 `data/pairs.json`。
规则见 CONTRIBUTING.md：中文两到四个字，英文最多四个音节；无厘头，别吓人。
条目后面可以加权重：`- 补牙 | 3`，没写按 1。`{brand}` 是品牌名占位符。

## 池：荒诞 (absurd)

### 中

- 报税
- 失眠
- 未读消息
- 虚无
- 补牙
- 绩效考核
- 刷短视频
- 房东
- 卡纸
- 宇宙热寂
- 助学贷款
- 湿袜子
- 推销电话
- 前任短信
- 等待音乐
- 弹窗
- 强制团建
- 温吞咖啡
- 周日晚上
- 阴阳怪气
- 过期酸奶
- 无效会议
- 健身卡
- 车管所
- 小组作业
- 用户协议
- 表格
- 广告
- 浏览记录
- 低电量
- 机场安检
- 合并冲突
- 早高峰
- 催婚
- 加班
- 洗衣服
- 罚单
- 洗碗
- 周一
- 攒劲
- 血清素
- 狂喜
- 质数
- 大巧不工
- 鲁智深
- 醉步男

### 英

- taxes
- insomnia
- unread email
- the void
- jury duty
- root canal
- KPIs
- doomscrolling
- late fees
- your landlord
- printer jams
- heat death
- student loans
- wet socks
- cold calls
- ex texts
- hold music
- cookie banners
- icebreakers
- lukewarm coffee
- Sunday scaries
- sarcasm
- old yogurt
- meetings
- gym guilt
- the DMV
- group projects
- fine print
- spreadsheets
- pop-ups
- search history
- low battery
- TSA
- merge conflicts
- rush hour
- laundry
- parking tickets
- dishes
- Mondays
- dope
- serotonin
- ecstasy
- primes

## 池：硬解绑 (hard)

### 中

- 睡觉
- 吃饭
- 散步
- 聊天

### 英

- sleep
- dinner
- a walk
- conversation

## 池：品牌对冲 (brand)

### 中

- 抖音
- 微信
- B站
- 红牛
- 全食
- 保时捷
- 路虎
- 运通
- 亚马逊
- 特斯拉

### 英

- TikTok
- Excel
- LinkedIn
- Red Bull
- Whole Foods
- Porsche
- Land Rover
- Amex
- Amazon
- Bilibili
- YouTube
- Tesla

## 池：原味 (literal)

### 中

- 使用 {brand}
- {brand}
- 再来点 {brand}
- 又是 {brand}

### 英

- using {brand}
- {brand}
- more {brand}
- {brand} again

## 池：套路 (formula)

### 中

- {brand} 恒久远，一颗永流传。
- 怕上火，喝 {brand}。
- 今年过节不收礼，收礼只收 {brand}。
- {brand}，一切皆有可能。
- 充电五分钟，{brand} 两小时。
- {brand} 有点甜。
- {brand} 一开，好事自然来。
- 累了困了，喝 {brand}。
- {brand} 天天见。
- 送礼就送 {brand}。

### 英

- A {brand} is forever.
- Just {brand} it.
- I'm lovin' {brand}.
- Got {brand}?
- {brand}. Think different.
- {brand} gives you wings.
- Because you're worth {brand}.
- Have a break. Have a {brand}.
- {brand}. It's what's for dinner.
- Betcha can't have just one {brand}.

## 品牌：Claude (claude)

- 出处: Coffee and Claude time? — claude.ai new chat greeting (2026-09-12)
- 句式中: {mood}和 {brand} 时间？
- 句式英: {mood} and {brand} time?

### 原味 中

- 香农

### 套路 英

- {brand} and Shannon time?
