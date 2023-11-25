from urllib.parse import quote

original_string = '是平啊～'
encoded_string = quote(original_string, encoding='utf-8')

print(encoded_string)
