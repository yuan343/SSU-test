import streamlit as st
import pandas as pd

st.set_page_config(page_title="IMM2510-002 SSU 协同站", layout="wide")

# 侧边栏：完整项目名片
with st.sidebar:
    st.title("🏥 项目索引")
    st.success("**方案版本**: V6.0 (2026.03.23)\n\n**IB版本**: V5.0 (IMM2510)")
    st.info("**药物管理点**:\n- 保存: 2-8℃ 避光\n- 配制后室温: 510(8h)/27M(4h)\n- 复溶时间: 约2分40秒")
    st.warning("**中心实验室**:\n- 康维讯 (PK/ADA)\n- 阿克曼 (病理/Biomarker)")
    st.error("**保险有效期**:\n- 至 2027-05-30\n- 已覆盖20家中心")

st.title("🚀 IMM2510-002 临床试验快速启动站")
st.markdown("---")

t1, t2, t3, t4 = st.tabs(["📂 公共资料库", "🔬 药物/实验室要点", "📍 全国20家中心", "🛠️ 智能命名助手"])

with t1:
    st.subheader("全量启动包索引 (共38个核心文档)")
    data = {
        "编号": ["01-08", "09-16", "17-24", "25-36"],
        "分类": ["申办方/CDE/方案", "IB/COA/监查计划", "保险/授权/名单", "使用手册/资质执照"],
        "最新状态": ["方案V6.0已获批", "IB已更新至V5.0", "保单已扩展37例", "执照生产证全补齐"]
    }
    st.table(pd.DataFrame(data))
    st.info("💡 提示：请向申办方索取对应编号的标准命名文件。")

with t2:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 💊 药物使用预警")
        st.error("配制后室温稳定时长: IMM2510(8小时) | IMM27M(4小时)")
        st.write("- **复溶**: IMM2510 冻干粉复溶非常迅速")
        st.write("- **超温**: 8-25℃ 累计不超过48小时可继续使用")
    with col2:
        st.markdown("### 🧪 实验室送检指南")
        st.write("- **康维讯**: 负责PK/ADA (ISO 9001认证)")
        st.write("- **阿克曼**: 负责组织切片 (CAP/ISO 15189双证)")

with t3:
    st.subheader("📍 分中心布局 (剂量探索阶段)")
    sites = ["复旦中山(组长)", "吉大一院", "河南肿瘤", "武汉协和", "华西医院", "湖南肿瘤", "南昌二院", "清华长庚"]
    st.success(" ✅ 已确定参加并覆盖保险: " + " 、 ".join(sites))

with t4:
    st.subheader("🤖 文件命名标准化")
    st.write("请将文件重命名为以下格式后再归档：")
    st.code("项目名_中心号_文件类型_版本_日期.pdf", language="text")
import streamlit as st
import pandas as pd

st.set_page_config(page_title="IMM2510-002 费用测算工作台", layout="wide")

st.title("💰 IMM2510-002 受试者检查费用全量试算表")
st.info("说明：本表频次依据【方案 V6.0】剂量探索阶段（单人完成 8 周期治疗）测算。各中心可根据物价局单价自行调整。")

# 1. 建立基础数据（全量项目 + 次数）
# 数据来源：方案 V6.0 流程表
budget_data = [
    {"项目分类": "实验室检查", "项目名称": "血常规/生化/凝血/尿常规", "方案频次": 12, "单价": 300, "备注": "筛选+EOT+每周期给药前"},
    {"项目分类": "实验室检查", "项目名称": "病毒学(乙肝/丙肝/HIV/梅毒)", "方案频次": 1, "单价": 200, "备注": "仅筛选期"},
    {"项目分类": "实验室检查", "项目名称": "妊娠检查 (育龄女性)", "方案频次": 10, "单价": 60, "备注": "每次给药前"},
    {"项目分类": "实验室检查", "项目名称": "甲状腺功能/心肌酶", "方案频次": 10, "单价": 260, "备注": "基线+每周期"},
    {"项目分类": "影像学评估", "项目名称": "增强CT (胸/腹/盆/颈部)", "方案频次": 5, "单价": 1500, "备注": "每8周评估一次"},
    {"项目分类": "辅助检查", "项目名称": "12导联心电图 (ECG)", "方案频次": 18, "单价": 40, "备注": "C1D1点位密集"},
    {"项目分类": "辅助检查", "项目名称": "超声心动图 (ECHO)", "方案频次": 3, "单价": 300, "备注": "基线+随访"},
    {"项目分类": "手术操作", "项目名称": "肿瘤组织活检 (穿刺及耗材)", "方案频次": 2, "单价": 2000, "备注": "筛选期+给药后"},
    {"项目分类": "手术操作", "项目名称": "病理组织处理与切片", "方案频次": 2, "单价": 800, "备注": "配合活检"},
    {"项目分类": "医院端其他", "项目名称": "床位费/诊查费/观察费", "方案频次": 10, "单价": 200, "备注": "按给药频次估算"}
]

df_base = pd.DataFrame(budget_data)

# 2. 网页交互部分
st.subheader("🛠️ 第一步：调整各中心单价")
st.write("请在下方表格的【单价】列直接修改（支持双击编辑），总价将自动更新。")

# 使用 Streamlit 的数据编辑器功能，允许用户修改单价
edited_df = st.data_editor(
    df_base,
    column_config={
        "单价": st.column_config.NumberColumn("单价 (元)", format="¥%d"),
        "方案频次": st.column_config.NumberColumn("方案频次 (次)", disabled=True),
    },
    disabled=["项目分类", "项目名称", "方案频次", "备注"],
    hide_index=True,
    use_container_width=True
)

# 3. 计算逻辑
edited_df["项目小计"] = edited_df["方案频次"] * edited_df["单价"]
total_budget = edited_df["项目小计"].sum()

st.markdown("---")
st.subheader("📊 第二步：测算结果汇总")

col1, col2 = st.columns(2)
with col1:
    st.metric(label="单名受试者（全周期）预计总费用", value=f"¥ {total_budget:,.2f}")
with col2:
    patient_count = st.number_input("该中心预计入组人数", value=3, step=1)
    st.write(f"**该中心项目总预算评估 (检查费):** :red[¥ {total_budget * patient_count:,.2f}]")

# 4. 补充提醒
with st.expander("📝 预算编制注意事项"):
    st.write("- **PK/ADA 采样**: 方案中采样点极多，虽然检测费由中心实验室承担，但医院可能收取『采血费』或『样本处理费』。")
    st.write("- **超量检查**: 若患者出现免疫相关不良反应(irAE)，产生的额外检查费需单独核算。")
    st.write("- **税费**: 最终合同总额通常需在此基础上增加 6% 左右的税费。")
