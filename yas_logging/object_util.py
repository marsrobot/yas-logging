import io
import pickle


class object_util:
    @staticmethod
    def deepcopy(obj):
        buffer = io.BytesIO()
        pickle.dump(obj, buffer)
        buffer.seek(0)
        new_obj = pickle.load(buffer)
        return new_obj

    @staticmethod
    def getattr(obj, name: str):
        try:
            return getattr(obj, name)
        except BaseException as ex:
            return None
