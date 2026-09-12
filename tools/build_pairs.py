#!/usr/bin/env python3
"""words.md  <->  data/pairs.json

  python3 tools/build_pairs.py          # words.md -> data/pairs.json
  python3 tools/build_pairs.py export   # data/pairs.json -> words.md (one-time, or to resync)

words.md format (headings are what the parser keys on):

  ## 池：荒诞 (absurd)          shared pool; then "### 中" / "### 英" with "- entry" lines
  ## 品牌：Claude (claude)      a brand; "- 键: 值" lines for name/source/templates,
                                then "### 池名 中/英" subsections for brand-only entries
  - entry | 3                   optional weight after a pipe

The JSON gets two extra top-level fields: "schema" (bumped by hand when the shape changes)
and "version" (a hash of words.md, so consumers can tell when the list changed).
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MD = ROOT / "words.md"
JS = ROOT / "data" / "pairs.json"

POOLS = [("absurd", "荒诞"), ("hard", "硬解绑"), ("brand", "品牌对冲"), ("literal", "原味"), ("formula", "套路")]
ZH2ID = {zh: k for k, zh in POOLS}
LANGS = [("zh", "中"), ("en", "英")]
ZH2LANG = {zh: k for k, zh in LANGS}


def entry_to_md(e):
    if isinstance(e, str):
        return f"- {e}"
    w = e.get("weight", 1)
    return f"- {e['text']}" + (f" | {w}" if w != 1 else "")


def md_to_entry(line):
    body = line[2:].strip()
    if " | " in body:
        text, w = body.rsplit(" | ", 1)
        return {"text": text.strip(), "weight": int(w)}
    return body


def export(d):
    out = ["# unbind 词表", "",
           "在 Obsidian 里改这个文件，然后在项目目录跑 `python3 tools/build_pairs.py` 重建 `data/pairs.json`。",
           "规则见 CONTRIBUTING.md：中文两到四个字，英文最多四个音节；无厘头，别吓人。",
           "条目后面可以加权重：`- 补牙 | 3`，没写按 1。`{brand}` 是品牌名占位符。", ""]
    for k, zh in POOLS:
        out += [f"## 池：{zh} ({k})", ""]
        for lang, lzh in LANGS:
            out += [f"### {lzh}", ""] + [entry_to_md(e) for e in d["pools"][k].get(lang, [])] + [""]
    for b in d["brands"]:
        out += [f"## 品牌：{b['name']} ({b['id']})", "",
                f"- 出处: {b['source']['text']} — {b['source']['where']} ({b['source']['seen']})"]
        for lang, lzh in LANGS:
            if lang in b["templates"]:
                out.append(f"- 句式{lzh}: {b['templates'][lang]}")
        out.append("")
        for k, zh in POOLS:
            for lang, lzh in LANGS:
                entries = b.get("pools", {}).get(k, {}).get(lang)
                if entries:
                    out += [f"### {zh} {lzh}", ""] + [entry_to_md(e) for e in entries] + [""]
    MD.write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")


def build():
    import hashlib
    src = MD.read_text(encoding="utf-8")
    d = {"schema": 1, "version": hashlib.sha1(src.encode("utf-8")).hexdigest()[:8],
         "brands": [], "pools": {k: {"zh": [], "en": []} for k, _ in POOLS}}
    section = None   # ("pool", id) or ("brand", dict)
    target = None    # list to append entries to
    for raw in src.splitlines():
        line = raw.rstrip()
        m = re.match(r"^## 池：(\S+) \((\w+)\)", line)
        if m:
            section = ("pool", m.group(2)); target = None; continue
        m = re.match(r"^## 品牌：(.+?) \((\w+)\)", line)
        if m:
            b = {"id": m.group(2), "name": m.group(1).strip(), "source": {}, "templates": {}, "pools": {}}
            d["brands"].append(b); section = ("brand", b); target = None; continue
        m = re.match(r"^### (\S+)(?: (\S+))?$", line)
        if m and section:
            if section[0] == "pool":
                target = d["pools"][section[1]][ZH2LANG[m.group(1)]]
            else:
                k = ZH2ID[m.group(1)]; lang = ZH2LANG[m.group(2)]
                target = section[1]["pools"].setdefault(k, {}).setdefault(lang, [])
            continue
        if line.startswith("- ") and section:
            if section[0] == "brand" and target is None:
                key, _, val = line[2:].partition(": ")
                if key == "出处":
                    mm = re.match(r"(.+?) — (.+?) \((.+)\)$", val)
                    section[1]["source"] = {"text": mm.group(1), "where": mm.group(2), "seen": mm.group(3)}
                elif key.startswith("句式"):
                    section[1]["templates"][ZH2LANG[key[2:]]] = val
            elif target is not None:
                target.append(md_to_entry(line))
    for b in d["brands"]:
        if not b["pools"]:
            del b["pools"]
    JS.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    n = sum(len(v[l]) for v in d["pools"].values() for l in ("zh", "en"))
    print(f"wrote {JS.relative_to(ROOT)}: {len(d['brands'])} brand(s), {n} shared entries")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "export":
        export(json.loads(JS.read_text(encoding="utf-8")))
        print(f"wrote {MD.relative_to(ROOT)}")
    else:
        build()
