import PyPDF2
import glob
import os
def remove_password(input_pdf, output_pdf, password):
    with open(input_pdf, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)

        # Check if the PDF is encrypted
        if pdf_reader.isEncrypted:
            # Try to decrypt using the provided password
            if pdf_reader.decrypt(password):
                # Create a new PDF writer
                pdf_writer = PyPDF2.PdfWriter()

                # Add all pages to the new PDF
                for page_num in range(len(pdf_reader.pages)):
                    pdf_writer.addPage(pdf_reader.getPage(page_num))

                # Write the new PDF to the output file
                with open(output_pdf, 'wb') as output_file:
                    pdf_writer.write(output_file)
            else:
                print("Incorrect password. Unable to decrypt the PDF.")
        else:
            print("The PDF is not encrypted. No need to remove the password.")


# Example usage
input_pdf = "/Data/Private/דנה/תלושים/"
output_pdf = "/Data/Private/דנה/תלושים/unprotected/"
password = "025453929"
for file in glob.glob(os.path.join(input_pdf, '*.pdf')):
    remove_password(file, output_pdf+file.split('/')[5][-11:-4], password)
