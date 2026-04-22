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
        {"姓名": "张三", "职位": "项目总监 (PD)", "联系方式": "138-xxxx-xxxx", "邮箱": "zhangsan@immuneonco.com"},
        {"姓名": "李四", "职位": "医学经理 (Medical)", "联系方式": "139-xxxx-xxxx", "邮箱": "lisi@immuneonco.com"}
    ])
    st.table(df_sponsor)

# 2. CRO & SMO - 津石 (Gemstone)
with st.expander("🤝 CRO & SMO (监查/启动/CRC)"):
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
