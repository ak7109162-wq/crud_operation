import streamlit as st
from pathlib import Path
import os
import shutil

st.set_page_config(page_title="CRUD File Manager", page_icon="📁")

st.title("📁 CRUD File Manager")

BASE_PATH = Path(".")


# ==========================
# SHOW FILES & FOLDERS
# ==========================
def show_files_and_folders():
    st.subheader("📂 Files & Folders")
    items = list(BASE_PATH.rglob("*"))

    if items:
        for index, item in enumerate(items):
            st.write(f"{index} - {item}")
    else:
        st.info("No files or folders found")


# ==========================
# CREATE FILE
# ==========================
def create_file():
    st.subheader("📄 Create File")

    file_name = st.text_input("Enter file name")

    content = st.text_area("Enter file content")

    if st.button("Create File"):
        try:
            p = Path(file_name)

            if p.exists():
                st.warning("File already exists")
            else:
                with open(file_name, "w") as file:
                    file.write(content)

                st.success("File created successfully")

        except Exception as e:
            st.error(e)


# ==========================
# READ FILE
# ==========================
def read_file():
    st.subheader("📖 Read File")

    file_name = st.text_input("Enter file name to read")

    if st.button("Read File"):
        try:
            p = Path(file_name)

            if p.exists():
                with open(file_name, "r") as file:
                    st.text(file.read())
            else:
                st.error("File not found")

        except Exception as e:
            st.error(e)


# ==========================
# UPDATE FILE
# ==========================
def update_file():
    st.subheader("✏️ Update File")

    file_name = st.text_input("Enter file name to update")

    option = st.radio(
        "Select update option",
        ["Overwrite Content", "Append Content"]
    )

    content = st.text_area("Enter new content")

    if st.button("Update File"):
        try:
            p = Path(file_name)

            if p.exists():

                if option == "Overwrite Content":
                    with open(file_name, "w") as file:
                        file.write(content)

                elif option == "Append Content":
                    with open(file_name, "a") as file:
                        file.write(content)

                st.success("File updated successfully")

            else:
                st.error("File does not exist")

        except Exception as e:
            st.error(e)


# ==========================
# DELETE FILE
# ==========================
def delete_file():
    st.subheader("🗑️ Delete File")

    file_name = st.text_input("Enter file name to delete")

    if st.button("Delete File"):
        try:
            p = Path(file_name)

            if p.exists():
                os.remove(p)
                st.success("File deleted successfully")
            else:
                st.error("File not found")

        except Exception as e:
            st.error(e)


# ==========================
# RENAME FILE
# ==========================
def rename_file():
    st.subheader("🔄 Rename File")

    old_name = st.text_input("Enter current file name")

    new_name = st.text_input("Enter new file name")

    if st.button("Rename File"):
        try:
            p = Path(old_name)

            if p.exists():
                p.rename(new_name)
                st.success("File renamed successfully")
            else:
                st.error("File not found")

        except Exception as e:
            st.error(e)


# ==========================
# CREATE FOLDER
# ==========================
def create_folder():
    st.subheader("📁 Create Folder")

    folder_name = st.text_input("Enter folder name")

    if st.button("Create Folder"):
        try:
            p = Path(folder_name)

            if p.exists():
                st.warning("Folder already exists")
            else:
                p.mkdir()
                st.success("Folder created successfully")

        except Exception as e:
            st.error(e)


# ==========================
# DELETE FOLDER
# ==========================
def delete_folder():
    st.subheader("❌ Delete Folder")

    folder_name = st.text_input("Enter folder name to delete")

    if st.button("Delete Folder"):
        try:
            p = Path(folder_name)

            if p.exists():

                if any(p.iterdir()):
                    shutil.rmtree(p)
                else:
                    p.rmdir()

                st.success("Folder deleted successfully")

            else:
                st.error("Folder not found")

        except Exception as e:
            st.error(e)


# ==========================
# CREATE FILE IN FOLDER
# ==========================
def create_file_in_folder():
    st.subheader("📄➕📁 Create File Inside Folder")

    folder_name = st.text_input("Enter folder name")

    file_name = st.text_input("Enter file name")

    content = st.text_area("Enter file content")

    if st.button("Create File In Folder"):
        try:
            folder_path = Path(folder_name)

            if not folder_path.exists():
                st.error("Folder does not exist")
                return

            file_path = folder_path / file_name

            if file_path.exists():
                st.warning("File already exists")

            else:
                with open(file_path, "w") as file:
                    file.write(content)

                st.success("File created successfully inside folder")

        except Exception as e:
            st.error(e)


# ==========================
# SIDEBAR MENU
# ==========================
menu = st.sidebar.selectbox(
    "Select Operation",
    [
        "Show Files & Folders",
        "Create File",
        "Read File",
        "Update File",
        "Delete File",
        "Rename File",
        "Create Folder",
        "Delete Folder",
        "Create File In Folder"
    ]
)


# ==========================
# MENU OPERATIONS
# ==========================
if menu == "Show Files & Folders":
    show_files_and_folders()

elif menu == "Create File":
    create_file()

elif menu == "Read File":
    read_file()

elif menu == "Update File":
    update_file()

elif menu == "Delete File":
    delete_file()

elif menu == "Rename File":
    rename_file()

elif menu == "Create Folder":
    create_folder()

elif menu == "Delete Folder":
    delete_folder()

elif menu == "Create File In Folder":
    create_file_in_folder()