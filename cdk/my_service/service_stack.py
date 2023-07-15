import os
from pathlib import Path

from aws_cdk import Stack, Tags
from constructs import Construct
from git import Repo
from my_service.api_construct import ApiConstruct  # type: ignore

from cdk.my_service.constants import SERVICE_NAME


def get_username() -> str:
    try:
        return os.getlogin().replace('.', '-')
    except Exception:
        return 'github'


def get_stack_name() -> str:
    repo = Repo(Path.cwd())
    username = get_username()
    try:
        return f'{username}-{repo.active_branch}-{SERVICE_NAME}'
    except TypeError:
        return f'{username}-{SERVICE_NAME}'


class ServiceStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        Tags.of(self).add('service_name', 'Order')

        self.api = ApiConstruct(self, f'{id}Service'[0:64])
