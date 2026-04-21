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

st.set_page_config(page_title="IMM2510-002 动态预算看板", layout="wide")

st.title("💰 IMM2510-002 全周期费用动态测算器")
st.markdown("---")

# 1. 动态参数设置区
with st.sidebar:
    st.header("⚙️ 测算参数设置")
    cycles = st.slider("预计治疗周期数 (1周期=3周)", min_value=1, max_value=24, value=8)
    patient_num = st.number_input("该中心预计入组人数", value=3, step=1)
    st.info(f"当前设定：完成 {cycles} 个周期治疗（约 {cycles*3} 周）")

# 2. 定义检查项目及其与周期的计算逻辑
# 逻辑说明：
# - 固定项：筛选期(1次) + EOT(1次)
# - 周期项：每周期做一次
# - 评估项：每2周期(8周)做一次
data_logic = [
    {"分类": "实验室", "项目": "血常规/生化/凝血/尿常规", "基数": 2, "周期系数": 1, "参考单价": 350, "备注": "筛选+EOT+每周期"},
    {"类别": "安全性", "项目": "心肌酶谱/肌钙蛋白", "基数": 1, "周期系数": 1, "参考单价": 150, "备注": "方案要求C1-C8给药前"},
    {"类别": "安全性", "项目": "D-二聚体", "基数": 0, "周期系数": 1, "参考单价": 80, "备注": "随每周期凝血监测"},
    {"类别": "实验室", "项目": "妊娠检查 (血/尿)", "基数": 1, "周期系数": 1, "参考单价": 60, "备注": "仅育龄女性"},
    {"类别": "影像辅检", "项目": "增强CT (胸/腹/盆/颈部)", "基数": 1, "周期系数": 0.5, "参考单价": 1500, "备注": "每8周(2周期)一次"},
    {"类别": "影像辅检", "项目": "12导联心电图 (ECG)", "基数": 6, "周期系数": 2, "参考单价": 40, "备注": "含C1密集期及每周期监测"},
    {"类别": "手术病理", "项目": "肿瘤组织活检 (含穿刺及处理)", "基数": 2, "周期系数": 0, "参考单价": 2800, "备注": "固定2次(筛选+给药后)"},
    {"类别": "采样费", "项目": "中心实验室样本处理费(PK/ADA)", "基数": 5, "周期系数": 3, "参考单价": 60, "备注": "C1密集采样+后期随访"},
    {"类别": "管理费", "项目": "诊查费/床位费/观察费", "基数": 0, "周期系数": 1, "参考单价": 300, "备注": "按治疗周期计算"}
]

# 3. 动态生成数据表
processed_list = []
for item in data_logic:
    # 核心公式：总次数 = 固定基数 + (周期数 * 周期系数)
    total_times = int(item["基数"] + (cycles * item["周期系数"]))
    processed_list.append({
        "分类": item.get("类别", item.get("分类")),
        "检查项目": item["项目"],
        "计算出的次数": total_times,
        "单价(元)": item["参考单价"],
        "备注": item["备注"]
    })

df_dynamic = pd.DataFrame(processed_list)

# 4. 网页交互编辑
st.subheader("🛠️ 第一步：核对次数并填入单价")
st.caption("次数已根据左侧【治疗周期数】自动更新。你可以双击单价列进行修改。")

edited_df = st.data_editor(
    df_dynamic,
    column_config={"单价(元)": st.column_config.NumberColumn("单价 (¥)", format="¥%d")},
    disabled=["分类", "检查项目", "计算出的次数", "备注"],
    hide_index=True,
    use_container_width=True
)

# 5. 计算结果汇总
edited_df["小计"] = edited_df["计算出的次数"] * edited_df["单价(元)"]
total_single = edited_df["小计"].sum()

st.divider()
c1, c2 = st.columns(2)
with c1:
    st.metric(f"单名受试者 ({cycles}周期) 总预算", f"¥ {total_single:,.2f}")
with c2:
    st.metric(f"该中心总预算评估 ({patient_num}人)", f"¥ {total_single * patient_num:,.2f}")

st.info(f"💡 专业提示：方案 V6.0 规定，若受试者在第 8 周期后仍获益，可继续治疗。建议预算至少按 **12 个周期** (约 9 个月) 进行编制以留有余量。")
