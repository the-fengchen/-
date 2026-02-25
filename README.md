# 微信朋友圈自动点赞（macOS）

已按朋友圈真实交互流程实现：**先点击右侧“···”按钮，再点击弹层里的 Like**，每处理一条后会自动滚动到下一条。

## 1. 安装依赖

```bash
python3 -m pip install pyautogui pillow opencv-python
```

## 2. 准备两张模板图

你需要截两张图：

1. `menu_icon.png`：朋友圈每条动态右下角的“···”按钮。
2. `like_button.png`：点击“···”后弹层里的 `Like` 按钮。

建议：
- 在你实际运行脚本的同一台机器、同一分辨率和缩放下截图。
- 图片尽量紧凑（只截按钮区域），不要带太多背景。

## 3. 运行脚本

```bash
python3 wechat_moments_auto_like_mac.py \
  --menu-template menu_icon.png \
  --like-template like_button.png
```

常用参数：

- `--confidence 0.87`：模板匹配置信度（越高越严格）
- `--interval 0.9`：每轮扫描间隔（秒）
- `--popup-wait 0.25`：点击“···”后等待弹层出现时间（秒）
- `--max-likes 20`：最多点赞数量
- `--dry-run`：演练模式，不会实际点击

演练模式示例：

```bash
python3 wechat_moments_auto_like_mac.py \
  --menu-template menu_icon.png \
  --like-template like_button.png \
  --dry-run --max-likes 5
```

## 4. 注意事项

- 将鼠标快速移到左上角可触发 PyAutoGUI failsafe 立即停止。
- UI 自动化对主题、分辨率、缩放非常敏感，识别不准请重截模板图。
- 请合理控制频率，避免账号异常风险。
