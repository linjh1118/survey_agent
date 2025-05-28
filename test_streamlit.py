import streamlit as st
import os

def main():
    st.title("文件上传测试应用")
    st.write("这个应用用于测试文件上传功能是否正常工作。")
    
    # 文件上传组件
    uploaded_file = st.file_uploader("请选择一个文件上传", type=None, accept_multiple_files=False)
    
    if uploaded_file is not None:
        # 显示文件信息
        st.subheader("文件信息")
        st.write(f"文件名: `{uploaded_file.name}`")
        st.write(f"文件类型: `{uploaded_file.type}`")
        st.write(f"文件大小: `{uploaded_file.size / 1024:.2f} KB`")
        
        # 保存文件（可选）
        if st.button("保存文件"):
            try:
                # 创建临时目录
                if not os.path.exists("temp"):
                    os.makedirs("temp")
                
                # 保存文件
                file_path = os.path.join("temp", uploaded_file.name)
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                
                st.success(f"文件已成功保存到: `{file_path}`")
                
                # 提供下载链接
                with open(file_path, "rb") as f:
                    st.download_button(
                        label="下载保存的文件",
                        data=f,
                        file_name=uploaded_file.name,
                        mime=uploaded_file.type
                    )
                    
            except Exception as e:
                st.error(f"保存文件时出错: {str(e)}")

if __name__ == "__main__":
    main()