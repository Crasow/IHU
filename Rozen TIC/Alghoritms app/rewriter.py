from chardet.universaldetector import UniversalDetector


def to_utf_8(path):
    with open(path, 'rb') as file:
        file_bytes = file.read()
        detector = UniversalDetector()
        for line in file.readlines():
            detector.feed(line)
            if detector.done: break
        detector.close()
        encoding = detector.result
        # print(encoding)
        decoded = file_bytes.decode(encoding['encoding'])
        with open(path, 'w', encoding='utf-8') as ffile:
            ffile.write(decoded)
