# Project Zomboid 模组依赖关系图

本文档详细记录了bin^2的B42.13合集中所有模组的依赖关系，提供了模组加载顺序的参考。

## 模组总览

| 模组名称 | Workshop ID | 分类 | 前置要求 | 兼容状态 |
|---------|------------|------|---------|----------|
| [B42]CleanUI V2.3 | 3437629766 | 界面增强 | [B42]NeatUI Framework | ✅ B42.13.1兼容 |
| [B42]ModernStatus V2.0 | 3451167732 | 界面增强 | [B42]NeatUI Framework | ✅ B42.13兼容 |
| B42简体中文修复 | 3386522562 | 本地化 | 无 | ✅ B42.13兼容 |
| [B42]统一·中文汉化 | 3556544454 | 本地化 | 无 | ✅ B42.13兼容 |
| [B42]统一·模组汉化 | 3556540080 | 本地化 | [B42]统一·中文汉化 | ✅ B42.13兼容 |
| [B42]NeatUI Framework | 3508537032 | 框架 | 无 | ✅ B42.13兼容 |
| [B42]Neat Crafting V1.5 | 3502080466 | 界面增强 | [B42]NeatUI Framework | ✅ B42.13兼容 |
| [B42]Neat Building + More Buildings V1.4 | 3536052310 | 界面增强 | [B42]NeatUI Framework | ✅ B42.13兼容 |
| [B42]Project Cook (New)V1.0 | 3490188370 | 界面增强 | [B42]NeatUI Framework | ✅ B42.13兼容 |
| Neat Crafting & Neat Building - Addon XP Display | 3540503606 | 附加组件 | [B42]Neat Crafting, [B42]Neat Building | ✅ B42.13兼容 |
| Smart Radial Menu | 3494108029 | 界面增强 | 无 | ✅ B42.13兼容 |
| [B42]Clean HotBar v1.8 | 3461263912 | 界面增强 | 无 | ✅ B42.13兼容 |
| [b42]The Shortcut | 3470659758 | 界面增强 | 无 | ✅ B42.13兼容 |
| [B42.13] SimpleStatus-Fixed | 3622457795 | 界面增强 | 无 | ✅ B42.13兼容 |
| [B42.13] Detailed Descriptions for Occupations and Traits | 待补充 | 游戏信息 | 无 | ✅ B42.13兼容 |
| [B41/42] Known And Collected | 待补充 | 界面增强 | 无 | ⚠️ B42.13需要补丁 |
| Eat whole stack | 3617669428 | 界面增强 | 无 | ✅ B42.13兼容 |
| [B42] Water Pipes (aka Plumbing) | 待补充 | 系统功能 | 无 | ✅ B42.12和B42.13兼容 |
| [B42] Mod Manager | 3624320539 | 系统功能 | 无 | ✅ B42.13兼容 |
| Equipment UI - Paper Doll Equipment Interface [B42/41] | 待补充 | 界面增强 | 无 | ✅ B42/B41兼容 |
| [B42] Nested Containers | 待补充 | 界面增强 | 无 | ✅ B42.13兼容 |
| Auto Tailoring | 待补充 | 系统功能 | 无 | ✅ B42.13兼容 |
| [B42]ShelterHold : Beehive | 3596827035 | 农业生物 | 无 | ⚠️ B42.13需要补丁 |
| [B42]舌尖上的中国 | 待补充 | 农业生物 | 无 | ✅ B42.13.1兼容 |
| More Mre&Millitary foodV3 | 待补充 | 食物 | 无 | ✅ B42.13兼容 |
| Clean UI Menu Support | 待补充 | 界面增强 | [B42]CleanUI | ✅ B42.13兼容 |
| Sidebar Controller Support | 待补充 | 控制器 | 无 | ✅ B42.13兼容 |
| Neat Ingredients List | 待补充 | 界面增强 | 无 | ✅ B42.13兼容 |
| Consolidate All Fix (B42) | 3485382965 | 游戏修复 | 无 | ✅ B42.13兼容 |
| Comfy Sleeping [B41 & B42] | 待补充 | 生存环境 | 无 | ✅ B42.13兼容 |
| Here Goes the Sun [MP42.13+] | 待补充 | 生存环境 | 无 | ✅ B42.13多人兼容 |
| Better Server Settings | 待补充 | 服务器 | 无 | ✅ B42.13兼容 |
| errorMagnifier | 待补充 | 工具 | 无 | ✅ B42.13兼容 |
| Fast Forward (MP) - Build 42 | 3623959321 | 时间控制 | 无 | ✅ B42.13兼容 |
| Legendary Katana | 3418366499 | 武器 | 无 | ✅ B42.13兼容 |
| Combat Text (B40+B41+B42) | 待补充 | 游戏信息 | 无 | ✅ B42.13兼容 |
| Mini Health Panel [B41/B42.13] | 待补充 | 界面增强 | 无 | ✅ B42.13兼容 |

## 框架依赖

