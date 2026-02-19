#!/usr/bin/env python3
"""
模组兼容性检查脚本
检查所有已知模组与Project Zomboid B42.14.1的兼容性
"""

import re
import json
from datetime import datetime
import time

# 配置
TARGET_VERSION = "B42.14.1"
OUTPUT_FILE = "compatibility_report.md"

# 从文档中提取的模组列表
MODS = [
    {"name": "bin^2的B42.13合集", "id": "3624259825", "category": "合集"},
    {"name": "Legendary Naginata", "id": "3580577925", "category": "武器"},
    {"name": "Legendary Tactical Knife", "id": "3575320927", "category": "武器"},
    {"name": "Legendary Katana", "id": "3418366499", "category": "武器"},
    {"name": "Legendary Satchel", "id": "3560352772", "category": "背包/容器"},
    {"name": "Legendary DuffelBag", "id": "3558839307", "category": "背包/容器"},
    {"name": "Legendary Fanny Pack", "id": "3552050880", "category": "背包/容器"},
    {"name": "Legendary Backpacks", "id": "3538353228", "category": "背包/容器"},
    {"name": "Legendary Cap", "id": "3549294472", "category": "服装/配饰"},
    {"name": "Read While Walking", "id": "2845952197", "category": "实用工具"},
    {"name": "Simple Read While Walking 42.13+ compatibility patch", "id": "3625232801", "category": "补丁"},
    {"name": "[B42.13] Fruits in jars", "id": "3432006285", "category": "食物/储藏"},
    {"name": "Fast Forward (MP) - Build 42", "id": "3623959321", "category": "时间管理"},
    {"name": "[B42]CleanUI V2.3", "id": "3437629766", "category": "界面优化"},
    {"name": "Smart Radial Menu", "id": "3494108029", "category": "交互优化"},
    {"name": "[B42]Clean HotBar v1.8", "id": "3461263912", "category": "快捷栏优化"},
    {"name": "[B42]Neat Crafting V1.5", "id": "3502080466", "category": "制作界面"},
    {"name": "[B42]Neat Building + More Buildings V1.4", "id": "3536052310", "category": "建造界面"},
    {"name": "[B42]Project Cook (New)V1.0", "id": "3490188370", "category": "烹饪界面"},
    {"name": "[B42]ModernStatus V2.0", "id": "3451167732", "category": "状态指示器"},
    {"name": "Neat Crafting & Neat Building - Addon XP Display", "id": "3540503606", "category": "经验值显示"},
    {"name": "[b42]The Shortcut", "id": "3470659758", "category": "快捷工具栏"},
    {"name": "Eat whole stack", "id": "3617669428", "category": "食物交互"},
    {"name": "[B42]ShelterHold : Beehive", "id": "3596827035", "category": "蜜蜂养殖"},
    {"name": "ShelterHold : Beehive Patch for B42.13", "id": "3625028417", "category": "补丁"},
    {"name": "[B42]舌尖上的中国", "id": "3508537032", "category": "食物/农业"},
    {"name": "More Mre&Millitary foodV3", "id": "2872282653", "category": "食物"},
    {"name": "B42简体中文修复", "id": "3386522562", "category": "中文本地化"},
    {"name": "[B42]统一·中文汉化", "id": "3556544454", "category": "中文本地化"},
    {"name": "[B42]统一·模组汉化", "id": "3556540080", "category": "模组本地化"},
    {"name": "True Music Radio B42 MP+", "id": "2948224756", "category": "音乐电台"},
    {"name": "True Music CN", "id": "2957823594", "category": "中文音乐"},
    {"name": "True Music Jukebox B42", "id": "2948225412", "category": "音乐点唱机"},
    {"name": "[B42]MisterB's Radio Overhaul", "id": "3636999001", "category": "音频增强"},
    {"name": "[B42]Custom Radio Stations", "id": "3636999002", "category": "音频增强"},
    {"name": "Evolving Traits World (ETW) [B41/B42]", "id": "2636997653", "category": "角色系统"},
    {"name": "[B42.13] [SP/MP] Getting Old", "id": "3643959369", "category": "角色系统"},
    {"name": "[B42] VSGirlBody v3.1 (42.131)", "id": "待补充", "category": "角色体型"},
    {"name": "[B41/42] Known And Collected", "id": "待补充", "category": "收藏管理"},
    {"name": "Comfy Sleeping [B41 & B42]", "id": "2286124931", "category": "睡眠系统"},
    {"name": "Here Goes the Sun [MP42.13+]", "id": "待补充", "category": "环境效果"},
    {"name": "[B41->B42.13] [SP/MP] Days Until Winter", "id": "待补充", "category": "环境系统"},
    {"name": "[B42] Water Pipes (aka Plumbing)", "id": "3317416792", "category": "基础设施"},
    {"name": "[B42] Mod Manager", "id": "待补充", "category": "模组管理"},
    {"name": "Auto Tailoring", "id": "待补充", "category": "自动裁缝"},
    {"name": "[b42.13.1]Multiplayer Crafting Fixes", "id": "待补充", "category": "多人修复"},
    {"name": "DryingRacksFixed B42 MP", "id": "待补充", "category": "多人修复"},
    {"name": "[b42.13.1] Multiplayer Timed Actions Fix [Beta]", "id": "待补充", "category": "多人修复"},
    {"name": "[B42 MP] Teach Knowledge", "id": "待补充", "category": "多人修复"},
    {"name": "CookingSync - Multiplayer Cooking Fix [v5.0]", "id": "3773820803", "category": "多人修复"},
    {"name": "Rip All Clothes", "id": "待补充", "category": "衣物系统"},
    {"name": "[B42.13]Realistic Disease Mod", "id": "3804257569", "category": "疾病系统"},
    {"name": "Replace Bandage [B41, B42]", "id": "待补充", "category": "医疗系统"},
    {"name": "Equipment UI - Paper Doll Equipment Interface [B42/41]", "id": "待补充", "category": "界面增强"},
    {"name": "[B42] Nested Containers", "id": "待补充", "category": "界面增强"},
    {"name": "Better Server Settings", "id": "待补充", "category": "界面增强"},
    {"name": "Simple Context Menu Icons", "id": "待补充", "category": "界面增强"},
    {"name": "Context Menu Icons", "id": "待补充", "category": "界面增强"},
    {"name": "Consolidate All Fix (B42)", "id": "待补充", "category": "实用工具"},
    {"name": "Neat Crafting & Neat Building - Addon XP Display", "id": "3540503606", "category": "实用工具"},
    {"name": "[OBSOLETE] CleanUI Patch for B42.13", "id": "3623352001", "category": "已过时"},
    {"name": "[42.13.1] Barrel Fluids Container", "id": "待补充", "category": "容器系统"},
    {"name": "Upgradeable Storage", "id": "待补充", "category": "容器系统"},
    {"name": "Realistic Dashboard & Gauges [MP] [Beta]", "id": "待补充", "category": "车辆系统"},
    {"name": "Ladders!?", "id": "待补充", "category": "建筑工具"},
    {"name": "PRY DOOR ADVANCED v1.4 [B42]", "id": "待补充", "category": "建筑工具"},
    {"name": "Expanded Attachments (Build 42)", "id": "待补充", "category": "附件系统"},
    {"name": "[B42.13] Wallet Fix", "id": "待补充", "category": "附件系统"},
    {"name": "[B42.13] Key Ring Plus", "id": "待补充", "category": "附件系统"},
    {"name": "[B42.13] Hidden Carry", "id": "待补充", "category": "附件系统"},
    {"name": "Karas Animal Foraging For B42.13", "id": "待补充", "category": "动物系统"},
    {"name": "Karas Fully Automatic Fishing B42.13 (SP/MP)", "id": "待补充", "category": "动物系统"},
    {"name": "Moodle Framework", "id": "待补充", "category": "开发框架"},
    {"name": "errorMagnifier", "id": "待补充", "category": "调试工具"},
    {"name": "Legendary Katana", "id": "3418366499", "category": "武器"},
]

