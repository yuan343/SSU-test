import streamlit as st
import pandas as pd

st.set_page_config(page_title="IMM2510-002 SSU 协同站", layout="wide")

# 侧边栏：完整项目名片
with st.sidebar:
    st.title("🏥 项目索引")
    st.success("**方案版本**: V6.0 (2026.03.23)\n\n**IB版本**: V5.0 (IMM2510)")
# 核心模块：项目会信息
    st.subheader("📅 项目会信息")
    st.info("⏰ **每周五 14:00**\n\n项目周会 (临床运营)\n\n腾讯会议：727-7862-0848")

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

# --- 左侧侧边栏设置 ---
with st.sidebar:
    st.title("📂 功能导航")
    # 这里是你的其他功能，比如 SSU 资料、费用测算等
    st.info("当前页面：项目通讯录")
    st.markdown("---")
    st.write("💡 提示：点击中间页面的各部门标签即可查看人员联系方式。")

# --- 中间主页面设置 ---
st.title("📇 IMM2510-002 项目核心通讯录")
st.write("请点击对应的部门展开人员名单：")

# 1. 申办方 - 宜明昂科
with st.expander("🏢 申办方 (ImmuneOnco)"):
    df_sponsor = pd.DataFrame([
        {"姓名": "王琼", "职位": "项目总监 (PMD)", "联系方式": "138-xxxx-xxxx", "邮箱": "zhangsan@immuneonco.com"},
        {"姓名": "吕志刚", "职位": "项目经理 (Medical)", "联系方式": "139-xxxx-xxxx", "邮箱": "lisi@immuneonco.com"},
        {"姓名": "XXX", "职位": "医学 (Medical)", "联系方式": "139-xxxx-xxxx", "邮箱": "lisi@immuneonco.com"}
    ])
    st.table(df_sponsor)

# 2. SMO - 津石
with st.expander("🤝  SMO (CRC)"):
    df_cro = pd.DataFrame([
        {"姓名": "王五", "职位": "SSU 负责人", "联系方式": "137-xxxx-xxxx", "邮箱": "wangwu@gemstone.com"},
        {"姓名": "赵六", "职位": "区域监查经理 (CRM)", "联系方式": "136-xxxx-xxxx", "邮箱": "zhaoliu@gemstone.com"},
        {"姓名": "各中心 CRC", "职位": "现场协调员", "联系方式": "见各中心子目录", "邮箱": "-"}
    ])
    st.table(df_cro)

# 3. 中心实验室 - 康维讯 & 阿克曼
with st.expander("🔬 中心实验室 (Lab Support)"):
    df_lab = pd.DataFrame([
        {"机构": "康维讯 (KangaBio)", "对接项目": "PK/ADA 样本转运", "联系电话": "400-xxx-xxxx", "备注": "负责样本箱申领"},
        {"机构": "阿克曼 (Ackerman)", "对接项目": "组织切片/Biomarker", "联系电话": "021-xxxx-xxxx", "备注": "负责切片回寄"}
    ])
    st.table(df_lab)

# 4. 冷链物流 - 药运/样运
with st.expander("🚚 物流供应商 (Logistics)"):
    st.write("**顺丰医药**: 95338 (备注：IMM2510月结账号 XXXX)")
    st.write("**专业冷链**: 400-xxx-xxxx (负责 2-8℃ 样本回寄)")

st.success("📝 建议：如人员有变动，请及时联系 SSU 经理更新，以防由于联系不畅导致资料递交延误。")
import streamlit as st
import pandas as pd

# 1. 定义 Tracker 数据
def get_file_tracker_data():
    file_data = [
        {"编号": "01", "分类": "申办方/CDE/方案", "文档名称": "临床试验方案 (Protocol V6.0)", "状态": "✅ 已获批", "备注": "最新版"},
        {"编号": "02", "分类": "申办方/CDE/方案", "文档名称": "CDE 受理通知书", "状态": "✅ 已获取", "备注": "-"},
        {"编号": "09", "分类": "IB/COA/监查计划", "文档名称": "研究者手册 (IB V5.0)", "状态": "⏳ 待更新", "备注": "预计下周更新"},
        {"编号": "17", "分类": "保险/授权/名单", "文档名称": "临床试验保险单", "状态": "✅ 已扩展37例", "备注": "-"},
        {"编号": "25", "分类": "使用手册/资质执照", "文档名称": "生产许可证/资质执照", "状态": "✅ 已补齐", "备注": "-"},
    ]
    return pd.DataFrame(file_data)

# 2. 页面展示逻辑
st.title("📂 IMM2510-002 SSU 文件 Tracker")

# 使用交互式表格展示 Tracker
df_tracker = get_file_tracker_data()

# 增加搜索和过滤功能
search_query = st.text_input("🔍 搜索文档名称或编号", "")
if search_query:
    df_tracker = df_tracker[df_tracker['文档名称'].str.contains(search_query) | df_tracker['编号'].str.contains(search_query)]

# 渲染 Tracker 表格
st.dataframe(
    df_tracker,
    use_container_width=True,
    column_config={
        "状态": st.column_config.SelectboxColumn(
            "最新状态",
            options=["✅ 已获取", "⏳ 待更新", "❌ 缺失", "⚠️ 待盖章"],
            required=True,
        )
    },
    hide_index=True,
)

# 3. 进度统计摘要
st.divider()
col1, col2, col3 = st.columns(3)
col1.metric("总文档数", "38")
col2.metric("已完成", "32", delta="2 (本周)")
col3.metric("待跟进", "6", delta="-1", delta_color="inverse")