### NeatUI Framework
- **Workshop ID**: 3508537032
- **Mod ID**: NeatUI_Framework
- **依赖**: 无
- **被依赖的模组**:
  - [B42]CleanUI V2.3 (3437629766)
  - [B42]ModernStatus V2.0 (3451167732)
  - [B42]Neat Crafting V1.5 (3502080466)
  - [B42]Neat Building + More Buildings V1.4 (3536052310)
  - [B42]Project Cook (New)V1.0 (3490188370)
- **特点**: UI相关框架库，用于简化UI创建
- **兼容性**: B42.13.1部分问题，多人游戏需测试

### 中文本地化链
```
B42简体中文修复
[B42]统一·中文汉化
[B42]统一·模组汉化 → [B42]统一·中文汉化
```

### Neat系列模组
```
NeatUI Framework (3508537032)
├── [B42]CleanUI V2.3 (3437629766)
├── [B42]ModernStatus V2.0 (3451167732)
├── [B42]Neat Crafting V1.5 (3502080466)
├── [B42]Neat Building + More Buildings V1.4 (3536052310)
└── [B42]Project Cook (New)V1.0 (3490188370)

Neat Crafting (3502080466) + Neat Building (3536052310)
└── Neat Crafting & Neat Building - Addon XP Display (3540503606)
    ├── 包括B42.13兼容性补丁
    ├── 可选择显示模式：基础XP/最终XP/倍数/详细分解
    └── 可选显示模组来源信息
```

### CleanUI系列模组
```
[B42]CleanUI V2.3
└── Clean UI Menu Support → [B42]CleanUI V2.3
```

### Known And Collected
```
[B41/42] Known And Collected
└── Known and Collected 42.13+ compatibility patch → [B41/42] Known And Collected
```

### ShelterHold
```
[B42]ShelterHold : Beehive
└── ShelterHold : Beehive Patch for B42.13 → [B42]ShelterHold : Beehive
```

## 推荐的模组加载顺序

基于依赖关系，推荐的模组加载顺序如下：

### 第一层：框架和基础
1. NeatUI Framework (3508537032)
2. B42简体中文修复 (3386522562)
3. [B42]统一·中文汉化 (3556544454)

### 第二层：核心功能
1. [B42]CleanUI V2.3 (3437629766)
2. [B42]ModernStatus V2.0 (3451167732)
3. [B42]Neat Crafting V1.5 (3502080466)
4. [B42]Neat Building + More Buildings V1.4 (3536052310)
5. [B42]Project Cook (New)V1.0 (3490188370)
6. [B42]统一·模组汉化 (3556540080)

### 第三层：扩展和增强
1. Neat Crafting & Neat Building - Addon XP Display
2. Clean UI Menu Support
3. [B42]Mod Manager
4. [B42] Water Pipes (aka Plumbing)

### 第四层：修复和补丁
1. Neat Crafting Patch for B42.13
2. ShelterHold : Beehive Patch for B42.13
3. Known and Collected 42.13+ compatibility patch

### 第五层：其他独立模组
1. [B42]ModernStatus V2.0
2. Smart Radial Menu
3. [B42]Clean HotBar v1.8
4. [b42]The Shortcut
5. [B42.13] SimpleStatus-Fixed
6. Fast Forward (MP) - Build 42
7. Legendary Katana
8. ...（其余无依赖的模组）

## 注意事项

1. **补丁模组**：补丁类模组（如Known and Collected 42.13+ compatibility patch）必须加载在原版模组之后
2. **框架优先**：框架类模组（如NeatUI Framework）必须先加载
3. **本地化顺序**：中文汉化应尽早加载，确保其他模组中的中文显示正确
4. **多人游戏兼容性**：部分模组（如Here Goes the Sun [MP42.13+]）专为多人游戏优化
5. **Build版本兼容性**：部分模组需要特定的补丁才能在B42.13中工作

## 依赖冲突和解决方案

### Known And Collected
- **问题**：B42.13版本存在兼容性问题
- **解决方案**：同时使用原版模组和B42.13兼容性补丁
- **加载顺序**：原版模组 → B42.13补丁

### Neat Crafting & Neat Building
- **问题**：B42.13版本存在兼容性问题
- **解决方案**：使用官方B42.13补丁
- **加载顺序**：原版Neat Crafting → B42.13补丁

### ShelterHold : Beehive
- **问题**：B42.13版本存在兼容性问题
- **解决方案**：使用B42.13补丁
- **加载顺序**：原版ShelterHold → B42.13补丁

## 模组兼容性矩阵

| 模组名称 | B42.12兼容 | B42.13兼容 | B42.13.1兼容 | 多人游戏支持 | 备注 |
|---------|-----------|-----------|-------------|-------------|------|
| [B42]NeatUI Framework | ✅ | ✅ | ⚠️ 部分问题 | ⚠️ 需测试 | 框架基础 |
| [B42]CleanUI V2.3 | ✅ | ⚠️ 需补丁 | ✅ | ❌ 需测试 | 需要补丁才能在B42.13中使用 |
| [B42]ModernStatus V2.0 | ✅ | ⚠️ 部分问题 | ✅ | ✅ | 状态指示器 |
| [B42]Neat Crafting V1.5 | ✅ | ❌ 需补丁 | ⚠️ 需补丁 | ❌ 需补丁 | 制作系统重设计 |
| [B42]Neat Building + More Buildings V1.4 | ✅ | ⚠️ 部分问题 | ✅ | ❌ 需测试 | 建筑系统增强 |
| [B42]Mod Manager | ❌ | ✅ | ✅ | ✅ | 模组管理工具 |

