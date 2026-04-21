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

st.set_page_config(page_title="IMM2510-002 全量预算表", layout="wide")

st.title("💰 IMM2510-002 全周期全量检查费测算表 (方案 V6.0)")
st.info("说明：本表将各阶段（3个月/6个月/1年）的次数与合计直接并列展示，方便合同预算全覆盖。")

# 1. 定义核心数据库 (包含所有你要求的细节)
# 逻辑：总次数 = 基数(筛选+EOT) + (周期数 * 系数)
raw_data = [
    {"分类": "实验室", "项目": "血常规/生化/凝血/尿常规", "基数": 2, "系数": 1.0, "单价": 350, "备注": "每周期1次+筛选/EOT"},
    {"分类": "安全性", "项目": "心肌酶谱/肌钙蛋白", "基数": 1, "系数": 1.0, "单价": 150, "备注": "方案C1-C8给药前必查"},
    {"分类": "安全性", "项目": "D-二聚体", "基数": 0, "系数": 1.0, "单价": 80, "备注": "随每周期凝血功能监测"},
    {"分类": "实验室", "项目": "甲状腺功能/TBNK细胞", "基数": 1, "系数": 0.6, "单价": 300, "备注": "约每2周期一次"},
    {"分类": "实验室", "项目": "妊娠检查 (仅限育龄女性)", "基数": 1, "系数": 1.0, "单价": 60, "备注": "每周期给药前"},
    {"分类": "实验室", "项目": "24h尿蛋白 (风险预留)", "基数": 3, "系数": 0.0, "单价": 100, "备注": "尿蛋白≥2+时触发"},
    {"分类": "影像辅检", "项目": "增强 CT (胸/腹/盆/颈部)", "基数": 1, "系数": 0.5, "单价": 1500, "备注": "每8周(2周期)一次"},
    {"分类": "影像辅检", "项目": "12导联心电图 (ECG)", "基数": 6, "系数": 2.0, "单价": 40, "备注": "含C1密集期及随访"},
    {"分类": "影像辅检", "项目": "超声心动图 (LVEF评估)", "基数": 3, "系数": 0.0, "单价": 300, "备注": "基线+C4+EOT"},
    {"分类": "风险预留", "项目": "特殊检查 (眼科/肺功能/MRI)", "基数": 1, "系数": 0.0, "单价": 800, "备注": "视临床指征按需进行"},
    {"分类": "手术病理", "项目": "肿瘤组织活检 (穿刺费)", "基数": 2, "系数": 0.0, "单价": 2500, "备注": "固定2次 (筛选+给药后)"},
    {"分类": "手术病理", "项目": "病理组织处理费 (含白片)", "基数": 2, "系数": 0.0, "单价": 800, "备注": "配合中心实验室送检"},
    {"分类": "采样费", "项目": "中心实验室样本处理(PK/ADA/ctDNA)", "基数": 5, "系数": 3.0, "单价": 60, "备注": "含全周期离心/分装人工费"},
    {"分类": "医院管理", "项目": "诊查费/观察费/床位费", "基数": 0, "系数": 1.0, "单价": 200, "备注": "按给药周期计费"}
]

# 2. 单价编辑区
st.subheader("第一步：编辑单价 (双击下方单价列修改)")
df_input = pd.DataFrame(raw_data)[["分类", "项目", "单价", "备注"]]
edited_df = st.data_editor(
    df_input,
    column_config={"单价": st.column_config.NumberColumn("单价 (¥)", format="¥%d")},
    disabled=["分类", "项目", "备注"],
    hide_index=True,
    use_container_width=True
)

# 3. 计算并展示三个阶段的次数与合计
st.subheader("第二步：全周期费用对比明细 (已含最全检查项)")

# 定义展示的三个周期：4周期(3个月), 8周期(半年), 16周期(1年)
milestones = [4, 8, 16]
final_rows = []

for i, item in enumerate(raw_data):
    current_price = edited_df.iloc[i]["单价"]
    row = {"项目": item["项目"]}
    
    for m in milestones:
        # 计算次数
        count = int(item["基数"] + (m * item["系数"]))
        row[f"{m}周期次数"] = count
        row[f"{m}周期合计"] = count * current_price
        
    row["备注"] = item["备注"]
    final_rows.append(row)

# 转换为大表并展示
df_final = pd.DataFrame(final_rows)

# 优化列表头显示
column_order = ["项目"]
for m in milestones:
    column_order.extend([f"{m}周期次数", f"{m}周期合计"])
column_order.append("备注")

st.dataframe(df_final[column_order], use_container_width=True, hide_index=True)

# 4. 底部总额汇总
st.divider()
total_cols = st.columns(len(milestones))
for idx, m in enumerate(milestones):
    total_val = df_final[f"{m}周期合计"].sum()
    total_cols[idx].metric(f"{m}周期 (总预算)", f"¥ {total_val:,.2f}")

st.success("💡 提示：该表已包含安全性监测（心肌酶、D-二聚体）及样本处理费。建议按 16 周期版本进行合同洽谈。")
