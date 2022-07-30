
from PyPDF2 import PdfReader, PdfWriter
from PyPDF2.errors import PdfReadError


def encrypt(path, password):
    reader = PdfReader(path)
    writer = PdfWriter()

    if reader.is_encrypted:
        return None
    else:
        for page in reader.pages:
            writer.add_page(page)

        writer.encrypt(password)

        name = 'encrypted_' + path.split('/')[-1]

        with open(name, 'wb') as file:
            writer.write(file)

        return name


def decrypt(path, password):
    reader = PdfReader(path)
    writer = PdfWriter()

    if reader.is_encrypted:
        try:
            reader.decrypt(password)
            for page in reader.pages:
                writer.add_page(page)
        except PdfReadError:
            return 'Invalid password'
        else:
            name = path.split('/')[-1]
            if 'encrypted' in name:
                name = name.replace('encrypted', 'decrypted')
            else:
                name = 'decrypted_' + name

            with open(name, 'wb') as file:
                writer.write(file)

            return name
    else:
        return None


if __name__ == '__main__':
    print(encrypt('encrypted_CSS.pdf', password='pass'))
    print(decrypt('encrypted_CSS.pdf', password='password'))


