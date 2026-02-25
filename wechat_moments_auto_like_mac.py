"""在 macOS 上辅助自动给微信朋友圈点赞（基于屏幕识别）。

流程：先点朋友圈每条动态右侧“···”按钮，再点弹出的 Like。
"""

from __future__ import annotations

import argparse
import time
from dataclasses import dataclass
from typing import Optional

import pyautogui


@dataclass
class Config:
    menu_template: str
    like_template: str
    confidence: float
    interval: float
    max_likes: Optional[int]
    dry_run: bool
    popup_wait: float


def locate_center(template: str, confidence: float) -> Optional[tuple[int, int]]:
    """返回模板匹配到的中心坐标。"""
    match = pyautogui.locateCenterOnScreen(template, confidence=confidence)
    if not match:
        return None
    return int(match.x), int(match.y)


def click_point(x: int, y: int, dry_run: bool) -> None:
    pyautogui.moveTo(x, y, duration=0.12)
    if not dry_run:
        pyautogui.click(x, y)


def like_one_moment(config: Config) -> bool:
    """点赞一条朋友圈：先点“···”，再点 Like。"""
    menu_point = locate_center(config.menu_template, config.confidence)
    if not menu_point:
        return False

    click_point(menu_point[0], menu_point[1], config.dry_run)
    time.sleep(config.popup_wait)

    like_point = locate_center(config.like_template, config.confidence)
    if not like_point:
        return False

    click_point(like_point[0], like_point[1], config.dry_run)
    return True


def run(config: Config) -> None:
    pyautogui.FAILSAFE = True
    pyautogui.PAUSE = 0.10

    print("3 秒后开始，请切换到微信朋友圈窗口...")
    time.sleep(3)

    total = 0
    rounds_without_like = 0

    while True:
        liked = like_one_moment(config)
        if liked:
            total += 1
            rounds_without_like = 0
            msg = "模拟点赞" if config.dry_run else "已点赞"
            print(f"{msg}第 {total} 条")
            # 每成功处理一条后自动下滚，进入下一条
            pyautogui.scroll(-520)
        else:
            rounds_without_like += 1
            # 没成功也下滚，继续找下一条
            pyautogui.scroll(-320)
            if rounds_without_like % 8 == 0:
                print("连续多轮未找到可点赞项，继续滚动扫描...")

        if config.max_likes is not None and total >= config.max_likes:
            print(f"达到上限 {config.max_likes}，结束。")
            break

        time.sleep(config.interval)


def parse_args() -> Config:
    parser = argparse.ArgumentParser(description="微信朋友圈自动点赞（macOS，先点···再点Like）")
    parser.add_argument("--menu-template", required=True, help="右侧‘···’按钮模板图路径")
    parser.add_argument("--like-template", required=True, help="弹层中 Like 按钮模板图路径")
    parser.add_argument("--confidence", type=float, default=0.87, help="模板匹配置信度，默认 0.87")
    parser.add_argument("--interval", type=float, default=0.9, help="每轮扫描间隔秒数，默认 0.9")
    parser.add_argument("--popup-wait", type=float, default=0.25, help="点击‘···’后等待弹层秒数")
    parser.add_argument("--max-likes", type=int, default=20, help="最多点赞数量，默认 20")
    parser.add_argument("--dry-run", action="store_true", help="只移动和打印，不实际点击")
    args = parser.parse_args()

    if not 0.1 <= args.confidence <= 1.0:
        raise SystemExit("--confidence 必须在 0.1 到 1.0 之间")
    if args.interval <= 0:
        raise SystemExit("--interval 必须大于 0")
    if args.popup_wait < 0:
        raise SystemExit("--popup-wait 不能小于 0")
    if args.max_likes is not None and args.max_likes <= 0:
        raise SystemExit("--max-likes 必须大于 0")

    return Config(
        menu_template=args.menu_template,
        like_template=args.like_template,
        confidence=args.confidence,
        interval=args.interval,
        max_likes=args.max_likes,
        dry_run=args.dry_run,
        popup_wait=args.popup_wait,
    )


if __name__ == "__main__":
    run(parse_args())
