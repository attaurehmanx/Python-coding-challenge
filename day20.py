import re
def convert_html(text):
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    text = re.sub(r'\#(.*?)\#', r'<h1>\1</h1>', text)

    return text


user = "This is **bold** and *italic* text. This is a #HH!# This is **BB** and *II* text."

done = convert_html(user)
print(done)
