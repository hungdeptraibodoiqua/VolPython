# for core module 
import subprocess

# windows.pslist.PsList
def run_pslist(memory_dump_path):
    try:
        cmd = [
            'vol', 
            '-f', memory_dump_path, 
            'windows.pslist.PsList'
        ]
        result = subprocess.run(
            cmd, 
            capture_output=True, 
            text=True, 
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error:\n{e.stderr}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"

# windows.pstree.PsTree
def run_pstree(memory_dump_path):
    try:
        cmd = [
            'vol', 
            '-f', memory_dump_path, 
            'windows.pstree.PsTree'
        ]
        result = subprocess.run(
            cmd, 
            capture_output=True, 
            text=True, 
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error:\n{e.stderr}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"
    
# windows.cmdline.CmdLine
def run_cmdline(memory_dump_path):
    try:
        cmd = [
            'vol', 
            '-f', memory_dump_path, 
            'windows.cmdline.CmdLine'
        ]
        result = subprocess.run(
            cmd, 
            capture_output=True, 
            text=True, 
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error:\n{e.stderr}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"    

# windows.malfind.Malfind
def run_malfind(memory_dump_path):
    try:
        cmd = [
            'vol', 
            '-f', memory_dump_path, 
            'windows.malfind.Malfind'
        ]
        result = subprocess.run(
            cmd, 
            capture_output=True, 
            text=True, 
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Error:\n{e.stderr}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"
    
# Hàm xuất dữ liệu ra file CSV
# Chuyển đổi dữ liệu từ output_text thành định dạng CSV và lưu vào file
def export_csv(output_text, save_path):
    try:
        lines = output_text.split('\n')
        with open(save_path, 'w') as f:
            for line in lines:
                if line.strip():
                    f.write(line.replace('\t', ',') + '\n')
        return None
    except Exception as e:
        return f"Export failed: {str(e)}"
