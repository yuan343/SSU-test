import streamlit as st
import pandas as pd
from datetime import datetime

# 页面基础配置
st.set_page_config(page_title="SSU项目协同与文件管理门户", layout="wide")

# 自定义样式
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stAlert { border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 侧边栏：项目核心名片（解决合作方不清晰） ---
with st.sidebar:
    st.title("项目核心名片")
    st.info("""
    **💊 药物供应商** 名称：XX医药供应链公司  
    联系人：张经理 (138...)  
    发货周期：申请后5个工作日
    """)
    st.success("""
    **🧪 中心实验室 (Central Lab)** 名称：迪安医学检验中心  
    样本类型：冻存血浆/全血  
    寄送频率：每周三统一寄送
    """)
    st.warning("""
    **📞 申办方/CRO联系人** 项目经理(PM)：李工  
    CRA负责人：王工
    """)

# --- 主界面标题 ---
st.title("🚀 SSU 临床试验启动加速器")
st.caption("解决分中心找资料难、信息不对称、命名混乱的专项工具")

# --- 功能模块分栏 ---
tab1, tab2, tab3 = st.tabs(["📂 公共文件库", "📋 协议执行清单", "🤖 智能命名助手"])

# TAB 1: 公共文件库（解决找资料长、分中心不清晰）
with tab1:
    st.subheader("组长单位及公共资料 (Single Source of Truth)")
    # 模拟数据：实际应用中可对接数据库或文件夹
    file_data = {
        "分类": ["方案类", "方案类", "伦理类", "资质类", "手册类"],
        "文档名称": ["临床研究方案_Protocol", "知情同意书模板_ICF", "组长单位伦理批件", "申办方营业执照", "研究者手册_IB"],
        "最新版本": ["V2.0", "V1.1", "2026-04版", "2026年度", "V5.0"],
        "更新日期": ["2026-04-10", "2026-04-12", "2026-04-15", "2026-01-01", "2026-03-20"],
        "下载链接": ["🔗点击下载", "🔗点击下载", "🔗点击下载", "🔗点击下载", "🔗点击下载"]
    }
    df_files = pd.DataFrame(file_data)
    st.table(df_files)

# TAB 2: 协议框架要点（解决检查项混乱）
with tab2:
    st.subheader("核心协议框架（研究协调员/PI快速查阅）")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("##### **🗓️ 访视周期安排**")
        visit_schedule = {
            "阶段": ["筛选期", "访视1 (基线)", "访视2", "访视3", "访视4"],
            "时间点": ["D-14 to D0", "D1", "W2 (±2d)", "W4 (±3d)", "W8 (±3d)"],
            "关键任务": ["签署ICF/化验", "首次给药", "安全性评估", "有效性评估", "结束给药"]
        }
        st.dataframe(pd.DataFrame(visit_schedule), use_container_width=True)
    
    with col2:
        st.markdown("##### **🔍 检查项及频率**")
        st.write("- **血常规/生化**：筛选期、V1、V2、V4（共4次）")
        st.write("- **PK采血**：V1给药前、给药后0.5h, 1h, 2h, 4h, 8h（共6个点）")
        st.write("- **ECG心电图**：每次访视均需进行")
        st.write("- **妊娠检测**：仅育龄期女性，每次给药前")

# TAB 3: 智能命名助手（解决命名不清晰的根源）
with tab3:
    st.subheader("🛠️ SSU文件规范命名生成器")
    st.write("在上传文件前，请先用此工具生成标准文件名，避免他人找不到资料。")
    
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        site_code = st.text_input("中心编号", placeholder="如: 001")
    with c2:
        doc_type = st.selectbox("文件类型", ["EC(伦理)", "Contract(合同)", "HGRAC(遗传办)", "CV(简历)", "GCP(证书)"])
    with c3:
        version = st.text_input("版本号", placeholder="如: V1.0")
    with c4:
        date_str = st.date_input("文件日期")

    # 生成标准名
    if site_code:
        standard_name = f"PROJ_{site_code}_{doc_type}_{version}_{date_str.strftime('%Y%m%d')}.pdf"
        st.code(standard_name, language="text")
        st.info("💡 请将你的原始文件重命名为上方代码块中的名称后，再进行归档。")

# 页脚
st.divider()
st.center = st.markdown("项目管理支持：SSU 加速器 v1.0")
