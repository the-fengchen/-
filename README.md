# 微信朋友圈自动点赞（macOS）

这个仓库提供一个基于 **PyAutoGUI + 图像识别** 的脚本，用于在 macOS 上辅助给微信朋友圈点赞。

## 1. 安装依赖

```bash
python3 -m pip install pyautogui pillow opencv-python
```

## 2. 准备模板图

1. 打开微信电脑版，进入朋友圈。
2. 对“未点赞”按钮截一张清晰小图，保存为 `like_icon.png`。
3. 建议在与你运行脚本相同的显示缩放下截图。

## 3. 运行脚本

```bash
python3 wechat_moments_auto_like_mac.py --template like_icon.png
```

常用参数：

- `--confidence 0.85`：图像匹配置信度（越高越严格）
- `--interval 0.8`：每轮扫描间隔（秒）
- `--max-likes 20`：最多点赞数量
- `--dry-run`：演练模式，不会实际点击

示例（先演练）：

```bash
python3 wechat_moments_auto_like_mac.py --template like_icon.png --dry-run --max-likes 5
```

## 4. 安全与注意事项

- 将鼠标快速移到左上角可触发 PyAutoGUI failsafe 立即停止。
- 请勿高频、长时间自动操作，避免账号异常风险。
- UI 自动化对分辨率和界面变化敏感，匹配不到可尝试重截模板图。
