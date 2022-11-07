from cx_Freeze import setup, Executable
exe = Executable(
    script="Aplicacao.pyw",
    base="Win32GUI",                           # Retirar comentario se for contruir um executavel para windows
    icon="C:\\Users\\Evaldo\\Downloads\\Projeto_Atendimento-main\\Projeto_Atendimento-main\\Icons\\icon.ico",
    shortcut_name="Controle de Atendimentos",
    shortcut_dir="DesktopFolder",
    target_name="ControleAtendimentos.exe",
    )
setup(
    name = "Cadastro de Atendimentos",
    version = "2.1.0",
    author = "Meta Certificado Digital",
    description = "Programa para cadastrar atendimentos do suporte",
    options = {"build_exe": {
    'include_files': ['Icons'],
    'include_msvcr': True,
    }},
    executables = [exe]
    )

#comando
#python setup.py bdist_msi