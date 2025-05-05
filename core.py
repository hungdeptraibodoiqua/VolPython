import subprocess

def run_volatility_plugin(memory_dump_path, plugin_name, offset=None, extra_args=None):
    try:
        cmd = ["vol", "-f", memory_dump_path, plugin_name]
        if offset is not None:
            cmd += ["--virtaddr", f"{offset:#x}"]
        if extra_args:
            cmd += extra_args
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f"Volatility Error: {e.stderr}"
    except Exception as e:
        return f"Error: {str(e)}"

def run_dumpfiles(memory_dump_path, offset):
    return run_volatility_plugin(memory_dump_path, "windows.dumpfiles", offset)

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

def export_csv(output_text, save_path):
    try:
        lines = output_text.split('\n')
        with open(save_path, 'w', newline='') as f:
            for line in lines:
                if line.strip():
                    f.write(line.replace('\t', ',') + '\n')
        return None
    except Exception as e:
        return f"Export failed: {str(e)}"
