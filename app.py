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

# --- 1. 页面基本配置 (必须放在第一行) ---
st.set_page_config(page_title="IMM2510-002 SSU工作站", layout="wide")

# --- 2. 数据函数定义 ---
def get_full_contact_data():
    # 宜明昂科管理团队 (已补全逗号和括号)
    mgmt_data = [
        ["CMO", "吴诸丽"], ["VP", "周玉斌"], ["PMD", "王琼"], ["PM", "吕志刚"],
        ["CTA", "马佳怡"], ["项目管理总监", "庞鑫"], ["运营副总监", "邵倩雯"],
        ["医学副总监", "孙本全"], ["医学总监", "张金超"], ["数据管理经理", "王韵"],
        ["药物警戒高级经理", "唐田晶"], ["统计师", "任宇铭"], ["临床药理高级经理", "陈杰桃"]
    ]
    
    # 研究中心与CRA全量 (已补全逗号)
    cra_data = [
        ["复旦大学附属中山医院", "李銮銮", "19821875816", "luanluan.li@immuneonco.com"],
        ["四川大学华西医院", "邱妍锫", "15390309353", "yanpei.qiu@immuneonco.com"],
        ["河南省肿瘤医院", "李艺雯", "13461035295", "yiwen.li@immuneonco.com"],
        ["华中科技大学同济医学院附属协和医院", "杨勐", "待定", "待定"],
        ["吉林大学第一医院", "赵婉霞", "13940406713", "wanxia.zhao@immuneonco.com"],
        ["河南科技大学第一附属医院", "李艺雯", "13461035295", "yiwen.li@immuneonco.com"],
        ["福建省肿瘤医院", "陶文静", "18890072100", "wenjing.tao@immuneonco.com"],
        ["临沂市肿瘤医院", "亢德川", "15617645026", "dechuan.kang@immuneonco.com"],
        ["南昌大学第一附属医院", "王新鑫", "13974531757", "xinxin.wang@immuneonco.com"],
        ["湘潭市中心医院", "王新鑫", "13974531757", "xinxin.wang@immuneonco.com"],
        ["浙江大学医学院附属第二医院", "田甜", "13770991661", "tian.tian@immuneonco.com"],
        ["郑州大学第一附属医院", "杨洋", "13681047537", "yang.yang@immuneonco.com"],
        ["大连大学附属中山医院", "赵婉霞", "13940406713", "wanxia.zhao@immuneonco.com"],
        ["河南省人民医院", "杨洋", "13681047537", "yang.yang@immuneonco.com"],
        ["西安交通大学第一附属医院", "韩旭", "15701197417", "xu.han@immuneonco.com"],
        ["河北医科大学第四医院", "马慧子", "待定", "待定"],
        ["山西省肿瘤医院", "马慧子", "待定", "待定"],
        ["山东大学齐鲁医院", "谢明明", "待定", "待定"],
        ["北京胸科医院", "韩旭", "15701197417", "xu.han@immuneonco.com"]
    ]
    
    # SMO (津石) 团队 (已补全逗号)
    smo_data = [
        ["复旦大学附属中山医院", "待定", "待定", "待定"],
        ["河南科技大学第一附属医院", "杨洁", "13633893896", "yang_jie0108@wuxiapptec.com"],
        ["临沂市肿瘤医院", "李春潇", "18865490982", "li_chunxiao0101@wuxiapptec.com"],
        ["南昌大学第一附属医院", "余红梅", "18279539445", "yu_hongmei0701@wuxiapptec.com"],
        ["湘潭市中心医院", "陈玉玲", "15573214901", "chen_yuling@wuxiapptec.com"],
        ["浙江大学医学院附属第二医院", "蔡晶晶", "18329107307", "cai_jingjing@wuxiapptec.com"],
        ["湖南省肿瘤医院", "贺冬雪", "15580676917", "he_dongxue@wuxiapptec.com"],
        ["郑州大学第一附属医院", "韩璐悦", "15580676917", "han_luyue@wuxiapptec.com"],
        ["河南省人民医院", "党梦平", "15517818526", "dang_mengping@wuxiapptec.com"],
        ["西安交通大学第一附属医院", "王乐", "19916405427", "wang_le0701@wuxiapptec.com"],
        ["山西省肿瘤医院", "魏佳琪", "18834152547", "wei_jiaqi@wuxiapptec.com"],
        ["北京胸科医院", "杜佳睿", "15042590066", "du_jiarui@wuxiapptec.com"]
    ]
    return mgmt_data, cra_data, smo_data

def get_file_tracker_data():
    file_data = [
        {"编号": "01", "分类": "申办方/CDE/方案", "文档名称": "临床试验方案 (Protocol V6.0)", "状态": "✅ 已获批", "备注": "最新版"},
        {"编号": "02", "分类": "申办方/CDE/方案", "文档名称": "CDE 受理通知书", "状态": "✅ 已获取", "备注": "-"},
        {"编号": "09", "分类": "IB/COA/监查计划", "文档名称": "研究者手册 (IB V5.0)", "状态": "⏳ 待更新", "备注": "预计下周更新"},
        {"编号": "17", "分类": "保险/授权/名单", "文档名称": "临床试验保险单", "状态": "✅ 已扩展37例", "备注": "-"},
        {"编号": "25", "分类": "使用手册/资质执照", "文档名称": "生产许可证/资质执照", "状态": "✅ 已补齐", "备注": "-"},
    ]
    return pd.DataFrame(file_data)

# --- 3. 左侧边栏导航 ---
with st.sidebar:
    st.title("🚀 SSU 数字化管理")
    menu = st.selectbox("功能切换", ["项目全量通讯录", "文件 Tracker", "访视明细(一事一行)"])
    st.divider()
    st.caption("版本：V1.0 (2026-04-22)")

# --- 4. 中间主页面逻辑 ---
if menu == "项目全量通讯录":
    st.title("📇 IMM2510-002 项目核心通讯录")
    st.write("请点击对应的部门展开人员名单：")
    mgmt, cra, smo = get_full_contact_data()
    
    t1, t2, t3, t4 = st.tabs(["申办方管理团队", "研究中心 & CRA", "SMO 团队", "其他供应商"])
    
    with t1:
        st.subheader("宜明昂科 - 项目管理团队")
        df_mgmt = pd.DataFrame(mgmt, columns=["职位", "姓名"])
        st.dataframe(df_mgmt, use_container_width=True, hide_index=True)
        
    with t2:
        st.subheader("CRA 区域负责明细")
        df_cra = pd.DataFrame(cra, columns=["中心名称", "CRA姓名", "电话", "邮箱"])
        st.table(df_cra)
        
    with t3:
        st.subheader("津石 - SSU CRC 联络表")
        df_smo = pd.DataFrame(smo, columns=["中心名称", "SSU CRC", "电话", "邮箱"])
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
    st.title("📂 IMM2510-002 SSU 文件 Tracker")
    df_tracker = get_file_tracker_data()
    
    search_query = st.text_input("🔍 搜索文档名称或编号", "")
    if search_query:
        df_tracker = df_tracker[df_tracker['文档名称'].str.contains(search_query) | df_tracker['编号'].str.contains(search_query)]

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
    
    st.divider()
    col1, col2, col3 = st.columns(3)
    col1.metric("总文档数", "38")
    col2.metric("已完成", "32", delta="2 (本周)")
    col3.metric("待跟进", "6", delta="-1", delta_color="inverse")

elif menu == "访视明细(一事一行)":
    st.title("📊 访视动作流水账")
    st.info("此处展示 C1-C8 的极致平铺流水账...")
    # 可在此处添加之前的访视逻辑代码
