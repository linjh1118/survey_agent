"""
通过这个指令 git add -n ./
检查git add -n ./输出的文件列表中是否有大于50MB的文件
如果有，则自动添加到.gitignore中
"""

import subprocess
import os
import re

def get_git_add_files():
    """获取git add -n ./会添加的文件列表"""
    try:
        result = subprocess.run(['git', 'add', '-n', './'], 
                              capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"执行git add -n ./失败: {e}")
        return None

def parse_git_add_output(output):
    """解析git add -n ./的输出，提取文件路径"""
    files = []
    for line in output.strip().split('\n'):
        if line.startswith('add'):
            # git add -n ./的输出格式通常是: "add 'filepath'"
            match = re.search(r"add '(.+)'", line)
            if match:
                filepath = match.group(1)
                files.append(filepath)
    return files

def get_file_size(filepath):
    """获取文件大小（字节）"""
    try:
        if os.path.exists(filepath):
            return os.path.getsize(filepath)
        return 0
    except OSError:
        return 0

def check_large_files(files, size_limit_mb=10):
    """检查文件列表中是否有大于指定大小的文件"""
    size_limit_bytes = size_limit_mb * 1024 * 1024
    large_files = []
    
    for filepath in files:
        file_size = get_file_size(filepath)
        if file_size > size_limit_bytes:
            large_files.append((filepath, file_size))
    
    return large_files

def add_to_gitignore(large_files):
    """将大文件添加到.gitignore中"""
    gitignore_path = '.gitignore'
    
    # 读取现有的.gitignore内容
    existing_content = ""
    if os.path.exists(gitignore_path):
        with open(gitignore_path, 'r', encoding='utf-8') as f:
            existing_content = f.read()
    
    # 准备要添加的内容
    new_entries = []
    for filepath, size_mb in large_files:
        # 转换为相对路径格式
        if filepath.startswith('./'):
            filepath = filepath[2:]
        new_entries.append(f"# 大文件: {filepath} ({size_mb / (1024*1024):.2f} MB)")
        new_entries.append(filepath)
    
    # 添加分隔符和新条目
    if existing_content and not existing_content.endswith('\n'):
        existing_content += '\n'
    
    if new_entries:
        existing_content += '\n# 自动添加的大文件\n'
        existing_content += '\n'.join(new_entries) + '\n'
    
    # 写入.gitignore
    with open(gitignore_path, 'w', encoding='utf-8') as f:
        f.write(existing_content)
    
    print(f"已将 {len(large_files)} 个大文件添加到 .gitignore")

def main():
    """主函数"""
    print("正在检查git add -n ./会添加的文件...")
    
    # 获取git add -n ./的输出
    git_output = get_git_add_files()
    if not git_output:
        print("无法获取git add文件列表")
        return
    
    # 解析文件列表
    files = parse_git_add_output(git_output)
    if not files:
        print("没有找到要添加的文件")
        return
    
    print(f"找到 {len(files)} 个文件")
    
    # 检查大文件
    large_files = check_large_files(files, 50)
    
    if large_files:
        print(f"\n发现 {len(large_files)} 个大于50MB的文件:")
        for filepath, size_bytes in large_files:
            size_mb = size_bytes / (1024 * 1024)
            print(f"  - {filepath}: {size_mb:.2f} MB")
        
        # 添加到.gitignore
        add_to_gitignore(large_files)
    else:
        print("没有发现大于50MB的文件")

if __name__ == "__main__":
    main()