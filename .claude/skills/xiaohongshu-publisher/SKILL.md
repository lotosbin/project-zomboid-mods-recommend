---
name: xiaohongshu-publisher
description: 使用 Playwright 或浏览器自动化发布内容到小红书平台。支持登录、发布笔记、添加图片和标签。适用于需要手动登录后自动发布笔记的场景。
---

# 小红书发布 Skill

使用 Playwright 或浏览器自动化操作发布小红书笔记。

## 使用场景

当用户要求发布内容到小红书时使用此 skill。可以是：
- 发布新的小红书笔记
- 自动填写笔记内容
- 添加话题标签

## 重要提示

**小红书有严格的反自动化措施：**
1. 创作者平台 `creator.xiaohongshu.com` 需要登录才能访问
2. 直接访问发布页面可能被阻止（会显示"页面不见了"）
3. 建议通过主页的"创作中心"进入
4. 可能需要处理验证码

## 工作流程

### 1. 准备工作

获取笔记内容信息：
- **标题**：笔记标题（不超过20字）
- **正文**：笔记正文内容
- **图片**：图片文件路径或 URL 列表
- **标签**：话题标签列表

### 2. 尝试访问小红书主页

```javascript
// 先访问小红书主页，检查登录状态
await page.goto('https://www.xiaohongshu.com/explore');
await page.waitForLoadState('networkidle');
```

### 3. 通过创作中心发布

如果主页可以访问：

1. **点击"创作中心"按钮**
   ```javascript
   await page.getByRole('button', { name: '创作中心' }).click();
   ```

2. **点击"创作服务"**
   ```javascript
   await page.getByRole('link', { name: '创作服务' }).click();
   ```

3. **在创作者平台发布**
   - 如果需要登录，引导用户手动登录
   - 如果已登录，寻找发布入口

### 4. 备用方法：通过主页"发布"按钮

1. **点击底部导航的"发布"**
   ```javascript
   // 在主页找到发布链接
   await page.getByRole('link', { name: '发布' }).click();
   ```

2. **或者直接导航**
   ```javascript
   await page.goto('https://creator.xiaohongshu.com/publish/publish?source=official');
   ```

### 5. 填写笔记内容

```javascript
// 填写标题
await page.getByPlaceholder('添加标题').fill('笔记标题');

// 填写正文
await page.getByRole('textbox').first().fill('笔记正文内容...');

// 添加标签
await page.getByText('#添加话题').click();
await page.getByPlaceholder('搜索话题').fill('游戏');
await page.getByText('游戏').first().click();

// 发布
await page.getByText('发布').click();
```

### 6. 验证发布

```javascript
await page.waitForTimeout(2000);
const success = await page.getByText('发布成功').isVisible();
```

## 常用选择器

| 功能 | 选择器 |
|------|--------|
| 创作中心按钮 | `button:has-text("创作中心")` |
| 发布按钮 | `link:has-text("发布")`, `link[href*="publish"]` |
| 标题输入 | `input[placeholder*="标题"]`, `getByPlaceholder('添加标题')` |
| 正文输入 | `div[contenteditable="true"]`, `getByRole('textbox')` |
| 上传图片 | `input[type="file"]` |
| 发布按钮 | `button:has-text("发布")`, `getByText('发布')` |
| 标签输入 | `input[placeholder*="标签"]` |

## 注意事项

1. **登录状态**：小红书需要登录才能发布，确保浏览器已登录
2. **反爬虫**：小红书有反自动化措施
   - 可能显示"页面不见了"
   - 创作者平台可能需要验证码
   - 建议先通过主页操作
3. **图片上传**：本地图片需要使用绝对路径
4. **验证码**：如果遇到验证码，引导用户手动处理

## 错误处理

| 错误 | 解决方案 |
|------|----------|
| 页面不见了 | 尝试从主页点击创作中心进入 |
| 未登录 | 引导用户手动登录，或使用已登录浏览器 |
| 上传失败 | 检查图片路径是否正确 |
| 发布被拒 | 检查内容是否违规 |
| 超时 | 增加等待时间 |

## 快速开始

1. 先访问 `https://www.xiaohongshu.com/explore`
2. 检查是否已登录（查看是否有"我"按钮）
3. 点击"创作中心"或"发布"
4. 如果需要登录，告知用户手动登录
5. 登录后继续自动发布流程
