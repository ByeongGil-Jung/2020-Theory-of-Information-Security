class Util(object):

    @classmethod
    def load(cls, file_path):
        with open(file=file_path, mode='r') as f:
            data = f.read()

        return data

    @classmethod
    def save(cls, file_path, data):
        with open(file=file_path, mode="w") as f:
            f.write(data)
