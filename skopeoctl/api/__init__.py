from typing import Any
from typing import Dict
from typing import List
from typing import Tuple


class RegisterBaseAPIV2(object):

    def __init__(self):
        pass

    def list_tags(self, name, **kwargs) -> Any:
        raise NotImplemented

    def sort_tags(self, name) -> (bool, List[Tuple[str, int]], Dict):
        """ return sorted tags by timestamp desc

        :param name: image name
        :return: (bool, List[Tuple[str, int]], Dict)
        Dict is image's tag and sha256 map
        e.g. (True, [(tag1, last_update_timestamp), ...], {tag1: sha2561, ...})
        """
        raise NotImplemented
