
import envi

while True:
    text = input('env > ')
    result, error = envi.run('<stdin>', text)

    if error: print(error.as_string())
    else: print(result)
