import connexion
import six

from swagger_server.models.new_task import NewTask  # noqa: E501
from swagger_server.models.task import Task  # noqa: E501
from swagger_server.models.update_task import UpdateTask  # noqa: E501
from swagger_server import util


def tasks_get():  # noqa: E501
    """Получить список всех заданий

     # noqa: E501


    :rtype: List[Task]
    """
    return 'do some magic!'


def tasks_id_delete(id):  # noqa: E501
    """Удалить задание

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: None
    """
    return 'do some magic!'


def tasks_id_get(id):  # noqa: E501
    """Получить задание по ID

     # noqa: E501

    :param id: 
    :type id: int

    :rtype: Task
    """
    return 'do some magic!'


def tasks_id_patch(body, id):  # noqa: E501
    """Обновить статус задания (например, отметить выполненным)

     # noqa: E501

    :param body: 
    :type body: dict | bytes
    :param id: 
    :type id: int

    :rtype: Task
    """
    if connexion.request.is_json:
        body = UpdateTask.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def tasks_post(body):  # noqa: E501
    """Создать новое задание (дедлайн)

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: Task
    """
    if connexion.request.is_json:
        body = NewTask.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
