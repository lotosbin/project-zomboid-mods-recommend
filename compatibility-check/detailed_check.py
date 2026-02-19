#!/usr/bin/env python3
"""
更精确的模组兼容性检查脚本
基于现有文档中的已知信息分析每个模组与Project Zomboid B42.14.1的兼容性
"""

from datetime import datetime
from collections import defaultdict

# 已知的需要补丁的模组
NEEDS_PATCH = {
    "2845952197": {
        "name": "Read While Walking",
        "patch_id": "3625232801",
        "patch_name": "Simple Read While Walking 42.13+ compatibility patch",
        "note": "原版在B42.13中有问题，需要补丁"
    },
    "3596827035": {
        "name": "[B42]ShelterHold : Beehive",
        "patch_id": "3625028417",
        "patch_name": "ShelterHold : Beehive Patch for B42.13",
        "note": "需要B42.13兼容性补丁"
    },
    "待提供": {
        "name": "[B41/42] Known And Collected",
        "patch_id": "未知",
        "patch_name": "Known and Collected 42.13+ compatibility patch",
        "note": "需要B42.13兼容性补丁"
    }
}

# 已知的损坏或过时的模组
BROKEN_OBSOLETE = {
    "3502080466": {
        "name": "[B42]Neat Crafting V1.5",
        "status": "已损坏",
        "replacement": "3540503606 - Neat Crafting & Neat Building – XP & Mod Display + B42.13 Fixes",
        "note": "原版已停止更新，需要使用社区制作的修复版本"
    },
    "3536052310": {
        "name": "[B42]Neat Building + More Buildings V1.4",
        "status": "已损坏",
        "replacement": "3540503606 - Neat Crafting & Neat Building – XP & Mod Display + B42.13 Fixes",
        "note": "原版已停止更新，需要使用社区制作的修复版本"
    },
    "3623352001": {
        "name": "[OBSOLETE] CleanUI Patch for B42.13",
        "status": "已过时",
        "note": "已标记为过时，会导致崩溃，不应使用"
    }
}

# 已确认B42.13.1兼容的模组
CONFIRMED_B42_13_1 = {
    "3437629766": {"name": "[B42]CleanUI V2.3", "note": "2025年12月22日更新"},
    "3494108029": {"name": "Smart Radial Menu"},
    "3461263912": {"name": "[B42]Clean HotBar v1.8"},
    "3490188370": {"name": "[B42]Project Cook (New)V1.0"},
    "3451167732": {"name": "[B42]ModernStatus V2.0"},
    "3540503606": {"name": "Neat Crafting & Neat Building - Addon XP Display", "note": "包含B42.13修复补丁"},
    "3470659758": {"name": "[b42]The Shortcut"},
    "3617669428": {"name": "Eat whole stack"},
    "3508537032": {"name": "[B42]舌尖上的中国"},
    "2872282653": {"name": "More Mre&Millitary foodV3"},
    "3386522562": {"name": "B42简体中文修复"},
    "3556544454": {"name": "[B42]统一·中文汉化"},
    "3556540080": {"name": "[B42]统一·模组汉化"},
    "2948224756": {"name": "True Music Radio B42 MP+", "note": "兼容B42多人游戏"},
    "2957823594": {"name": "True Music CN", "note": "兼容B42"},
    "3643959369": {"name": "[B42.13] [SP/MP] Getting Old", "note": "兼容B42.13单人和多人"},
    "3773820803": {"name": "CookingSync - Multiplayer Cooking Fix [v5.0]", "note": "v5.0（最新稳定版）"},
    "3317416792": {"name": "[B42] Water Pipes (aka Plumbing)", "note": "支持Build 42.12和Build 42.13"},
    "3804257569": {"name": "[B42.13]Realistic Disease Mod"}
}

# 传说系列模组（已确认更新至B42.13.1）
LEGENDARY_SERIES = {
    "3580577925": {"name": "Legendary Naginata", "note": "v.1.0.4, 2025年12月15日"},
    "3575320927": {"name": "Legendary Tactical Knife"},
    "3418366499": {"name": "Legendary Katana"},
    "3560352772": {"name": "Legendary Satchel"},
    "3558839307": {"name": "Legendary DuffelBag"},
    "3552050880": {"name": "Legendary Fanny Pack", "note": "装备后可能不显示在背包栏"},
    "3538353228": {"name": "Legendary Backpacks"},
    "3549294472": {"name": "Legendary Cap", "note": "v.2.0.4, 已添加可安装手电筒功能"}
}

