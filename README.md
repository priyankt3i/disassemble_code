## Binary Code Disassembler Using StreamLit

To create a basic Streamlit application that utilizes diStorm3 for disassembling binary code, follow these steps:

1. **Install the Required Libraries:**

   Ensure you have both `streamlit` and `distorm3` installed. You can install them using pip:

   ```bash
   pip install streamlit distorm3
   ```

2. **Create the Streamlit Application:**

   Create a Python file (e.g., `disassembler_app.py`) and add the following code:

   ```python
   import streamlit as st
   import distorm3

   def disassemble_code(binary_code):
       # Decode the binary code using diStorm3
       decoded_instructions = distorm3.Decode(0, binary_code, distorm3.Decode32Bits)
       disassembled_code = "\n".join([f"{hex(offset)}: {hexdump}  {instruction}" for offset, _, instruction, hexdump in decoded_instructions])
       return disassembled_code

   def main():
       st.title("Binary Code Disassembler")

       # File uploader for binary files
       uploaded_file = st.file_uploader("Upload a binary file", type=["bin", "exe", "dll", "sys"])

       if uploaded_file is not None:
           # Read the binary content
           binary_code = uploaded_file.read()

           # Disassemble the binary code
           disassembled_code = disassemble_code(binary_code)

           # Display the disassembled code
           st.text_area("Disassembled Code", disassembled_code, height=300)

   if __name__ == "__main__":
       main()
   ```

3. **Run the Application:**

   Navigate to the directory containing `disassembler_app.py` and run:

   ```bash
   streamlit run disassembler_app.py
   ```

   This will start a local Streamlit server, and you can access the application in your web browser.

4. **Using the Application:**

   - Upload a binary file (e.g., `.bin`, `.exe`, `.dll`, `.sys`) using the file uploader.
   - The application will read the binary content and disassemble it using diStorm3.
   - The disassembled code will be displayed in a text area within the application.

**Note:** Ensure that the `distorm3` library is correctly installed. If you encounter issues during installation, such as errors related to the Microsoft Visual C++ compiler, you may need to install the necessary build tools. You can download them from the [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/) page. After installation, restart your terminal or IDE to ensure the environment variables are set correctly.

For more information on diStorm3, you can refer to its [GitHub repository](https://github.com/gdabah/distorm). 