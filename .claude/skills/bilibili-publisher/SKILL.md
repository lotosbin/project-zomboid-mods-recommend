---
name: bilibili-publisher
description: 使用 Playwright 自动化浏览器发布内容到哔哩哔哩专栏平台。支持登录、发布文章、添加话题、保存草稿。适用于需要手动登录后自动发布专栏文章的场景。
---

# 哔哩哔哩发布 Skill

使用 Playwright 或浏览器自动化操作发布哔哩哔哩专栏文章。

## 使用场景

当用户要求发布内容到哔哩哔哩时使用此 skill。可以是：
- 发布新的专栏文章
- 填写文章内容
- 添加话题标签
- 保存为草稿

## 重要提示

**哔哩哔哩有反自动化措施：**
1. 创作者中心 `member.bilibili.com` 需要登录才能访问
2. 可能需要处理验证码
3. 建议使用已登录的浏览器

## 工作流程

### 1. 准备工作

获取文章内容信息：
- **标题**：文章标题（建议30字以内）
- **正文**：文章正文内容
- **话题**：可选的话题标签

### 2. 访问哔哩哔哩创作者中心

```javascript
// 访问专栏文章编辑页
await page.goto('https://member.bilibili.com/platform/upload/text/new-edit');
```

### 3. 填写内容

```javascript
// 填写标题
await page.getByPlaceholder('请输入标题（建议30字以内）').fill('文章标题');

// 填写正文
await page.getByPlaceholder('请输入正文').fill('文章正文内容...');

// 添加话题（可选）
await page.getByText('添加话题').click();
```

### 4. 保存草稿

```javascript
// 点击保存为草稿按钮
await page.getByText('保存为草稿').click();
```

### 5. 验证

```javascript
// 检查是否成功保存
await page.waitForTimeout(2000);
const success = await page.getByText('保存成功').isVisible();
```

## 常用选择器

| 功能 | 选择器 |
|------|--------|
| 标题输入 | `getByPlaceholder('请输入标题（建议30字以内）')` |
| 正文输入 | `getByPlaceholder('请输入正文')` |
| 添加话题 | `getByText('添加话题')` |
| 保存草稿 | `getByText('保存为草稿')` |
| 发布按钮 | `getByText('发布')` |

## 注意事项

1. **登录状态**：哔哩哔哩需要登录才能发布，确保浏览器已登录
2. **反爬虫**：有反自动化措施，操作时注意：
   - 适当添加随机延迟
   - 使用 human-like 的操作节奏
3. **草稿保存**：用户要求保存草稿而非直接发布
4. **封面设置**：可选择自定义封面或自动抓取正文开头文字

## 错误处理

| 错误 | 解决方案 |
|------|----------|
| 未登录 | 手动登录后继续，或使用已登录的浏览器配置 |
| 保存失败 | 检查内容是否填写完整，重新保存 |
| 发布被拒 | 检查内容是否违规，修改后重试 |
| 超时 | 增加等待时间或检查网络连接 |
