#!/usr/bin/env python3
"""pwntools 通用模板：本地调试 / 远程攻击一键切换"""
from pwn import *

# ---------- 基本配置 ----------
context.update(arch="amd64", os="linux", log_level="info")
context.terminal = ["wt", "-w", "0", "split-pane", "wsl", "-e"]  # 按本地环境调整

BINARY = "./pwn"          # 目标二进制
HOST, PORT = "host", 1337  # 远程地址
LIBC = ""                  # 需要时指定 libc，如 "./libc.so.6"

elf = context.binary = ELF(BINARY, checksec=False)
libc = ELF(LIBC, checksec=False) if LIBC else None


def start():
    if args.REMOTE:
        return remote(HOST, PORT)
    if args.GDB:
        return gdb.debug(BINARY, gdbscript="b main\nc")
    return process(BINARY)


def main():
    io = start()

    # ---------- exploit 逻辑 ----------
    # io.sendlineafter(b"> ", payload)

    io.interactive()


if __name__ == "__main__":
    main()
