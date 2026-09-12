# Contributing / 参与

## Add a scenario / 投一个场景

**Easiest:** open an issue with the "Submit a pairing" template. The maintainer adds it to `data/pairs.json`.

**Or a pull request:** edit `words.md` (the source; plain Markdown headings and bullets), then run `python3 tools/build_pairs.py` to regenerate `data/pairs.json`. Do not edit the JSON by hand. 改 `words.md`（源文件，普通的 Markdown 标题和列表），然后跑 `python3 tools/build_pairs.py` 生成 `data/pairs.json`。不要手改 JSON。

Four kinds of entries / 四种手法:

- **absurd / 荒诞**: contrast, e.g. "root canal". 靠反差，比如"补牙"。
- **hard unbind / 硬解绑**: not a joke. Something worth doing instead, e.g. "sleep". The pairing is impossible on its face, and that is the point. 不是笑话，是本来该去做的事，比如"睡觉"。这句话本身就不成立，这就是它的力度。
- **brand hedge / 品牌对冲**: another brand in the same slot, e.g. "Starbucks". Shows the slot was an ad all along. Plain text only, no logos. 同一位置换成别家名字，比如"星巴克"，让人看出那个位置本来就是广告位。只用纯文字。
- **literal / 原味**: the sentence eats itself, e.g. "using {brand}". Use `{brand}` as a placeholder. 句子自己咬自己，比如"使用 {brand}"。用 `{brand}` 占位。

An entry that only works for one brand (Claude → "Shannon") goes under that brand's section in words.md (e.g. `### 原味 英` under `## 品牌：Claude`), not in the shared pools. 只对某个品牌成立的梗（Claude → "香农"）放在 words.md 里该品牌的小节下（如 `## 品牌：Claude` 下的 `### 原味 中`），不放共用池。
- **formula / 套路**: the brand dropped into a famous slogan, e.g. "A {brand} is forever." These are whole sentences, so the syllable rule does not apply; the rhythm is the slogan's own. Plain text only. 把品牌放进一句著名广告语，比如"{brand} 恒久远，一颗永流传。"这类是整句，音节规则不适用，节奏就是那条广告自己的节奏。只用纯文字。

最简单：用「投稿」Issue 模板。或者直接改 `data/pairs.json`，在 `moods.en` 或 `moods.zh` 里追加，保持 JSON 合法。

## Rules / 规则

- Absurd and mundane is the target. Nothing scary, nothing heavy: a wet sock, yes; an illness, no. 要的是无厘头和琐碎。别吓人、别沉重：湿袜子可以，生病不行。
- No real people, no slurs, nothing targeting a group. A historical name that the brand itself points to is fine ("Claude and Shannon time?"). 不要真实人物，不要歧视，不要针对群体。品牌名本身指向的历史人物可以（"Claude and Shannon time?"）。
- The original is "Coffee": two syllables. Match its length by sound, not by word count. Three syllables is the target, four is the limit ("root canal" yes, "performance review" no). In Chinese, two to four characters. Why: the rhythm is the binding. The new line only lands if it rides the same beat as the original; break the cadence and it is just a sentence. 中文两到四个字。为什么：节奏本身就是绑定的载体。换了词的那句要踩在原句同一个拍子上才会被同一套反应接住，节奏一乱就只是一句普通的话。原句是 "Coffee"，两个音节。按发音长度对齐，不按词数：三个音节是目标，四个封顶（"root canal" 行，"performance review" 不行）。中文两到四个字。
- Any brand that greets you with a mood is fair game. Claude is just the first entry. To add a brand, give its real greeting line, where you saw it, and a template per language in `data/pairs.json`. 任何用情绪跟你打招呼的品牌都可以收录，Claude 只是第一个词条。加品牌时在 `data/pairs.json` 里给出它的真实欢迎语、出处，以及每种语言的句式模板。

## Votes / 投票

Like an entry? Give its submission issue a 👍 on GitHub. There is no vote button on the page and no backend; the maintainer folds 👍 counts into a `weight` field in `data/pairs.json` now and then, and the generator draws by weight. Entries without a weight count as 1.

喜欢某一条？去它的投稿 Issue 点个 👍。页面上没有投票按钮，也没有后端；维护者隔一阵把 👍 数折算进 `data/pairs.json` 的 `weight` 字段，生成器按权重抽。没写 weight 的按 1 算。

Entry format in words.md / 条目格式: `- root canal` or `- root canal | 3`.

## Screenshots / 截图

Crop to the greeting line only. Do not include the whole page, sidebars, or any account information.
只截欢迎语那一行，不要整页、侧边栏或任何账号信息。

## Legal boundaries already decided / 已定的边界

- In anything we write or design ourselves, brand names are plain text only, no logos. Logos that appear inside a product screenshot are part of the record and stay. 我们自己写或画的部分，商标只用纯文字，不用 logo；截图里产品自带的 logo 属于客观记录，保留。
- Keep the "not affiliated" notice on the page. 页面上保留「非官方关联」声明。
- Screenshots are partial crops, never full pages. 截图只截局部。