# 其他已知模组
OTHER_KNOWN_MODS = {
    "3624259825": {"name": "bin^2的B42.13合集", "note": "核心参考合集"},
    "3623959321": {"name": "Fast Forward (MP) - Build 42", "note": "兼容B42.13.1"},
    "3432006285": {"name": "[B42.13] Fruits in jars", "note": "兼容B42.13.1"},
    "2636997653": {"name": "Evolving Traits World (ETW) [B41/B42]", "note": "兼容B41/B42"},
    "2286124931": {"name": "Comfy Sleeping [B41 & B42]", "note": "兼容B42.13"}
}

# 合并所有已知模组信息
ALL_KNOWN_MODS = {
    **CONFIRMED_B42_13_1,
    **LEGENDARY_SERIES,
    **OTHER_KNOWN_MODS
}

def analyze_compatibility(mod_id, mod_name=None, category=None):
    """
    分析模组与Project Zomboid B42.14.1的兼容性
    返回: (状态, 详细说明, 建议)
    """
    # 检查是否是损坏/过时的模组
    if mod_id in BROKEN_OBSOLETE:
        info = BROKEN_OBSOLETE[mod_id]
        status = "❌ 已损坏/过时"
        details = info["note"]
        if "replacement" in info:
            details += f"\n替代方案: {info['replacement']}"
        recommendation = "寻找替代方案或更新版本"
        return status, details, recommendation

    # 检查是否需要补丁
    if mod_id in NEEDS_PATCH:
        info = NEEDS_PATCH[mod_id]
        status = "⚠️ 需要补丁"
        details = info["note"]
        if info["patch_id"] != "未知":
            details += f"\n补丁ID: {info['patch_id']} - {info['patch_name']}"
        recommendation = "安装对应补丁后使用"
        return status, details, recommendation

    # 检查已知模组
    if mod_id in ALL_KNOWN_MODS:
        info = ALL_KNOWN_MODS[mod_id]
        status = "⚠️ 需要验证"
        details = f"已确认与B42.13/42.13.1兼容"
        if "note" in info:
            details += f"\n备注: {info['note']}"

        # 基于名称的额外分析
        if "B42.13" in mod_name or "B42.13.1" in mod_name:
            details += "\n模组名称明确标识B42.13，需要验证B42.14.1兼容性"
        elif "[B42]" in mod_name and "13" not in mod_name:
            details += "\n模组名称标识B42，可能需要更新以支持B42.14.1"

        recommendation = "在B42.14.1环境中测试验证"
        return status, details, recommendation

    # 未知模组
    status = "❓ 信息不足"
    details = "缺乏足够的兼容性信息"
    recommendation = "需要手动检查Steam Workshop页面或测试验证"
    return status, details, recommendation

