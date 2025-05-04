# for core module 
import subprocess

def run_volatility_plugin(
    memory_dump_path, 
    plugin_name, 
    offset=None, 
    extra_args=None
):
    try:
        cmd = ["vol", "-f", memory_dump_path, plugin_name]
        if offset is not None:
            cmd += ["--virtaddr", f"{offset:#x}"]
    
        if extra_args:
            cmd += extra_args
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        
    except subprocess.CalledProcessError as e:
        return f"Volatility Error: {e.stderr}"
    except Exception as e:
        return f"Error: {str(e)}"

# python vol.py -f C:\Users\HungDepTrai\Desktop\PythonVolatility\192-Reveal.dmp -o "C:\Users\HungDepTrai\Desktop\PythonVolatility" windows.dumpfiles --virtaddr 0xc90c060d80a0
#full command to choose output directory
def run_dumpfiles(memory_dump_path, offset):
    return run_volatility_plugin(
        memory_dump_path=memory_dump_path,
        plugin_name="windows.dumpfiles",
        offset=offset
    )
# hàm chạy các plugin của Volatility 3 với xử lý lỗi
# def run_volatility_plugin(memory_dump_path, plugin_name):
#     """Generic function to run Volatility plugins with error handling."""
#     try:
#         cmd = ['vol', '-f', memory_dump_path, plugin_name]
#         result = subprocess.run(
#             cmd, 
#             capture_output=True, 
#             text=True, 
#             check=True
#         )
#         return result.stdout
#     except subprocess.CalledProcessError as e:
#         return f"Volatility Error ({plugin_name}):\n{e.stderr}"
#     except FileNotFoundError:
#         return "Error: 'vol' command not found. Install Volatility 3 first."
#     except Exception as e:
#         return f"Unexpected Error ({plugin_name}): {str(e)}"

# Plugin-specific functions (no duplicate try-except)
def run_pslist(memory_dump_path):
    return run_volatility_plugin(memory_dump_path, 'windows.pslist.PsList')

def run_pstree(memory_dump_path):
    return run_volatility_plugin(memory_dump_path, 'windows.pstree.PsTree')

def run_cmdline(memory_dump_path):
    return run_volatility_plugin(memory_dump_path, 'windows.cmdline.CmdLine')

def run_malfind(memory_dump_path):
    return run_volatility_plugin(memory_dump_path, 'windows.malfind.Malfind')

def run_filescan(memory_dump_path):
    return run_volatility_plugin(memory_dump_path, 'windows.filescan.FileScan')

def run_filescan(memory_dump_path):
    return run_volatility_plugin(memory_dump_path, 'windows.filescan.FileScan') 

# def run_dumpfiles(memory_dump_path):
#     return run_volatility_plugin(memory_dump_path, 'windows.dumpfiles.DumpFiles')
# # windows.pslist.PsList
# def run_pslist(memory_dump_path):
#     try:
#         cmd = [
#             'vol', 
#             '-f', memory_dump_path, 
#             'windows.pslist.PsList'
#         ]
#         result = subprocess.run(
#             cmd, 
#             capture_output=True, 
#             text=True, 
#             check=True
#         )
#         return result.stdout
#     except subprocess.CalledProcessError as e:
#         return f"Error:\n{e.stderr}"
#     except Exception as e:
#         return f"Unexpected error: {str(e)}"

# # windows.pstree.PsTree
# def run_pstree(memory_dump_path):
#     try:
#         cmd = [
#             'vol', 
#             '-f', memory_dump_path, 
#             'windows.pstree.PsTree'
#         ]
#         result = subprocess.run(
#             cmd, 
#             capture_output=True, 
#             text=True, 
#             check=True
#         )
#         return result.stdout
#     except subprocess.CalledProcessError as e:
#         return f"Error:\n{e.stderr}"
#     except Exception as e:
#         return f"Unexpected error: {str(e)}"
    
# # windows.cmdline.CmdLine
# def run_cmdline(memory_dump_path):
#     try:
#         cmd = [
#             'vol', 
#             '-f', memory_dump_path, 
#             'windows.cmdline.CmdLine'
#         ]
#         result = subprocess.run(
#             cmd, 
#             capture_output=True, 
#             text=True, 
#             check=True
#         )
#         return result.stdout
#     except subprocess.CalledProcessError as e:
#         return f"Error:\n{e.stderr}"
#     except Exception as e:
#         return f"Unexpected error: {str(e)}"    

# # windows.malfind.Malfind
# def run_malfind(memory_dump_path):
#     try:
#         cmd = [
#             'vol', 
#             '-f', memory_dump_path, 
#             'windows.malfind.Malfind'
#         ]
#         result = subprocess.run(
#             cmd, 
#             capture_output=True, 
#             text=True, 
#             check=True
#         )
#         return result.stdout
#     except subprocess.CalledProcessError as e:
#         return f"Error:\n{e.stderr}"
#     except Exception as e:
#         return f"Unexpected error: {str(e)}"

# # windows.filescan.FileScan
# def run_filescan(memory_dump_path):
#     try:
#         cmd = [
#             'vol', 
#             '-f', memory_dump_path, 
#             'windows.filescan.FileScan'
#         ]
#         result = subprocess.run(
#             cmd, 
#             capture_output=True, 
#             text=True, 
#             check=True
#         )
#         return result.stdout
#     except subprocess.CalledProcessError as e:
#         return f"Error:\n{e.stderr}"
#     except Exception as e:
#         return f"Unexpected error: {str(e)}"
    

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
