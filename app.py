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

import streamlit as st
import pandas as pd
from io import BytesIO

# --- 页面基本配置 ---
st.set_page_config(page_title="IMM2510-002 SSU工作站", layout="wide")

# --- 1. 数据函数：确保所有明细都在这里 ---
def get_full_contact_data():
    # 宜明昂科管理团队全量
    mgmt_data = [
        ["CMO", "吴诸丽", "-", "-"], ["VP", "周玉斌", "-", "-"],
        ["PMD", "王琼", "-", "-"], ["PM", "吕志刚", "13764295352", "zhigang.lv@immuneonco.com"],
        ["CTA", "马佳怡", "18601636864", "jiayi.ma@immuneonco.com"], ["项目管理总监", "庞鑫", "-", "-"],
        ["运营副总监", "邵倩雯", "-", "-"], ["资深总监", "景德强", "-", "-"],
        ["医学总监", "张金超", "-", "-"], ["数据管理总监", "棘玉荣", "-", "-"],
        ["药物警戒总监", "潘萍", "-", "-"], ["统计师", "任宇铭", "-", "-"]
    ]
    # 研究中心与CRA全量
    cra_data = [
        ["复旦中山", "李銮銮", "19821875816", "luanluan.li@immuneonco.com", "上海"],
        ["四川华西", "邱妍锫", "15390309353", "yanpei.qiu@immuneonco.com", "成都"],
        ["河南肿瘤", "李艺雯", "13461035295", "yiwen.li@immuneonco.com", "郑州"],
        ["华西(另一职责)", "邱妍锫", "15390309353", "yanpei.qiu@immuneonco.com", "成都"],
        ["浙大二院", "蔡晶晶", "18329107307", "cai_jingjing@wuxiapptec.com", "杭州"],
        ["湖南肿瘤", "贺冬雪", "15580676917", "he_dongxue@wuxiapptec.com", "长沙"]
    ]
    # SMO (津石) SSU CRC全量
    smo_data = [
        ["09", "河科大一附院", "杨洁", "13633893896", "yang_jie0108@wuxiapptec.com"],
        ["11", "临沂市肿瘤", "李春潇", "18865490982", "li_chunxiao0101@wuxiapptec.com"],
        ["12", "南昌一附院", "余红梅", "18279539445", "yu_hongmei0701@wuxiapptec.com"],
        ["13", "湘潭市中心", "陈玉玲", "15573214901", "chen_yuling@wuxiapptec.com"],
        ["14", "浙大二院", "蔡晶晶", "18329107307", "cai_jingjing@wuxiapptec.com"],
        ["15", "湖南省肿瘤", "贺冬雪", "15580676917", "he_dongxue@wuxiapptec.com"]
    ]
    return mgmt_data, cra_data, smo_data

# --- 2. 左侧边栏导航 ---
with st.sidebar:
    st.title("🚀 SSU 数字化看板")
    st.info("📅 **项目周会：每周五 14:00**")
    st.divider()
    menu = st.selectbox("功能切换", ["项目全量通讯录", "文件 Tracker", "访视明细(一事一行)"])
    st.divider()
    st.caption("版本：V1.0 (2026-04-22)")

# --- 3. 中间页面逻辑 ---

if menu == "项目全量通讯录":
    st.header("📇 项目核心通讯录 (全量版)")
    mgmt, cra, smo = get_full_contact_data()
    
    # 使用 Tabs 减少垂直空间占用，防止显示不全
    t1, t2, t3, t4 = st.tabs(["申办方管理团队", "研究中心 & CRA", "SMO (津石) 团队", "其他供应商"])
    
    with t1:
        st.subheader("宜明昂科 - 项目管理团队")
        df_mgmt = pd.DataFrame(mgmt, columns=["职位", "姓名", "电话", "邮箱"])
        st.dataframe(df_mgmt, use_container_width=True, hide_index=True)
        
    with t2:
        st.subheader("CRA 区域负责明细")
        df_cra = pd.DataFrame(cra, columns=["中心名称", "CRA姓名", "电话", "邮箱", "驻地"])
        st.table(df_cra)
        
    with t3:
        st.subheader("津石 - SSU CRC 联络表")
        df_smo = pd.DataFrame(smo, columns=["中心编号", "中心名称", "SSU CRC", "电话", "邮箱"])
        st.dataframe(df_smo, use_container_width=True, hide_index=True)
        
    with t4:
        col_l, col_r = st.columns(2)
        with col_l:
            st.markdown("**中心实验室**")
            st.write("🧪 康维讯 PM: 赵娟 | 15996268113")
            st.write("🔬 阿克曼 PM: 任卫 | 17621905332")
        with col_r:
            st.markdown("**物流与保险**")
            st.write("🚚 生生物流紧急联系人: 王金麟 | 15821381794")
            st.write("🛡️ 保险公司: 华泰财产保险有限公司")

elif menu == "文件 Tracker":
    st.header("📂 启动包文件 Tracker (38项)")
    # 此处放置您之前确定的 Tracker 逻辑
    st.write("正在追踪 38 项核心文件进度...")

elif menu == "访视明细(一事一行)":
    st.header("📊 访视动作流水账 (无单价版)")
    # 这里放之前为您生成的“一事一行”不含费用的 Excel 逻辑
    st.write("此处可放置下载按钮，直接下载全量 Excel 表格。")

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
