"""在 macOS 上辅助自动给微信朋友圈点赞（基于屏幕识别）。

使用方式：
1. pip install pyautogui pillow opencv-python
2. 截图一个“未点赞”的朋友圈点赞按钮，保存为 like_icon.png
3. 打开微信并进入朋友圈，确保点赞按钮在屏幕中可见
4. 运行：python wechat_moments_auto_like_mac.py --template like_icon.png
5. 将鼠标移动到屏幕左上角可紧急终止（PyAutoGUI failsafe）

注意：
- 该脚本是桌面 UI 自动化，依赖屏幕分辨率、缩放和微信 UI 主题。
- 请合理使用，避免高频操作导致账号风险。
"""

from __future__ import annotations

import argparse
import time
from dataclasses import dataclass
from typing import Optional

import pyautogui


@dataclass
class Config:
    template: str
    confidence: float
    interval: float
    max_likes: Optional[int]
    dry_run: bool


def find_and_like(template: str, confidence: float, dry_run: bool) -> bool:
    """查找一个点赞按钮并执行点击。返回是否成功点击。"""
    match = pyautogui.locateCenterOnScreen(template, confidence=confidence)
    if not match:
        return False

    x, y = match
    pyautogui.moveTo(x, y, duration=0.15)
    if not dry_run:
        pyautogui.click(x, y)
    return True


def run(config: Config) -> None:
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = 0.12

    print("3 秒后开始，请切换到微信朋友圈窗口...")
    time.sleep(3)

    total = 0
    while True:
        liked = find_and_like(config.template, config.confidence, config.dry_run)
        if liked:
            total += 1
            action = "模拟点赞" if config.dry_run else "已点赞"
            print(f"{action}第 {total} 条")
            # 点赞后向下滚动，继续寻找下一个
            pyautogui.scroll(-450)
        else:
            # 没找到时也略微滚动，继续扫描
            pyautogui.scroll(-250)

        if config.max_likes is not None and total >= config.max_likes:
            print(f"达到上限 {config.max_likes}，结束。")
            break

        time.sleep(config.interval)


def parse_args() -> Config:
    parser = argparse.ArgumentParser(description="微信朋友圈自动点赞（macOS）")
    parser.add_argument("--template", required=True, help="未点赞按钮模板图路径")
    parser.add_argument("--confidence", type=float, default=0.85, help="模板匹配置信度，默认 0.85")
    parser.add_argument("--interval", type=float, default=0.8, help="每轮扫描间隔秒数，默认 0.8")
    parser.add_argument("--max-likes", type=int, default=20, help="最多点赞数量，默认 20")
    parser.add_argument("--dry-run", action="store_true", help="只移动和打印，不实际点击")
    args = parser.parse_args()

    if not 0.1 <= args.confidence <= 1.0:
        raise SystemExit("--confidence 必须在 0.1 到 1.0 之间")
    if args.interval <= 0:
        raise SystemExit("--interval 必须大于 0")
    if args.max_likes is not None and args.max_likes <= 0:
        raise SystemExit("--max-likes 必须大于 0")

    return Config(
        template=args.template,
        confidence=args.confidence,
        interval=args.interval,
        max_likes=args.max_likes,
        dry_run=args.dry_run,
    )


if __name__ == "__main__":
    run(parse_args())
