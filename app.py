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
import streamlit as st
import pandas as pd
from io import BytesIO

# --- 1. 页面基本配置 (必须置顶) ---
st.set_page_config(page_title="IMM2510-002 SSU工作站", layout="wide")

# --- 2. 数据函数定义 ---
def get_full_contact_data():
    # 宜明昂科管理团队
    mgmt_data = [
        ["CMO", "吴诸丽"], ["VP", "周玉斌"], ["PMD", "王琼"], ["PM", "吕志刚"],
        ["CTA", "马佳怡"], ["项目管理总监", "庞鑫"], ["运营副总监", "邵倩雯"],
        ["医学副总监", "孙本全"], ["医学总监", "张金超"], ["数据管理经理", "王韵"],
        ["药物警戒高级经理", "唐田晶"], ["统计师", "任宇铭"], ["临床药理高级经理", "陈杰桃"]
    ]
    # 研究中心与CRA全量
    cra_data = [
        ["复旦大学附属中山医院", "李銮銮", "19821875816", "luanluan.li@immuneonco.com"],
        ["四川大学华西医院", "邱妍锫", "15390309353", "yanpei.qiu@immuneonco.com"],
        ["河南省肿瘤医院", "李艺雯", "13461035295", "yiwen.li@immuneonco.com"],
        ["吉林大学第一医院", "赵婉霞", "13940406713", "wanxia.zhao@immuneonco.com"],
        ["福建省肿瘤医院", "陶文静", "18890072100", "wenjing.tao@immuneonco.com"],
        ["临沂市肿瘤医院", "亢德川", "15617645026", "dechuan.kang@immuneonco.com"],
        ["南昌大学第一附属医院", "王新鑫", "13974531757", "xinxin.wang@immuneonco.com"],
        ["浙江大学医学院附属第二医院", "田甜", "13770991661", "tian.tian@immuneonco.com"],
        ["西安交通大学第一附属医院", "韩旭", "15701197417", "xu.han@immuneonco.com"]
    ]
    # SMO (津石) 团队
    smo_data = [
        ["河南科技大学第一附属医院", "杨洁", "13633893896", "yang_jie0108@wuxiapptec.com"],
        ["临沂市肿瘤医院", "李春潇", "18865490982", "li_chunxiao0101@wuxiapptec.com"],
        ["南昌大学第一附属医院", "余红梅", "18279539445", "yu_hongmei0701@wuxiapptec.com"],
        ["湘潭市中心医院", "陈玉玲", "15573214901", "chen_yuling@wuxiapptec.com"],
        ["浙江大学医学院附属第二医院", "蔡晶晶", "18329107307", "cai_jingjing@wuxiapptec.com"],
        ["湖南省肿瘤医院", "贺冬雪", "15580676917", "he_dongxue@wuxiapptec.com"]
    ]
    return mgmt_data, cra_data, smo_data

# --- 3. 左侧边栏导航 ---
with st.sidebar:
    st.title("🚀 IMM2510-002 SSU")
    st.info("📅 **项目周会：每周五 14:00**")
    st.divider()
    menu = st.radio("功能切换", ["项目主页 (Timeline & Tracker)", "核心通讯录", "访视明细"])
    st.divider()
    st.caption("版本：V1.0 (2026-04-22)")

# --- 4. 中间主页面逻辑 ---

# 页面公用顶部：Timeline 图片
st.title("🗓️ 项目启动关键里程碑")
st.image("9db03bde-565b-44ac-b35a-1bacb4b05380.png", use_container_width=True)
st.divider()

if menu == "项目主页 (Timeline & Tracker)":
    st.header("📂 启动包文件 Tracker (38项)")
    # 这里放置文件Tracker表格
    tracker_data = [
        {"编号": "01", "文档名称": "临床试验方案 (V6.0)", "状态": "✅ 已获取"},
        {"编号": "09", "文档名称": "研究者手册 (V5.0)", "状态": "⏳ 待更新"},
        {"编号": "17", "文档名称": "受试者保险单", "状态": "✅ 已获取"}
    ]
    st.dataframe(pd.DataFrame(tracker_data), use_container_width=True, hide_index=True)
    
    # 进度统计
    col1, col2 = st.columns(2)
    col1.metric("已完成文档", "32 / 38", delta="2")
    col2.metric("目标首家启动", "2026-Q2")

elif menu == "核心通讯录":
    mgmt, cra, smo = get_full_contact_data()
    t1, t2, t3 = st.tabs(["申办方团队", "CRA团队", "SMO/供应商"])
    
    with t1:
        st.dataframe(pd.DataFrame(mgmt, columns=["职位", "姓名"]), use_container_width=True, hide_index=True)
    with t2:
        st.table(pd.DataFrame(cra, columns=["中心名称", "CRA姓名", "电话", "邮箱"]))
    with t3:
        st.dataframe(pd.DataFrame(smo, columns=["中心名称", "SSU CRC", "电话", "邮箱"]), use_container_width=True, hide_index=True)

elif menu == "访视明细":
    st.header("📊 访视流水账 (一事一行)")
    st.info("此模块展示方案 V6.0 极致拆解后的访视明细...")