def generate_detailed_report():
    """生成详细的兼容性检查报告"""
    report = f"""# Project Zomboid B42.14.1 详细兼容性报告

**生成时间**: {datetime.now().strftime("%Y年%m月%d日 %H:%M:%S")}
**目标版本**: B42.14.1
**检查模组数量**: 75+ (基于bin^2的B42.13合集)

## 兼容性分析摘要

| 状态 | 数量 | 模组示例 |
|------|------|---------|
| ✅ 可能在B42.14.1中工作 | {len(CONFIRMED_B42_13_1) + len(LEGENDARY_SERIES)} | [B42]CleanUI V2.3, Legendary Naginata |
| ⚠️ 需要验证 | {len(ALL_KNOWN_MODS) - len(LEGENDARY_SERIES)} | [B42]ModernStatus V2.0, True Music Radio |
| ⚠️ 需要补丁 | {len(NEEDS_PATCH)} | Read While Walking, [B42]ShelterHold : Beehive |
| ❌ 已损坏/过时 | {len(BROKEN_OBSOLETE)} | [B42]Neat Crafting V1.5, [OBSOLETE] CleanUI Patch |
| ❓ 信息不足 | 多个 | Workshop ID未提供或信息不完整的模组 |

## 需要特别关注的模组

### 1. 已损坏/过时的模组（不应使用）
"""

    # 添加损坏/过时的模组
    for mod_id, info in BROKEN_OBSOLETE.items():
        report += f"\n- **{info['name']}** (ID: {mod_id})\n"
        report += f"  - 状态: {info['status']}\n"
        report += f"  - 说明: {info['note']}\n"
        if "replacement" in info:
            report += f"  - 替代方案: {info['replacement']}\n"

    report += "\n### 2. 需要补丁的模组\n"

    # 添加需要补丁的模组
    for mod_id, info in NEEDS_PATCH.items():
        report += f"\n- **{info['name']}** (ID: {mod_id})\n"
        report += f"  - 说明: {info['note']}\n"
        if info["patch_id"] != "未知":
            report += f"  - 补丁: {info['patch_name']} (ID: {info['patch_id']})\n"

    report += "\n### 3. 传说系列模组（已更新至B42.13.1）\n"

    # 添加传说系列模组
    for mod_id, info in LEGENDARY_SERIES.items():
        report += f"\n- **{info['name']}** (ID: {mod_id})\n"
        report += f"  - 状态: 已更新至B42.13.1\n"
        if "note" in info:
            report += f"  - 备注: {info['note']}\n"

    report += "\n### 4. 已确认B42.13.1兼容的其他模组\n"

    # 添加其他已知模组
    for mod_id, info in ALL_KNOWN_MODS.items():
        if mod_id not in LEGENDARY_SERIES:
            report += f"\n- **{info['name']}** (ID: {mod_id})\n"
            report += f"  - 状态: 已确认B42.13.1兼容\n"
            if "note" in info:
                report += f"  - 备注: {info['note']}\n"

    # 添加B42.14.1兼容性预测
    report += f"""
## B42.14.1兼容性预测

### 高可能兼容的模组
以下模组有很高概率在B42.14.1中正常工作，因为它们：
1. 最近有更新（2025年12月）
2. 作者活跃，持续维护
3. 不涉及核心游戏机制的重大更改
4. 已在B42.13.1中稳定运行

- **[B42]CleanUI V2.3** - 2025年12月22日更新
- **传说系列模组** - 作者Akyrohunter持续更新
- **本地化模组** - 通常不受版本更新影响
- **多人游戏修复模组** - 专注于特定问题修复

### 需要验证的模组
以下模组需要优先测试：
1. 涉及新B42.14.1功能的模组
2. 修改核心游戏机制的模组
3. 有复杂交互系统的模组

### 建议的测试流程
1. **基础测试** (单玩家)
   - 游戏启动和加载
   - 基本功能可用性
   - 菜单和界面正常显示

2. **高级测试** (多人游戏)
   - 多人游戏同步
   - 服务器设置应用
   - 模组间交互

3. **长期测试** (游戏进程)
   - 长时间游戏稳定性
   - 存档加载/保存
   - 关键游戏事件处理

## 需要采取的行动

### 立即行动
1. **移除过时补丁**: 不使用[OBSOLETE] CleanUI Patch for B42.13
2. **安装必需补丁**: 为需要补丁的模组安装对应补丁
3. **使用替代方案**: 使用修复版本代替原版Neat Crafting和Neat Building

### 测试计划
1. 创建B42.14.1测试环境
2. 按类别分批测试模组
3. 记录任何兼容性问题或冲突
4. 在问题出现时寻找解决方案

### 监控更新
1. 关注模组作者的Steam Workshop页面
2. 检查是否有针对B42.14.1的更新
3. 寻找社区讨论和兼容性报告
4. 及时更新文档中的兼容性信息

---
*此报告基于已知信息和文档内容生成，实际兼容性请在B42.14.1游戏环境中测试验证*
"""

    return report

if __name__ == "__main__":
    # 生成详细报告
    detailed_report = generate_detailed_report()

    # 保存报告
    with open("detailed_compatibility_report.md", "w", encoding="utf-8") as f:
        f.write(detailed_report)

    print("详细兼容性报告已生成: detailed_compatibility_report.md")
