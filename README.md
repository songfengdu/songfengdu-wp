# 松风渡のwp

个人 CTF 题解与解题脚本仓库。

## 目录结构

```
contests/
└── <年份>-<比赛名>/
    ├── <分类>-<题目名>/
    │   ├── attachments/   # 题目附件
    │   ├── solver.py      # 解题脚本
    │   └── README.md      # 单题 writeup
    └── WRITEUP.md         # 整场复盘
templates/                 # 常用脚本模板（pwntools 等）
```

## 分类约定

`web` / `pwn` / `reverse` / `crypto` / `misc` / `forensic`

## 使用方式

1. 比赛结束后把题目附件和解题脚本按上面的结构归档
2. 每道题一个 README，记录思路、关键步骤、flag
3. 每场一个 WRITEUP.md 做整体复盘
