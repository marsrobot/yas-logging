import tempfile


class fs_config:

    @staticmethod
    def get_temp_dir() -> str:
        temp_dir = tempfile.gettempdir()
        return temp_dir
