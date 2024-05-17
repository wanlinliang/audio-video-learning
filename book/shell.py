import os

def remove_string_from_filenames(target_string):
    # 获取当前目录下的所有文件和目录
    current_dir = os.getcwd()
    items = os.listdir(current_dir)
    
    for item in items:
        # 获取完整路径
        item_path = os.path.join(current_dir, item)
        
        # 确保只处理文件
        if os.path.isfile(item_path) and target_string in item:
            # 构建新的文件名（去除指定字符串）
            new_name = item.replace(target_string, "")
            new_name_path = os.path.join(current_dir, new_name)
            
            # 检查新文件名是否已存在
            if os.path.exists(new_name_path):
                print(f'Error: Cannot rename {item} to {new_name}, file already exists.')
            else:
                # 重命名文件
                os.rename(item_path, new_name_path)
                print(f'Renamed: {item} -> {new_name}')

if __name__ == "__main__":
    target_string = "(Z-Library)"  # 指定要去除的字符串
    remove_string_from_filenames(target_string)