# 兼容性状态规则
def check_compatibility(mod_name, mod_description="", known_issues=None):
    """
    检查模组与B42.14.1的兼容性
    返回: (状态, 备注)
    """
    status = "待检查"
    notes = ""

    # 基于名称的简单检查
    if "B42" in mod_name and "14.1" in mod_name:
        status = "✅ 兼容"
        notes = "明确标识支持B42.14.1"
    elif "B42.13" in mod_name or "B42.13.1" in mod_name:
        status = "⚠️ 需要验证"
        notes = "仅确认与B42.13/42.13.1兼容，B42.14.1兼容性需进一步验证"
    elif "[B41" in mod_name or "B41" in mod_name:
        status = "⚠️ 需要验证"
        notes = "支持B41和B42，但B42.14.1兼容性需进一步验证"
    elif "[B42]" in mod_name and "13" not in mod_name:
        status = "⚠️ 需要验证"
        notes = "支持B42，但B42.14.1兼容性需进一步验证"
    elif "补丁" in mod_name or "patch" in mod_name.lower():
        status = "⚠️ 需要验证"
        notes = "补丁类模组，需确认是否与B42.14.1兼容"
    elif "过时" in mod_name or "OBSOLETE" in mod_name:
        status = "❌ 不推荐"
        notes = "已标记为过时，不应使用"

    # 基于已知问题的检查
    if known_issues:
        for issue in known_issues:
            if "B42.13" in issue and "补丁" in issue:
                status = "⚠️ 需要补丁"
                notes = f"需要补丁: {issue}"
            elif "损坏" in issue:
                status = "❌ 已损坏"
                notes = f"已知问题: {issue}"

    return status, notes