## 特殊依赖关系

### 依赖链分析
1. **最长依赖链**:
   NeatUI Framework → CleanUI ModernStatus → (用户界面增强)
   长度：2层

2. **核心框架**:
   NeatUI Framework是整个UI增强体系的基础，6个主要模组依赖它

3. **孤立模组**:
   无依赖的独立模组：B42简体中文修复、Fast Forward、Legendary Katana等

### 冲突警告
1. **UI冲突**:
   - CleanUI与其他UI重设计模组可能冲突
   - 不能同时使用多个制作界面重设计模组

2. **功能冲突**:
   - 不同状态指示器模组可能相互干扰
   - 容器管理模组可能有重叠功能

## 性能影响评估

| 影响程度 | 模组 | 说明 |
|---------|------|------|
| 高 | NeatUI Framework, CleanUI | 完全重设计UI，可能影响性能 |
| 中 | ModernStatus, Neat Crafting | 部分UI修改，适度影响性能 |
| 低 | 多数独立模组 | 功能性增强，性能影响最小 |

## 推荐安装策略

### 新手玩家推荐
1. 只安装核心基础模组：
   - [B42]NeatUI Framework
   - [B42]CleanUI V2.3
   - [B42]ModernStatus V2.0

### 高级玩家推荐
1. 完整安装，但注意加载顺序
2. 使用Mod Manager模组来管理冲突和兼容性
3. 在游戏设置中调整每个模组的功能，避免性能影响

### 多人游戏推荐
1. 优先考虑多人游戏兼容的模组
2. 避免安装UI重设计类模组（可能不兼容多人）
3. 使用服务器端验证的模组列表

## 完整依赖关系图

```
基础框架层
├── NeatUI Framework (3508537032)
└── B42简体中文修复 (3386522562)

核心功能层 (依赖NeatUI Framework)
├── [B42]CleanUI V2.3 (3437629766)
├── [B42]ModernStatus V2.0 (3451167732)
├── [B42]Neat Crafting V1.5 (3502080466)
├── [B42]Neat Building + More Buildings V1.4 (3536052310)
└── [B42]Project Cook (New)V1.0 (3490188370)

本地化层
├── [B42]统一·中文汉化 (3556544454)
└── [B42]统一·模组汉化 (3556540080) → [B42]统一·中文汉化

扩展功能层
├── Neat Crafting & Neat Building - Addon XP Display (3540503606)
│   ├── 依赖: [B42]Neat Crafting (3502080466)
│   └── 依赖: [B42]Neat Building (3536052310)
├── Clean UI Menu Support → [B42]CleanUI V2.3
├── Known And Collected 42.13+ compatibility patch → [B41/42] Known And Collected
└── ShelterHold : Beehive Patch for B42.13 → [B42]ShelterHold : Beehive

独立模组层
├── [B42] Water Pipes (aka Plumbing)
├── [B42] Mod Manager (3624320539)
├── Equipment UI - Paper Doll Equipment Interface [B42/41]
├── [B42] Nested Containers
├── Auto Tailoring
├── Smart Radial Menu
├── [B42]Clean HotBar v1.8
├── [b42]The Shortcut
├── [B42.13] SimpleStatus-Fixed
├── Eat whole stack
├── [B42.13] Detailed Descriptions for Occupations and Traits
├── [B42]ShelterHold : Beehive
├── [B42]舌尖上的中国
├── More Mre&Millitary foodV3
├── Sidebar Controller Support
├── Neat Ingredients List
├── Consolidate All Fix (B42)
├── Comfy Sleeping [B41 & B42]
├── Here Goes the Sun [MP42.13+]
├── Better Server Settings
├── errorMagnifier
├── Fast Forward (MP) - Build 42
├── Legendary Katana
├── Combat Text (B40+B41+B42)
└── Mini Health Panel [B41/B42.13]
```

## 结论

这个依赖关系图提供了合集中39个模组的详细关系，可以作为设置模组加载顺序的参考。正确的加载顺序对于避免冲突、确保所有功能正常工作至关重要。建议按照上述推荐顺序加载模组，并根据实际使用情况调整。

特别注意事项：
1. B42.13版本中，Rocco系列的模组需要额外的补丁才能正常工作
2. Neat Crafting & Neat Building - Addon XP Display包含了内置的B42.13兼容性补丁
3. Mod Manager模组可以帮助检测和管理模组之间的冲突
4. 在多人游戏环境中，建议先进行小规模测试
5. 框架类模组必须优先加载，如NeatUI Framework
6. 补丁类模组必须加载在对应原版模组之后

---
**[← 返回项目主页](./README.md)**