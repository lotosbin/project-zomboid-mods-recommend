---
name: douyin-publisher
description: 使用 Playwright 自动化浏览器发布内容到抖音平台。支持登录、发布文章、使用AI配图、暂存草稿。适用于需要手动登录后自动发布内容的场景。
---

# 抖音发布 Skill

使用 Playwright 或浏览器自动化操作发布抖音文章。

## 使用场景

当用户要求发布内容到抖音时使用此 skill。可以是：
- 发布新的文章
- 使用AI配图
- 暂存为草稿

## 重要提示

**抖音有反自动化措施：**
1. 创作者平台 `creator.douyin.com` 需要登录才能访问
2. 建议通过主页进入发布页面
3. 可能需要处理验证码

## 工作流程

### 1. 准备工作

获取文章内容信息：
- **标题**：文章标题
- **正文**：文章正文内容
- **配图**：使用AI配图功能

### 2. 访问抖音创作者平台

```javascript
// 访问抖音创作者平台文章发布页
await page.goto('https://creator.douyin.com/creator-micro/content/post/article?default-tab=5&enter_from=publish_page&media_type=article&type=new');
```

### 3. 通过主页发布

如果直接访问被阻止：
1. 先访问 `https://creator.douyin.com/creator-micro/home`
2. 登录后寻找发布入口
3. 选择发布文章

### 4. 填写内容

```javascript
// 填写标题
await page.getByPlaceholder('请输入标题').fill('文章标题');

// 填写正文
await page.getByRole('textbox').first().fill('文章正文内容...');

// 使用AI配图
await page.getByText('AI配图').click();
```

### 5. 暂存草稿

```javascript
// 点击暂存离开按钮
await page.getByText('暂存离开').click();
```

### 6. 验证

```javascript
// 检查是否成功暂存
const success = await page.getByText('草稿保存成功').isVisible();
```

## 常用选择器

| 功能 | 选择器 |
|------|--------|
| 标题输入 | `input[placeholder*="标题"]`, `getByPlaceholder('请输入标题')` |
| 正文输入 | `div[contenteditable="true"]`, `getByRole('textbox')` |
| AI配图按钮 | `getByText('AI配图')` |
| 暂存离开按钮 | `getByText('暂存离开')` |
| 发布按钮 | `getByText('发布')` |

## 注意事项

1. **登录状态**：抖音需要登录才能发布
2. **反爬虫**：有反自动化措施，可能需要验证码
3. **AI配图**：使用平台提供的AI配图功能
4. **暂存**：用户要求暂存而非直接发布

## 错误处理

| 错误 | 解决方案 |
|------|----------|
| 未登录 | 引导用户手动登录 |
| 页面加载失败 | 刷新页面重试 |
| AI配图失败 | 手动选择图片 |
