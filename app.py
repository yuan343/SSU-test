import streamlit as st
import pandas as pd
import os

# --- 1. 页面基本配置 (必须放在第一行) ---
st.set_page_config(page_title="IMM2510-002 SSU工作站", layout="wide")

# --- 2. 顶部置顶内容：Timeline 图片 ---
# 无论切换哪个菜单，Timeline 图片都作为“总览地图”显示在最上方
st.title("🚀 IMM2510-002 临床试验快速启动站")

image_path = "project_timeline.png"
if os.path.exists(image_path):
    st.image(image_path, use_container_width=True, caption="项目启动里程碑 Timeline")
else:
    st.warning(f"⚠️ 提示：未检测到图片 {image_path}。请确保图片已上传至 GitHub 仓库根目录。")

st.divider()

# --- 3. 数据准备函数 ---
def get_full_contact_data():
    # 宜明昂科管理团队
    mgmt_data = [
        ["CMO", "吴诸丽"], ["VP", "周玉斌"], ["PMD", "王琼"], ["PM", "吕志刚"],
        ["CTA", "马佳怡"], ["项目管理总监", "庞鑫"], ["运营副总监", "邵倩文"],
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
        ["南昌大学第一附属医院", "王新鑫", "13974531757", "xinxin.wang@immuneonco.com"],
        ["浙江大学附属第二医院", "田甜", "13770991661", "tian.tian@immuneonco.com"],
        ["西安交通大学第一附属医院", "韩旭", "15701197417", "xu.han@immuneonco.com"]
    ]
    # SMO (津石) 团队
    smo_data = [
        ["河南科技大学第一附属医院", "杨洁", "13633893896", "yang_jie0108@wuxiapptec.com"],
        ["临沂市肿瘤医院", "李春潇", "18865490982", "li_chunxiao0101@wuxiapptec.com"],
        ["南昌大学第一附属医院", "余红梅", "18279539445", "yu_hongmei0701@wuxiapptec.com"],
        ["湘潭市中心医院", "陈玉玲", "15573214901", "chen_yuling@wuxiapptec.com"],
        ["浙江大学附属第二医院", "蔡晶晶", "18329107307", "cai_jingjing@wuxiapptec.com"],
        ["湖南省肿瘤医院", "贺冬雪", "15580676917", "he_dongxue@wuxiapptec.com"]
    ]
    return mgmt_data, cra_data, smo_data

# --- 4. 侧边栏：名片与导航 ---
with st.sidebar:
    st.title("🏥 项目名片")
    st.success("**方案**: V6.0 (2026.03.23)\n\n**IB**: V5.0 (IMM2510)")
    st.info("📅 **项目周会**\n\n每周五 14:00\n\n会议号：727-7862-0848")
    st.divider()
    menu = st.radio("功能导航", ["项目概览与资料", "核心通讯录", "📦 物资申领(新)", "访视明细(一事一行)"])
    st.caption("版本：V1.2 | 更新：2026-04-22")

# --- 5. 主页面逻辑 ---
mgmt, cra, smo = get_full_contact_data()

if menu == "项目概览与资料":
    t1, t2, t3, t4 = st.tabs(["📂 公共资料库", "🔬 药物/实验室要点", "📍 全国20家中心", "🤖 智能命名助手"])
    
    with t1:
        st.subheader("全量启动包索引 (共38个核心文档)")
        data = {
            "编号": ["01-08", "09-16", "17-24", "25-36"],
            "分类": ["申办方/CDE/方案", "IB/COA/监查计划", "保险/授权/名单", "使用手册/资质执照"],
            "最新状态": ["方案V6.0已获批", "IB已更新至V5.0", "保单已扩展37例", "执照生产证全补齐"]
        }
        st.table(pd.DataFrame(data))
    
    with t2:
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 💊 药物使用预警")
            st.error("配制后室温稳定时长: IMM2510(8小时) | IMM27M(4小时)")
            st.write("- **复溶**: IMM2510 冻干粉复溶迅速")
            st.write("- **超温**: 8-25℃ 累计不超过48小时可继续使用")
        with col2:
            st.markdown("### 🧪 实验室送检指南")
            st.write("- **康维讯**: 负责PK/ADA")
            st.write("- **阿克曼**: 负责组织切片")
            
    with t3:
        st.subheader("📍 分中心布局 (剂量探索阶段)")
        sites = ["复旦中山(组长)", "吉大一院", "河南肿瘤", "武汉协和", "华西医院", "湖南肿瘤", "南昌二院", "清华长庚"]
        st.success(" ✅ 已确定参加并覆盖保险: " + " 、 ".join(sites))
        
    with t4:
        st.subheader("🤖 文件命名标准化")
        st.code("项目名_中心号_文件类型_版本_日期.pdf", language="text")

elif menu == "核心通讯录":
    st.subheader("📇 项目全量通讯录")
    c1, c2, c3, c4 = st.tabs(["宜明昂科团队", "CRA 负责中心", "SMO 团队", "其他供应商"])
    with c1:
        st.dataframe(pd.DataFrame(mgmt, columns=["职位", "姓名"]), use_container_width=True, hide_index=True)
    with c2:
        st.table(pd.DataFrame(cra, columns=["中心名称", "CRA姓名", "电话", "邮箱"]))
    with c3:
        st.dataframe(pd.DataFrame(smo, columns=["中心名称", "SSU CRC", "电话", "邮箱"]), use_container_width=True, hide_index=True)
    with c4:
        col_l, col_r = st.columns(2)
        with col_l:
            st.markdown("**中心实验室**")
            st.write("🧪 康维讯 PM: 赵娟 | 15996268113")
            st.write("🔬 阿克曼 PM: 任卫 | 17621905332")
        with col_r:
            st.markdown("**物流与保险**")
            st.write("🚚 生生物流紧急: 王金麟 | 15821381794")
            st.write("🛡️ 保险: 华泰财产保险有限公司")

elif menu == "📦 物资申领(新)":
    st.subheader("📦 项目物资与物流申领专区")
    st.info("💡 模块建设中：未来将在此处集成实验室耗材、样本箱及药物一键申请流程。")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### **🕒 预期申请时效**")
        st.write("建议提前 **2 周** 发起申领，以确保物流覆盖及库存充足。")
    with col2:
        st.markdown("### **📞 物资催单联系人**")
        st.write("项目 PM：吕志刚 (宜明昂科)")
        st.write("实验室 PM：赵娟 (康维讯)")

    st.divider()
    st.markdown("#### 📝 拟定申请步骤")
    st.markdown("""
    1. **盘点库存**：每月 25 日盘点剩余耗材。
    2. **提交申请**：通过 [预留链接] 填写申请单。
    3. **邮件审批**：PM 审批后物流发货。
    4. **确认收货**：CRC 核对批号并归档受赠清单。
    """)

elif menu == "访视明细(一事一行)":
    st.subheader("📊 访视动作拆解流水账")
    st.info("此处展示基于方案 V6.0 拆解后的访视明细，用于指导 CRA/CRC 实地操作。")
