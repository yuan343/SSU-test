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

st.set_page_config(page_title="IMM2510-002 预算看板", layout="wide")

st.title("💰 IMM2510-002 项目全量检查费用试算器")
st.warning("依据：方案 V6.0 流程表 | 测算阶段：剂量探索期 | 统计口径：单人完成 8 周期治疗")

# 1. 定义最全的检查项目数据库
all_inspection_items = [
    # 类别, 项目名称, 方案次数, 默认单价, 备注
    ["实验室", "血常规 (CBC)", 14, 60, "筛选+给药期+EOT+随访"],
    ["实验室", "血生化 (全项)", 14, 280, "肝肾功/电解质/血脂等"],
    ["实验室", "凝血功能+D-二聚体", 12, 120, "VEGF靶向药风险监测"],
    ["实验室", "尿常规 (含镜检)", 12, 30, "重点监测尿蛋白"],
    ["实验室", "甲状腺功能/心肌酶/TBNK", 9, 450, "免疫相关AE监测"],
    ["实验室", "病毒学五项 (仅筛选)", 1, 200, "乙肝/丙肝/HIV/梅毒"],
    ["实验室", "妊娠检查 (血/尿)", 11, 60, "育龄女性每周期必做"],
    ["实验室", "24小时尿蛋白定量", 3, 100, "风险预留：蛋白尿二级及以上时"],
    
    ["影像辅检", "增强 CT (胸/腹/盆/颈部)", 5, 1600, "每8周一次疗效评估"],
    ["影像辅检", "12导联心电图 (ECG)", 22, 40, "含C1D1多点位监测(4次/日)"],
    ["影像辅检", "超声心动图 (LVEF评估)", 3, 300, "基线+C4+EOT"],
    ["影像辅检", "MRI/骨扫描 (仅筛选)", 1, 1000, "基线确认转移灶"],
    ["影像辅检", "风险预留(眼科/肺功能)", 1, 800, "视临床指征按需进行"],

    ["手术病理", "肿瘤组织活检 (穿刺费)", 2, 2500, "筛选期+给药后强制/可选"],
    ["手术病理", "病理组织处理费 (含白片)", 2, 800, "配合中心实验室送检"],
    
    ["人工采样", "PK/ADA 样本处理费", 40, 60, "离心/分装/超低温存储(全周期)"],
    ["人工采样", "ctDNA/PBMC 采样处理费", 5, 100, "按方案要求点位采集"],
    
    ["医院管理", "诊查费/床位费/观察费", 12, 300, "视中心住院或门诊给药政策"]
]

# 2. 转换为 DataFrame
df_init = pd.DataFrame(all_inspection_items, columns=["分类", "检查项目", "方案频次", "单价(元)", "备注"])

# 3. 页面交互：单价调整区
st.subheader("🛠️ 第一步：输入贵中心单价")
st.caption("双击下方【单价】列即可修改，表格将根据方案预设频次自动计算总额。")

edited_df = st.data_editor(
    df_init,
    column_config={
        "单价(元)": st.column_config.NumberColumn("实际单价 (¥)", format="¥%d"),
        "方案频次": st.column_config.NumberColumn("方案频次 (次)", disabled=True),
    },
    disabled=["分类", "检查项目", "方案频次", "备注"],
    hide_index=True,
    use_container_width=True
)

# 4. 计算与结果展示
edited_df["小计"] = edited_df["方案频次"] * edited_df["单价(元)"]
total_per_patient = edited_df["小计"].sum()

st.divider()

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("单名受试者总检查费", f"¥ {total_per_patient:,.2f}")
with col2:
    patient_num = st.number_input("该中心预计入组人数", value=3, step=1)
with col3:
    st.metric("中心项目总预算(估算)", f"¥ {total_per_patient * patient_num:,.2f}")

# 5. 导出提示
st.info(f"💡 建议：该中心合同总额建议在 **¥ {total_per_patient * patient_num * 1.06:,.2f}** 以上 (已含6%税费预估)")

with st.expander("📌 费用编制必看说明"):
    st.markdown("""
    - **关于频次**：心电图和采样费已计入 C1D1 的密集点位，请勿自行删减。
    - **超温/AE费用**：本表已预留了 **24h尿蛋白** 和 **风险特殊检查** 的单次预算。
    - **中心实验室**：检测费已由申办方支付，本表仅核算医院端收取的『耗材及处理费』。
    """)
