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

st.set_page_config(page_title="IMM2510-002 费用测算全表", layout="wide")

st.title("💰 IMM2510-002 全周期全量费用测算表")
st.markdown("---")

# 1. 第一部分：受试者检查费 (随周期变动)
st.subheader("第一部分：受试者检查费 (Variable Subject Fees)")
st.caption("以下项目次数随访视周期增加而累计。")

exam_data = [
    {"项目": "血常规/生化/凝血/尿常规", "基数": 2, "系数": 1.0, "单价": 350, "备注": "每周期1次+筛选/EOT"},
    {"项目": "心肌酶谱/肌钙蛋白", "基数": 1, "系数": 1.0, "单价": 150, "备注": "方案C1-C8给药前"},
    {"项目": "D-二聚体", "基数": 0, "系数": 1.0, "单价": 80, "备注": "随每周期监测"},
    {"项目": "增强 CT (胸/腹/盆/颈部)", "基数": 1, "系数": 0.5, "单价": 1500, "备注": "每8周(2周期)一次"},
    {"项目": "12导联心电图 (ECG)", "基数": 6, "系数": 2.0, "单价": 40, "备注": "含C1密集期多点位"},
    {"项目": "肿瘤组织活检 (穿刺费)", "基数": 2, "系数": 0.0, "单价": 2500, "备注": "固定2次"},
    {"项目": "中心实验室样本处理(PK/ADA)", "基数": 5, "系数": 3.0, "单价": 60, "备注": "离心/分装/存储人工费"}
]

# 2. 第二部分：项目费用标准 (固定次数为1)
st.subheader("第二部分：项目费用标准 (Fixed Project Fees)")
st.caption("以下项目按【方式】计算，在各阶段测算中次数固定为 1。")

project_data = [
    {"项目": "中心启动费 (Startup Fee)", "单价": 5000, "备注": "中心启动一次性费用"},
    {"项目": "伦理初始审查费 (EC Fee)", "单价": 5000, "备注": "伦理委员会审查"},
    {"项目": "药房/药柜管理费", "单价": 3000, "备注": "药物存储与管理"},
    {"项目": "人类遗传资源管理费", "单价": 2000, "备注": "人遗办备案相关"},
    {"项目": "资料归档费 (Archiving)", "单价": 1000, "备注": "试验结束资料保存"},
    {"项目": "每例受试者管理费", "单价": 2000, "备注": "机构收取的按例管理费"}
]

# 3. 编辑单价逻辑 (合在一起方便修改)
all_items = exam_data + project_data
df_input = pd.DataFrame(all_items)[["项目", "单价"]]
st.write("🔧 **编辑中心单价：**")
edited_df = st.data_editor(df_input, column_config={"单价": st.column_config.NumberColumn("单价 (¥)", format="¥%d")}, hide_index=True, use_container_width=True)

# 4. 计算逻辑与对比表展示
milestones = [4, 8, 16] # 4周期, 8周期, 16周期
final_rows = []

for i, item in enumerate(all_items):
    current_price = edited_df.iloc[i]["单价"]
    row = {"项目明细": item["项目"]}
    
    for m in milestones:
        # 如果是受试者检查项(i < len(exam_data)), 按周期计算次数
        # 如果是项目费用项(i >= len(exam_data)), 次数固定为 1
        if i < len(exam_data):
            count = int(item["基数"] + (m * item["系数"]))
        else:
            count = 1
            
        row[f"{m}周期 次数"] = count
        row[f"{m}周期 小计"] = count * current_price
        
    row["备注"] = item["备注"]
    final_rows.append(row)

df_final = pd.DataFrame(final_rows)

# 5. 最终表格平铺展示
columns_order = ["项目明细"]
for m in milestones:
    columns_order.extend([f"{m}周期 次数", f"{m}周期 小计"])
columns_order.append("备注")

st.dataframe(df_final[columns_order], use_container_width=True, hide_index=True)

# 6. 总额统计
st.divider()
total_cols = st.columns(3)
for idx, m in enumerate(milestones):
    total_val = df_final[f"{m}周期 小计"].sum()
    total_cols[idx].metric(f"{m}周期 预计总额", f"¥ {total_val:,.2f}")

st.success("✅ 更新成功：已将项目费用标准设置为固定次数 (1次)，受试者检查费保持动态计算。")
