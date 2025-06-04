import os
import sys
import platform
import pkgutil


def gather_info():
    info = {
        "python_executable": sys.executable,
        "python_version": sys.version,
        "platform": f"{platform.system()} {platform.release()} ({platform.version()})",
        "machine": platform.machine(),
        "processor": platform.processor(),
        "architecture": platform.architecture(),
        "cwd": os.getcwd(),
        "sys_path": list(sys.path),
        "modules": sorted(m.name for m in pkgutil.iter_modules()),
    }
    return info


def print_info(info):
    print("=" * 40)
    print("\U0001FA7A DoctorMyPass - Local Python Diagnostic")
    print("=" * 40)
    print(f"Python Executable: {info['python_executable']}")
    print(f"Python Version: {info['python_version']}")
    print(f"Platform: {info['platform']}")
    print(f"Machine: {info['machine']}")
    print(f"Processor: {info['processor']}")
    print(f"Architecture: {info['architecture']}")
    print(f"Current Working Directory: {info['cwd']}")
    print("\n\U0001F4C2 sys.path (where Python looks for modules):")
    for p in info['sys_path']:
        print(f" - {p}")
    print("\n\U0001F4DA Importable Modules (minimal check):")
    for mod in info['modules']:
        print(f" - {mod}")


def save_report(info, filename):
    try:
        with open(filename, "w") as f:
            f.write("DoctorMyPass - Local Python Diagnostic\n")
            f.write("=" * 40 + "\n")
            f.write(f"Python Executable: {info['python_executable']}\n")
            f.write(f"Python Version: {info['python_version']}\n")
            f.write(f"Platform: {info['platform']}\n")
            f.write(f"Machine: {info['machine']}\n")
            f.write(f"Processor: {info['processor']}\n")
            f.write(f"Architecture: {info['architecture']}\n")
            f.write(f"Current Working Directory: {info['cwd']}\n")
            f.write("\nsys.path:\n")
            for p in info['sys_path']:
                f.write(f" - {p}\n")
            f.write("\nImportable Modules:\n")
            for mod in info['modules']:
                f.write(f" - {mod}\n")
        print(f"\U0001F4DD Diagnostic saved to {filename}")
    except Exception as e:
        print(f"\u26A0\uFE0F Could not write to {filename}: {e}")


def main():
    info = gather_info()
    print_info(info)
    paths = [
        os.path.join(os.getcwd(), "DoctorMyPass.txt"),
        "/sdcard/DoctorMyPass.txt",
        "/storage/emulated/0/DoctorMyPass.txt",
    ]
    for path in paths:
        save_report(info, path)
    print("=" * 40)
    print("\U0001FA7A DoctorMyPass - Done")
    print("=" * 40)


if __name__ == "__main__":
    main()
