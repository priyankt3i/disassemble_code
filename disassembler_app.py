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