def generate_report():
    """生成兼容性检查报告"""
    report = f"""# Project Zomboid B42.14.1 模组兼容性报告

**生成时间**: {datetime.now().strftime("%Y年%m月%d日 %H:%M:%S")}
**目标版本**: {TARGET_VERSION}
**检查模组数量**: {len(MODS)}

## 概览

| 状态 | 数量 |
|------|------|
| ✅ 确认兼容 | 0 |
| ⚠️ 需要验证 | 0 |
| ⚠️ 需要补丁 | 0 |
| ❌ 已损坏/不推荐 | 0 |
| ❓ 待检查 | {len(MODS)} |

## 详细检查结果

| 模组名称 | Workshop ID | 类别 | 状态 | 备注 |
|---------|------------|------|------|------|
"""

    compatible_count = 0
    needs_verification_count = 0
    needs_patch_count = 0
    broken_count = 0
    unchecked_count = 0

    for mod in MODS:
        status, notes = check_compatibility(mod["name"])

        # 更新计数
        if "兼容" in status:
            compatible_count += 1
        elif "需要验证" in status:
            needs_verification_count += 1
        elif "需要补丁" in status:
            needs_patch_count += 1
        elif "损坏" in status or "不推荐" in status:
            broken_count += 1
        elif "待检查" in status:
            unchecked_count += 1

        # 添加到报告
        report += f"| {mod['name']} | {mod['id']} | {mod['category']} | {status} | {notes} |\n"

    # 更新概览部分
    report = report.replace("| ✅ 确认兼容 | 0 |", f"| ✅ 确认兼容 | {compatible_count} |")
    report = report.replace("| ⚠️ 需要验证 | 0 |", f"| ⚠️ 需要验证 | {needs_verification_count} |")
    report = report.replace("| ⚠️ 需要补丁 | 0 |", f"| ⚠️ 需要补丁 | {needs_patch_count} |")
    report = report.replace("| ❌ 已损坏/不推荐 | 0 |", f"| ❌ 已损坏/不推荐 | {broken_count} |")
    report = report.replace("| ❓ 待检查 | {len(MODS)} |", f"| ❓ 待检查 | {unchecked_count} |")

    # 添加总结和建议
    report += f"""
## 总结与建议

### 需要特别关注的模组
以下模组可能需要特别关注或寻找替代方案：

1. **已损坏/不推荐的模组**:
   - [OBSOLETE] CleanUI Patch for B42.13 - 已标记为过时，会导致崩溃

2. **需要补丁的模组**:
   - Read While Walking - 需要B42.13兼容性补丁
   - [B42]ShelterHold : Beehive - 需要B42.13兼容性补丁

3. **B42.13明确依赖的模组**:
   - 多个标记为B42.13或B42.13.1兼容的模组需要进一步验证

### 建议行动
1. 优先测试标记为"需要验证"的模组
2. 寻找已损坏模组的替代方案
3. 检查是否有针对B42.14.1的新补丁发布
4. 对于关键模组，考虑联系模组作者确认兼容性

### 手动验证优先级
1. **高优先级** - 核心游戏机制模组
2. **中优先级** - 界面和体验增强模组
3. **低优先级** - 装饰性和可选模组

---
*此报告基于文档中的已知信息生成，实际情况请在游戏环境中测试验证*
"""

    return report

if __name__ == "__main__":
    # 生成报告
    report = generate_report()

    # 保存报告
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"兼容性报告已生成: {OUTPUT_FILE}")
