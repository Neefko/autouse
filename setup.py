from cx_Freeze import setup, Executable

executables = [
    Executable(
        "server.py",
        base="Win32GUI",
        target_name="school.exe",
    )
]

setup(
    name="autouse",
    version="1.0",
    description="Flask App",
    executables=executables,
    options={
        "build_exe": {
            "packages": [
                "flask",
                "pyautogui",
                "subprocess",
                "webbrowser",
                "socket",
                "smtplib",
            ],
        }
    }
)