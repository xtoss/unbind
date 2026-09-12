# unbind

A tiny satire of brand-and-mood pairing in AI greetings.

A dictionary of brand-and-mood bindings, and their undoing. Some products greet you with a line like "Coffee and Claude time?". It quietly ties a brand to a pleasant feeling. **unbind** keeps the sentence and swaps the word, at random:

> Claude and **a root canal** time?
> **报税**和 Claude 时间？

If the trick works one way, it should work the other way too.

## Run locally

It is a static page, but it loads `data/pairs.json` with `fetch`, so open it over HTTP rather than as a file:

```bash
python3 -m http.server 8000
```

Then visit <http://localhost:8000>.

## Structure

```
index.html                              main page, random generator, EN / 中文 toggle
data/pairs.json                         brands (each with its real greeting and templates), mood lists
screenshots/                            cropped greeting screenshots (chatgpt.png, claude.png)
.github/ISSUE_TEMPLATE/submission.yml   submission form
```

## Contribute

Open a GitHub issue using the **Submit a pairing** template, or edit `data/pairs.json` directly in a pull request. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Disclaimer

Unofficial satire. Not affiliated with, endorsed by, or sponsored by Anthropic or OpenAI. In our own text, brand names appear only as plain words. The screenshots are cropped excerpts of each product's own interface, shown for comparison and commentary; the logos and interfaces in them belong to their respective owners.

## License

MIT

---

## 中文

有些 AI 产品用「Coffee and Claude time?」跟你打招呼，把品牌和愉快的情绪悄悄绑在一起。**unbind** 把句子留着，随机换掉那个词。

本地运行：`python3 -m http.server 8000`，然后打开 <http://localhost:8000>。

投稿：用仓库里的 **投稿** Issue 模板，或直接改 `data/pairs.json` 提 PR。

非官方讽刺作品，与 Anthropic、OpenAI 无关联。我们自己写的内容里品牌名只以纯文字出现；截图是各产品界面的局部节选，用于对比评论，其中的 logo 和界面归各自所有者所有。MIT 许可。
