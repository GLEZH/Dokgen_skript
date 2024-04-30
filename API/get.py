from typing import Callable, Any


def get(
        self,
        path: str,
) -> Callable[..., Any]:
    return self.route.get(path)